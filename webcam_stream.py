import cv2
import requests
import numpy as np
# URL of the backend API
BACKEND_URL = "http://127.0.0.1:5000/process_frame"
cap = cv2.VideoCapture(0)  # Open the webcam
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Encode the frame as JPEG
    _, encoded_frame = cv2.imencode('.jpg', frame)
    # Send the frame to the backend
    response = requests.post(BACKEND_URL, files={'frame': encoded_frame.tobytes()})
    # Get processed frame from backend
    if response.status_code == 200:
        # Decode the received frame
        processed_frame = cv2.imdecode(
            np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR
        )
        # Display the processed frame
        cv2.imshow("Processed Frame", processed_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()