import os
import errno
import sys
import numpy as np
import cv2

width = int(sys.argv[1])     # 400
height = int(sys.argv[2])    # 640
channels = int(sys.argv[3])  # 1
imageDir = sys.argv[4]       # ./

print "image width " + str(width)
print "image height " + str(height)
print "number of channels " + str(channels)
print "image path " + imageDir

try:
    os.makedirs(imageDir + "/jpeg")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

for filename in os.listdir(imageDir):
    filePath = os.path.join(imageDir, filename)
    if not os.path.isfile(filePath):
        continue
    imgData = np.fromfile(filePath, dtype=np.uint8) # raw pixel type
    imgData = imgData.reshape(width, height, channels)
    cv2.imwrite(imageDir + "/jpeg/" + filename + ".jpg", imgData)
    print filename + " converted"

print "All files in \"" + imageDir + "\" converted."
