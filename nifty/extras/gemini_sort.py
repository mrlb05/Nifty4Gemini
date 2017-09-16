from sort import *

##################################################################################################################
#                                                                                                                #
#                                       CASE 2: GEMINI NETWORK FUNCTIONS                                         #
#                                                                                                                #
#                            Used in copying data from internal Gemini network                                   #
#                                                                                                                #
##################################################################################################################


def start(tel, sort, over, copy, program, date):
    """Copy and sort data based on command line input. Data copied from Internal Gemini
    network (used ONLY within Gemini).

    Args:
        tel (boolean):  Specified with -t at command line. If False no
                        telluric corrections will be executed. Default: True.
        over (boolean): Specified with -o at command line. If True
                        old files will be overwritten during data reduction. Default: False.
        sort (boolean): Specified with -s or --sort at command line. If False data will not be
                        sorted. Default: True.
        copy (boolean): Specified with -c or --copy at command line. If True data
                        will be copied from Gemini network. Default: False.
        program:        Specified with -p at command line. Eg GN-2013B-Q-109. Used only within Gemini network.
        date:           Specified with -d at command line. YYYYMMDD. Used only within Gemini network.

    """

    FORMAT = '%(asctime)s %(message)s'
    DATEFMT = datefmt()
    logging.basicConfig(filename='Nifty.log',format=FORMAT,datefmt=DATEFMT,level=logging.DEBUG)
    log = os.getcwd()+'/Nifty.log'

    path = os.getcwd()


    # Copy from Gemini Internal Network AND sort. This will be executed IF ONLY -c True is
    # specified at command line. MUST provide a program id or date with -d or -p.

    if copy and sort:
        # Copy data from archives and sort ONLY IF a program is given with -p.
        if program:
            allfilelist, filelist, skyFrameList, telskyFrameList = getProgram(program, date, over)
            arclist, arcdarklist, flatlist, flatdarklist, ronchilist, obsidDateList  = getCals(filelist, over)
            objDateGratingList, objDirList, obsDirList, telDirList = sortObsGem(allfilelist, skyFrameList, telskyFrameList)
            calDirList = sortCalsGem(arcdarklist, arclist, flatlist, flatdarklist, ronchilist, objDateGratingList, objDirList, obsidDateList)
            # If a telluric correction will be performed sort the science and telluric images based on time between observations.
            # This will ONLY NOT be executed if -t False is specified at command line.
            if tel:
                telSort(telDirList, obsDirList)
        # Copy data from archives and sort ONLY IF a date is given with -d.
        elif date:
            allfilelist, filelist, skyFrameList, telskyFrameList = getScience(date, over)
            arclist, arcdarklist, flatlist, flatdarklist, ronchilist, obsidDateList = getCals(filelist, over)
            objDateGratingList, objDirList, obsDirList, telDirList = sortObsGem(allfilelist, skyFrameList, telskyFrameList)
            calDirList = sortCalsGem(arcdarklist, arclist, flatlist, flatdarklist, ronchilist, objDateGratingList, objDirList, obsidDateList)
            # If telluric correction will be performed sort the science and telluric images based on time between observations.
            # This will ONLY NOT be executed if -t False is specified at command line.
            if tel:
                telSort(telDirList, obsDirList)
            # Exit if a program or date was not probided with -p or -d at command line.
            else:
                print "\n Error in sort.py. Please enter a program ID or observation date with -p or -d at command line.\n"
                raise SystemExit

    # Copy from Gemini Internal network and DON'T sort. This will be executed IF -c True and -s False are specified at command line. MUST provide a program id or date with -d or -p.
    elif copy and not sort:
        # When a program is given (looks for program using /net/mko-nfs/sci/dataflow)
        if program:
            allfilelist, filelist, skyFrameList, telskyFrameList = getProgram(program, date, over)
            arclist, arcdarklist, flatlist, flatdarklist, ronchilist, obsidDateList  = getCals(filelist, over)
            allfilelist, arclist, arcdarklist, flatlist, flatdarklist, ronchilist, objDateGratingList, skyFrameList, telskyFrameList, obsidDateList = makeSortFiles(dir)
            obsDirList, calDirList, telDirList = getPaths(allfilelist, objDateGratingList, dir)
        # When a date is given (looks for data using /net/mko-nfs/sci/dataflow)
        elif date:
            allfilelist, filelist, skyFrameList, telskyFrameList = getScience(date, over)
            arclist, arcdarklist, flatlist, flatdarklist, ronchilist, obsidDateList  = getCals(filelist, over)
            allfilelist, arclist, arcdarklist, flatlist, flatdarklist, ronchilist, objDateGratingList, skyFrameList, telskyFrameList, obsidDateList = makeSortFiles(dir)
            obsDirList, calDirList, telDirList = getPaths(allfilelist, objDateGratingList, dir)
        # Exit if a program or date was not provided with -p or -d at command line.
        else:
            print "\n Error in sort.py. Please enter a program ID or observation date with -p or -d at command line.\n"
            raise SystemExit

    # Sort data ALREADY copied from Gemini Network. Specified if -s and -c are NOT specified at command line.
    elif not copy and sort:
        allfilelist, arclist, arcdarklist, flatlist, flatdarklist, ronchilist, objDateGratingList, skyFrameList, telskyFrameList, obsidDateList = makeSortFiles(dir)
        # Sort and get data from Gemini Internal Network
        if program or date:
            objDateGratingList, objDirList, obsDirList, telDirList = sortObsGem(allfilelist, skyFrameList, telskyFrameList)
            calDirList = sortCalsGem(arcdarklist, arclist, flatlist, flatdarklist, ronchilist, objDateGratingList, objDirList, obsidDateList)
        # if a telluric correction will be performed sort the science and telluric images based on time between observations
        if tel:
            telSort(telDirList, obsDirList)

    # Exit if no or incorrectly formatted input is given
    else:
        print "\n Enter a program ID, observation date, or directory where the raw files are located.\n"
        raise SystemExit

    os.chdir(path)

    return obsDirList, calDirList, telDirList



