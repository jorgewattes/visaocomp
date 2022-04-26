import cv2 as cv

cap = cv.VideoCapture(2)

while(True):
    ret,frame = cap.read()

    cv.imshow('Frame',frame)
    if(cv.waitKey(1) & 0xFF ==ord('q')):
        #Printar ao quitar
        cv.imwrite('Aula02/print.png',frame)
        break

cap.release()
cv.destroyAllWindows()