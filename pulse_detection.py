import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import io
import time

cap = cv.VideoCapture(0)
cap.set(4,1920)
cap.set(3,1080)
cap.set(5, 30)

beats = [0]*120
secs = [time.time()]*120

fig  = plt.figure()
graph = fig.add_subplot(111)

l = []
ret = True
while ret:
    ret, img = cap.read()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_img = img[300:400, 660:760]
    
    beats = beats[1:] + [np.average(face_img)]
    secs = secs[1:] + [time.time()]
    graph.plot(secs,beats)
    
    #GRAPH PLOTTING  (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)
    fig.canvas.draw()
    beat_monitor = np.fromstring(fig.canvas.tostring_rgb(),dtype=np.uint8, sep='')
    beat_monitor = beat_monitor.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.cla()
    #GRAPH PLOTTING
    
    cv.imshow("hearbeat",beat_monitor)
    l.append(np.average(beats))
    cv.imshow('skin_frame', face_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

lp = np.array(l)
print(np.average(lp))
cap.release()
cv.destroyAllWindows()
