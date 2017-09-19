"""Copyright (C) 2015-2016 Association of Universities for Research in Astronomy, Inc. (AURA)

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
       this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.

    3. The names of AURA, its representatives and contributors may not be used
       to endorse or promote products derived from this software without
       specific prior written permission.

THIS SOFTWARE IS PROVIDED BY AURA AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL AURA OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE."""

# Copyright(c) 2015 Association of Universities for Research in Astronomy, Inc.
# by James E.H. Turner.
# Modified in 2017 by Nat Comeau

import os, os.path
import sys
from contextlib import closing
from StringIO import StringIO
import urllib2
import xml.dom.minidom as xmd
import tarfile
import hashlib

def download_query_gemini(query, dirname='', cookieName=''):
    """
    Perform a user-specified Gemini science archive query and save the files
    returned to a specified directory.

    Any existing files with the same names are overwritten, since there's no
    way to avoid downloading them all as part of the query anyway. However,
    only files that pass their checksum comparison (or have no checksum, which
    shouldn't happen) get written to disk. In the event that one or more files
    are corrupt, the caller can therefore re-try the query, omitting any files
    that were fetched successfully the first time if the query supports it.

    The downloaded tar file is stored in memory while processing its contents,
    which should be optimal as long as the archive isn't unreasonably large
    (to do: consider adding an option to write it to a temporary file).

    Parameters
    ----------

    query : str
        The query URL (or just the path component) to request from the server.

    dirname : str, optional
        The (absolute or relative) directory path in which to place the files.

    """
    checksum_fn = 'md5sums.txt'
    aux_fn = [checksum_fn, 'README.txt']


    # Perform Web query and download the tar file to a StringIO file object
    # in memory, passing through any HTTP errors.
    # Added by ncomeau: support for proprietary downloads
    if cookieName:
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', 'gemini_archive_session={}'.format(cookieName)))
        with closing(opener.open(query)) as fileobj:
            fobj_buff = StringIO(fileobj.read())
    else:
        with closing(urllib2.urlopen(query)) as fileobj:
            fobj_buff = StringIO(fileobj.read())

    # Open the in-memory tar file & extract its contents.
    with tarfile.open(fileobj=fobj_buff) as tar_obj:

        # Read the filenames & checksums for each file:
        chk_dict = {}
        with closing(tar_obj.extractfile(checksum_fn)) as chk_fobj:
            for line in chk_fobj:
                try:
                    checksum, fn = line.split()
                except ValueError:
                    raise ValueError('failed to parse {0}'\
                                     .format(checksum_fn))
                chk_dict[fn] = checksum

        # Get a list of the remaining files in the archive, without making
        # assumptions as to how the name(s) match the input list (eg. they
        # have a compression suffix).
        tarlist = [tinfo for tinfo in tar_obj.getmembers() \
                   if tinfo.name not in aux_fn]

        nosum, corrupt = [], []

        # Verify each data file and extract it to disk:
        for member in tarlist:

            fn = member.name

            # Extract the (compressed) file from the archive to memory.
            # This probably duplicates the memory usage momentarily for
            # each file in turn but that's unlikely to be critical.
            with closing(tar_obj.extractfile(fn)) as fobj:
                data_file = fobj.read()

            # Compare the checksums and record any problems. If one fails,
            # the whole query will need re-trying, so we'll just raise an
            # exception at the end and let the caller try again (ideally
            # excluding those files we've already got successfully here).
            if fn in chk_dict:
                checksum = hashlib.md5(data_file).hexdigest()
                if checksum == chk_dict[fn]:
                    good = True
                else:
                    corrupt.append(fn)
                    good = False
            else:
                nosum.append(fn)
                good = False

            # Write the file only if it didn't have a bad checksum:
            if good:
                decompress_to_disk(data_file, fn, dirname)

        if nosum:
            sys.stderr.write(
                'Files downloaded with missing checksums: {0}\n\n'\
                .format(' '.join(nosum)))

        if corrupt:
            raise IOError('Corrupt files skipped: {0}'\
                          .format(' '.join(corrupt)))

def decompress_to_disk(data, filename, dirname=''):
    """
    Write the contents of a file in memory to the named file on disk,
    decompressing it first if the file extension is recognized as a
    compressed data format. The file will be overwritten if it already exists.
    """

    outname, ext = os.path.splitext(filename)
    cmp_format = ext.lstrip(os.extsep)

    # If the file format is recognized, decompress the data before writing to
    # disk, otherwise just write the file as it is already.
    if cmp_format == 'bz2':
        import bz2
        data = bz2.decompress(data)

    elif cmp_format == 'gz':
        import gzip
        with gzip.GzipFile(fileobj=StringIO(data)) as gzip_obj:
            data = gzip_obj.read()

    else:
        # Restore the original file extension since we're not decompressing:
        outname += ext

    path = os.path.join(dirname, outname)

    # Write the file, clobbering any existing copy:
    with open(path, 'w') as fobj:
        fobj.write(data)