##################################################################################################################
#                                                                                                                #
#                                                   FUNCTIONS                                                    #
#                                                                                                                #
##################################################################################################################


def sortObsGem(allfilelist, skyFrameList, telskyFrameList):

    """Sorts the science images, tellurics and acquisitions into the appropriate directories based
    on date, grating, obsid, obsclass; called when sorting in the Gemini network.
    """

    path = os.getcwd()
    Raw = path+'/Raw'
    pathlist = []
    pathlist2 = []
    objDirList = []
    objDateGratingList = []
    obsDirList = []
    telDirList = []

    fitsKeyWords = ['OBSID', 'OBJECT', 'OBSCLASS', 'DATE', 'GRATING', 'POFFSET', 'QOFFSET']

    for entry in allfilelist:
        header = getFitsHeader(entry, fitsKeyWords)
        header[2] = header[2].replace(' ', '')
        DATE = header[4].replace('-','')
        if header[3]=='science':
            # create the object directory (name of target) in the current directory
            if not os.path.exists(path+'/'+header[2]):
                os.mkdir(path+'/'+header[2])
                objDir = path+'/'+header[2]
            # append object directory list (used in sortCalsGem)
                if not objDirList or not objDirList[-1]==objDir:
                    objDirList.append(objDir)
            else:
                objDir = path+'/'+header[2]
                if not objDirList or not objDirList[-1]==objDir:
                     objDirList.append(objDir)

    # append object date list of the form objDateGratingList = [[obj1, DATE1],[obj2, DATE1]...] (used in sortCalsGem)
    for entry in allfilelist:
        header = getFitsHeader(entry, fitsKeyWords)
        DATE = header[4].replace('-','')
        obj = header[2]
        if header[3]=='science':
            list1 = [obj, DATE]
            if not objDateGratingList or not objDateGratingList[-1]==list1:
                objDateGratingList.append(list1)

    for entry in allfilelist:
        header = getFitsHeader(entry, fitsKeyWords)
        DATE = header[4].replace('-','')
        objDir = path+'/'+header[2]
        obsid = header[1][-3:].replace('-','')
        if header[3]=='science':
            # create a directory for each observation date (YYYYMMDD) in objDir/
            if not os.path.exists(objDir+'/'+DATE):
                os.mkdir(objDir+'/'+DATE)
            # create a directory for each grating used in objDir/YYYYMMDD/
            if not os.path.exists(objDir+'/'+DATE+'/'+header[5][0]):
                os.mkdir(objDir+'/'+DATE+'/'+header[5][0])
            # create a directory for each obsid (eg. obs25) in objDir/YYYYMMDD/grating/
            if not os.path.exists(objDir+'/'+DATE+'/'+header[5][0]+'/obs'+obsid):
                os.mkdir(objDir+'/'+DATE+'/'+header[5][0]+'/obs'+obsid)
            # append obsid directory list; a list of all the different observation directories (used in nifsScience.py and nifsMerge.py)
                obsDirList.append(objDir+'/'+DATE+'/'+header[5][0]+'/obs'+obsid)
            elif not obsDirList or not obsDirList[-1]==objDir+'/'+DATE+'/'+header[5][0]+'/obs'+obsid:
                obsDirList.append(objDir+'/'+DATE+'/'+header[5][0]+'/obs'+obsid)

    # copy science, telluric, and acquisition images to the appropriate folder
    for i in range(len(allfilelist)):
        header = getFitsHeader(allfilelist[i], fitsKeyWords)
        DATE = header[4].replace('-','')
        obsid = header[1][-3:].replace('-','')
        if header[3]=='science':
            objDir = path+'/'+header[2]
            shutil.copy(Raw+'/'+allfilelist[i], objDir+'/'+DATE+'/'+header[5][0]+'/obs'+obsid+'/')
            # make an objlist in the relevant directory
            if allfilelist[i] not in skyFrameList:
                writeList(allfilelist[i], 'objlist', objDir+'/'+DATE+'/'+header[5][0]+'/obs'+obsid+'/')
            # make a skyFrameList in the relevant directory
            if allfilelist[i] in skyFrameList:
               writeList(allfilelist[i], 'skyFrameList', objDir+'/'+DATE+'/'+header[5][0]+'/obs'+obsid+'/')

        if header[3]=='partnerCal':
            # create a Tellurics directory in objDir/YYYYMMDD/grating
            for objDir in objDirList:
                if not os.path.exists(objDir+'/'+DATE+'/'+header[5][0]+'/Tellurics'):
                    os.mkdir(objDir+'/'+DATE+'/'+header[5][0]+'/Tellurics')
                if not os.path.exists(objDir+'/'+DATE+'/'+header[5][0]+'/Tellurics/obs'+obsid):
                    os.mkdir(objDir+'/'+DATE+'/'+header[5][0]+'/Tellurics/obs'+obsid)
                    telDirList.append(objDir+'/'+DATE+'/'+header[5][0]+'/Tellurics/obs'+obsid)
                elif not telDirList or not telDirList[-1]==objDir+'/'+DATE+'/'+header[5][0]+'/Tellurics/obs'+obsid:
                    telDirList.append(objDir+'/'+DATE+'/'+header[5][0]+'/Tellurics/obs'+obsid)
                shutil.copy(Raw+'/'+allfilelist[i], objDir+'/'+DATE+'/'+header[5][0]+'/Tellurics/obs'+obsid+'/')
                # make a tellist in the relevant directory
                if allfilelist[i] not in telskyFrameList:
                    writeList(allfilelist[i], 'tellist', objDir+'/'+DATE+'/'+header[5][0]+'/Tellurics/obs'+obsid+'/')
                # make a skyFrameList in the relevant telluric directory
                if allfilelist[i] in telskyFrameList:
                    writeList(allfilelist[i], 'skyFrameList', objDir+'/'+DATE+'/'+header[5][0]+'/Tellurics/obs'+obsid+'/')

        if i!=(len(allfilelist)-1):
            header2= getFitsHeader(allfilelist[i+1], fitsKeyWords)
        if header[3]=='acq' and header2[3]=='science': #or header[3]=='acqCal' and header2[3]=='partnerCal':
            # create an Acquisitions directory in objDir/YYYYMMDD/grating
            if not os.path.exists(header2[2]+'/'+DATE+'/'+header[5][0]+'/Acquisitions/'):
                os.mkdir(header2[2]+'/'+DATE+'/'+header[5][0]+'/Acquisitions/')
            shutil.copy(Raw+'/'+allfilelist[i], header2[2]+'/'+DATE+'/'+header[5][0]+'/Acquisitions/')

    os.chdir(path)

    return objDateGratingList, objDirList, obsDirList, telDirList

