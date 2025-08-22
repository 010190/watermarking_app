from tkinter import *
from tkinter import filedialog, font, colorchooser
from tkinter.messagebox import askquestion
from tkinter.simpledialog import askstring, askinteger
from tkinter.ttk import Combobox
from matplotlib import colors

from PIL import Image, ImageTk, ImageDraw, ImageFont

app = Tk()
app.title("Watermark application")

fonts = list(font.families())

font_size = [num for num in range(1,50)]

var_font = StringVar()
var_size = StringVar()


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/Desktop",
                                          title="Select a File",
                                          filetypes=(("images", "*.jpg"
                                                      "*.jpeg"),
                                                     ("all files",
                                                      "*.*")))


    if filename:

        dialog = Toplevel()
        im = Image.open(filename)

        im = im.resize((200,200))

        render = ImageTk.PhotoImage(im)
        my_var = Label(dialog, image=render,width=200, height=200)
        my_var.image = render
        my_var.grid(row=1, column=1)


        def text_watermark():
            color_code = colorchooser.askcolor(title="Choose color")[0]


            text = askstring(prompt="text", title="Enter text")
            

            x = askinteger(title="Enter x", prompt="Enter x")
            y = askinteger(title="Enter y", prompt="Enter y")


            edit = ImageDraw.Draw(im)
            size = askinteger(title="Enter size", prompt="Enter size")
            font = ImageFont.truetype("arial.ttf", size)

            edit.text((x,y), text=text, fill=color_code, font=font)
            new_im = ImageTk.PhotoImage(im)
            my_var.configure(image=new_im)
            my_var.grid(row=1, column=1)
            my_var.image = new_im

            save = askquestion(title="Do you want to save this image?",message="Would you like to save this image?")
            if save == "yes":
                im.save(f"{text}.jpg")

        # def add_symbol():
        #     pass
        #
        # def save():
        #     global new_im
        #     global text


        choose_font = Combobox(dialog, values=fonts, textvariable=var_font,)


        add_text = Button(dialog, text="Add text", command=text_watermark)
        add_text.grid(row=2, column=1, sticky=E)
        add_sym = Button(dialog, text="Add symbol")
        add_sym.grid(row=2, column=1, sticky=W)


        # save_button = Button(dialog, text="Save", command=save)
        # save_button.grid(row=2, column=2, sticky=E)

        choose_font.grid(row=3, column=1, sticky=W)



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