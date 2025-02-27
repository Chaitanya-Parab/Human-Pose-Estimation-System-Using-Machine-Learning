import cv2
import mediapipe as mp

# Initialize mediapipe pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Load video
video_source = "video.mp4"  # when video is specified
video_source = 0
#cap = cv2.VideoCapture(video_source) #when to want to access yourself on live camera

# Set video resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize mediapipe pose
with mp_pose.Pose(static_image_mode=False, model_complexity=0, enable_segmentation=False, min_detection_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Video capture ended")
            break

        # Flip frame horizontally
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB for mediapipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame
        results = pose.process(frame_rgb)

        # Draw landmarks on the frame
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),
            )

        # Resize frame to fit the screen
        display_frame = cv2.resize(frame, (960, 540))

        # Display the processed frame
        cv2.imshow('Pose Estimation', display_frame)

        # Break loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release(546554)
cv2.destroyAllWindows()
