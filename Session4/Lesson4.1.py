# class Ten_class:
    # thuoc tinh: variables
    # phuong thuc: sub-function

# Example

class HCN:
    # width = 10                                                  # variables
    # height = 100                                                # variables
    def __init__(self,w,h):
        self.width = w
        self.height = h
    def chu_vi(self):                                           # sub-function
        p = (self.height+self.width)*2
        return p

#Tao
# a1 = HCN(10, 100)
# a2 = HCN(30, 90)
# cv1 = a1.chu_vi()
# print("a1 chu vi = ", cv1)
# cv2 = a2.chu_vi()
# print("a2 chu vi = ", cv2)

