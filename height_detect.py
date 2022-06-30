import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)

while True:
    minheight =1000
    maxheight=0
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            if(id==32 or id==30 or id==29 or id==31):
                minheight=min(minheight,lm.y)
            if(id==2 or id==5 ):
                maxheight=max(maxheight,lm.y)
            print(id, lm)

            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    cv2.putText(img, str(  6.5+ ( (-maxheight+minheight)*283.25)     ), (70, 450), cv2.FONT_HERSHEY_PLAIN, 2,
                (255, 0, 0), 2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
