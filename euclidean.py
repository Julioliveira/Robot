from robot.utils import asserts
from math import sqrt, pow

def distance_between(pt1, pt2):
  distance = 0
  for x in range(len(pt1)):
    distance += pow((pt1[x]-pt2[x]), 2)
  distance = sqrt(distance)
  return distance

def should_be_close(pt1, pt2, delta=0.00001, msg=None):
  if distance_between(pt1,pt2) > delta:
    pt1 = str(pt1)
    pt2 = str(pt2)
    raise AssertionError(msg or  "%s and %s should be within %f" % (pt1, pt2, delta))