import cv2

img = cv2.imread("background_white.jpg")

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)

cv2.namedWindow("Drawing Circles on Mouse Click")
cv2.setMouseCallback("Drawing Circles on Mouse Click", draw_circle)

while True:
    cv2.imshow("Drawing Circles on Mouse Click", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()