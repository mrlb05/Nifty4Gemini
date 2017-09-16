
# Old nifsSort.py functions.

#-----------------------------------------------------------------------------#

def getPaths(allfilelist, objectDateGratingList, sciImageList, dir):

    """Creates lists of Calibrations, science observations
    and Tellurics/ directories.

    """

    obsDirList = []
    calDirList = []
    telDirList = []

    # Modify allfilelist to remove sorted/not sorted flag data used in previous steps.
    '''tempList = []
    for i in range(len(allfilelist)):
         tempList.append(allfilelist[i][0])
    allfilelist = tempList'''

    path = os.getcwd()
    if dir:
        Raw = dir
    else:
        Raw = path+'/Raw'

    logging.info("\nGetting list of paths to science observations.")
    for i in range(len(allfilelist)):
        # Make a 2D list of paths to science observations and the time of each one.
        header = astropy.io.fits.open(Raw+'/'+allfilelist[i][0])

        obstype = header[0].header['OBSTYPE'].strip()
        obsid = header[0].header['OBSID']
        grat = header[0].header['GRATING'][0:1]
        date = header[0].header[ 'DATE'].replace('-','')
        obsclass = header[0].header['OBSCLASS']
        obj = header[0].header['OBJECT'].replace(' ','')
        time = timeCalc(Raw+'/'+allfilelist[i][0])

        if obsclass=='science':
            objDir = path+'/'+obj
            path1 = (objDir+'/'+date+'/'+grat+'/obs'+obsid[-3:].replace('-',''))
            if not obsDirList or not obsDirList[-1][1]==path1:
                obsDirList.append([[time], path1])
            elif obsDirList[-1][1] == path1:
                obsDirList[-1][0].append(time)
            allfilelist[i][1] = 0

    # Get list of paths to Tellurics/ot_observation_id directories.
    logging.info("\nGetting list of paths to telluric observations.")
    for i in range(len(allfilelist)):
        header = astropy.io.fits.open(Raw+'/'+allfilelist[i][0])

        obstype = header[0].header['OBSTYPE'].strip()
        obsid = header[0].header['OBSID'][-3:].replace('-','')
        grat = header[0].header['GRATING'][0:1]
        date = header[0].header[ 'DATE'].replace('-','')
        obsclass = header[0].header['OBSCLASS']
        obj = header[0].header['OBJECT'].replace(' ', '')
        telluric_time = timeCalc(Raw+'/'+allfilelist[i][0])

        # Match tellurics to science data by date, grating and time.
        if obsclass=='partnerCal':
            logging.info(allfilelist[i][0])
            timeList = []
            for k in range(len(obsDirList)):
                # Make sure date and gratings match.
                tempDir = obsDirList[k][1].split(os.sep)
                if date in tempDir and grat in tempDir:
                    # Open the times of all science images in obsDirList[k][0].
                    times = obsDirList[k][0]
                    # Find difference in each time from the telluric frame we're trying to sort.
                    diffList = []
                    for b in range(len(times)):
                        difference = abs(telluric_time-obsDirList[k][0][b])
                        templist = []
                        templist.append(difference)
                        templist.append(obsDirList[k][1])
                        diffList.append(templist)
                    # Find the science image with the smallest difference.
                    minDiff = min(diffList)
                    # Pass that time and path out of the for loop.
                    timeList.append(minDiff)
            # Out of the for loop, compare min times from different directories.
            if timeList:
                closest_time = min(timeList)
                # Copy the telluric frame to the path of that science image.
                path_to_science_dir = closest_time[1]
                path_to_tellurics = os.path.split(path_to_science_dir)[0]
                if not telDirList or telDirList[-1] != path_to_tellurics+'/Tellurics/obs'+obsid:
                    telDirList.append(path_to_tellurics+'/Tellurics/obs'+obsid)

    # Append Calibrations directories to the calDirList (ie. YYYYMMDD/Calibrations).
    for item in objectDateGratingList:
            Calibrations = (path+'/'+item[0]+'/'+item[1]+'/Calibrations_'+item[2])
            calDirList.append(Calibrations)


    # ---------------------------- Tests ------------------------------------- #


    # Check that each science observation has valid telluric data.
    logging.info("\nChecking that each science observation has valid telluric data.")
    # For each science observation:
    for i in range(len(obsDirList)):
        os.chdir(obsDirList[i][1])
        # Store science observation name in science_observation_name
        science_observation_name = obsDirList[i][1].split(os.sep)[-1]
        # Optional: store time of a science frame in science_time.
        try:
            scienceFrameList = open('scienceFrameList', "r").readlines()
        except IOError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: science "+str(science_observation_name))
            logging.info("                      does not contain science images.")
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")


            scienceFrameList = open('skyFrameList', "r").readlines()
        scienceFrameList = [image.strip() for image in scienceFrameList]

        # Open image and get science image grating from header.
        science_image = scienceFrameList[0]
        science_header = astropy.io.fits.open('./'+ science_image + '.fits')
        science_time = timeCalc(science_image+'.fits')
        science_date = science_header[0].header[ 'DATE'].replace('-','')

        # Check that directory obsname matches header obsname.
        temp_obs_name = 'obs' + science_header[0].header['OBSID'][-3:].replace('-','')
        if science_observation_name != temp_obs_name:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: science "+ str(science_observation_name)+ " :")
            logging.info("                      observation name data in headers and directory")
            logging.info("                      do not match.")
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")

        # Check that a tellurics directory exists.
        if os.path.exists('../Tellurics/'):
            os.chdir('../Tellurics/')
        else:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: telluric directory for science "+str(science_observation_name))
            logging.info("                      does not exist.")
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")

        found_telluric_flag = False

        # Iterate through tellurics observation directories.
        for directory in list(glob.glob('obs*')):
            os.chdir('./'+directory)
            # Check that a file, scienceMatchedTellsList exists.
            try:
                scienceMatchedTellsList = open('scienceMatchedTellsList', "r").readlines()
                # Check that the science observation name is in the file.
                # Check that immediately after is at least one telluric image name.
                # Do this by checking for the science date in the telluric name.
                for i in range(len(scienceMatchedTellsList)):
                    telluric_observation_name = scienceMatchedTellsList[i].strip()
                    if telluric_observation_name == science_observation_name:
                        if science_date in scienceMatchedTellsList[i+1].strip():
                            found_telluric_flag = True
                            break
            except IOError:
                pass

            if found_telluric_flag:
                os.chdir('../')
                break
            else:
                os.chdir('../')

        if not found_telluric_flag:
            os.chdir('../')
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: no tellurics data found for science "+str(science_observation_name))
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")


        else:
            logging.info("\nFound telluric data for all science observations.")
        # TO DO:
        # Optional: open that telluric image and store time in telluric_time
        # Check that abs(telluric_time - science_time) < 1.5 hours

    os.chdir(path)

    # Check that each science directory exists and has associated calibration data.
    # Pseudocode (repeated below with actual code):
    # For each science directory, make sure that:
    # a calibrations directory is present.
    # flatlist exists and has more than one file.
    # flatdarklist exists and has more than one file.
    # arclist exists and has more than one file.
    # arcdarklist exists and has more than one file.
    # ronchilist exists and has more than one file.

    logging.info("\nChecking that each science image has required calibration data. ")
    # For each science image, read its header data and try to change to the appropriate directory.
    # Check that:
    for i in range(len(sciImageList)):
        header = astropy.io.fits.open(dir+sciImageList[i])

        obstype = header[0].header['OBSTYPE'].strip()
        obsid = header[0].header['OBSID'][-3:].replace('-','')
        grat = header[0].header['GRATING'][0:1]
        date = header[0].header[ 'DATE'].replace('-','')
        obsclass = header[0].header['OBSCLASS']
        obj = header[0].header['OBJECT'].replace(' ','')

        # a science and Calibrations directory are present.
        try:
            os.chdir(path+'/'+obj+'/'+date+'/'+grat+'/obs'+obsid+'/')
            os.chdir('../../Calibrations_'+grat+'/')
        except OSError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: no Calibrations directory found for ")
            logging.info("                      science frame "+str(sciImageList[i]))
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")
            continue

        # flatlist exists and has more than one file.
        try:
            flatlist = open('flatlist', "r").readlines()
            if len(flatlist) <= 1:
                logging.info("\n#####################################################################")
                logging.info("#####################################################################")
                logging.info("")
                logging.info("     WARNING in sort: only 1 lamps on flat frame found for science")
                logging.info("                      frame "+str(sciImageList[i]))
                logging.info("")
                logging.info("#####################################################################")
                logging.info("#####################################################################\n")
        except OSError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: no flatlist found for science frame")
            logging.info("                      "+str(sciImageList[i]))
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")

        # flatdarklist exists and has more than one file.
        try:
            flatdarklist = open('flatdarklist', "r").readlines()
            if len(flatdarklist) <= 1:
                logging.info("\n#####################################################################")
                logging.info("#####################################################################")
                logging.info("")
                logging.info("     WARNING in sort: only 1 lamps off flat frame found for science")
                logging.info("                      frame "+str(sciImageList[i]))
                logging.info("")
                logging.info("#####################################################################")
                logging.info("#####################################################################\n")
        except OSError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: no flatdarklist found for science frame")
            logging.info("                      "+str(sciImageList[i]))
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")

        # arclist exists and has more than one file.
        try:
            arclist = open('arclist', "r").readlines()
            if len(arclist) <= 1:
                logging.info("\n#####################################################################")
                logging.info("#####################################################################")
                logging.info("")
                logging.info("     WARNING in sort: only 1 arc frame found for science frame")
                logging.info("                      "+str(sciImageList[i]))
                logging.info("")
                logging.info("#####################################################################")
                logging.info("#####################################################################\n")
        except OSError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: no arclist found for science frame")
            logging.info("                      "+str(sciImageList[i]))
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")

        # arcdarklist exists and has more than one file.
        try:
            arcdarklist = open('arcdarklist', "r").readlines()
            if len(arcdarklist) <= 1:
                logging.info("\n#####################################################################")
                logging.info("#####################################################################")
                logging.info("")
                logging.info("     WARNING in sort: only 1 dark arc frame found for science frame")
                logging.info("                      "+str(sciImageList[i]))
                logging.info("")
                logging.info("#####################################################################")
                logging.info("#####################################################################\n")
        except OSError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: no arcdarklist found for science frame")
            logging.info("                      "+ str(sciImageList[i]))
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")

        # ronchilist exists and has more than one file.
        try:
            ronchilist = open('ronchilist', "r").readlines()
            if len(ronchilist) <= 1:
                logging.info("\n#####################################################################")
                logging.info("#####################################################################")
                logging.info("")
                logging.info("     WARNING in sort: only 1 ronchi flat frame found for science frame")
                logging.info("                      " + str(sciImageList[i]))
                logging.info("")
                logging.info("#####################################################################")
                logging.info("#####################################################################\n")
        except OSError:
            logging.info("\n#####################################################################")
            logging.info("#####################################################################")
            logging.info("")
            logging.info("     WARNING in sort: no ronchilist found for science frame")
            logging.info("                      " + str(sciImageList[i]))
            logging.info("")
            logging.info("#####################################################################")
            logging.info("#####################################################################\n")

        os.chdir(path)

    logging.info("Done checking that each science image has required calibration data.\n")

    # Check to see what files were copied.
    logging.info("\nChecking for non-copied science, tellurics and acquisitions.\n")
    for i in range(len(allfilelist)):
        # Check the copied flag. If not 0, logging.info("the entry.")
        if allfilelist[i][1] != 0:
            logging.info(str(allfilelist[i][0]) + " " + str(allfilelist[i][2]) +  " was not copied.")
    logging.info("\nEnd non-copied science, tellurics and acquisitions.\n")

    # Check that all science frames were copied.
    count_from_raw_files = len(sciImageList)

    count = 0
    for i in range(len(obsDirList)):
        for file in os.listdir(obsDirList[i][1]):
            if file.endswith('.fits'):
                count += 1

    if count_from_raw_files != count:
        logging.info("\nWARNING: "+ str(count_from_raw_files - count) + " science images (or sky frames) \
        were not copied.\n")
    else:
        logging.info("\nExpected number of science and sky frames copied.\n")

    # ---------------------------- End Tests --------------------------------- #

    # Modify obsDirList to remove extra time information.
    tempList = []
    for i in range(len(obsDirList)):
        tempList.append(obsDirList[i][1])
    obsDirList = tempList

    os.chdir(path)


    return obsDirList, calDirList, telDirList


