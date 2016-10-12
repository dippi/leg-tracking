import numpy as np
from primesense import openni2

class VideoStream(object):
    def __init__(self):
        openni2.initialize('/usr/lib/')

        device = openni2.Device.open_file(filename='../old/examples/exampleVideo.oni')
        device.playback.set_repeat_enabled(False)
        device.playback.set_speed(0.05)

        self.depth_stream = device.create_depth_stream()
        self.depth_stream.start()

    def get_frame(self):
        """
            Retrieve a new frame from the stream

            Returns
            -------
            out : numpy.ndarray
                The matrix of depth information
        """
        frame = self.depth_stream.read_frame()
        data = np.frombuffer(frame.get_buffer_as_uint16(), dtype=np.int16)
        return np.reshape(data, (frame.height, frame.width))

# ESEMPIO
# from primesense import openni2
# import numpy as np
# import matplotlib.pyplot as plt
#
# openni2.initialize('/usr/lib/')
# dev = openni2.Device.open_file(filename='../old/examples/exampleVideo.oni')
# dev.playback.set_repeat_enabled(False)
# dev.playback.set_speed(0.05)
# depth_stream = dev.create_depth_stream()
# depth_stream.start()
# frame = depth_stream.read_frame()
# frame_data = frame.get_buffer_as_uint16()
# tmp = np.frombuffer(frame_data, dtype=np.int16)
# arr = np.reshape(tmp, (frame.height, frame.width))
# plt.imshow(arr)
# plt.show()
