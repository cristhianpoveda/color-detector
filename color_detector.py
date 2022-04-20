import picamera
import picamera.array
import os
from time import sleep

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    with picamera.array.PiRGBArray(camera) as output:
        camera.capture(output, 'rgb')
        output = output.array
        print(output.shape)
        splits=os.environ['N_SPLITS']
        print(splits)
        for i in range(splits/2, splits):
            if output[i][160][0] < 200 and output[i][160][0] > 120:
                print("Red color detected")
