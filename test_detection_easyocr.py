import cv2
from easyocr import Reader
from PIL import Image

# img_path = 'data/helloworld.png'
# img = cv2.imread(img_path)
cap=cv2.VideoCapture(0)
text=''
reader=Reader(['en'])
while cap.isOpened():
    ret,frame=cap.read()
    if ret is None:
        print(f"Error: Could not load image from {img_path}")
    else:
        
        results=reader.readtext(frame)
        for i in results:
            text=text+i[1]+' '
        print(text)
        cv2.imshow('image',frame)
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break
cap.release()    
cv2.destroyAllWindows()
