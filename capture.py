import cv2,time

video=cv2.VideoCapture(0) #0 as only 1 video taking hardware is present

                    #video = capturing images again and again as frame and show
while True:
    check,frame=video.read()            #check-image running or not ,frame=store first images
    # print(check)
    # print(frame)
    time.sleep(3)       #wait for 3 sec
    cv2.imshow("Capture video",frame)       #just show first image
    key=cv2.waitKey(1)      #return which key clicked

    if(key==ord('q')):      #to stop video working press q
        break

video.release()              #to open camera
cv2.destroyAllWindows()