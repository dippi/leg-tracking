class Tracker(object):
    """
        People tracker

        Parameters
        ----------
        sourceType : str
            Source of the RGB-D data, one of the following
                - 'oni'     OpenNI recorded video file
                - 'oniLive' OpenNI compatible sensor directly connected to the PC.
                - 'ros'     The people tracker acts as ROS node. It subscribes
                            to the RGB-D sensor topics (/camera/depth_registered/image_raw
                            and /camera/rgb/image_raw) and to the
                            odometry topic (/odom), and publish the found
                            people (/people, with message type people_msg/People)
        uri : str
            Uri where to search for data, one of the following corresponding to the chosen source type
                - 'oni'     String containing the path to the .oni file
                - 'oniLive' String containing the path to a valid OpenNI XML sensor configuration
                            (see openni/SensorConfig.xml as example)
                - 'ros'     String containig address and port of the ROS core
        enablePlotPhoto : bool, optional
            Enable the point cloud plot with overlay of tracked people,
            for debugging purposes. Default is false.
        enablePlotMap : bool, optional
            Enable the plot of a top view map containing the tracked people,
            for debugging purposes. Default is false.
        enableOdometry : bool, optional
            Enable the reading of odometry from ros topic/odom. Default is false.

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

    def __init__(self, sourceType, uri, enablePlotPhoto = False, enablePlotMap = False, enableOdometry = False):

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

        #################################################################################
        # stralETH configuration - uncomment the following lines when running on starlETH
        # tracker.upsideDown = true; # adjust the sensor upside-down
        # tracker.mirrored = true; # adjust the sensor upside-down
        # rgbTopic = '/rgb/image_raw'; # message type: sensor_msgs/Image encoding: yuv422
        # depthTopic = '/depth_registered/image_raw'; # message type: sensor_msgs/Image encoding: 16UC1
        # odometryTopic = '/starleth/robot_state/pose'; # topic for odometry
        # odometryMsgType = 'geometry_msgs/PoseWithCovarianceStamped'; # message type
        #################################################################################

        self.recordVideo = false

        # TODO look for equivalent in python
        # libraryPath = fileparts(which('setupTracker'));
        # addpath([libraryPath filesep 'libsvm']);
        # addpath([libraryPath filesep 'openni']);
        # addpath([libraryPath filesep 'ros_matlab_bridge']);

        self.svm = None # TODO load svm from file

        self.sourceType = sourceType
        self.enablePlotPhoto = enablePlotPhoto
        self.enablePlotMap = enablePlotMap
        self.enableOdom = enableOdometry

        if self.enablePlotPhoto and self.recordVideo:
            self.writerObjPhoto = None # TODO record a video

        if self.enablePlotMap and self.recordVideo:
            self.writerObjMap = None # TODO record a video

        if self.enablePlotPhoto or self.enablePlotMap:
            pass # TODO plot everythig

        # TODO see https://github.com/jmendeth/PyOpenNI
        def updateFromOni(sensorHandle, tracker):
            pass