# ---------------------------------------------------------------------------- #

# Old nifsMerge.py code.


def mergeOld(obsDirList, over=""):
    path = os.getcwd()
    cubelist = []
    mergedCubes = []
    obsidlist = []
    pixScaleX = 0.05
    pixScaleY = 0.043
    # Set up the logging file
    FORMAT = '%(asctime)s %(message)s'
    DATEFMT = datefmt()
    logging.basicConfig(filename='Nifty.log',format=FORMAT,datefmt=DATEFMT,level=logging.DEBUG)
    log = os.getcwd()+'/Nifty.log'
    logging.info('###############################')
    logging.info('#                             #')
    logging.info('#         Start Merge         #')
    logging.info('#                             #')
    logging.info('###############################')
    print '###############################'
    print '#                             #'
    print '#         Start Merge         #'
    print '#                             #'
    print '###############################'
    # Unlearn the used tasks
    iraf.unlearn(iraf.gemini,iraf.gemtools,iraf.gnirs,iraf.nifs)
    # Prepare the package for NIFS
    iraf.nsheaders("nifs",logfile=log)
    iraf.set(stdimage='imt2048')
    user_clobber=iraf.envget("clobber")
    iraf.reset(clobber='yes')
    # change to the directory in iraf
    iraffunctions.chdir(path)
    for obsDir in obsDirList:
        temp1 = os.path.split(obsDir)
        temp2 = os.path.split(temp1[0])
        temp3 = os.path.split(temp2[0])
        temp4 = os.path.split(temp3[0])
        objname = temp4[1]
        date = temp3[1]
        obsid = temp1[1]
        obsPath = temp3[0]
        os.chdir(obsDir)
        obsidlist.append(date+'_'+obsid)
        # create a directory called Merged and copy all the data cubes to this directory
        if not os.path.exists(obsPath+'/Merged/'):
            os.mkdir(obsPath+'/Merged/')
        Merged = obsPath+'/Merged'
        if not os.path.exists(Merged+'/'+date+'_'+obsid):
            os.mkdir(Merged+'/'+date+'_'+obsid)
        # if a list called shiftedcubes already exists then just merge those shifted cubes and continue
        if glob.glob("./shif*.fits"):
            if over:
                if os.path.exists('./'+obsid+'_merged.fits'):
                    os.remove('./'+obsid+'_merged.fits')
                    iraf.gemcube(input="shif*.fits[SCI]", output=obsid+'_merged', logfile = log)
            elif not os.path.exists('./'+obsid+'_merged.fits'):
                iraf.gemcube(input="shif*.fits[SCI]", output=obsid+'_merged', logfile = log)
            else:
                print "Output exists and -over- not set - shifted cubes are not being merged"
            shutil.copy('./'+obsid+'_merged.fits', Merged)
            if obsDir==obsDirList[-1]:
                return
            else:
                continue
        # create a list called cubes, which stores all the cubes from a particular night
        # store all the cubes lists in a list of lists called cubelist
        cubes = glob.glob('bbatfbrgnN*.fits')
        if cubes:
            cubelist.append(cubes)
            pre = 'atfbrgn'
        else:
            cubes = glob.glob('tfbrgn*.fits')
            cubelist.append(cubes)
            pre = 'tfbrgn'
        # copy cubes to their date directory within Merged
        for cube in cubes:
            if cubes.index(cube)==0:
                shutil.copy('c'+pre+cube[-19:], Merged+'/'+date+'_'+obsid)
            shutil.copy(cube, Merged+'/'+date+'_'+obsid)
    os.chdir(Merged)
    n=0
    for cubes in cubelist:
        if cubes:
            os.chdir(Merged+'/'+obsidlist[n])
            # set the zero point p and q offsets to the p and q offsets of the first cube in each sequence (assumed to have a p and q of 0)
            print cubes
            print cubelist
            header = astropy.io.fits.open(cubes[0])
            p0 = header[0].header['POFFSET']
            q0 = header[0].header['QOFFSET']
            refCube = "cube"+cubes[0][-8:-5]
            iraffunctions.chdir(os.getcwd())
            if over:
                if os.path.exists('./'+refCube+'.fits'):
                    os.remove('./'+refCube+'.fits')
                iraf.imcopy('c'+pre+cubes[0][-19:-5]+"[sci,1][*,0:62,*]", output=refCube)
            elif not os.path.exists('./'+refCube+'.fits'):
                iraf.imcopy('c'+pre+cubes[0][-19:-5]+"[sci,1][*,0:62,*]", output=refCube)
            else:
                "Output file exists and -over not set - skipping imcopy reference cube"
            fx = open('offsetsX.txt', 'w')
            fx.write('%d\t%d\t%d\n' % (0, 0, 0))
            foff = open('offsets.txt', 'w')
            foff.write('%d\t%d\t%d\n' % (0, 0, 0))
        for i in range(len(cubes)-1):
            i+=1
            header2 = astropy.io.fits.open(cubes[i])
            # find the p and q offsets of the other cubes in the sequence
            poff = header2[0].header['POFFSET']
            qoff = header2[0].header['QOFFSET']
            # find the reference pixel values of the other cubes in the sequence
            refX = header2[0].header['CRPIX1']
            refY = header2[0].header['CRPIX2']
            # calculate the difference between the zero point offsets and the offsets of the other cubes and convert that to pixels
            pShift = round((poff - p0)/pixScaleX)
            qShift = round((qoff - q0)/pixScaleY)
            # write the y offsets to a text file (used in gemcombine step)
            fy = open('offsetsY.txt', 'w')
            fy.write('%d\t%d\t%d\t\n%d\t%d\t%d\n' % (0.,0.,0.,0., qShift, 0.))
            fy.close()
            # write the x offsets to a text file (used in imcombine step)
            fx = open('offsetsX.txt', 'a')
            fx.write('%d\t%d\t%d\n' % (pShift, 0., 0.))
            fx.close()
            # write all offsets to a text file (keep in mind that the x and y offsets use different pixel scales)
            foff = open('offsets.txt', 'a')
            foff.write('%d\t%d\t%d\n' % (pShift, qShift, 0.))
            foff.close()
            suffix = cubes[i][-8:-5]
            f = open('atlist', 'w')
            f.write(cubes[0].lstrip('c')+'\n'+cubes[i].lstrip('c'))
            f.close()
            atlist = open('atlist', 'r').readlines()
            # gemcombine the 2D spectra of the zero point offset and a cube that needs to be shifted
            # executes the shift in the y direction
            if over:
                if os.path.exists('./at'+suffix+'.fits'):
                    os.remove('./at'+suffix+'.fits')
                iraf.gemcombine(listit(atlist, ""), output = "at"+suffix, combine = 'average', offsets = 'offsetsY.txt', logfile = log)
            elif not os.path.exists('./at'+suffix+'.fits'):
                iraf.gemcombine(listit(atlist, ""), output = "at"+suffix, combine = 'average', offsets = 'offsetsY.txt', logfile = log)
            else:
                print "Output file exists and -over not set - skipping gemcombine (y-shift)"
            # nifcube sometimes runs into an unpredictable error
            # the pexpect sequence below anticipates this error to avoid a crash
            if over:
                if os.path.exists('./cat'+suffix+'.fits'):
                    os.remove('./cat'+suffix+'.fits')
                child = p.spawn('pyraf')
                child.expect("")
                child.sendline('gemini')
                child.expect("")
                child.sendline('nifs')
                child.expect("")
                child.sendline("nifcube at"+suffix+" logfile="+log)
                index = child.expect(["Using input files:", "Name of science extension:"])
                if index==0:
                    pass
                elif index==1:
                    child.sendline('SCI')
                child.expect("NIFCUBE  Exit status good", timeout=100)
                child.sendline('.exit')
                print child.before
                child.interact()
            elif not os.path.exists('./cat'+suffix+'.fits'):
                child = p.spawn('pyraf')
                child.expect("")
                child.sendline('gemini')
                child.expect("")
                child.sendline('nifs')
                child.expect("")
                child.sendline("nifcube at"+suffix+" logfile="+log)
                index = child.expect(["Using input files:","Name of science extension:"])
                if index==0:
                    pass
                elif index==1:
                    child.sendline('SCI')
                child.expect("NIFCUBE  Exit status good", timeout=100)
                child.sendline('.exit')
                print child.before
                child.interact()
            else:
                print "Output file exists and -over not set - skipping nifcube"
            # need to trim the image to use in imarith
            # trim to the same dimensions and position as the zero point offset image
            # this is the part of this script that does not work for faint objects
            if over:
                if os.path.exists('./ccat'+suffix+'.fits'):
                    os.remove('./ccat'+suffix+'.fits')
                if qShift < 0.:
                    iraf.imcopy("cat"+suffix+".fits[sci,1][*,"+str(int((qShift*(-1))-1))+":"+(str(int(62+(qShift*(-1))-1)))+",*]",  output = "ccat"+suffix)
                else:
                    iraf.imcopy("cat"+suffix+".fits[sci,1][*,0:62,*]", output = "ccat"+suffix)
            elif not os.path.exists('./ccat'+suffix+'.fits'):
                if qShift < 0.:
                    iraf.imcopy("cat"+suffix+".fits[sci,1][*,"+str(int((qShift*(-1))-1))+":"+(str(int(62+(qShift*(-1))-1)))+",*]",  output = "ccat"+suffix)
                else:
                    iraf.imcopy("cat"+suffix+".fits[sci,1][*,0:62,*]", output = "ccat"+suffix)
            else:
                print "Output file exists and -over not set - skipping imcopy y-shifted cube"
            # remove the zero point offset image from the average combined data cube
            if over:
                if os.path.exists('./temp'+suffix+'.fits'):
                    os.remove('./temp'+suffix+'.fits')
                iraf.imarith(operand1 = "ccat"+suffix, operand2 = 2, op = "*", result = "temp"+suffix)
            elif not os.path.exists('./temp'+suffix+'.fits'):
                iraf.imarith(operand1 = "ccat"+suffix, operand2 = 2, op = "*", result = "temp"+suffix)
            else:
                 print "Output file exists and -over not set - skipping imarith multiplication"
            if over:
                if os.path.exists('./cube'+suffix+'.fits'):
                    os.remove('./cube'+suffix+'.fits')
                iraf.imarith(operand1 = "temp"+suffix, operand2 = refCube, op = "-", result = "cube"+suffix)
            elif not os.path.exists('./cube'+suffix+'.fits'):
                iraf.imarith(operand1 = "temp"+suffix, operand2 = refCube, op = "-", result = "cube"+suffix)
            else:
                print "Output file exists and -over not set - skipping imarith subtraction"
        # sum all the y shifted data cubes and zero point offset cube
        # x shift is done in this step
        if over:
            if os.path.exists('./'+obsidlist[n]+'_merged.fits'):
                os.remove('./'+obsidlist[n]+'_merged.fits')
            iraf.imcombine("cube*.fits", output = obsidlist[n]+'_merged',  combine = 'sum', offsets = 'offsetsX.txt', logfile = log)
        elif not os.path.exists('./'+obsidlist[n]+'_merged.fits'):
            iraf.imcombine("cube*.fits", output = obsidlist[n]+'_merged',  combine = 'sum', offsets = 'offsetsX.txt', logfile = log)
        else:
            print "Output file exists and -over not set - skipping imcombine (x-shift)"
        mergedCubes.append(obsidlist[n]+'_merged')
        n+=1
    os.chdir(Merged)
    # copy the merged observation sequence data cubes to the Merged directory
    for i in range(len(mergedCubes)):
        shutil.copy(Merged+'/'+obsidlist[i]+'/'+mergedCubes[i]+'.fits', './')
    # merge all the individual merged observation sequence data cubes
    if len(mergedCubes)>1:
        iraf.imcombine("*_obs*_merged.fits", output = objname+'_merged.fits', combine = 'sum')


