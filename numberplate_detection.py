import cv2

harcascade = "indian_license_plate.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640) # width
cap.set(4, 480) #height

min_area = 500

def is_detected(frame):
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
           
           #cropping the number plate part and saving the plate area
            img_roi = img[y: y+h, x:x+w]
            #cv2.imshow("ROI", img_roi)
            return True
        else:
            return False


    
    cv2.imshow("Result", img)

