import cv2
import numpy as np


kamera = cv2.VideoCapture(0)

print("Kamera açılıyor... Kapatmak için klavyeden 'q' tuşuna basın.")

while True:
    basarili_mi, kare = kamera.read()
    if not basarili_mi:
        break
        
    kare = cv2.flip(kare, 1)
    hsv_kare = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)

    alt_mavi = np.array([90, 50, 50])
    ust_mavi = np.array([130, 255, 255])

    maske = cv2.inRange(hsv_kare, alt_mavi, ust_mavi)
    sinirlar, _ = cv2.findContours(maske, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for sinir in sinirlar:
        alan = cv2.contourArea(sinir)
        if alan > 500: 
            x, y, w, h = cv2.boundingRect(sinir)
            
            cv2.rectangle(kare, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(kare, "Hedef Tespit Edildi", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("STNM Gorev 2 - Hedef Takibi", kare)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()