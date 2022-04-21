import picamera
import picamera.array
import os
from time import sleep

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    splits=os.environ['N_SPLITS']
    print(splits)
    rangemin=splits/2
    while True:
        with picamera.array.PiRGBArray(camera) as output:
            camera.capture(output, 'rgb')
            output = output.array
            print(output.shape)
            for i in range(rangemin, splits, 1):
                if output[i][160][0] < 200 and output[i][160][0] > 120:
                    print("Red color detected")
            sleep(1)