#----------------------------------------------------------------------------------------#

def sortCalsGem(arcdarklist, arclist, flatlist, flatdarklist, ronchilist, dateObjList, objDirList, obsidDateList):

    """Sort calibrations into the appropriate directory based on date.
    """
    calDirList = []

    path = os.getcwd()
    Raw = path+'/Raw'

    fitsKeyWords = ['OBSID', 'OBSCLASS', 'DATE']

    # create Calibrations directories in each of the observation date directories (ie. YYYYMMDD/Calibrations)
    for item in dateObjList:
        if not os.path.exists(path+'/'+item[0]+'/'+item[1]+'/Calibrations'):
            os.mkdir(path+'/'+item[0]+'/'+item[1]+'/Calibrations')
            calDirList.append(path+'/'+item[0]+'/'+item[1]+'/Calibrations')
        elif not calDirList or not calDirList[-1]==path+'/'+item[0]+'/'+item[1]+'/Calibrations':
            calDirList.append(path+'/'+item[0]+'/'+item[1]+'/Calibrations')



    # sort lamps on flats
    for entry in flatlist:
        header = getFitsHeader(entry, fitsKeyWords)
        DATE = header[3].replace('-','')
        for obj in objDirList:
            if obsidDateList:
                for item in obsidDateList:
                    if header[1] in item:
                        DATE = item[0]
            path1 = obj+'/'+DATE+'/Calibrations/'
            shutil.copy(Raw+'/'+entry, path1)
            # create a flatlist in the relevant directory
            writeList(entry, 'flatlist', path1)

    # sort lamps off flats
    for entry in flatdarklist:
        header = getFitsHeader(entry, fitsKeyWords)
        DATE = header[3].replace('-','')
        for obj in objDirList:
            if obsidDateList:
                for item in obsidDateList:
                    if header[1] in item:
                        DATE = item[0]
            path1 = obj+'/'+DATE+'/Calibrations/'
            shutil.copy(Raw+'/'+entry, path1)
            # create a flatdarklist in the relevant directory
            writeList(entry, 'flatdarklist', path1)

    # sort ronchi flats
    for entry in ronchilist:
        header = getFitsHeader(entry, fitsKeyWords)
        DATE = header[3].replace('-','')
        for obj in objDirList:
            if obsidDateList:
                for item in obsidDateList:
                    if header[1] in item:
                        DATE = item[0]
            path1 = obj+'/'+DATE+'/Calibrations/'
            shutil.copy(Raw+'/'+entry, path1)
            # create a ronchilist in the relevant directory
            writeList(entry, 'ronchilist', path1)

    # sort arcs
    for entry in arclist:
        header = getFitsHeader(entry, fitsKeyWords)
        DATE = header[3].replace('-','')
        for obj in objDirList:
            path1 = obj+'/'+DATE+'/Calibrations/'
            shutil.copy(Raw+'/'+entry,path1)
            # create an arclist in the relevant directory
            writeList(entry, 'arclist', path1)

    # sort arc darks
    for entry in arcdarklist:
        header = getFitsHeader(entry, fitsKeyWords)
        DATE = header[3].replace('-','')
        for obj in objDirList:
            if obsidDateList:
                for item in obsidDateList:
                    if header[1] in item:
                        DATE = item[0]
            path1 = obj+'/'+DATE+'/Calibrations/'
            shutil.copy(Raw+'/'+entry,path1)
            # create an arcdarklist in the relevant directory
            writeList(entry, 'arcdarklist', path1)

    os.chdir(path)

    return calDirList

