import cv2
from deepface import DeepFace
faceCascade = cv2.CascadeClassifier (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
ans=True
while ans:
    print("1.Detect Gender")
    print("2.Detect Race")
    print("3.Detect Emotion")
    print("4.Exit/Quit")
    ans=input("What would you like to do?" )
    if ans=="1":
        cap= cv2.VideoCapture(1)
        # Check if the webcam is opened correctly
        if not cap.isOpened():
            cap= cv2.VideoCapture(0) 
        if not cap.isOpened():
            raise IOError("cannot open cam")
        while True:
            ret, frame = cap.read()
            result = DeepFace.analyze(frame, actions = ['gender'])
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
            #print (faceCascade.empty()) 
            faces = faceCascade.detectMultiScale (gray,1.1,4)
            # Draw a rectangle around the faces 
            for(x, y, w, h) in faces: 
                cv2.rectangle(frame, 
                            (x, y), 
                            (x+w, y+h),
                            (0, 255, 0),
                            2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            # Use putText() method for 
            # inserting text on video
            cv2.putText(frame,result['gender'],(80, 80),font, 3,(0, 0, 255),2,cv2.LINE_4)
            cv2.imshow('Original video', frame)
            if cv2.waitKey(2) & 0xFF == ord('q') :
                break
        cap.release()
        cv2.destroyAllWindows()
    elif ans=="2":
        cap= cv2.VideoCapture(1)
        # Check if the webcam is opened correctly
        if not cap.isOpened():
            cap= cv2.VideoCapture(0) 
        if not cap.isOpened():
            raise IOError("cannot open cam")
        while True:
            ret, frame = cap.read()
            result = DeepFace.analyze(frame, actions = ['race'])
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
            #print (faceCascade.empty()) 
            faces = faceCascade.detectMultiScale (gray,1.1,4)
            # Draw a rectangle around the faces 
            for(x, y, w, h) in faces: 
                cv2.rectangle(frame, 
                            (x, y), 
                            (x+w, y+h),
                            (0, 255, 0),
                            2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            # Use putText() method for 
            # inserting text on video
            cv2.putText(frame,result['dominant_race'],(80, 80),font, 3,(0, 0, 255),2,cv2.LINE_4)
            cv2.imshow('Original video', frame)
            if cv2.waitKey(2) & 0xFF == ord('q') :
                break
        cap.release()
        cv2.destroyAllWindows()
    elif ans=="3":
        cap= cv2.VideoCapture(1)
        # Check if the webcam is opened correctly
        if not cap.isOpened():
            cap= cv2.VideoCapture(0) 
        if not cap.isOpened():
            raise IOError("cannot open cam")
        while True:
            ret, frame = cap.read()
            result = DeepFace.analyze(frame, actions = ['emotion'])
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
            #print (faceCascade.empty()) 
            faces = faceCascade.detectMultiScale (gray,1.1,4)
            # Draw a rectangle around the faces 
            for(x, y, w, h) in faces: 
                cv2.rectangle(frame, 
                            (x, y), 
                            (x+w, y+h),
                            (0, 255, 0),
                            2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            # Use putText() method for 
            # inserting text on video
            cv2.putText(frame,result['dominant_emotion'],(80, 80),font, 3,(0, 0, 255),2,cv2.LINE_4)
            cv2.imshow('Original video', frame)
            if cv2.waitKey(2) & 0xFF == ord('q') :
                break
        cap.release()
        cv2.destroyAllWindows()
    elif ans=="4":
        print("\n Goodbye") 
    elif ans !="":
        print("\n Not Valid Choice Try again") 