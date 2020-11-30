import sys
import cv2
import numpy as np
import urllib.request

def usage():
    print("This file needs to be called with two parameters.")
    print("Please call it in the form:")
    print("python3  image_check image.jpg URL\n")
    sys.exit()

def main(image, url):
    original = cv2.imread(image)
    req = urllib.request.urlopen('https://hips.hearstapps.com/ghk.h-cdn.co/assets/16/08/gettyimages-464163411.jpg')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    dupe = cv2.imdecode(arr, -1) # 'Load it as it is'

    if original.shape == dupe.shape:
        print("Images have same size and channels")
        diff = cv2.subtract(original, dupe)
        b, g, r = cv2.split(diff)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("The images are completely equal")
        else:
            print("The images are not the same")
    else:
        print("The images are not the same")

    dupe = None

if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    else:
        image = sys.argv[1]
        url = sys.argv[2]
        main(image, url)