#----------------------------------------------------------------------------------------#

def getProgram(program, date, over):

    """Copies all the science, acquisition, and telluric images for a given program to the Raw directory.
    """
    rawfiles = []
    missingRaw = []
    filelist = []
    skyFrameList = []
    telskyFrameList = []

    if date:
        url = '/net/mko-nfs/sci/dataflow/'+program+'/'+date+'/OBJECT'
    else:
        # internal site where observations can be found
        url = '/net/mko-nfs/sci/dataflow/'+program+'/OBJECT'

    # find and create a list of all the .fits files from a given night
    allfilelist = checkQAPIreq(getUrlFiles(url, 'file'))

    if allfilelist:
        # check to make sure that the program ID matches the OBSID in the science headers
        checkEntry(program, 'program', allfilelist)
    else:
        print '\n Either no files found or the PI and QI requirements have not been met. \n'
        raise SystemExit

    # check to make sure that all telluric and acquisition files were taken on the same night as science data and removes the ones that weren't
    removelist = checkDate(allfilelist)
    if removelist:
        for entry in removelist:
            allfilelist.remove(entry)

    # make a directory called Raw if one does not already exist
    path = os.getcwd()

    if not os.path.exists(path+'/Raw'):
        os.mkdir(path+'/Raw')
    Raw = path+'/Raw'

    # copy the files in allfilelist to the Raw directory, first checking if over is set and if the files have already been copied
    checkOverCopy(allfilelist, Raw, over)

    # make a list of all images excluding acq images (getCals cannot use acq images)
    for entry in allfilelist:
        fitsKeyWords= ["OBSCLASS", "DATE"]
        headerList = getFitsHeader(entry,fitsKeyWords)
        if not headerList[1]=='acq':
            filelist.append(entry)

    # make a list of all the sky images (science and telluric)
    for entry in allfilelist:
        fitsKeyWords = ['OBSCLASS', 'POFFSET', 'QOFFSET']
        header = getFitsHeader(entry, fitsKeyWords)
        if header[1] == 'science':
            rad = math.sqrt(header[2]**2 + header[3]**2)
            if rad > 3.0:
                skyFrameList.append(entry)
        if header[1] == 'partnerCal':
            rad = math.sqrt(header[2]**2 + header[3]**2)
            if rad > 2.5:
                telskyFrameList.append(entry)

    return allfilelist, filelist, skyFrameList, telskyFrameList

