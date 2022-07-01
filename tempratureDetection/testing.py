import numpy as np
import math, cv2, sys
import temperature_output as tempo

# fl = str(input("Input file: "))
# fl = "testing_images/"+fl
fl = r"tempratureDetection\testing_images\test2.jpg"
img = cv2.imread(fl, cv2.IMREAD_COLOR)



outs = tempo.Temperature_Contors(img)
img_out = outs[0]
tmp_l = outs[1]

cv2.putText(img_out, str(tempo.Mean_temperature(tmp_l))[0:7]+" F -> Avg", (25, 25), cv2.FONT_HERSHEY_PLAIN, 2,
                (255, 255, 255), 4)

cv2.imshow(mat=img_out, winname="test1")
# cv2.putText(img_out, str(tempo.Mean_temperature(tmp_l))+" F -> Avg", (70, 450), cv2.FONT_HERSHEY_PLAIN, 2,
#                 (255, 255, 255), 2)
cv2.waitKey(0)
print(tempo.Mean_temperature(tmp_l))


