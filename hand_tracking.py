# import asyncio
# import websockets
# import cv2
# import numpy as np
# import os
# import pytesseract
# import HandTrack as htp
# import json

# # Specify the path to Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ashua\AppData\Local\Tesseract-OCR\tesseract.exe'

# # Set brush and eraser thickness for drawing
# brushthickness = 15
# eraserthickness = 80

# # Initialize drawing coordinates
# xp, yp = 0, 0

# # Create a blank canvas to draw on
# imgCanvas = np.zeros((720, 1280, 3), np.uint8)

# # Load overlay images for the drawing header
# folderPath = "Header"
# myList = os.listdir(folderPath)
# overlaylist = []
# for inPath in myList:
#     image = cv2.imread(f'{folderPath}/{inPath}')
#     overlaylist.append(image)
# header = overlaylist[0]

# # Set initial drawing color
# drawColor = (17, 30, 60)

# # Initialize the webcam capture
# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)

# # Initialize the hand detector
# detector = htp.handDetector(detectionCon=0.85)

# # WebSocket server to handle client connections


# async def handle_client(websocket, path):
#     global recognized_text
#     while True:
#         if recognized_text:
#             message = json.dumps({"type": "text", "text": recognized_text})
#             await websocket.send(message)
#             recognized_text = ""
#         await asyncio.sleep(1)


# async def main():
#     async with websockets.serve(handle_client, "localhost", 8000):
#         await asyncio.Future()  # run forever

# # Main loop for real-time hand detection and drawing
# recognized_text = ""
# try:
#     while True:
#         success, img = cap.read()
#         if not success:
#             break

#         # Flip the image horizontally for a mirrored view
#         img = cv2.flip(img, 1)

#         # Detect hands in the frame
#         img = detector.findHands(img)
#         lmlist = detector.findPosition(img, draw=False)

#         if len(lmlist) != 0:
#             x1, y1 = lmlist[8][1:]
#             x2, y2 = lmlist[12][1:]

#             # Check finger positions for gesture recognition
#             fingers = detector.fingersUp()

#             if fingers[1] and fingers[2]:
#                 # Selection mode: Change color based on the selected area
#                 xp, yp = 0, 0
#                 cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25),
#                               drawColor, cv2.FILLED)
#                 if y1 < 125:
#                     if 250 < x1 < 450:
#                         header = overlaylist[0]
#                         drawColor = (255, 0, 255)
#                     elif 550 < x1 < 750:
#                         header = overlaylist[1]
#                         drawColor = (255, 0, 0)
#                     elif 800 < x1 < 950:
#                         header = overlaylist[2]
#                         drawColor = (0, 255, 0)
#                     elif 1050 < x1 < 1200:
#                         header = overlaylist[3]
#                         drawColor = (0, 0, 0)

#             if fingers[1] and not fingers[2]:
#                 # Drawing mode: Draw lines on the canvas
#                 cv2.circle(img, (x1, y1), 25, drawColor, cv2.FILLED)
#                 if xp == 0 and yp == 0:
#                     xp, yp = x1, y1

#                 # Determine whether to draw or erase
#                 if drawColor == (0, 0, 0):
#                     cv2.line(img, (xp, yp), (x1, y1),
#                              drawColor, eraserthickness)
#                     cv2.line(imgCanvas, (xp, yp), (x1, y1),
#                              drawColor, eraserthickness)
#                 else:
#                     cv2.line(img, (xp, yp), (x1, y1),
#                              drawColor, brushthickness)
#                     cv2.line(imgCanvas, (xp, yp), (x1, y1),
#                              drawColor, brushthickness)

#                 xp, yp = x1, y1

#         # Apply canvas and header to the displayed image
#         imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
#         _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
#         imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
#         img = cv2.bitwise_and(img, imgInv)
#         img = cv2.bitwise_or(img, imgCanvas)

#         img[0:125, 0:1280] = header

#         # Display the canvas and image
#         cv2.imshow("Canvas", imgCanvas)
#         cv2.imshow("Image", img)

#         # Wait for a key press (1ms)
#         key = cv2.waitKey(1) & 0xFF

#         # Exit loop if 'q' is pressed
#         if key == ord('q'):
#             break

#         # Trigger OCR if 'r' is pressed
#         if key == ord('r'):
#             # Recognize text using OCR
#             imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
#             recognized_text = pytesseract.image_to_string(imgGray)
#             # Print recognized text to the console
#             print("Recognized Text:", recognized_text)

#             # Display recognized text on the canvas
#             imgCanvasWithText = imgCanvas.copy()
#             cv2.putText(imgCanvasWithText, "OCR Output: " + recognized_text, (50, 670),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
#             cv2.imshow("Final Output with OCR", imgCanvasWithText)

#             # Wait for a few seconds to allow viewing the result
#             cv2.waitKey(3000)