#----------------------------------------------------------------------------------------#

def getScience(date, over):

    """Copies all the science, acquisition, and telluric images for a given date to the Raw directory.
    """
    allfilelist = []
    filelist = []
    templist = []
    datelist = []
    skyFrameList = []
    telskyFrameList = []

    # internal site where observations can be found
    url = 'http://fits/xmlfilelist/summary/'+date+'/NIFS/OBJECT'

    # find and create a list of all the .fits files from a given night, checking the QA and PI requirements
    templist = checkQAPIreq(getUrlFiles(url, 'file'))

    # identify the images by obsclass makes a listed list of filename, obsclass, and obsid
    fitsKeyWords = ['OBSCLASS', 'OBSID', 'DATE', 'OBJECT']
    for entry in templist:
        header = getFitsHeader(entry, fitsKeyWords)
        if header[1] == 'science':
            obsid = header[2]
            break

    url2 = 'http://fits/xmlfilelist/summary/'+date+'/NIFS/OBJECT/'+obsid[:-2]
    allfilelist = checkQAPIreq(getUrlFiles(url, 'file'))

    # check to make sure that all telluric and acquisition files were taken on the same night as science data and removes the ones that weren't
    removelist = checkDate(allfilelist)
    if removelist:
        for entry in removelist:
            allfilelist.remove(entry)

    # make a list of all the sky images
    for entry in allfilelist:
        fitsKeyWords = ['OBSCLASS', 'POFFSET', 'QOFFSET']
        header = getFitsHeader(entry, fitsKeyWords)
        if header[1] == 'science':
            rad = math.sqrt(header[2]**2 + header[3]**2)
            if rad > 3.0:
                skyFrameList.append(entry)
        if header[1] == 'partnerCal':
            rad = math.sqrt(header[2]**2 + header[3]**2)
            if rad > 2.5:
                telskyFrameList.append(entry)
        if header[1]!='acq':
            filelist.append(entry)

    # path to data archive
    raw = '/net/mko-nfs/sci/dataflow'


    # make a directory called Raw if one does not already exist
    path = os.getcwd()

    if not os.path.exists(path+'/Raw'):
        Raw = os.mkdir(path+'/Raw')

    Raw = path+'/Raw'

    # copy all science images from a given night into ./Raw/
    checkOverCopy(allfilelist, Raw, over)

    return allfilelist, filelist, skyFrameList, telskyFrameList

