import cv2
from django.http import StreamingHttpResponse
from django.shortcuts import render
from deepface import DeepFace
from django.core.files.storage import FileSystemStorage
from textblob import TextBlob

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def detect_emotion(face):
    try:
        result = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)

        if isinstance(result, list):
            return result[0].get('dominant_emotion', 'no emotion')
        else:
            return result.get('dominant_emotion', 'no emotion')

    except:
        return "error"


def gen_frames():
    cap = cv2.VideoCapture(0)
    emotion = "Detecting..."
    frame_count = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        frame_count += 1

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]

            if frame_count % 15 == 0:
                emotion = detect_emotion(face)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv2.putText(frame, "Emotion: " + str(emotion), (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
def index(request):
    return render(request, 'index.html')

def video_feed(request):
    return StreamingHttpResponse(
        gen_frames(),
        content_type='multipart/x-mixed-replace; boundary=frame'
    )
def image_emotion(request):
    emotion = None

    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        file_path = fs.path(filename)

        try:
            result = DeepFace.analyze(file_path, actions=['emotion'])

            if isinstance(result, list):
                emotion = result[0]['dominant_emotion']
            else:
                emotion = result['dominant_emotion']

        except:
            emotion = "Error detecting emotion"

    return render(request, 'image.html', {'emotion': emotion})
def text_emotion(request):
    result = None

    if request.method == 'POST':
        text = request.POST.get('text')

        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            result = "Positive "
        elif polarity < 0:
            result = "Negative "
        else:
            result = "Neutral "

    return render(request, 'text.html', {'result': result})