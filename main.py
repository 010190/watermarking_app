from tkinter import *
from tkinter import filedialog, font, colorchooser
from tkinter.simpledialog import askstring
from tkinter.ttk import Combobox

from PIL import Image, ImageTk, ImageDraw

app = Tk()
app.title("Watermark application")

fonts = list(font.families())

font_size = [num for num in range(1,50)]




def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/Desktop",
                                          title="Select a File",
                                          filetypes=(("images", ".jpg"
                                                      ".jpeg"),
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

        def choose_color():
            # variable to store hexadecimal code of color
            color_code = colorchooser.askcolor(title="Choose color")


        def on_screen_keyboard():
            text = askstring(prompt="text", title="Enter text")
            edit = ImageDraw.Draw(im)
            edit.text((0, 0), text=text, fill=(255, 0, 0))

            new_im = ImageTk.PhotoImage(im)
            my_var.configure(image=new_im)
            my_var.grid(row=1, column=1)
            my_var.image = new_im

        def add_symbol():
            pass

        def save():
            global new_im
            global text
            new_im.save(f"{text}.jpg")



        choose_font = Combobox(dialog, values=fonts)


        add_text = Button(dialog, text="Add text", command=on_screen_keyboard)
        add_text.grid(row=2, column=1, sticky=E)
        add_sym = Button(dialog, text="Add symbol")
        add_sym.grid(row=2, column=1, sticky=W)


        save_button = Button(dialog, text="Save", command=save)
        save_button.grid(row=2, column=2, sticky=E)

        choose_font.grid(row=3, column=1, sticky=W)

        choose_size = Combobox(dialog,  values=font_size)
        choose_size.grid(row=3, column=2, sticky=W)

        color_button = Button(dialog, text="Select color",
                        command=choose_color)
        color_button.grid(row=3, column=3, sticky=W)

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