# ------------------------- nifsUtils ----------------------------------------- #


def OLD_makeSkyList(skyFrameList, objlist, obsDir):
    """ check to see if the number of sky images matches the number of science
        images and if not duplicates sky images and rewrites the sky file and skyFrameList
    """

    objtime = []
    skytime = []
    b = ['bbbbbbbbbbbb']
    for item in objlist:
        item = str(item).strip()
        otime = timeCalc(item+'.fits')
        objtime.append(otime)
    for sky in skyFrameList:
        sky = str(sky).strip()
        stime = timeCalc(sky+'.fits')
        skytime.append(stime)
    logging.info(skytime)
    logging.info(objtime)

    templist = []
    for time in objtime:
        difflist = []
        for stime in skytime:
            difflist.append(abs(time-stime))
        ind = difflist.index(min(difflist))
        if templist and skyFrameList[ind] in templist[-1]:
            n+=1
            templist.append(skyFrameList[ind])
        else:
            n=0
            templist.append(skyFrameList[ind])
        writeList(skyFrameList[ind]+b[0][:n], 'skyFrameList', obsDir)
        if n>0:
            shutil.copyfile(skyFrameList[ind]+'.fits', skyFrameList[ind]+b[0][:n]+'.fits')
    '''
    for i in range(len(skyFrameList)-1):
        n=0
        for j in range(len(objtime)):
            if abs(skytime[i]-objtime[j])<abs(skytime[i+1]-objtime[j]):
                logging.info(skyFrameList[i]+b[0][:n])
                writeList(skyFrameList[i]+b[0][:n], 'skyFrameList', obsDir)
                if n>0:
                    shutil.copyfile(skyFrameList[i]+'.fits', skyFrameList[i]+b[0][:n]+'.fits')
                n+=1
    '''
    skyFrameList = open("skyFrameList", "r").readlines()
    skyFrameList = [image.strip() for image in skyFrameList]
    return skyFrameList

