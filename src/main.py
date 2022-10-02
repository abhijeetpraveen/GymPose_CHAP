from camera import VideoCamera
from model import predict
import os
from flask import Flask, flash, request,render_template, Response, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
import os

app = Flask(__name__, template_folder="client/build", static_folder="client/build/static")

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route('/url_route', methods=['POST'])
def fileUpload():
    target= "src/VideoUploaded" 
    if not os.path.isdir(target):
        os.makedirs(target)
    logger.info("welcome to upload`")
    file = request.files['file_from_react'] 
    filename = secure_filename(file.filename)
    destination="/".join([target, "exercise.mov"])
    file.save(destination)
    session['uploadFilePath']=destination
    response={"FileUploaded":"sucess"}
    return response

@app.route('/')
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/classify', methods=['GET'])
def classify():
    return {"exercise": predict()}

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)

CORS(app, expose_headers='Authorization')