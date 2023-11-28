def detect_and_save():
    pin = MotionSensor(22) # 센서의 GPIO 번호

    if pin.motion_detected:
        print("!!!!!!!")
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 440)

        ret, frame = cap.read() # 캡쳐
        cap.release()
        cv2.destroyAllWindows()

        if ret:
            cv2.imwrite('capture.jpg', frame)
            with open('capture.jpg', 'rb') as f:
                binary_data = f.read()
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            cursor = db.cursor()
            sql = "INSERT INTO images_table (current_time, image) VALUES (%s, %s)"
            val = (current_time, binary_data)
            cursor.execute(sql, val)
            db.commit()
