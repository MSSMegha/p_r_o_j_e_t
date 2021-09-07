import cv2
img = cv2.imread('katrina blog.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Title',img)
print(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
