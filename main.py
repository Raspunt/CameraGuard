import cv2
from telegaSend import TelegaBot


class Camera:

    cap = cv2.VideoCapture(0)

    def findFaces(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        while True:
            ret,frame = self.cap.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray,1.1,4)
            
            



            tb = TelegaBot()

            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                tb.send_text("вор помогите")
                imagePath = "Bor.png"
                cv2.imwrite(imagePath,frame)
                tb.send_photo(imagePath)




            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            


            
            # cv2.imshow("Bor",frame)

            
            






cap = Camera()

cap.findFaces()


        



