
import cv2            # for image processing OpenCV
import time           # to calculate fps
import mediapipe as mp  # for hand tracing mediapipe
import numpy as np    # for math operations

# ---------------------------------------------------------
# Camera and Video  recording settings
# ---------------------------------------------------------

cap = cv2.VideoCapture(0)  # open the computer cam

# Video kaydı için codec ve VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # for AVI format  XVID codec
out = cv2.VideoWriter('hand_drawing.avi', fourcc, 30.0, (640, 480))  # 30 FPS, 640x480 resolution

# ---------------------------------------------------------
# MediaPipe hand tracing code
# ---------------------------------------------------------

mpHand = mp.solutions.hands
hands = mpHand.Hands(
    max_num_hands=1,              # only one hand will follow 
    min_detection_confidence=0.7, # perception confidence
    min_tracking_confidence=0.7   # follow confidence
)
mpDraw = mp.solutions.drawing_utils  # Helper for drawing Landmarks

# ---------------------------------------------------------
# Variables
# ---------------------------------------------------------
ptime = 0          # previous time  (for calculate FPS )
canvas = None      # Blank image for draw on 
prev_x, prev_y = 0, 0  # Previous index finger coordinats

# ---------------------------------------------------------
# Main loop
# ---------------------------------------------------------
while True:
    success, img = cap.read()  # Read image for camera 
    if not success:            # İf he doesn't read it,give error 
        print("Kamera okunamadı")
        break

    img = cv2.flip(img, 1)     # Mirroing
    h, w, c = img.shape        # height,weight

   
    if canvas is None:
        canvas = np.zeros_like(img)

    # BGR → RGB 
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Do hand tracking
    result = hands.process(imgRGB)

    # if the hand detected
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            # index finger  landmark = 8
            lm = handLms.landmark[8]
            cx, cy = int(lm.x * w), int(lm.y * h)  # Normalized → pixel

            # If previous coordinate does not exist, start
            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = cx, cy

            # Do draweing
            cv2.line(canvas, (prev_x, prev_y), (cx, cy), (0, 255, 0), 5)

            # Update coordinates
            prev_x, prev_y = cx, cy

            # Draw to all of hand
            mpDraw.draw_landmarks(img, handLms, mpHand.HAND_CONNECTIONS)
    else:
        # If the hand is not visible, reset the coordinates
        prev_x, prev_y = 0, 0

    # Combine the camera image with the canvas
    combined = cv2.add(img, canvas)

    # FPS calculate
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    # Write to fps
    cv2.putText(combined, f'FPS: {int(fps)}', (20, 70), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the result
    cv2.imshow("Hand Drawing App", combined)

    # Save the video
    out.write(combined)

    # Exit with the ESC key
    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        break

# ---------------------------------------------------------
# Free up resources
# ---------------------------------------------------------
cap.release()
out.release()
cv2.destroyAllWindows()
