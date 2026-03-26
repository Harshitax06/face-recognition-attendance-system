import os
import cv2
import numpy as np
import face_recognition

# Paths (use absolute paths you already used)
modi_path = '/Users/shashankvns/Desktop/attendance_system/images_attendance/shashankian.jpg'
test_path = '/Users/shashankvns/Desktop/attendance_system/images_attendance/shashank.jpeg'

# quick existence check
for p in (modi_path, test_path):
    if not os.path.isfile(p):
        raise SystemExit(f"Image not found: {p}")

# face_recognition.load_image_file returns RGB arrays
imgModi_rgb = face_recognition.load_image_file(modi_path)
imgTest_rgb = face_recognition.load_image_file(test_path)

# convert to BGR for OpenCV display/rectangle (OpenCV expects BGR)
imgModi_bgr = cv2.cvtColor(imgModi_rgb, cv2.COLOR_RGB2BGR)
imgTest_bgr = cv2.cvtColor(imgTest_rgb, cv2.COLOR_RGB2BGR)

# safe helper to get the first encoding
def get_first_encoding(img_rgb, label):
    locations = face_recognition.face_locations(img_rgb)
    print(f"{label} - face locations found: {len(locations)}")
    if not locations:
        return None, []
    encodings = face_recognition.face_encodings(img_rgb, known_face_locations=locations)
    return (encodings[0] if encodings else None), locations

encodeModi, locsModi = get_first_encoding(imgModi_rgb, "Modi")
if encodeModi is None:
    raise SystemExit("No face/encoding found in Modi image. Check the file or use another image.")

encodeTest, locsTest = get_first_encoding(imgTest_rgb, "Test")
if encodeTest is None:
    raise SystemExit("No face/encoding found in Test image. Check the file or use another image.")

# draw rectangles (use first location from list)
top, right, bottom, left = locsModi[0]
cv2.rectangle(imgModi_bgr, (left, top), (right, bottom), (155, 0, 255), 2)

top_t, right_t, bottom_t, left_t = locsTest[0]
cv2.rectangle(imgTest_bgr, (left_t, top_t), (right_t, bottom_t), (155, 0, 255), 2)

# compare faces
results = face_recognition.compare_faces([encodeModi], encodeTest)
faceDis = face_recognition.face_distance([encodeModi], encodeTest)
print("compare result:", results, "distance:", faceDis)

# put text on test image
cv2.putText(imgTest_bgr, f'{results} {round(faceDis[0],2)}', (50, 50),
            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

# show images
cv2.imshow('modi', imgModi_bgr)
cv2.imshow('test', imgTest_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
