import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'images_attendance'
images = []
classNames = []

# helper to consider only images
def is_image_file(fn):
    return fn.lower().endswith(('.jpg', '.jpeg', '.png'))

# read folder contents safely
try:
    myList = sorted(os.listdir(path))
except FileNotFoundError:
    raise SystemExit(f"Images folder not found: {path}")

print("Files found:", myList)

# load images (skip non-image files and unreadable files)
for cl in myList:
    if not is_image_file(cl):
        print("SKIP (not image):", cl)
        continue
    img_path = os.path.join(path, cl)
    curImg = cv2.imread(img_path)
    if curImg is None:
        print("SKIP (cv2.imread failed):", img_path)
        continue
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

print("Names:", classNames)

# safe encoding builder
def findEncodings(images_list):
    encodeList = []
    for img in images_list:
        # ensure image loaded
        if img is None:
            print("skip None image")
            continue
        # convert BGR -> RGB for face_recognition
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encs = face_recognition.face_encodings(img_rgb)
        if not encs:
            print("No faces found in one of the known images (skipping)")
            continue
        encodeList.append(encs[0])
    return encodeList

# ensure Attendance.csv exists and has header
def ensure_csv():
    if not os.path.exists('Attendance.csv'):
        with open('Attendance.csv', 'w') as f:
            f.write('Name,Time,Date\n')

def markAttendance(name):
    ensure_csv()
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.strip().split(',')
            if entry:
                nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.now()
            tString = time_now.strftime('%H:%M:%S')
            dString = time_now.strftime('%d/%m/%Y')
            f.writelines(f'{name},{tString},{dString}\n')
            print(f"Marked attendance: {name} at {tString} {dString}")
        else:
            # optional: print that already present
            # print(f"{name} already in Attendance.csv")
            pass

# Build encodings (safe)
encodeListKnown = findEncodings(images)
print('Encoding Complete. Known count =', len(encodeListKnown))

# If no known encodings, don't continue
if len(encodeListKnown) == 0:
    raise SystemExit("No known face encodings found. Add valid images in the images_attendance folder.")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise SystemExit("Could not open webcam (0)")

while True:
    success, img = cap.read()
    if not success or img is None:
        print("Failed to read frame from webcam")
        break

    # resize frame for speed
    imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # debug distances
        print("distances:", faceDis)
        matchIndex = np.argmin(faceDis) if len(faceDis) > 0 else None
        if matchIndex is not None and matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print("Recognized:", name)
            y1, x2, y2, x1 = faceLoc
            # scale back up to original size
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 250, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow('webcam', img)
    # 13 => Enter, change if you prefer 'q' (ord('q')==113)
    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows()
