class Tracker(object):
    """
        People tracker

        Parameters
        ----------
        sourceType : str
        uri : str
        enablePlotPhoto : bool
        enablePlotMap : bool
        enableOdometry : bool

        Attributes
        ----------
        legSigmaZ : float
            Position measure uncertainty (m)
        legSigmaP : float
            Leg probability measure uncertainty
        legSigmaAcc : int
            Model uncertainty, taking into account accelerations (m/s^2)

        peopleSigmaZ : float
            Position measure uncertainty (m)
        peopleSigmaP : float
            Leg probability measure uncertainty
        peopleSigmaAcc : int
            Model uncertainty, taking into account accelerations (m/s^2)
        peopleDistThreshold : int
            Maximum distance between leg expansions, for leg associations
        legProbabilityThreshold : float
            Probability threshold over which a candidates is considere a leg

        refreshIntervalFloorPlane : float
            Parameter to specify how often searching for a floor plane (in seconds)

        fps : int
            Parameter to simulate different frame rates in recorded oni videos

        enablePlotFloor : bool
            Enable plot of floor plane

        floorPlaneTolerance : int
            Floor plane tolerance in mm

        upsideDown : bool
            Sensor upside down (vertical flip)
        mirrored : bool
            Mirrored data (horizontal flip)

        recordVideo : bool
            Record video of processed point cloud (at least one plot must be enabled)

    """

    # Parameters single candidates tracking
    legSigmaZ = 0.02
    legSigmaP = 0.2
    legSigmaAcc = 6 # TODO type check

    # Parameters people tracking
    peopleSigmaZ = 0.05
    peopleSigmaP = 0.2
    peopleSigmaAcc = 6 # TODO type check
    peopleDistThreshold = 75 # TODO type check
    legProbabilityThreshold = 0.8

    refreshIntervalFloorPlane = 0.05

    fps = 30 # TODO type check

    enablePlotFloor = False

    floorPlaneTolerance = 2 # TODO type check

    upsideDown = False
    mirrored = False

    recordVideo = False

    def __init__(self, sourceType, uri, enablePlotPhoto, enablePlotMap, enableOdometry):
        self.sourceType = sourceType
        self.uri = uri
        # Path to the trained svm classifier (libsvm)
		svmPath = "svm.mat" # TODO convert file from .mat

        # ROS topics
		# message type: sensor_msgs/Image encoding: yuv422
		rgbTopic = '/camera/rgb/image_raw'
		# message type: sensor_msgs/Image encoding: 16UC1
		depthTopic = '/camera/depth_registered/image_raw'
		# topic for odometry
		odometryTopic = '/odom'
		# message type: nav_msgs/Odometry
		odometryMsgType = 'nav_msgs/Odometry'

        # TODO look for equivalent in python
        # libraryPath = fileparts(which('setupTracker'));
        # addpath([libraryPath filesep 'libsvm']);
        # addpath([libraryPath filesep 'openni']);
        # addpath([libraryPath filesep 'ros_matlab_bridge']);
