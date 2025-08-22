from tkinter import *
from tkinter import filedialog, font, colorchooser
from tkinter.messagebox import askquestion
from tkinter.simpledialog import askstring, askinteger
from tkinter.ttk import Combobox, Style
from matplotlib import colors

from PIL import Image, ImageTk, ImageDraw, ImageFont

# style = Style()
#
# style.configure('TButton', font =
#                ('calibri', 10, 'bold', 'underline'),
#                 foreground = "#6C85D5")

app = Tk()
app.title("Watermark application")
app.geometry("400x400")
fonts = list(font.families())

font_size = [num for num in range(1,50)]

var_font = StringVar()
var_size = StringVar()

background = Image.open("C:/Users/olcza/Desktop/watermark_app/Gv56y4SWQAAHLUL.jpg")
background = background.resize((400, 400))
background_image = ImageTk.PhotoImage(background)

canvas1 = Canvas( app, width = 400,
                 height = 400,
                  borderwidth=0)

canvas1.place(x=-1, y=0)
# Display image
canvas1.create_image( 0, 0, image = background_image, anchor = "nw")

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/Desktop",
                                          title="Select a File",
                                          filetypes=[('Images','*.jpg *.jpeg *.png')])
    if filename:

        dialog = Toplevel(bg="#6C85D5")
        dialog.geometry("300x300")

        im =  Image.open(open(filename, 'rb'))

        im = im.resize((200,200))
        im = im.convert('RGBA')
        render = ImageTk.PhotoImage(im)
        my_var = Label(dialog, image=render,width=200, height=200)
        my_var.image = render
        my_var.place(x=0, y=0)


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
            my_var.place(x=0, y=0)
            my_var.image = new_im

            save = askquestion(title="Do you want to save this image?",message="Would you like to save this image?")
            if save == "yes":
                im.save(f"{text}.jpg")


        def photo_watermark():
            print(filename)
            watermark_filename = filedialog.askopenfilename(initialdir="/Desktop",
                                                  title="Select a File",
                                                  filetypes=[('Images', '*.jpg *.jpeg *.png')])
            watermark_image = Image.open(open(watermark_filename, 'rb'))
            im2 = watermark_image.resize((40,40))
            layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
            layer.paste(im2, (20, 20))
            layer2 = layer.copy()
            layer2.putalpha(1)
            layer.paste(layer2, (0, 0), layer2)
            result = Image.alpha_composite(im, layer)
            result.show()
            result.save("watermark1.png")

        add_text = Button(dialog, text="Add text", command=text_watermark,  style = 'TButton')
        add_text.place(x=220, y=50)
        add_sym = Button(dialog, text="Add photo", command=photo_watermark)
        add_sym.place(x=220, y=80)
        button_exit = Button(dialog,
                             text="Exit",
                             command=exit)
        button_exit.place(x=220, y=120)

content = Frame(app)
welcome_label = Label(app, text="Watermark application", font=("Arial", 30), fg="white",  justify="center", bg="#6C85D5")

label_canvas = canvas1.create_window(200, 70, window=welcome_label)
button_explore = Button(app,
                        text="Browse Files",
                        command=browseFiles)

button1_canvas = canvas1.create_window( 200, 300,
                                       anchor = "center",
                                       window = button_explore)
button_exit = Button(app,
                     text="Exit",
                     command=exit)
button2_canvas = canvas1.create_window( 200, 320,
                                       anchor = "n",
                                       window = button_exit)





app.minsize(400, 400)
app.mainloop()