#----------------------------------------------------------------------------------------#

def getCals(filelist, over):

    """Copies the necessary calibration files to the Raw directory using
    http://fits/calmgr to match calibrations frames to science frames.
    """
    # path to data archive
    raw = '/net/mko-nfs/sci/dataflow'

    # make a directory called Raw if one does not already exist
    path = os.getcwd()

    if os.path.exists(path+'/Raw'):
        Raw = path+'/Raw'
    else:
       Raw = os.mkdir(path+'/Raw')

    # find lamps on, lamps off, and ronchi flats
    flatlist, flatdarklist, ronchilist, obsidlist, obsidDateList = getFlat(filelist)
    # copy flats and  to Calibrations
    checkOverCopy(flatlist, Raw, over)
    checkOverCopy(flatdarklist, Raw, over)
    checkOverCopy(ronchilist, Raw, over)

    # find arc and arc darks
    arclist, arcdarklist = getArc(filelist, obsidlist)
    # copy arc to Calibrations
    checkOverCopy(arclist, Raw, over)
    checkOverCopy(arcdarklist, Raw, over)

    templist = flatlist+flatdarklist
    flatlist = []
    flatdarklist = []
    for entry in templist:
        header = astropy.io.fits.open(Raw+'/'+entry)

        obstype = header[0].header['OBSTYPE'].strip()  # used to sort out the acqs and acqCals in the trap
        aper = header[0].header['APERTURE']

        if obstype == 'FLAT' and not aper=='Ronchi_Screen_G5615':
            # open the image and store pixel values in an array
            array = astropy.io.fits.getdata(Raw+'/'+entry)
            # then this takes the mean of all of them
            mean_counts = np.mean(array)

            # once we've stored that to the variable we can use this conditional
            # to check whether the frame is a sky or an object based on the counts
            # 2000.0 is an arbitrary threshold that appears to work well.
            if mean_counts < 2000.0:
                flatdarklist.append(entry)
            else:
                flatlist.append(entry)

    return arclist, arcdarklist, flatlist, flatdarklist, ronchilist, obsidDateList

#----------------------------------------------------------------------------------------#

