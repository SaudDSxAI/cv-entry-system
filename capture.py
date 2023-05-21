import sys
sys.path.append('C:/Users/sauds/Desktop/my_project')
from recognizer import SimpleFacerec
import cv2
import os




sfr = SimpleFacerec()

#Loading Images
def Function1():
    people = []
    for i in os.listdir('C:/Users/sauds/Desktop/my_project/Pictures'):
        people.append(i)
        
    path = 'C:/Users/sauds/Desktop/my_project/Pictures/'


    # Encode faces from a folder
    for i in people:
        sfr.load_encoding_images(path+i)


cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
# Taking picture and then comparing with the trained data
def Function2():
    
    ret, frame = cap.read()
    name1 =    "\\\\\\\\Unknown////////"
    reg =      "\\\\\\\\Unknown////////"
    batch =    "\\\\\\\\Unknown////////"
    faculty  = "\\\\\\\\Unknown////////"
    name_list = []
    
    

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        
        if name != "Unknown":
            name_list = name.split("_")
            name1 = name_list[0]
            reg = name_list[2]
            batch = name_list[3]
            faculty = name_list[4]
            cv2.putText(frame, name1,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
        
        else:
            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
    
    cv2.imshow("Frame", frame)
    cv2.waitKey(6000)
    cv2.destroyAllWindows()
    return name1,reg,batch,faculty


def Function3():
    
    ret, frame = cap2.read()
    name1 =    "\\\\\\\\Unknown////////"
    reg =      "\\\\\\\\Unknown////////"
    batch =    "\\\\\\\\Unknown////////"
    faculty  = "\\\\\\\\Unknown////////"
    name_list = []
    
    

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        
        if name != "Unknown":
            name_list = name.split("_")
            name1 = name_list[0]
            reg = name_list[2]
            batch = name_list[3]
            faculty = name_list[4]
            cv2.putText(frame, name1,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
        
        else:
            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)


    cv2.imshow("Frame", frame)
    cv2.waitKey(6000)
    cv2.destroyAllWindows()
    return name1,reg,batch,faculty