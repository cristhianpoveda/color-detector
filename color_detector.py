import picamera
import picamera.array
import os
from time import sleep

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    totalPixels=108*120
    splits=int(os.environ['N_SPLITS'])
    print(splits)
    rangeMin=int(splits/2)
    while True:
        with picamera.array.PiRGBArray(camera) as output:
            camera.capture(output, 'rgb')
            output = output.array
            print(output.shape)
            redPixels=0
            for i in range(rangeMin, splits, 1):
                for j in range (105, 213, 1):
                    if output[i][j][0] < 200 and output[i][j][0] > 120:
                        if output[i][j][1] < 100 and output[i][j][2] < 100:
                            redPixels=redPixels+1
            redPercentage=100*redPixels/totalPixels
            print('Red pixels percentage is: ', redPercentage, ' %')
            sleep(3)