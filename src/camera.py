import cv2
import mediapipe as mp


class VideoCamera(object):
    def __init__(self):
      self.video = cv2.VideoCapture("src\VideoUploaded\exercise.mov")

    def __del__(self):
      self.video.release()

    def get_frame(self):
      success, img = self.video.read()
      mpDraw = mp.solutions.drawing_utils
      mpPose = mp.solutions.pose
      pose = mpPose.Pose()
      imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
      results = pose.process(imgRGB)
      if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
      ret, jpeg = cv2.imencode('.jpg', img)
      return jpeg.tobytes()
