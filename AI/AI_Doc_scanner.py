import cv2
import numpy as np

width = 1280
height = 720

# using the webcam
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
cap.set(10, 100)

def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
    imgCanny = cv2.Canny(imgBlur, 90, 95)
    kernel = np.ones((5, 5), np.uint8)
    imgDilated = cv2.dilate(imgCanny, kernel, iterations=3)
    imgEroded = cv2.erode(imgDilated, kernel, iterations=1)

    return imgEroded

def contourDetection(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    biggest = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 14000:
            perimeter = cv2.arcLength(cnt, True)
            approxCornerPoints = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            objCor = len(approxCornerPoints)
            if objCor == 4:
                if area > biggest:
                    biggest = area
                    corner = approxCornerPoints
    try:
        return corner
    except:
        return None

def reorder(points):
    point = points.reshape((4, 2))
    newPoints = np.zeros((4, 1, 2), np.int32)
    add = point.sum(1)

    newPoints[0] = point[np.argmin(add)]
    newPoints[3] = point[np.argmax(add)]

    minus = np.diff(point, axis=1)
    newPoints[1] = point[np.argmin(minus)]
    newPoints[2] = point[np.argmax(minus)]

    return newPoints

def warpImage(cnt, image):
    points = reorder(cnt)

    avgWidth = 210 * 2
    avgHeight = 297 * 2

    pts1 = np.float32(points)
    pts3 = np.float32([[0, 0], [avgWidth, 0], [0, avgHeight], [avgWidth, avgHeight]])

    matrix2 = cv2.getPerspectiveTransform(pts1, pts3)
    imgOutput1 = cv2.warpPerspective(image, matrix2, (avgWidth, avgHeight))

    return imgOutput1

def mainLoop():
    while True:

        success, img = cap.read()
        imgEroded = preProcessing(img)
        cntCrnr = contourDetection(imgEroded)
        resultantImg = img
        try:
            resultantImg = warpImage(cntCrnr, img)
            cv2.imshow("product", resultantImg)
        except Exception as e:
            pass

        cv2.imshow("product", resultantImg)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("doc.jpg", resultantImg)
            break

    cap.release()
    cv2.destroyAllWindows()

mainLoop()
