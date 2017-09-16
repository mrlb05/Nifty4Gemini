Preparing the .json Input File
==============================

**NOTE: This document is out of date. We are now using .cfg files. See
http://www.voidspace.org.uk/python/configobj.html for instructions on preparing the
new config format.**

For now we're using .json files to provide input to *Nifty*. This may not be an
optimal solution, my main worries being lack of comments in .json files and that
.json files can be difficult to edit by hand.

When preparing input files by hand there are a few things you should keep in mind:

Capitalization of Booleans
--------------------------

In Python, the Boolean values are **True** and **False** with *Capital T and Capital F*.
In JSON the Boolean values are *true* and *false* with *lower case t and lower case f*

Trailing Commas
---------------

The last parameter in a .json file **SHOULD NOT** be followed by a comma!

None vs null
------------

If you're trying to use None in a .json file... That will not work. Use **none**
instead, with a lowercase t.
