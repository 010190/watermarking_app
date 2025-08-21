from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


app = Tk()
app.title("Watermark application")


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=((".JPG", "*.JPG"
                                                      "*.JPEG*"),
                                                     ("all files",
                                                      "*.*")))

    im = Image.open(filename)
    im = im.resize((200,200))
    render = ImageTk.PhotoImage(im)
    my_var = Label(app, image=render,width=200, height=200)
    my_var.image = render

    my_var.grid(row=5, column=1)

content = Frame(app)

welcome = Label(app, text="Welcome to Watermark application")
welcome.grid(column=0, row=0)




label_file_explorer = Label(app,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")
label_file_explorer.grid(column=1, row=1)

button_explore = Button(app,
                        text="Browse Files",
                        command=browseFiles)

button_explore.grid(column=1, row=2)
button_exit = Button(app,
                     text="Exit",
                     command=exit)

button_exit.grid(column=1, row=3)



app.minsize(400, 400)
app.mainloop()