# ---------------------------------------------------------------------------- #

def OLD_writeCenters(objlist):
    """Write centers to a text file, load that textfile into list centers and
        return that list. """

    centers = []
    for image in objlist:
        header = astropy.io.fits.open(image+'.fits')
        poff = header[0].header['XOFFSET']
        qoff = header[0].header['YOFFSET']
        if objlist.index(image)==0:
            P0 = poff
            Q0 = qoff
            f=open('offsets', 'w')
            f.write(str(0)+'\t'+str(0)+'\n')
        else:
            f=open('offsets', 'a')
            f.write(str(P0-poff)+'\t'+str(Q0-qoff)+'\n')
    f.close()

    offlist = open('offsets', 'r').readlines()
    for line in offlist:
        centers.append([((float(line.split()[0])/5.0)/.1)+14.5, ((float(line.split()[1])/1.0)/.04)+34.5])

    return centers
# ---------------------------------------------------------------------------- #

def OBSOLETE_loadSortSave():
    """Opens and reads lists of:
        - Science directories,
        - Telluric directories, and
        - Calibration directories
        from runtimeData/scienceDirectoryList.txt, runtimeData/telluricDirectoryList.txt and runtimeData/calibrationDirectoryList.txt in
        the main Nifty directory.
    """
    # Don't use sortScript at all; read the paths to data from textfiles.
    # Load telluric observation directories.
    try:
        telDirList = open("runtimeData/telluricDirectoryList.txt", "r").readlines()
        telDirList = [entry.strip() for entry in telDirList]
    except IOError:
        logging.info("\n#####################################################################")
        logging.info("#####################################################################")
        logging.info("")
        logging.info("     WARNING in Nifty: no telluric data found. Setting telDirList to ")
        logging.info("                       an empty list.")
        logging.info("")
        logging.info("#####################################################################")
        logging.info("#####################################################################\n")
        telDirList = []
    # Load science observation directories.
    try:
        obsDirList = open("runtimeData/scienceDirectoryList.txt", "r").readlines()
        obsDirList = [entry.strip() for entry in obsDirList]
    except IOError:
        logging.info("\n#####################################################################")
        logging.info("#####################################################################")
        logging.info("")
        logging.info("     WARNING in Nifty: no science data found. Setting obsDirList to ")
        logging.info("                       an empty list.")
        logging.info("")
        logging.info("#####################################################################")
        logging.info("#####################################################################\n")
        obsDirList = []
    # Load calibration directories.
    try:
        calDirList = open("runtimeData/calibrationDirectoryList.txt", "r").readlines()
        calDirList = [entry.strip() for entry in calDirList]
    except IOError:
        logging.info("\n#####################################################################")
        logging.info("#####################################################################")
        logging.info("")
        logging.info("     WARNING in Nifty: no science data found. Setting calDirList to ")
        logging.info("                       an empty list.")
        logging.info("")
        logging.info("#####################################################################")
        logging.info("#####################################################################\n")
        calDirList = []

    return obsDirList, telDirList, calDirList

