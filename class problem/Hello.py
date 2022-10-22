import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
hand_detector = mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frame_hight, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output2 = face_mesh.process((rgb_frame))
    output = hand_detector.process(rgb_frame)
    landmark_points = output2.multi_face_landmarks
    hands = output.multi_hand_landmarks
    if landmark_points:
        landmarks_2 = landmark_points[0].landmark
        left = [landmarks_2[145],landmarks_2[159]]
        for landmark_3 in left:
            x2 = int(landmark_3.x * frame_width)
            y2 = int(landmark_3.y * frame_width)
            cv2.circle(frame, (x2, y2), 3, (0, 255, 0))
        print(left[0].y - left[1].y)
        if(left[0].y-left[1].y)<0.012:
            pyautogui.click()
            pyautogui.sleep(.5)
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_hight)
                if id == 8:
                    cv2.circle(img=frame,center=(x,y), radius=10,color=(0,255,255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_hight*y
                    pyautogui.moveTo(index_x,index_y)


                if id == 4:
                    cv2.circle(img=frame,center=(x,y), radius=10,color=(0,255,255))
                    thumb_x = screen_width/frame_width*x
                    thump_y = screen_height/frame_hight*y
                    print('outside',abs(index_y-thump_y))
                    if abs(index_y-thump_y)<30:
                        pyautogui.click()
                        pyautogui.sleep(1)


    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)