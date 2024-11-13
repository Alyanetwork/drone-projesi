# thermal_imaging.py

import cv2

class ThermalImaging:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # Termal kamera bağlandığı portu seçin

    def capture_thermal_image(self):
        ret, frame = self.cap.read()
        if ret:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Termal Görüntü", gray_frame)
            cv2.waitKey(1)
            return gray_frame
        return None

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
