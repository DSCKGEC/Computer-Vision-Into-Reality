from flask import Flask, render_template, request, jsonify, Response
from camera import VideoCamera
import requests
import base64, cv2

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        data = camera.get_frame()
        frame = data[0]
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
