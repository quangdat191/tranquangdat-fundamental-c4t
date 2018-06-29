from glyphfunctions_modded import *
from Detect_Thread import SiftMatching


s1 = SiftMatching()
s2 = SiftMatching()
s3 = SiftMatching()
s4 = SiftMatching()
s5 = SiftMatching()
s6 = SiftMatching()
I01 = cv2.imread("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Project\\Detect\\1.jpg")
I01 = cv2.resize(I01, (360, 240))
I02 = cv2.imread("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Project\\Detect\\2.png")
I02 = cv2.resize(I02, (360, 240))
I03 = cv2.imread("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Project\\Detect\\3.png")
I03 = cv2.resize(I03, (360, 240))
I04 = cv2.imread("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Project\\Detect\\4.png")
I04 = cv2.resize(I04, (360, 240))
I05 = cv2.imread("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Project\\Detect\\5.png")
I05 = cv2.resize(I05, (360, 240))
I06 = cv2.imread("C:\\Users\\Dell\\PycharmProjects\\Fundamental\\Project\\Detect\\6.png")
I06 = cv2.resize(I06, (360, 240))
s1.start(I01)
s2.start(I02)
s3.start(I03)
s4.start(I04)
s5.start(I05)
s6.start(I06)
s1.initiate_sound()

class Glyphs:
    QUADRILATERAL_POINTS = 4
    BLACK_THRESHOLD = 110
    WHITE_THRESHOLD = 150
    count = -46
    initial = 1
    corners_old = []
    name = 'None'

    def stabilize_corners(self, old, new):
        moved = False
        for idx in range(len(new)):
            if abs(new[idx][0] - old[idx][0]) > 10 or abs(new[idx][1] - old[idx][1]) > 20:
                moved = True
                break
        if moved is True:
            return True, new
        else:
            return False, old

    def detect(self, image):

        glyphs = []

        if s1.glyph_found or s2.glyph_found or s3.glyph_found or s4.glyph_found or s5.glyph_found or s6.glyph_found:
            approx = []
            if s1.glyph_found:
                approx = order_points(s1.npts.reshape(4, 2))
                if self.name != 'chicken':
                    self.name = 'chicken'
                    s1.stop_current_and_load_sound(self.name)
            elif s2.glyph_found:
                approx = order_points(s2.npts.reshape(4, 2))
                if self.name != 'elephant':
                    self.name = 'elephant'
                    s1.stop_current_and_load_sound(self.name)
            elif s3.glyph_found:
                approx = order_points(s3.npts.reshape(4, 2))
                if self.name != 'cat':
                    self.name = 'cat'
                    s1.stop_current_and_load_sound(self.name)
            elif s4.glyph_found:
                approx = order_points(s4.npts.reshape(4, 2))
                if self.name != 'octopus':
                    self.name = 'octopus'
                    s1.stop_current_and_load_sound(self.name)
            elif s5.glyph_found:
                approx = order_points(s5.npts.reshape(4, 2))
                if self.name != 'dog':
                    self.name = 'dog'
                    s1.stop_current_and_load_sound(self.name)
            elif s6.glyph_found:
                approx = order_points(s6.npts.reshape(4, 2))
                if self.name != 'tank_t54':
                    self.name = 'tank_t54'
                    s1.stop_current_and_load_sound(self.name)

            if self.initial == 1:
                self.corners_old = approx
                self.initial = 0
            # print(self.stabilize_corners(self.corners_old, approx))
            ret, approx = self.stabilize_corners(self.corners_old, approx)
            if ret is True:
                self.corners_old = approx
                # print(self.corners_old)
            # print(approx)

            if self.count == 45:
                self.count = -46
            self.count += 1

            for i in range(4):
                cv2.circle(image, (approx[i][0], approx[i][1]), 5, (0, 0, 255))
            cv2.imshow("img", image)
            rvecs, tvecs = get_vectors(image, approx, self.count)
            glyphs.append([rvecs, tvecs, self.name])

        else:
            self.name = 'silent'
            s1.stop_current_and_load_sound(self.name)

        return glyphs