# ---------------------------------------------------------------------------- #

def MEFarithOLD(MEF, image, out, op, result):

    if os.path.exists(out+'.fits'):
        os.remove(out+'.fits')
    for i in range(1,88):
        header = astropy.io.fits.open(MEF+'.fits')
        extname = header[i].header['EXTNAME']
        if extname == 'DQ' or extname == 'VAR':
            iraf.imarith(operand1=MEF+'['+str(i)+']', op='*', operand2 = '1', result = out)
        if extname == 'SCI':
            iraf.imarith(operand1=MEF+'['+str(i)+']', op=op, operand2 = image, result = out, divzero = 0.0)

    iraf.fxcopy(input=MEF+'[0],'+out, output = result)
    iraf.hedit(result+'[1]', field = 'EXTNAME', value = 'SCI', add = 'yes', verify = 'no')
    iraf.hedit(result+'[1]', field='EXTVER', value='1', add='yes', verify='no')

# ---------------------------------------------------------------------------- #

# old telluric and flux calibration code

#--------------------------------------------------------------------------------------------------------------------------------#

def applyTelluricPython(over):
    """Python method to divide each spaxel by an efficiency spectrum.
    Assumes function is called from a science observation directory.
    Args:
        over(bool): overwite old files.
    """

    """TODO(nat): implement this old code from makeCube. I think it makes more
    sense to be placed somewhere in here.

    hdulist = astropy.io.fits.open('c'+pre+frame+'.fits', mode = 'update')
    #            hdulist.info()
    exptime = hdulist[0].header['EXPTIME']
    cube = hdulist[1].data
    gain = 2.8
    cube_calib = cube / (exptime * gain)
    hdulist[1].data = cube_calib
    hdulist.flush()
    """

    observationDirectory = os.getcwd()
    # Get the efficiency spectrum we will use to do a telluric correction and flux calibration at the same time.
    os.chdir('../Tellurics')
    # Find a list of all the telluric observation directories.
    telDirList_temp = glob.glob('*')
    tempDir = os.path.split(observationDirectory)
    telDirList = []
    for telDir in telDirList_temp:
        telDirList.append(tempDir[0]+'/Tellurics/'+telDir)
    for telDir in telDirList:
        # Change to the telluric directory.
        os.chdir(telDir)
        # Make sure an scienceMatchedTellsList is present.
        try:
            scienceMatchedTellsList = open('scienceMatchedTellsList', 'r').readlines()
            scienceMatchedTellsList = [item.strip() for item in scienceMatchedTellsList]
        except:
            os.chdir('..')
            continue

        # Open the correction efficiency spectrum.
        telluric = str(open('finalcorrectionspectrum', 'r').readlines()[0]).strip()
        logging.info("\nFound a finalcorrectionspectrum in\n"), telDir
        # Open the final correction spectrum file as "telluric". Create a numpy array the same length
        # as the telluric spectrum with each element a wavelength matching that of the telluric.

        # Open the final correction spectrum so that we use its data.
        telluric = astropy.io.fits.open(telluric+'.fits')
        # Find the starting wavelength and the wavelength increment from the science header.
        wstart = telluric[1].header['CRVAL1']
        wdelt = telluric[1].header['CD1_1']
        # Create a numpy array of zeros. We will use this to hold the efficiency spectrum.
        effwave = np.zeros(2040)
        # Create a wavelength array using the starting wavelength and the wavelength increment.
        for i in range(2040):
            effwave[i] = wstart+(wdelt*i)

        # Open the efficiency spectrum as a numpy array.
        effspec = telluric[1].data
        # Store the airmass of the correction spectrum in telairmass.
        telairmass = telluric[0].header['AIRMASS']

        tempDir = observationDirectory.split(os.sep)
        if tempDir[-1] in scienceMatchedTellsList:
            os.chdir(observationDirectory)
            logging.info("\nWorking to apply tellurics in:\n"+ str(observationDirectory))
            scilist = glob.glob('c*.fits')
            for frame in scilist:
                # TODO: this will break if for some reason we don't do something like the sky subtraction... Perhaps we should
                # make sure the prefix is correct before the function starts?
                if frame.replace('ctfbrsn','').replace('.fits', '') in scienceMatchedTellsList:
                    if os.path.exists(frame[0]+'p'+frame[1:]):
                        if not over:
                            logging.info('Output already exists and -over- not set - skipping telluric correction and flux calibration')
                            continue
                        if over:
                            os.remove(frame[0]+'p'+frame[1:])
                            pass
                    logging.info("\nApplying python telluric correction to: \n"+ str(frame))
                    np.set_printoptions(threshold=np.nan)

                    # Read in cube data and create a 1D array "cubewave" of the wavelengths found in the cube.
                    # Open a data cube with astropy.io.fits. Read the data header to find the starting wavelength and wavelength increment.
                    # From readCube docstring:
                    #       Create a 1D array with length equal to the spectral dimension of the cube.
                    #    For each element in array, element[i] = starting wavelength + (i * wavelength increment).
                    #    Returns:
                    #        cube (object reference):   Reference to the opened data cube.
                    #        cubewave (1D numpy array): array representing pixel-wavelength mapping of data cube.
                    cube, cubewave = readCube(frame)

                    # Interpolate a function using the telluric spectrum.
                    # From scipy.interp1d help:
                    #   interp1d(x,y)
                    efficiencySpectrumFunction = interp1d(effwave, effspec, bounds_error = None, fill_value=0.)
                    # Extend the function to allow extrapolation.
                    extendedEfficiencySpectrumFunction = extrap1d(efficiencySpectrumFunction)
                    # For each element of the cube wavelength array, a 1D numpy array holding wavelengths from a single spaxel of the cube, evaluate extrapolatedfunction(wavelength) and
                    # store the result in the element.
                    # Iterate over each element, ie, wavelength, of the cubes wavelength array.
                    # evaluate f(wavelength) and store the result in that element.
                    effspec = extendedEfficiencySpectrumFunction(cubewave)
                    # Optional: plot things out.
                    #plt.ion()
                    #plt.figure(1)
                    #plt.plot(effspec)

                    exptime = cube[0].header['EXPTIME']

                    # See if we should attempt an airmass correction.
                    try:
                        sciairmass = cube[0].header['AIRMASS']
                        airmcor = True
                    except:
                        logging.info("No airmass found in header. No airmass correction being performed on "+ str(frame)+ " .\n")
                        airmcor= False

                    if airmcor:
                        airmassCorrection = sciairmass/telairmass
                        logging.info("\nDoing an airmass correction; correction factor is "+ str(airmassCorrection)+".")
                        # If effspec[i] is between 0 and 1, apply an airmass correction by multiplying ln(effspec[i]) by the correction factor.
                        for i in range(len(effspec)):
                            if effspec[i]>0. and effspec[i]<1.:
                                effspec[i] = np.log(effspec[i])
                                effspec[i] *= airmassCorrection
                                effspec[i] = np.exp(effspec[i])

                    plt.plot(effspec,"r--")
                    # Divide each spectrum in the cubedata array by the efficiency spectrum*exptime.
                    for i in range(cube[1].header['NAXIS2']):         # NAXIS2 is the y axis of the final cube.
                        for j in range(cube[1].header['NAXIS1']):     # NAXIS1 is the x axis of the final cube.
                            cube[1].data[:,i,j] /= (effspec*exptime)  # For each y and x, divide entire spectrum by effspec*exptime.

                    # Write the corrected cube to a new file with a "cp" prefix, "p" for "python corrected".
                    cube.writeto('cp'+frame[1:], output_verify='ignore')

    # Make sure we exit in the right directory.
    os.chdir(observationDirectory)

