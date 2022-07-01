import numpy as np
import cv2

def Temperature_Contors(image_array: np.array) -> list:
    
    frame = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
    heatmap_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    heatmap = cv2.applyColorMap(heatmap_gray, cv2.COLORMAP_JET)
    unused_val, binary_thresh = cv2.threshold(heatmap_gray, 200, 255, cv2.THRESH_BINARY) # threshold=200
    kernel = np.array([[1 for i in range(3)] for j in range(3)]);
    eros_dil_img = cv2.dilate(src=(cv2.erode(src=binary_thresh, kernel=kernel, iterations=1)),
                             kernel=kernel, iterations=1);

    contours, _ = cv2.findContours(eros_dil_img, 1, 2);
    all_tmp = []

    for contour in contours:
        outs = list(cv2.boundingRect(contour));
        x, y, w, h = outs[0], outs[1], outs[2], outs[3];

        if w*h<600:
            continue;

        mask = np.zeros_like(heatmap_gray)
        cv2.drawContours(mask, contour, -1, 255, -1);

        mean = (cv2.mean(heatmap_gray, mask=mask)[0])/2.20

        temperature = round(mean, 2)
        all_tmp.append(temperature)
        color = (255, 255, 255) if temperature < 102 else (
            255, 255, 255)

        heatmap = cv2.rectangle(heatmap, (x, y), (x + w, y + h), color, 2)

        cv2.putText(heatmap, "{} F".format(temperature), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2, cv2.LINE_AA)

    return [heatmap, all_tmp]

def Mean_temperature(temperature_list: list) -> float:
    cnt = 0.0
    sm = 0.0
    for i in temperature_list:
        if i>84 and i<115:
            cnt+=1
            sm+=i

    return sm/cnt


