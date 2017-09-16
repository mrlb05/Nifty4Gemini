Merging Data Cubes
==================

Nifty offers a few ways to merge data cubes. These are all contained in the
nifsMerge.py script.

**Note:** If cubes are not transposed each call to iraf.imcombine() can take
25 minutes or more. The current implementation is much slower at combining when cubes
have a y-offset.

Cubes Were Shifted by Hand with QFitsView or Similar
----------------------------------------------------
A user can shift cubes by hand and add the prefix "shift" to the cube name. The
pipeline will automatically find these cubes and combine them with gemcube.

If no "shift"-prefixed cubes exist the user has two more choices to make. The first is to
generate offsets automatically or to provide an offsets file by hand.

Generating an offsets.txt File
------------------------------
If use_pq_offsets is true, *Nifty* will determine offsets automatically from the
POFFSET and QOFFSET entry of each cubes .fits header. Otherwise, *Nifty* will pause
and wait for you to provide a suitably formatted offsets.txt file in the
scienceObjectName/Merged/date_obsid/ directory.

Using iraf.im3dtran()
---------------------
Cubes have been found to combine 50 times faster when the y and lambda axis are
swapped with iraf.im3dtran(). In our tests we found it took ~25 minutes to merge
cubes without transposition and ~0.5 minutes to merge cubes in a tranposed state.

We have found the cubes produced with and without tranposition to be identical. We
have made the default not to use transposition but we urge further testing.
