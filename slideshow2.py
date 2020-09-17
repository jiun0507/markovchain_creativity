from itertools import cycle
import tkinter as tk

class App(tk.Tk):
    def __init__(self, image_files, delay):
        tk.Tk.__init__(self)
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (w, h))
        self.delay = delay
        self.pictures = cycle((tk.PhotoImage(file=image), image)
                          for image in image_files)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()

    def show_slides(self):
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        self.title(img_name)
        self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()


delay = 3500
image_files = ["yoga_pose/boat.jpg"]

app = App(image_files, delay)
app.show_slides()
app.run()