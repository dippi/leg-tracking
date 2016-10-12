import Tracker

# flags for enabling plots
enablePlotPhoto = True # plot of colored people
enablePlotMap = True # plot of 2D map top-view

# oni files
videoFilename = "exampleVideo.oni"
sourceType = "oni"

vidLen = 45 # number of frames to process - restart from beginning if video ends beforehand

# setup tracker
tracker = Tracker(sourceType, videoFilename, enablePlotPhoto, enablePlotMap)

for i in range(vidLen):
    print "{:d}/{:d}".format(i, vidLen)

    # update tracking with current frame information
    people, tracker = tracker.track()
    raw_input("Press Enter to continue...")

# delete tracker
tracker.delete()
