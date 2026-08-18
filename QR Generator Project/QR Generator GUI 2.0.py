from tkinter import filedialog,messagebox,colorchooser
from tkinter import *
from PIL import ImageTk,ImageOps,Image
import qrcode
from matplotlib.colors import is_color_like


def Colour_Picker():
    Colour_Picked = colorchooser.askcolor()[1]
    return Colour_Picked


def QR_Generate():
    Data = Data_Input.get()
    if Data:
        Colour_Picked1 = Colour_Picker()
        Colour_Picked2 = Colour_Picker()
        Pattern_Fill = Pattern_Input.get() or Colour_Picked1 or"black" 
        Background = Background_Input.get() or Colour_Picked2 or"white"
        qr = qrcode.QRCode(version = 1,
                        box_size = 20,
                            border = 2,
        error_correction = qrcode.constants.ERROR_CORRECT_H,)

        qr.add_data(Data)
        qr.make(fit = True) #if data input is present, then makes the qr
        img = qr.make_image(fill_color = Pattern_Fill,
                            back_color = Background)
        qr_mk = img
        img = ImageOps.fit(img, (220, 220),Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img
        return qr_mk
    else:
        messagebox.showwarning("Error","Enter the data first")
    
def Clear_Field():
    Data_Input.delete(0,'end')
    Background_Input.delete(0,'end')
    Pattern_Input.delete(0,'end')
    
def Save_QR():
    img = QR_Generate()
    Path = filedialog.asksaveasfilename(defaultextension="*.png",
                                        filetypes=[("PNG files", '*.png'),("JPG files",'*.jpg'),("All files",'*')],
                                        initialdir="C:\QR Generator Project\Saved QR Codes",
                                        title="Save"
                                        )
    if Path:
        img.save(Path)
        messagebox.showinfo("Success", "QR code is saved in %s successfully."%(Path))
    else:
        messagebox.showwarning("Error","Select the path first")
        
main_window = Tk()
main_window.geometry("400x500")
main_window.title("QR Code Generator")
main_window.configure(bg="#F4F1DE")
main_window.iconbitmap("QR Generator Project\Icons\Simple.ico")
main_window.resizable(width=False,height=False)

# borderwidth or bd="size of border, relief="flat/raised/sunken/ridge/solid/groove"
Main_Heading = Label(main_window,
                     text=" QR Code Generator ",
                     bd=5,relief="groove",
                     font="CastleTUlt 25",
                     fg="#3D405B",bg="#F4F1DE")
Main_Heading.place(x=35,y=10)

Notice = Label(main_window,
              text="📌  Please enter all the required Data in the input box,then click on\nGenerate button to generate the QR Code.",
              justify=CENTER,
              bg="#F4F1DE",
              fg="#632413")
Notice.place(x=20,y=70)

Data_text = Label(main_window,
                  text="Data :",
                  bg="#F4F1DE",
                  fg="black")
Data_text.place(x=118,y=120)

Data_Input = Entry(main_window,
                   width=30,
                   bg="#F4F1DE",
                    fg="#632413")
Data_Input.insert(0,"Insert Data")
Data_Input.place(x=160,y=120)


Pattern_text = Label(main_window,
                     text="Pattern colour :",
                     bg="#F4F1DE",
                     fg="black")
Pattern_text.place(x=66,y=140)


Pattern_Input = Entry(main_window,text="Enter the color or choose one",
                        width=30,
                        bg="#F4F1DE",
                        fg="#632413")
Pattern_Input.insert(0,"Insert colour or HEX code")
Pattern_Input.place(x=160,y=140)
Background_text = Label(main_window,
                        text="Background colour :",
                        bg="#F4F1DE",
                        fg="black")
Background_text.place(x=40,y=160)

Background_Input = Entry(main_window,
                        width=30,
                        bg="#F4F1DE",
                        fg="#632413")
Background_Input.insert(0,"Insert colour or HEX code")
Background_Input.place(x=160,y=160)


Generate_Button = Button(main_window,
                         text="Generate",
                         width=15,
                         bg="#93BDA9",
                         fg="#000000",
                         command=QR_Generate)
Generate_Button.place(x=30,y=190)

Clear_Button = Button(main_window,
                        text="Clear",
                        width=10,
                        bg="#93BDA9",
                        fg="#000000",
                        command=Clear_Field)
Clear_Button.place(x=170,y=190)


Save_Button = Button(main_window,
                     text="Save",
                     width=10,
                     bg="#93BDA9",
                     fg="#000000",
                     command=Save_QR)
Save_Button.place(x=280,y=190)

Wheel_img = PhotoImage(file="QR Generator Project\Icons\Wheel25.png")

Wheel_Label = Label(image=Wheel_img)

Colour_Button = Button(main_window,
                     image=Wheel_img,
                     bg="#93BDA9",
                     fg="#000000",
                     command=Colour_Picker)
Colour_Button.place(x=20,y=120)


label = Label(main_window)
label.place(x=90,y=250)


main_window.mainloop()