#--------------------------------------------------------------------------------------------------------------------------------#

def applyTelluricIraf(scienceList, obsid, telinter, log, over):
    """Corrects the data for telluric absorption features with iraf.nftelluric.
    iraf.nftelluric is currently only run interactively. Output: -->atfbrsgn

    NFTELLURIC

    NFTELLURIC uses input science and a 1D spectrum of a telluric
    calibrator to correct atmospheric absorption features.
    """

    observationDirectory = os.getcwd()
    os.chdir('../Tellurics')
    telDirList = glob.glob('*')

    if telinter:
        telinter = 'yes'
    else:
        telinter = 'no'

    # Used for brighter objects.
    for telDir in telDirList:
        if 'obs' in telDir:
            os.chdir(telDir)
            if os.path.exists('scienceMatchedTellsList'):
                scienceMatchedTellsList = open("scienceMatchedTellsList", "r").readlines()
                scienceList = [frame.strip() for frame in scienceMatchedTellsList]
            else:
                os.chdir('..')
                continue
            try:
                telluric = str(open('finalcorrectionspectrum', 'r').readlines()[0]).strip()
            except:
                logging.info("No telluric spectrum found in "), telDir
                os.chdir('..')
                continue
            shutil.copy(telluric+'.fits', observationDirectory)

            '''
            continuum = str(open('continuumfile', 'r').readlines()[0]).strip()
            bblist = open('blackbodyfile', 'r').readlines()
            bblist = [frame.strip() for frame in bblist]
            '''

            os.chdir(observationDirectory)
            iraffunctions.chdir(observationDirectory)
            if obsid in scienceList:
                index = scienceList.index(obsid)
                i=index+1

                while i<len(scienceList) and 'obs' not in scienceList[i]:
                    if os.path.exists("atfbrsn"+scienceList[i]+".fits"):
                        if over:
                            iraf.delete("atfbrsgn"+scienceList[i]+".fits")
                            if telinter == "yes":
                                iraf.nftelluric('tfbrsn'+scienceList[i], outprefix='a', calspec=telluric, fl_inter = telinter, logfile=log)
                            else:
                                iraf.nftelluric('tfbrsn'+scienceList[i], outprefix='a', xc=15.0, yc=33.0, calspec=telluric, fl_inter = telinter, logfile=log)
                        else:
                            logging.info("Output file exists and -over not set - skipping nftelluric in applyTelluric")
                    elif not os.path.exists('atfbrsn'+scienceList[i]+'.fits'):
                        logging.info('\ntfbrsn'+scienceList[i])
                        logging.info(telluric)
                        logging.info(telinter)
                        if telinter == "yes":
                            iraf.nftelluric('tfbrsn'+scienceList[i], outprefix='a', calspec=telluric, fl_inter = telinter, logfile=log)
                        else:
                            iraf.nftelluric('tfbrsn'+scienceList[i], outprefix='a', xc=15.0, yc=33.0, calspec=telluric, fl_inter = telinter, logfile=log)

                    '''
                    # remove continuum fit from reduced science image
                    if over:
                        if os.path.exists("cont"+scienceList[i]+".fits"):
                            iraf.delete("cont"+scienceList[i]+".fits")
                        MEFarithpy('atfbrsgn'+scienceList[i], '../Tellurics/'+telDir+'/'+continuum, 'divide', 'cont'+scienceList[i]+'.fits')
                    elif not os.path.exists('cont'+scienceList[i]+'.fits'):
                        MEFarithpy('atfbrsgn'+scienceList[i], '../Tellurics/'+telDir+'/'+continuum, 'divide', 'cont'+scienceList[i]+'.fits')
                    else:
                        logging.info("Output file exists and -over not set - skipping continuum division in applyTelluric")

                    # multiply science by blackbody
                    for bb in bblist:
                        objheader = astropy.io.fits.open(observationDirectory+'/'+scienceList[i]+'.fits')
                        exptime = objheader[0].header['EXPTIME']
                        if str(int(exptime)) in bb:
                            if over:
                                if os.path.exists('bbatfbrsgn'+scienceList[i]+'.fits'):
                                    os.remove('bbatfbrsgn'+scienceList[i]+'.fits')
                                MEFarithpy('cont'+scienceList[i], '../Tellurics/'+telDir+'/'+bb, 'multiply', 'bbatfbrsgn'+scienceList[i]+'.fits')
                            elif not os.path.exists('bbatfbrsgn'+scienceList[i]+'.fits'):
                                MEFarithpy('cont'+scienceList[i], '../Tellurics/'+telDir+'/'+bb, 'multiply', 'bbatfbrsgn'+scienceList[i]+'.fits')
                            else:
                                logging.info("Output file exists and -over- not set - skipping blackbody calibration in applyTelluric")
                    '''
                    i+=1
        os.chdir('../Tellurics')

