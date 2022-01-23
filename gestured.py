import mouse
import cv2
q=1
videoCaptureObject = cv2.VideoCapture(0)

def capture(baseline_image):
     ret,frame = videoCaptureObject.read()
     grayScaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
     cv2.imwrite("Down.png",smoothGrayScale)
     videoCaptureObject.release()
     cv2.destroyAllWindows()
def left(frame):
    left = cv2.imread("./gestured_image/Left.png")
    delta=cv2.absdiff(frame,left)
    threshold=cv2.threshold(delta,35,255, cv2.THRESH_BINARY)[1]
    (contours,_)=cv2.findContours(threshold,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            mouse.drag(100, 100, 0, 0, absolute=False, duration=0.1)
            continue
        continue
def right(frame):
    left = cv2.imread("./gestured_image/Right.png")
    delta=cv2.absdiff(frame,left)
    threshold=cv2.threshold(delta,35,255, cv2.THRESH_BINARY)[1]
    (contours,_)=cv2.findContours(threshold,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            mouse.drag(100, 100, 0, 0, absolute=False, duration=0.1)
            continue
        continue
def up(frame):
    left = cv2.imread("./gestured_image/Up.png")
    delta=cv2.absdiff(frame,left)
    threshold=cv2.threshold(delta,35,255, cv2.THRESH_BINARY)[1]
    (contours,_)=cv2.findContours(threshold,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            mouse.drag(100, 100, 0, 0, absolute=False, duration=0.1)
            continue
        continue
def down(frame):
    left = cv2.imread("./gestured_image/Down.png")
    delta=cv2.absdiff(frame,left)
    threshold=cv2.threshold(delta,35,255, cv2.THRESH_BINARY)[1]
    (contours,_)=cv2.findContours(threshold,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            mouse.drag(100, 100, 0, 0, absolute=False, duration=0.1)
            continue
        continue
def click(frame):
    left = cv2.imread("./gestured_image/Click.png")
    delta=cv2.absdiff(frame,left)
    threshold=cv2.threshold(delta,35,255, cv2.THRESH_BINARY)[1]
    (contours,_)=cv2.findContours(threshold,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            mouse.click('left')
            continue
        continue
while(q==1):
    net,first = videoCaptureObject.read()
    grayScaleImage = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    cv2.imshow('Set_Base',first)
    # Remove this Part to insert your own image
    left(smoothGrayScale)
    right(smoothGrayScale)
    up(smoothGrayScale)
    down(smoothGrayScale)
    click(smoothGrayScale)
    # Remove till here to capture ur own image
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        q=2
        cv2.destroyAllWindows()
        capture(smoothGrayScale)
    