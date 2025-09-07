import cv2
import numpy as np

img = cv2.imread("sekil.jpg")
if img is None:
    print("Hata: Gorsel yuklenemedi. Lutfen dosya adini ve yolunu kontrol edin.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 1)

edges = cv2.Canny(blur, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 300:
        continue

    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(hull)

    if hull_area > 0:
        solidity = float(area) / hull_area
    else:
        solidity = 0

    if solidity < 0.8:
        continue

    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
    corners = len(approx)

    if corners == 3:
        shape_name = "Ucgen"
    elif corners == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        shape_name = "Kare" if 0.95 <= aspect_ratio <= 1.05 else "Dikdortgen"
    elif corners == 5:
        shape_name = "Besgen"
    elif corners == 6:
        shape_name = "Altigen"
    else:
        shape_name = "Daire"

    cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)

    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        x, y = approx[0][0]
        cX, cY = x, y
        
    cv2.putText(img, shape_name, (cX - 20, cY),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

cv2.imshow("Sekil Tespiti", img)
cv2.waitKey(0)
cv2.destroyAllWindows()