#--------------------------------------------------------------------------------------------------------------------------------#

def effspec(telDir, combined_extracted_1d_spectra, mag, T, over):
    """This flux calibration method was adapted to NIFS.

    Args:
        telDir: telluric directory.
        combined_extracted_1d_spectra:
        final_tel_no_hlines_no_norm (string):
        mag:
        T: temperature in kelvin.
        over (boolean): overwrite old files.

    """

    # define constants
    c = 2.99792458e8
    h = 6.62618e-34
    k = 1.3807e-23

    logging.info('Input Standard spectrum for flux calibration is ' +  str(combined_extracted_1d_spectra))

    if os.path.exists('c'+combined_extracted_1d_spectra+'.fits'):
        if not over:
            logging.info('Output already exists and -over- not set - calculation of efficiency spectrum')
            return
        if over:
            os.remove('c'+combined_extracted_1d_spectra+'.fits')
            pass

    combined_spectra_file = astropy.io.fits.open(combined_extracted_1d_spectra+'.fits')
    band = combined_spectra_file[0].header['GRATING'][0]
    exptime = float(combined_spectra_file[0].header['EXPTIME'])
    telfilter = combined_spectra_file[0].header['FILTER']

    # Create a black body spectrum at a given temperature.
    # Create a 1D array equal in length to the nfextracted 1d spectrum. Eg: length == 2040
    bb_spectrum_wavelengths = np.zeros(combined_spectra_file[1].header['NAXIS1'])
    # Find the wavelength at the start of the nfextracted 1d spectrum.
    wstart = combined_spectra_file[1].header['CRVAL1']
    # Find the change in wavelength with each pixel of the nfextracted 1d spectrum.
    wdelt = combined_spectra_file[1].header['CD1_1']
    # Starting at wstart, at intervals of wdelt, write a wavelength into each element of bb_spectrum_wavelengths.
    for i in range(len(bb_spectrum_wavelengths)):
        bb_spectrum_wavelengths[i] = wstart+(i*wdelt)
    # Plank function. Results in J/s/m^2/str/m
    blackbodyFunction = lambda x, T: (2.*h*(c**2)*(x**(-5))) / ( (np.exp((h*c)/(x*k*T))) - 1 )
    # Evaluate that function at each wavelength of the bb_spectrum_wavelengths array,
    # at the temperature of the standard star. Results in ergs/s/cm^2/Angstrom
    blackbodySpectrum = (blackbodyFunction(bb_spectrum_wavelengths*1e-10, T))*1e-7

    # Divide final telluric correction spectrum by blackbody spectrum.
    final_telluric = astropy.io.fits.open('final_tel_no_hlines_no_norm.fits')
    # Multiply by the gain to go from ADU to counts.
    tel_bb = final_telluric[0].data/blackbodySpectrum

    # Look up the coefficients for the appropriate grating and filter.
    if 'HK' in telfilter:
        f0 = 5.09501198044e-12
    if 'JH' in telfilter:
        f0 = 1.60036273943e-11
    if 'ZJ' in telfilter:
        f0 = 7.38127838152e-11

    effspec = (tel_bb/exptime)*(10**(0.4*mag))*(f0/3.631e-20)

    # Modify our working copy of the original extracted 1d spectrum. Note though that we aren't permanently writing these changes to disk.
    combined_spectra_file[1].data = effspec
    # Don't write our changes to the original extracted 1d spectra; write them to a new file, 'c'+combined...+'.fits'.
    combined_spectra_file.writeto('c'+combined_extracted_1d_spectra+'.fits',  output_verify='ignore')
    writeList('c'+combined_extracted_1d_spectra, 'finalcorrectionspectrum', telDir)


