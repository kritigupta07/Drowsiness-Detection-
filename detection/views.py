from django.http import StreamingHttpResponse, JsonResponse
from django.shortcuts import render
import cv2
import imutils
from scipy.spatial import distance
from imutils import face_utils
import dlib
from pygame import mixer
import threading

# Initialize Pygame mixer for alert sound
mixer.init()
mixer.music.load("models/music.wav")

# Model variables
thresh = 0.25
frame_check = 20
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

# Global flag to control model prediction
is_detecting = False

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def detect_drowsiness_live():
    global is_detecting
    cap = cv2.VideoCapture(0)
    flag = 0
    
    while is_detecting:  # Only run if is_detecting is True
        ret, frame = cap.read()
        if not ret:
            break
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        subjects = detect(gray, 0)

        for subject in subjects:
            shape = predict(gray, subject)
            shape = face_utils.shape_to_np(shape)
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            ear = (leftEAR + rightEAR) / 2.0
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            if ear < thresh:
                flag += 1
                if flag >= frame_check:
                    cv2.putText(frame, "****************ALERT!****************", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    mixer.music.play()
            else:
                flag = 0
        
        # Encode the frame as a JPEG image to stream it
        ret, jpeg = cv2.imencode('.jpg', frame)
        if jpeg is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
    
    cap.release()

# View to handle the starting of detection
def start_detection(request):
    global is_detecting
    is_detecting = True
    return JsonResponse({'status': 'started'})

# View to handle the stopping of detection
def stop_detection(request):
    global is_detecting
    is_detecting = False
    return JsonResponse({'status': 'stopped'})

# Streaming the video feed to the template
def video_feed(request):
    return StreamingHttpResponse(detect_drowsiness_live(), content_type='multipart/x-mixed-replace; boundary=frame')

# Template view
def detection(request):
    return render(request, 'detection.html')
