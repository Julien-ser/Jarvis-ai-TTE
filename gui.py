import numpy as np
import cv2
import mediapipe as mp
import Hand_track as ht
import os
import webbrowser
import time
import math
import speech
import pyautogui
import subprocess
import jsearch
cap = cv2.VideoCapture('jarvis.gif')
cap2 = cv2.VideoCapture(0)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", int(650*2.5), int(426*2.5))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(650*2.5))
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(426*2.5))
detector = ht.handDetector(maxHands = 1, detectionCon = 0.6)
images = ["chrome.png", "discord.png",  "notepad.png", "search.png", "question.png", "music.png", "settings.png"]
im_size = (100, 100)
locations = [[0, 0, 100, 100], [0, 150, 100, 250], [550, 0, 650, 100], [550, 150, 650, 250], [550, 300, 650, 400], [400, 0, 500, 100],[400, 150, 500, 250]]
cv_loaded = []
paths = ["C:\Program Files\Google\Chrome\Application\chrome.exe", "C://Users//a1//AppData//Local//Discord//app-1.0.9036//Discord.exe", "Notepad", "Search", "Question", "Music", "Settings"]
paint_mode = 0
is_img = 0
#search("Jarvis")
limiterX = 0
limiterY = 0
limX = 0
limY = 0
circles = []
colors = [[(0,0,0), [0, 0]], [(0, 0, 255),[100, 0]], [(0, 255, 0),[200, 0]], [(255, 0, 0),[300, 0]], [(255, 255, 0), [400, 0]], [(0, 255, 255), [500, 0]], [(255, 0, 255), [600, 0]]]
paint_color = (0,0,0)
dist2 = 100
imgX = 200
imgY = 200
speech.SpeakText("Hello, I am Jarvis, your personal assistant! Navigate throughout my many functions using your hand, making sure I track your fingers on the webcam")
strikes = 3

for i in range(0, len(images)):
    image = cv2.imread(images[i], cv2.IMREAD_UNCHANGED)
    cv_loaded.append(cv2.resize(image, im_size))

def in_bounds(c1, c2):
    if(c2[0] < c1[0] < c2[2] and c2[1] < c1[1] < c2[3]):
        return True
    else:
        return False

def add_to_img(background, overlay, location):
    # separate the alpha channel from the color channels
    alpha_channel = overlay[:, :, 3] / 255 # convert from 0-255 to 0.0-1.0
    overlay_colors = overlay[:, :, :3]

    # To take advantage of the speed of numpy and apply transformations to the entire image with a single operation
    # the arrays need to be the same shape. However, the shapes currently looks like this:
    #    - overlay_colors shape:(width, height, 3)  3 color values for each pixel, (red, green, blue)
    #    - alpha_channel  shape:(width, height, 1)  1 single alpha value for each pixel
    # We will construct an alpha_mask that has the same shape as the overlay_colors by duplicate the alpha channel
    # for each color so there is a 1:1 alpha channel for each color channel
    alpha_mask = np.dstack((alpha_channel, alpha_channel, alpha_channel))

    # The background image is larger than the overlay so we'll take a subsection of the background that matches the
    # dimensions of the overlay.
    # NOTE: For simplicity, the overlay is applied to the top-left corner of the background(0,0). An x and y offset
    # could be used to place the overlay at any position on the background.
    h, w = overlay.shape[:2]
    background_subsection = background[location[1]:location[3], location[0]:location[2]]

    # combine the background with the overlay image weighted by alpha
    composite = background_subsection * (1 - alpha_mask) + overlay_colors * alpha_mask

    
    background[location[1]:location[3], location[0]:location[2]] = composite
    return background

