import cv2
import mediapipe as mp

#initialize mediapipe pose
mp_pose =mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

#load image
image_path = "man.png"
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#perform pose estimation
results = pose.process(image_rgb)

#draw landmarks
if results.pose_landmarks:
    print("Pose landmarks detected!")

    #extract landmark
    for idx,landmark in enumerate(results.pose_landmarks.landmark):
        print(f"Landmark {idx}: (x: {landmark.x},y: {landmark.y},z: {landmark.z})")
    for landmark in results.pose_landmarks.landmark:
        #get image dimensions
        h,w,c=image.shape

        #convert normalized coordinates
        cx,cy=int(landmark.x*w), int(landmark.y *h)

        #draw the keypoints
        cv2.circle(image,(cx,cy),5,(255,0,0),-1)

        #draw landmark
        annotated_image=image.copy()
        mp_drawing.draw_landmarks(annotated_image,results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

#display the output
cv2.imshow("Pose Landmarks",image)
cv2.imshow("Pose drawing", annotated_image)

cv2.waitKey(6455)
cv2.destroyAllWindows()

pose.close()
