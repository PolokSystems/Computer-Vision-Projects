import os
import cv2

image_path = os.path.join ('sigma.png')
image = cv2.imread(image_path)

cv2.imwrite(os.path.join('sigma_clone.png'),image)

cv2.imshow("Clone", image)
cv2.waitKey(0)