#enables drawing on hannds
mpDraw = mp.solutions.drawing_utils
while(cap.isOpened()):
        ret, frame = cap.read()
        #cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
        #cv2.setWindowProperty("Image",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        #cv2.imshow("Hands", img)
        if ret:
            for i in range(0, len(cv_loaded)):
                frame = add_to_img(frame, cv_loaded[i], locations[i])
            success, img = cap2.read()
            img = cv2.flip(img, 1)
            img = cv2.resize(img, (frame.shape[1], frame.shape[0]))
            img = detector.findHands(img)
            lmLis = detector.findPos(img)
            if not paint_mode:
                frame = cv2.rectangle(frame, (0, 300), (100, 400), (255, 255, 255), -1)
                # Using cv2.putText() method 
                frame = cv2.putText(frame, 'PAINT', (10, 330), cv2.FONT_HERSHEY_SIMPLEX , 1, (0,0,0), 2, cv2.LINE_AA)
            else:
                frame = cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (255, 255, 255), -1)
                for color in colors:
                    frame = cv2.rectangle(frame, (color[1][0], 0), (color[1][0] + 75, 75), color[0], -1)
                frame = cv2.rectangle(frame, (0, 200), (100, 300), (255, 0, 255), -1)
                # Using cv2.putText() method 
                frame = cv2.putText(frame, 'EXIT', (10, 230), cv2.FONT_HERSHEY_SIMPLEX , 1, (0,0,0), 2, cv2.LINE_AA)
                frame = cv2.rectangle(frame, (550, 200), (650, 300), (0, 255, 0), -1)
                # Using cv2.putText() method 
                frame = cv2.putText(frame, 'CLEAR', (560, 230), cv2.FONT_HERSHEY_SIMPLEX , 1, (0,0,0), 2, cv2.LINE_AA)
            try:
                if is_img:
                    thing = cv2.imread("image.png")
                    thing = cv2.resize(thing, im_size)
                    frame[imgY:imgY+100, imgX:imgX+100] = thing
            except:
                imgY = 0
                imgX = 0
            for item in lmLis:
                if(item[0] == 8):
                    color = (255, 0, 255)
                    dist = math.sqrt((item[1] - limiterX)**2 + (item[2] - limiterY)**2)
                    for i in range(0, len(locations)):
                        if(dist > 50):
                            if not paint_mode:
                                if(in_bounds([item[1],  item[2]], locations[i])):
                                    if("exe" in paths[i]):
                                        os.startfile(paths[i])
                                        time.sleep(0.5)
                                    else:
                                        if paths[i] == "Notepad":
                                            text = ""
                                            speech.SpeakText("say what you want until you say exit, the text will be put on a txt file")
                                            fileinfo = ""
                                            while("exit" not in text.lower()):
                                                if(strikes >= 1):
                                                    speech.SpeakText("Try typing instead: ")
                                                    text = input("Enter it here please: ")
                                                else:
                                                    text = speech.getText()
                                                if(text == ""):
                                                    speech.SpeakText("I couldn't hear that, please try again: ")
                                                    strikes += 1
                                                else:
                                                    speech.SpeakText("Got it! Added to txt file")
                                                    fileinfo += text
                                                    fileinfo += '\n'

                                            txt = open("Log.txt","a")
                                            txt.write(fileinfo)
                                            txt.close()
                                            speech.SpeakText("TXT file is saved!")
                                            os.startfile("Log.txt")
                                        elif paths[i] == "Settings":
                                            subprocess.run(['control.exe', 'desk.cpl'])
                                        elif paths[i] == "Search" or paths[i] == "Music":
                                            if paths[i] == "Search":
                                                if not is_img:
                                                    is_img = 1
                                            topic = ""
                                            speech.SpeakText("Tell me the topic you want an image or song for: ")
                                            while topic == "":
                                                if(strikes >= 1):
                                                    speech.SpeakText("Try typing instead: ")
                                                    topic = input("Enter it here please: ")
                                                else:
                                                    topic = speech.getText()
                                                if(topic == ""):
                                                    strikes += 1
                                                    speech.SpeakText("I couldn't hear that, please try again: ")
                                                else:
                                                    speech.SpeakText("Got it! Give me less than a minute!")
                                            if paths[i] == "Search":
                                                jsearch.GetImage(topic)
                                                #os.startfile("image.png")
                                            else:
                                                jsearch.GetMusic(topic)
                                        elif paths[i] == "Question":
                                            topic = ""
                                            speech.SpeakText("Ask me a question: ")
                                            while topic == "":
                                                if(strikes >= 1):
                                                    speech.SpeakText("Try typing instead: ")
                                                    topic = input("Enter it here please: ")
                                                else:
                                                    topic = speech.getText()
                                                if(topic == ""):
                                                    strikes += 1
                                                    speech.SpeakText("I couldn't hear that, please try again: ")
                                                else:
                                                    speech.SpeakText("Got it! Give me less than a minute!")
                                            speech.SpeakText(jsearch.chat(topic))
                                            
                                                
                                                
                                    break
                                elif(in_bounds([item[1], item[2]], [0, 300, 100, 400])):
                                    print("switching to paint")
                                    paint_mode = 1
                                circles = []
                            else:
                                for bound in colors:
                                    if(in_bounds([item[1], item[2]], [bound[1][0], 0, bound[1][0]+75, bound[1][1]+75])):
                                        paint_color = bound[0]
                                if(in_bounds([item[1], item[2]], [0, 200, 100, 300])):
                                    print("switching back")
                                    paint_mode = 0
                                elif(in_bounds([item[1], item[2]], [550, 200, 650, 300])):
                                    circles = []
                                if(dist > 50):
                                    circles.append([item[1], item[2], paint_color])
                        else:
                            if item[1] >= imgX and item[1] <= imgX + 100:
                                if item[2] >= imgY and item[2] <= imgY + 100:
                                    imgX = item[1] - 50
                                    imgY = item[2] - 50
                else:
                    if(item[0] == 4):
                        limiterX = item[1]
                        limiterY = item[2]
                    if(item[0] == 20):
                        limX = item[1]
                        limY = item[2]
                    color = (0, 255, 255)
                
                #dist2 = math.sqrt((limX - limiterX)**2 + (limY - limiterY)**2)
                #if(dist2 < 40):
                #    pyautogui.hotkey('alt', 'tab')
                frame = cv2.circle(frame, (item[1], item[2]), 3, color, -1)
            for circle in circles:
                frame = cv2.circle(frame, (circle[0], circle[1]), 5, circle[2], -1)
            cv2.imshow("Image", frame)
            #try:
            #    print(frame.shape)
            #except:
            #    pass
        else:
           #print('no video')
           cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
           continue
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    
cap.release()
cv2.destroyAllWindows()
