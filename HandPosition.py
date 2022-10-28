from pickletools import UP_TO_NEWLINE
import SnakaGame as game
from turtle import left
import cv2
from cv2 import FONT_HERSHEY_SIMPLEX
import mediapipe as mp
import numpy as np
import pygame
drawing_utils = mp.solutions.drawing_utils
from settingsSnakeFun import DOWN, LEFT, RIGHT,UP

from multiprocessing import Process
from threading import Thread
 

mp_hands = mp.solutions.hands
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
hybrid = (23, 234, 223)


# Set up the drawing window


# Run until the user asks to quit
running = True
def video():
    cap = cv2.VideoCapture(0)
    while running:
    

        # Did the user click the window close button?
    
    
        with mp_hands.Hands() as hands:
            
                

                
                
                ret,frame = cap.read()
                imag = cv2.resize(frame, (600,600))
                image = cv2.cvtColor(imag,cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
            
                if results.multi_hand_landmarks:
                    for landmarks in results.multi_hand_landmarks:
                    
                        for id, land in enumerate(landmarks.landmark):
                            height, width, z = image.shape
                            x, y = int(width * land.x), int(height * land.y)
                            if id == 8:
                                    cv2.circle(image, (x, y), 25, hybrid, cv2.FILLED)
                                    # win_x,win_y,win_w,win_h = cv2.getWindowImageRect("Hand Tracking")
                                    # print(cv2.getWindowImageRect("Hand Tracking"))
                                    cv2.line(image, (200,200), (400,200), (0,0,0))
                                    cv2.line(image, (200,200), (200,400), (0,0,0))
                                    cv2.line(image, (200,400), (400,400), (0,0,0))
                                    cv2.line(image, (400,400), (400,200), (0,0,0))
                                    if landmarks.landmark[8].x *width <=200 and landmarks.landmark[8].y*height  >=200 and landmarks.landmark[8].y*height  <=400:
                                        
                                        cv2.putText(image, "Left ",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)
                                        game.TurnSnake(LEFT)
                                    elif landmarks.landmark[8].x*width >=400 and landmarks.landmark[8].y*height  >=200 and landmarks.landmark[8].y*height  <=400:
                                        game.TurnSnake(RIGHT)
                                        cv2.putText(image, "Right ",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)
                                    elif landmarks.landmark[8].y*height  <=200 and landmarks.landmark[8].x*width <=400 and landmarks.landmark[8].x*width >=200:
                                        game.TurnSnake(UP)
                                        cv2.putText(image, "Top ",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)
                                    elif landmarks.landmark[8].y*height >=400 and landmarks.landmark[8].x*width <=400 and landmarks.landmark[8].x*width >=200:
                                        game.TurnSnake(DOWN)
                                        cv2.putText(image, "Bottom ", (100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)
                                    
                                    
                                    
                        drawing_utils.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)
                    
                    
                cv2.imshow("Hand Tracking", image)
                
            
                if cv2.waitKey(10) & 0xFF==ord('q'):
                    break
            
    cap.release()
    cv2.destroyAllWindows() 
def play_sound(): 
    # import your script A
    a = (r"C:\Users\A\Desktop\sound.mp3")
    (a)

def CV2_stuff():
    # import your script B
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    cap = cv2.VideoCapture("video.mp4")
    ...


Thread(target = game.main).start() 
Thread(target = video).start()