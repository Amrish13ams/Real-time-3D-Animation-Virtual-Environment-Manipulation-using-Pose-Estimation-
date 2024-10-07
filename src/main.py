import cv2
from pose_estimation.pose_estimator import PoseEstimator
from pose_estimation.utils import draw_landmarks

def main():
    cap = cv2.VideoCapture(0)  # Capture video from webcam
    pose_estimator = PoseEstimator()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        landmarks = pose_estimator.estimate_pose(frame)
        frame = draw_landmarks(frame, landmarks)
        
        cv2.imshow("Pose Estimation", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