def getArc(filelist, obsidlist):

    """Finds and returns a list of arcs and arc darks to use to reduce the science data.
    """
    templist = []
    arclist = []
    arcdarklist = []
    obsid2list = []

    # find all the different obsid's
    for i in range(len(filelist)):
        url = 'http://fits/calmgr/arc/'+filelist[i]
        file1 = getUrlFiles(url, 'calibration')
        if i==0 or not arclist[-1]==file1[0]:
            arclist.append(file1[0])

    fitsKeyWords= ["OBSID", "RAWPIREQ","RAWGEMQA", 'DATE']

    # find all the obsid's and dates of the arcs
    for entry in templist:
        headerList = getFitsHeader(entry,fitsKeyWords)
        obsid2 = headerList[1]
        obsid2list.append(obsid2)
        datelist.append(headerList[4].replace('-',''))

    # check to make sure that the arcs meet the PI and QA requirements
    for entry in arclist:
        headerList = getFitsHeader(entry, fitsKeyWords)
        rawPIreq = headerList[2]
        rawGemQA = headerList[3]
        if rawPIreq in ["YES","UNKNOWN"] and rawGemQA in ["USABLE","UNKNOWN"]:
            pass
        else:
            print 'Arc\'s QA not PASS or UNKNOWN so skipped'

    # find arc darks
    # first check if there are arc darks in the same observing program as the arc(s)
    for obsid2 in obsid2list:
        for date in datelist:
            url = 'http://fits/xmlfilelist/summary/'+obsid2+'/DARK/'+date
            tempdarklist = getUrlFiles(url, 'file')
            for item in tempdarklist:
                arcdarklist.append(item)

    # if not arc darks were found above, use the arc darks taken in the daycal program
    if not arcdarklist:
        for obsid in obsidlist:
            url = 'http://fits/xmlfilelist/summary/'+obsid+'/DARK'
            tempdarklist = getUrlFiles(url, 'file')
            for item in tempdarklist:
                arcdarklist.append(item)

    return arclist, arcdarklist

#----------------------------------------------------------------------------------------#

def getFlat(filelist):

    """Finds and returns a list of flats (lamps on, lamps off, and ronchi) to use to
    reduce the science data.
    """

    templist = []
    flatlist = []
    flatdarklist = []
    obsidlist = []
    ronchilist = []
    flattemp = []
    obsidDateList = []

    fitsKeyWords = ['DATE', 'OBSID']

    #find first flat for each image and record the obsids of the science image and the flat
    for i in range(len(filelist)):
        url = 'http://fits/calmgr/flat/'+filelist[i]
        file1 = str(getUrlFiles(url, 'calibration'))
        file1 = file1[2:-2]
        if i==0 or not templist[-1]==file1:
            templist.append(file1)
        header1 = getFitsHeader(filelist[i], fitsKeyWords)
        header2 = getFitsHeader(file1, fitsKeyWords)
        date = header1[1]
        obsid = header2[2]
        list1 = [date.replace('-',''), obsid]
        if date!=header2[2]:
            if not obsidDateList or not obsidDateList[-1]==list1:
                obsidDateList.append(list1)

    for entry in templist:
        fitsKeyWords = ['OBSID', 'GCALSHUT', 'OBSCLASS']
        headerList = getFitsHeader(entry, fitsKeyWords)
        obsid = headerList[1]
        obsidlist.append(obsid)
        url2 = 'http://fits/xmlfilelist/summary/'+obsid+'/FLAT'
        tempflatlist = getUrlFiles(url2, 'file')
        for item in tempflatlist:
            flattemp.append(item)

    # use the obsid of the first flat to find the other lamps on flats and lamps off flats
    for entry in flattemp:
       fitsKeyWords = ['GCALSHUT']
       header = getFitsHeader(entry, fitsKeyWords)
       # differentiate between lamps on and lamps off flats by looking for "OPEN"(lamps on) or "CLOSED"(lamps off) for GCALSHUT in the fits header
       if header[1] == 'OPEN':
           flatlist.append(entry)
       else:
           flatdarklist.append(entry)

    # use the obsid to find ronchi flats
    for obsid in obsidlist:
        url3 = 'http://fits/xmlfilelist/summary/'+obsid+'/RONCHI'
        tempronchilist = getUrlFiles(url3, 'file')
        for item in tempronchilist:
            ronchilist.append(item)

    return flatlist, flatdarklist, ronchilist, obsidlist, obsidDateList

#----------------------------------------------------------------------------------------#

if __name__ == '__main__':
    print "gemini_sort"
