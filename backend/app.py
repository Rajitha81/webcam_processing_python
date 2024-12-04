from flask import Flask, request, Response
import cv2
import numpy as np
app = Flask(__name__)
@app.route('/process_frame', methods=['POST'])
def process_frame():
    # Read the incoming frame
    file = request.files['frame'].read()
    np_img = np.frombuffer(file, np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    # Add a bounding box to the frame
    height, width, _ = frame.shape
    start_point = (50, 50)  # Top-left corner
    end_point = (width - 50, height - 50)  # Bottom-right corner
    color = (0, 255, 0)  # Green box
    thickness = 2  # Thickness of the box
    cv2.rectangle(frame, start_point, end_point, color, thickness)
    # Encode the frame as JPEG
    _, encoded_frame = cv2.imencode('.jpg', frame)
    return Response(encoded_frame.tobytes(), mimetype='image/jpeg')
if __name__ == '__main__':
    app.run(debug=True)
