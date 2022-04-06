import cv2
import numpy as np


class MyImage:

    def __init__(self, file_name, name_windows):
        self.__file_name = file_name
        self.__name_windows = name_windows
        self.__img = cv2.imread(file_name)
        self.__generator = self.affect_iterator()

        height, width, channels = self.__img.shape
        height = int(height * 0.15)
        width = int(width * 0.1)
        dim = (width, height)
        self.__img = cv2.resize(self.__img, dim)
        cv2.destroyAllWindows()
        cv2.imshow(name_windows, self.__img)
        # mouse events
        cv2.setMouseCallback(name_windows, self.affect)

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, i):
        self.__img = i

    @property
    def name_windows(self):
        return self.__name_windows

    @name_windows.setter
    def name_windows(self, i):
        self.__name_windows = i

    # עיבודים על תמונה
    def affect(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            next(self.__generator)

    def affect_iterator(self):
        global img2
        while True:
            # grey
            img1 = self.__img
            img2 = self.__img = cv2.cvtColor(self.__img, cv2.COLOR_RGB2GRAY)
            cv2.imshow(self.name_windows, self.__img)
            self.__img = img1
            yield
            # edges-
            # מציאת קצוות של התמונה
            img1 = self.__img
            img2 = self.__img = cv2.Canny(self.__img, 50, 300)
            cv2.imshow(self.name_windows, self.__img)
            self.__img = img1
            yield
            # erosion
            img1 = self.__img
            mask = np.ones((10, 10), np.uint8)
            img2 = self.__img = cv2.erode(self.__img, mask, iterations=1)
            cv2.imshow(self.name_windows, self.__img)
            self.__img = img1
            yield
            # deletion
            img1 = self.__img
            img2 = self.__img = cv2.dilate(self.__img, mask, iterations=1)
            cv2.imshow(self.name_windows, self.__img)
            self.__img = img1
            yield

    def cut(self, event, x, y, flags, param):
        global ix, iy, cutting, img2
        # start cut
        if event == cv2.EVENT_LBUTTONDOWN:
            cutting, ix, iy = True, x, y
        elif event == cv2.EVENT_LBUTTONUP:
            cutting = False
            img1 = img2[iy:y, ix:x]
            cv2.imshow(self.__name_windows, img1)
            self.__img = self.__img[iy:y, ix:x]


ix, iy, cutting = 0, 0, False

image1 = MyImage("g.jpg", "flower")
img2 = image1.img
