# color-detector
Red color detector using numpy arrays. The python script includes picamera initilization to capture images in real time with a specific frequency. This application is tested on a duckiebot DB18.

The total number of considered pixels is calculated based on the desired section of the curent captured image. Subsequently, red pixels are classified using RGB code ranges. Finally, the percentaje of red pixels in the desired section is displayed.
