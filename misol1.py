import cv2

# DroidCam odatda shu URL orqali oqim beradi:
url = "http://192.168.95.209:8080/video"  

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("❌ Ulanmadi.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Kadr olinmadi.")
        break

    cv2.imshow("DroidCam IP Stream", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
