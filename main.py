import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width of the webcam
cap.set(4, 720)  # Height of the webcam

# Initialize hand detector
detector = HandDetector(detectionCon=0.7)
startDist = None
scale = 0
cx, cy = 500, 500

dragging = False
image_position = [cx, cy]
hand_start_pos = None

while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img)
    img1 = cv2.imread("sample.jpg")  # Load your image here

    if len(hands) == 2:
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and \
                detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            if startDist is None:
                length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                startDist = length

            length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
            scale = int((length - startDist) // 2)
            cx, cy = info[4:]
    else:
        startDist = None

    if len(hands) == 1:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        # Check if the hand is in a grabbing state (all fingers down)
        if fingers == [0, 0, 0, 0, 0]:
            if not dragging:
                # Start dragging
                dragging = True
                hand_start_pos = hand["center"]
            else:
                # Calculate offset based on hand movement
                offset_x = hand["center"][0] - hand_start_pos[0]
                offset_y = hand["center"][1] - hand_start_pos[1]
                cx += offset_x
                cy += offset_y
                hand_start_pos = hand["center"]
        else:
            dragging = False
            hand_start_pos = None

    try:
        h1, w1, _ = img1.shape
        newH, newW = ((h1 + scale) // 2) * 2, ((w1 + scale) // 2) * 2
        img1 = cv2.resize(img1, (newW, newH))

        # Ensure the image stays within the bounds of the webcam view
        cx = max(newW // 2, min(cx, img.shape[1] - newW // 2))
        cy = max(newH // 2, min(cy, img.shape[0] - newH // 2))

        # Place the resized image at the new location
        img[cy - newH // 2:cy + newH // 2, cx - newW // 2:cx + newW // 2] = img1
    except:
        pass

    # Display the video feed
    cv2.imshow("Drag and Drop Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close all windows
cap.release()
cv2.destroyAllWindows()
