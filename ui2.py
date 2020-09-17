from PIL import Image 
  
# creating a image1 object and convert it to mode 'P' 
im1 = Image.open(r"yoga_pose/big-toe.jpg").convert('L') 
# creating a image2 object and convert it to mode 'P' 
im2 = Image.open(r"yoga_pose/boat.jpg").convert('L') 
# alpha is 0.0, a copy of the first image is returned 

im2.thumbnail(im1.size, Image.ANTIALIAS)
print(im1.size, im2.size)
# im1.show()
# im2.show()
im3 = Image.blend(im1, im2, 0.1) 
im3.show()