import cv2
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)

#gets frame
# ret,frame = cap.read()
# print(ret)
# plt.imshow(frame)
# cap.release()

while cap.isOpened():
    ret,frame = cap.read()
    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()