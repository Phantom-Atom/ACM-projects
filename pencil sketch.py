# Importing the libraries
import cv2
import matplotlib.pyplot as plt

# Reading the image
img=cv2.imread("Images\Input\filename")

# Since the above image uses BGR instead of RGB, we'll have to convert it into RGB
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
plt.axis(False)

# Convert to Grey Image
grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert Image
invert_img=cv2.bitwise_not(grey_img)

# Blur image
blur_img=cv2.GaussianBlur(invert_img, (111,111),0)

# Invert Blurred Image
invblur_img=cv2.bitwise_not(blur_img)

# Sketch Image
sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

# Save Sketch 
cv2.imwrite('sketch.jpg', sketch_img)

# Display sketch
cv2.imshow('sketch image',sketch_img)
cv2.waitKey(0)
cv2.destroyAllWindows()