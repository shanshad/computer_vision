import cv2
import mediapipe as mp


mp_face_detection=mp.solutions.face_detection
def face_blur(img):  
    H,W=img.shape[0],img.shape[1]  
    with mp_face_detection.FaceDetection(model_selection=0,min_detection_confidence=0.5) as face_detection:
        img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        out=face_detection.process(img_rgb)
        #print(out.detections)
        if out.detections is not None:
            for detections in out.detections:
                location=detections.location_data
                bbox=location.relative_bounding_box
                x1,y1,w,h=bbox.xmin,bbox.ymin,bbox.width,bbox.height #it gives a value between 0 and 1
                x1=int(x1*W)
                y1=int(y1*H)
                w=int(w*W)
                h=int(h*H)
                img[y1:y1+h,x1:x1+w]=cv2.blur(img[y1:y1+h,x1:x1+w],(30,30))
    return(img)
cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame=cap.read()
    image=face_blur(frame)
    cv2.imshow('poto',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

