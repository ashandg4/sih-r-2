import cv2
import numpy as np
import pyautogui

# Set up the video capture
cap = cv2.VideoCapture(1)  # 0 for default camera

# Define the color range for hand detection (adjust as needed)
lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)

print("Starting in 5 seconds...")
cv2.waitKey(5000)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    mask = cv2.dilate(mask, None, iterations=2)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Find contours
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Find the largest contour
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Calculate center of the contour
        center_x, center_y = x + w // 2, y + h // 2

        # Map to screen coordinates (ensure this is correctly mapped to your screen)
        screen_x = int(pyautogui.size().width * center_x / frame.shape[1])
        screen_y = int(pyautogui.size().height * center_y / frame.shape[0])

        # Simulate mouse movement
        pyautogui.moveTo(screen_x, screen_y)

        # Draw a rectangle around the detected hand
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.circle(frame, (center_x, center_y), 10, (0, 0, 255), -1)

    # Show the frame
    cv2.imshow('Hand Tracking', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
