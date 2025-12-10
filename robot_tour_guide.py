import sys
import signal
import time
import os
from joblib import dump, load  # To get the model to the robot

from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier

from mbot_bridge.api import MBot
from utils.camera import CameraHandler
from utils.robot import plan_to_pose, turn_to_theta
from waypoint_writer import read_labels_and_waypoints

# TODO: Update PATH_TO_MODEL.
PATH_TO_MODEL = "/home/mbot/project4/p4/P4/utils/model.joblib"

robot = MBot()


def signal_handler(sig, frame):
    print("Stopping...")
    robot.stop()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def main():
  ch = CameraHandler()  # Initialize the camera

  # NOTE: This code will fail if you have not updated PATH_TO_MODEL above.
  assert os.path.exists(PATH_TO_MODEL), f"Model file {PATH_TO_MODEL} does not exist."
  model = load(PATH_TO_MODEL)
  
  # TODO: Either uncomment and modify the hard coded definitions for
  # waypoints and labels below or run waypoint_writer.py to write
  # waypoints and labels for your current map to output/waypoints.txt.
  #
  # You must handle the case where your model detects a label which is not part of the
  # given course.

  labels, waypoints = read_labels_and_waypoints()  # Load from waypoints.txt

  # labels = [1, 2, 3, 0]
  # waypoints = [[0, 0, 0], [9, 2, 8], [3, 6, 4]]


  # NOTE: To get the cropped image of a post-it from the camera, do:
  #
  frame = ch.get_processed_image()
  #
  # If a post-it is not detected, frame will be None. Make sure you check for this
  # case. To save the image to the folder "output", pass `save=True` to this
  # function. It will be the last image labeled 08_bordered_frame_X.jpg. Check out
  # the previous images to understand how the preprocessing step works. This might 
  # slow down execution slightly. 
  
  
  # NOTE: To plan a path to a goal position (x and y, in meters), do:
  #
  #     plan_to_pose(x, y, robot)
  #
  # To turn to a given angle (theta, in radians), do:
  #
  #     turn_to_theta(theta, robot)
  #
  # You must turn to the theta after x, y location is reached.
  


  # TODO: Your code here!
  # Write your code to detect the label on a poster at a given waypoint, and use
  # the result to determine which waypoint to visit next. You will need to use the
  # "labels" and "waypoints" variables! When the robot reads a poster with label "0",
  # it should return to the start position (0, 0, 0) and the program should exit.

  while True:
    #get processed image
    frame = ch.get_processed_image(save = True)
    if frame is None:
      print("no poster found")

    else:
      #get robot to position

      #get the photo from the frame

  
  
      y_pred = model.predict([frame])[0]
      #check to see if the y_pred is the same as index 0 from the label list
      index = labels.index(y_pred) #loops through the indexes starting with index 0 to check what y_pred is seeing
      print(y_pred)

      #get the x, y, and theta values for plan to pose and turn to theta at the specific index
      values = waypoints[index]
      x = values[0]
      y = values[1]
      theta = values[2]

      print("x: " , x)


      plan_to_pose(x, y, robot)
      turn_to_theta(theta, robot)


      if y_pred == 0:
        break



if __name__ == '__main__':
    main()
