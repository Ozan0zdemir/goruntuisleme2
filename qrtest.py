import cv2

# QR kod tarayıcı nesnesi oluştur
qr_detector = cv2.QRCodeDetector()

# Kamerayı başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Kamera açılamadı.")
    exit()

print("QR kod okutmak icin kameraya gosterin. Cikmak icin 'q' tusuna basin.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # QR kodu tara
    data, bbox, _ = qr_detector.detectAndDecode(frame)

    # QR kod verisi bulunduysa yazdır
    if bbox is not None and data:
        # Dörtgen çiz
        for i in range(len(bbox)):
            pt1 = tuple(bbox[i][0])
            pt2 = tuple(bbox[(i+1) % len(bbox)][0])
            cv2.line(frame, (int(pt1[0]), int(pt1[1])), (int(pt2[0]), int(pt2[1])), (255, 0, 0), 2)

        # Veriyi ekrana yazdır
        cv2.putText(frame, f"Veri: {data}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        print(f"QR Kodu Icerigi: {data}")

    # Kamerayı göster
    cv2.imshow("QR Kod Okuyucu", frame)

    # 'q' ile çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
