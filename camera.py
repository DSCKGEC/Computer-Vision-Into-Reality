import cv2
import pickle
from imutils.video import WebcamVideoStream


class VideoCamera(object):
    def __init__(self):
        self.stream = WebcamVideoStream(src=0).start()

    def __del__(self):
        self.stream.stop()

    def get_frame(self):
        image = self.stream.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        data = []
        data.append(jpeg.tobytes())
        return data
