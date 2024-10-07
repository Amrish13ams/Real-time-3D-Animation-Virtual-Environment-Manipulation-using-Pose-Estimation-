def draw_landmarks(image, landmarks):
    if landmarks:
        for landmark in landmarks.landmark:
            h, w, _ = image.shape
            x, y = int(landmark.x * w), int(landmark.y * h)
            cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
    return image
