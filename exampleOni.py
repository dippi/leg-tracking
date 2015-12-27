import Tracker

# flags for enabling plots
enablePlotPhoto = true # plot of colored people
enablePlotMap = true # plot of 2D map top-view

# oni files
videoFilename = 'exampleVideo.oni'
sourceType = 'oni'

vidLen = 45 # number of frames to process - restart from beginning if video ends beforehand

# setup tracker
tracker = Tracker(sourceType, videoFilename, enablePlotPhoto, enablePlotMap)

for i in range(vidLen):
    fprintf('#d/#d\n',i,vidLen)

    # update tracking with current frame information
    people, tracker = tracker.track()
    waitforbuttonpress() # FIXME find equivalent in python

# delete tracker
tracker.delete()
