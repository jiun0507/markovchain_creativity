import tkinter as tk
from PIL import Image, ImageTk
from start import get_sequence_of_yoga_moves

"""
This is the slideshow constructor file of this system.
It constructs a slideshow using tk library and PIL library to use images in
the working directory. It displays the sequence of yoga poses constructed
using makrov chain.
"""

class HiddenRoot(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_geometry("0x0+0+0")
        self.window = MySlideShow(self)
        self.window.startSlideShow()


class MySlideShow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        #remove window decorations
        self.overrideredirect(True)

        #save reference to photo so that garbage collection
        #does not clear image variable in show_image()
        self.persistent_image = None
        self.imageList = []
        self.pixNum = 0

        # Set the fixed width and height of the slideshow
        self.width = 600
        self.height = 450

        #used to display as background image
        self.label = tk.Label(self)
        self.label.pack(side="top", fill="both", expand=True)

        self.getImages()

    def getImages(self):
        '''
        Get image sequences from yoga_pose folder
        '''
        # Get random yoga pose routine
        images = get_sequence_of_yoga_moves(10)

        # Construct list of paths to pictures of corresponding yoga poses
        for i in range(0, len(images)-1):
            print(images[i])
            self.imageList.append("./yoga_pose/" + images[i] + ".jpg")
        return images

    def startSlideShow(self, delay=4): #delay in seconds
        myimage = self.imageList[self.pixNum]
        self.pixNum = (self.pixNum + 1) % len(self.imageList)
        self.showImage(myimage)
        #its like a callback function after n seconds (cycle through pics)
        self.after(delay*1000, self.startSlideShow)

    def showImage(self, filename):
        image = Image.open(filename)
        # Resizes the images to width and height
        image.thumbnail((self.width, self.height), Image.ANTIALIAS)

        #set window size after scaling the original image up/down to fit screen
        #removes the border on the image
        scaled_w, scaled_h = image.size
        self.wm_geometry("{}x{}+{}+{}".format(scaled_w,scaled_h,0,0))

        # create new image
        self.persistent_image = ImageTk.PhotoImage(image)
        self.label.configure(image=self.persistent_image)

# Instantiates the slideshow class
slideShow = HiddenRoot()
slideShow.bind("<Escape>", lambda e: slideShow.destroy())  # exit on esc
slideShow.mainloop() # Start the slideshow