#             # Save the recognized text to a file and handle exceptions
#             try:
#                 with open("recognized_text.txt", "w") as file:
#                     file.write(recognized_text)
#                 print("Text successfully saved to recognized_text.txt")
#             except Exception as e:
#                 print(f"Error saving text to file: {e}")

# finally:
#     cap.release()
#     cv2.destroyAllWindows()
#     asyncio.run(main())

# Import necessary libraries
import cv2
import numpy as np
import mediapipe as mp
import time
import os
import HandTrack as htp
import pytesseract  # Import pytesseract for OCR
import re  # Import regular expression library for input validation

# Specify the path to Tesseract executable
# Update with your Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ashua\AppData\Local\Tesseract-OCR\tesseract.exe'

# Set brush and eraser thickness for drawing
brushthickness = 15
eraserthickness = 80

# Initialize drawing coordinates
xp, yp = 0, 0

# Create a blank canvas to draw on
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

# Load overlay images for the drawing header
folderPath = "Header"
myList = os.listdir(folderPath)
overlaylist = []
for inPath in myList:
    image = cv2.imread(f'{folderPath}/{inPath}')
    overlaylist.append(image)
header = overlaylist[0]

# Set initial drawing color
drawColor = (17, 30, 60)

# Initialize the webcam capture
cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize the hand detector
detector = htp.handDetector(detectionCon=0.85)

# Function to evaluate mathematical expressions


def evaluate_expression(expression):
    # Strip unwanted characters and spaces
    expression = expression.replace(" ", "")

    # Validate expression to only allow numbers and operators
    if re.match(r'^[\d+\-*/().]+$', expression):
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            return "Error"
    else:
        return "Invalid Input"


# Main loop for real-time hand detection and drawing
while True:
    success, img = cap.read()
    if not success:
        break

    # Flip the image horizontally for a mirrored view
    img = cv2.flip(img, 1)

    # Detect hands in the frame
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)

    if len(lmlist) != 0:
        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]

        # Check finger positions for gesture recognition
        fingers = detector.fingersUp()

        if fingers[1] and fingers[2]:
            # Selection mode: Change color based on the selected area
            xp, yp = 0, 0
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25),
                          drawColor, cv2.FILLED)
            if y1 < 125:
                if 250 < x1 < 450:
                    header = overlaylist[0]
                    drawColor = (255, 0, 255)
                elif 550 < x1 < 750:
                    header = overlaylist[1]
                    drawColor = (255, 0, 0)
                elif 800 < x1 < 950:
                    header = overlaylist[2]
                    drawColor = (0, 255, 0)
                elif 1050 < x1 < 1200:
                    header = overlaylist[3]
                    drawColor = (0, 0, 0)

        if fingers[1] and not fingers[2]:
            # Drawing mode: Draw lines on the canvas
            cv2.circle(img, (x1, y1), 25, drawColor, cv2.FILLED)
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            # Determine whether to draw or erase
            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserthickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1),
                         drawColor, eraserthickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushthickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1),
                         drawColor, brushthickness)

            xp, yp = x1, y1

    # Apply canvas and header to the displayed image
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    img[0:125, 0:1280] = header

    # Display the canvas and image
    cv2.imshow("Canvas", imgCanvas)
    cv2.imshow("Image", img)

    # Wait for a key press (1ms)
    key = cv2.waitKey(1) & 0xFF

    # Exit loop if 'q' is pressed
    if key == ord('q'):
        break

    # Trigger OCR if 'r' is pressed
    if key == ord('r'):
        # Preprocess the image for OCR
        imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
        imgGray = cv2.GaussianBlur(imgGray, (5, 5), 0)
        _, imgThresh = cv2.threshold(
            imgGray, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Recognize text using OCR
        recognized_text = pytesseract.image_to_string(imgThresh)
        # Print recognized text to the console
        print("Recognized Text:", recognized_text)

        # Evaluate the recognized text if it is a mathematical expression
        result = evaluate_expression(recognized_text.strip())
        print("Expression Result:", result)  # Print result to console

        # Display recognized text and result on the canvas
        imgCanvasWithText = imgCanvas.copy()
        cv2.putText(imgCanvasWithText, "OCR Output: " + recognized_text, (50, 620),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(imgCanvasWithText, "Result: " + result, (50, 670),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("Final Output with OCR", imgCanvasWithText)

        # Wait for a few seconds to allow viewing the result
        cv2.waitKey(3000)

        # Save the recognized text and result to a file
        try:
            with open("recognized_text_and_result.txt", "w") as file:
                file.write(f"Recognized Text: {recognized_text}\n")
                file.write(f"Result: {result}\n")
            print("Text and result successfully saved to recognized_text_and_result.txt")
        except Exception as e:
            print(f"Error saving text to file: {e}")

# Clean up and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
