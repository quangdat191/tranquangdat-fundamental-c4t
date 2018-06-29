import cv2
from threading import Thread
from Webcam import Webcam
import numpy as np
import pygame


class SiftMatching:
    def __init__(self):
        self.webcam = Webcam()
        self.webcam.start()
        self.glyph_found = False
        self.npts = []
        self.sound_play = False

    def match(self, _, I2):
        while True:
            I1 = self.webcam.get_current_frame()
            gray1 = cv2.cvtColor(I1, cv2.COLOR_RGB2GRAY)
            sift = cv2.xfeatures2d.SIFT_create()
            kpt1, des1 = sift.detectAndCompute(gray1, None)
            gray2 = cv2.cvtColor(I2, cv2.COLOR_RGB2GRAY)
            kpt2, des2 = sift.detectAndCompute(gray2, None)
            # Matching Brute force
            bf = cv2.BFMatcher_create()
            matches = bf.knnMatch(des2, des1, 2)  # knn: k nearest neighbor
            # Choose good matches
            good = []
            new_good = []
            for m, n in matches:
                if m.distance < 0.4 * n.distance:
                    good.append([m])
                    new_good.append(m)
            if len(good) > 3:
                srcPoints = np.float32([kpt2[m.queryIdx].pt for m in new_good]).reshape(-1, 1, 2)
                dstPoints = np.float32([kpt1[m.trainIdx].pt for m in new_good]).reshape(-1, 1, 2)
                M, H = cv2.findHomography(srcPoints, dstPoints)
                w = gray2.shape[1]
                h = gray2.shape[0]
                n_corners = np.float32([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]]).reshape(-1, 1, 2)
                if M is not None:
                    self.npts = cv2.perspectiveTransform(n_corners, M)
                    # self.npts = np.int32(self.npts)
                self.glyph_found = True
            else:
                self.glyph_found = False

    def start(self, src_img):
        Thread(target=self.match, args=(None, src_img)).start()

    def initiate_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Project\\Silent.mp3")
        pygame.mixer.music.play(-1)

    def stop_current_and_load_sound(self, sound):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Project\\" + sound + ".mp3")
        pygame.mixer.music.play(-1)