#------------------------------------- utilities ----------------------------------------------------------------#

def extrap1d(interpolator):
    """Extrap1d takes an interpolation function and returns a function which can also extrapolate.
    From https://stackoverflow.com/questions/2745329/how-to-make-scipy-interpolate-give-an-extrapolated-result-beyond-the-input-range
    """
    xs = interpolator.x
    ys = interpolator.y
    def pointwise(x):
        if x < xs[0]:
            return ys[0]+(x-xs[0])*(ys[1]-ys[0])/(xs[1]-xs[0])
        elif x > xs[-1]:
            return ys[-1]+(x-xs[-1])*(ys[-1]-ys[-2])/(xs[-1]-xs[-2])
        else:
            return interpolator(x)
    def ufunclike(xs):
        return array(map(pointwise, array(xs)))
    return ufunclike

def readCube(cube):
    """Open a data cube with astropy.io.fits. Read the data header to find the starting wavelength and wavelength increment.
        Create a 1D array with length equal to the spectral dimension of the cube.
        For each element in array, element[i] = starting wavelength + (i * wavelength increment).

        Returns:
            cube (object reference):   Reference to the opened data cube.
            cubewave (1D numpy array): array representing pixel-wavelength mapping of data cube.

    """
    # read cube into an HDU list
    cube = astropy.io.fits.open(cube)

    # find the starting wavelength and the wavelength increment from the science header of the cube
    wstart = cube[1].header['CRVAL3']
    wdelt = cube[1].header['CD3_3']

    # initialize a wavelength array
    cubewave = np.zeros(2040)

    # create a wavelength array using the starting wavelength and the wavelength increment
    for i in range(2040):
        cubewave[i] = wstart+(i*wdelt)

    return cube, cubewave

def write_line_positions(nextcur, var):
    """Write line x,y info to file containing Lorentz fitting commands for bplot

    """

    curfile = open(nextcur, 'w')
    i=-1
    for line in var:
        i+=1
        if i!=0:
            var[i]=var.split()
            var[i][2]=var[i][2].replace("',",'').replace("']", '')
        if not i%2 and i!=0:
            #even number, means RHS of H line
            #write x and y position to file, also "k" key
            curfile.write(var[i][0]+" "+var[i][2]+" 1 k \n")
            #LHS of line, write info + "l" key to file
            curfile.write(var[i-1][0]+" "+var[i-1][2]+" 1 l \n")
            #now repeat but writing the "-" key to subtract the fit
            curfile.write(var[i][0]+" "+var[i][2]+" 1 - \n")
            curfile.write(var[i-1][0]+" "+var[i-1][2]+" 1 - \n")
        curfile.write("0 0 1 i \n")
        curfile.write("0 0 q \n")
        curfile.close()

def getTelluricSpec(scienceObjectName, over):
    """
    For a given science cube, copies appropriate telluric correction spectrum to current directory.
    TODO(nat): have to be able to choose telluric spectrum that is closest in time!
    """

    # New method:
    #
    # Check if telluricCorrection.fits exists. If so, we'll use those to do our telluric correction.
    #
    # Else:
    # Try going to telluricProducts, reading the .json file, looking for the science cube name.
    # If you find it, copy appropriate telluricCorrection_obsname.fits to telluricCorrection.fits.
    #
    # If you don't, return False for foundTelluricFlag. Abandon the telluric correction attempt there.

    observationDirectory = os.getcwd()
    foundTelluricFlag = False
    if os.path.exists('telluricCorrection.fits') and os.path.exists('fit.fits') and not over:
        # User supplied their own telluric correction and fit in the science directory.
        logging.info("\nUsing user-supplied normalized telluric correction and fit to telluric correction")
        foundTelluricFlag = True
        return foundTelluricFlag
    if not os.path.exists('telluricCorrection.fits') or not os.path.exists('fit.fits'):
        os.chdir('../Tellurics')
        # Find a list of all the telluric observation directories.
        telDirList_temp = glob.glob('obs*')
        for telDir in telDirList_temp:
            # Change to the telluric directory
            print os.getcwd()
            os.chdir(telDir)
            # Make sure an scienceMatchedTellsList is present.
            try:
                scienceMatchedTellsList = open('scienceMatchedTellsList', 'r').readlines()
                scienceMatchedTellsList = [item.strip() for item in scienceMatchedTellsList]
            except:
                os.chdir('..')
                continue
            foundTelluricFlag = False
            if scienceObjectName in scienceMatchedTellsList:
                print "made it here"
                # Open the correction efficiency spectrum.
                if os.path.exists(observationDirectory + "/telluricCorrection.fits"):
                    os.remove(observationDirectory + "/telluricCorrection.fits")
                shutil.copy("telluricCorrection.fits", observationDirectory)
                if os.path.exists(observationDirectory+"/fit.fits"):
                    os.remove(observationDirectory+"/fit.fits")
                shutil.copy("fit.fits", observationDirectory)
                os.chdir(observationDirectory)
                logging.info("\nUsing combined standard spectrum from " + str(telDir) + " for " + str(scienceObjectName))
                foundTelluricFlag = True
                break
            else:
                os.chdir('..')
                continue
        if not foundTelluricFlag:
            logging.info("\nWARNING: No Telluric correction spectrum found for " + str(scienceObjectName))
        os.chdir(observationDirectory)
    return foundTelluricFlag
