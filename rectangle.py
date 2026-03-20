import cv2

drawing = False
ix, iy = -1, -1

img = cv2.imread("background_white.jpg")

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp_img = img.copy()
            cv2.rectangle(temp_img, (ix, iy), (x, y), (0, 255, 255), -1)
            cv2.imshow("Interactive Rectangle Drawing with Mouse", temp_img)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 255), -1)

cv2.namedWindow("Interactive Rectangle Drawing with Mouse")
cv2.setMouseCallback("Interactive Rectangle Drawing with Mouse", draw_rectangle)

while True:
    cv2.imshow("Interactive Rectangle Drawing with Mouse", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()