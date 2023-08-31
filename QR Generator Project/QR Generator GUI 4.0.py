from tkinter import filedialog,messagebox,colorchooser
from PIL import ImageTk,ImageOps,Image
from colour import Color
from tkinter import *
import qrcode



def check_color(picked):
    """This function is used for checking if the user input is colour or not.

    check_color:
    check_color(picked): first it replaces the spaces with empty space in the given input.\nAfter that checks if the input is color or not with Color(picked) method.\n The try and except block are used for error correction.

    Returns:
        True: If the input is color.
        False: if the input is not color.
    """
    try:
        picked = picked.replace(" ", "")
        Color(picked) 
        return True
    except ValueError:
        return False
        
        
def QR_Generate(Data,Pattern_Fill,Background):
    """This function is used for generating the QR code with the own color combination.

    QR_Generate:
    QR_Generate(Data,Pattern_Fill,Background): first it holds the qrcode.QRCode in the qr variable.\nThen it sets the level of error correction in the code(basically if the code is damaged at some points, even after the information can be taken.
    qr.add_data(Data): this method add the data in the qr code for generation.

    Returns:
        qr_make: it holds the value of generated QR code.
    """
    qr = qrcode.QRCode(version = 1,
                    box_size = 20,
                        border = 2,
    error_correction = qrcode.constants.ERROR_CORRECT_H,)

    qr.add_data(Data)
    qr.make(fit = True) #if data input is present, then makes the qr
    img = qr.make_image(fill_color = Pattern_Fill,
                        back_color = Background)
    qr_make = img
    img = ImageOps.fit(img, (220, 220))
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img
    return qr_make
    
    
def Colour_Check():
    Data = Data_Input.get()
    if Data:
        Pattern_Fill = Pattern_Input.get()   
        if Pattern_Fill:
            if check_color(Pattern_Fill): #check if input is color or not
                Background = Background_Input.get()
                if Background:
                    if check_color(Background): #check if input is color or not
                        return Data,Pattern_Fill,Background
                    else:
                        messagebox.showwarning("Error","Enter the correct background colour")
                else:
                    Background = colorchooser.askcolor(title="Background Colour")[1] or "white"
                    Background_Input.insert(0,Background)
                    return Data,Pattern_Fill,Background
            else:
                messagebox.showwarning("Error","Enter the correct pattern colour")
        else:
            Pattern_Fill = colorchooser.askcolor(title="Pattern Colour")[1] or "black"
            Pattern_Input.insert(0,Pattern_Fill)
            Background = Background_Input.get()
            if Background:
                    if check_color(Background): #check if input is color or not
                        return Data,Pattern_Fill,Background
                    else:
                        messagebox.showwarning("Error","Enter the correct background colour")
            else:
                Background = colorchooser.askcolor(title="Background Colour")[1] or "white"
                Background_Input.insert(0,Background)
    else:
        messagebox.showwarning("Error","Enter the data first")
    return Data,Pattern_Fill,Background


def Generated_QR():
    Obtained = Colour_Check()
    D_obt = Obtained[0]
    P_obt = Obtained[1]
    B_obt = Obtained[2]
    QR_Generate(D_obt,P_obt,B_obt)
    
    
def Clear_Field():
    Data_Input.delete(0,'end')
    Background_Input.delete(0,'end')
    Pattern_Input.delete(0,'end')
    
def Save_QR():
    Obtained = Colour_Check()
    D_obt = Obtained[0]
    P_obt = Obtained[1]
    B_obt = Obtained[2]
    img = QR_Generate(D_obt,P_obt,B_obt)
    Path = filedialog.asksaveasfilename(defaultextension="*.png",
                                        filetypes=[("PNG files", '*.png'),("JPG files",'*.jpg'),("All files",'*')],
                                        initialdir="QR Generator Project\Saved QR Codes",
                                        title="Save"
                                        )
    if Path:
        img.save(Path)
        messagebox.showinfo("Success", "QR code is saved in %s successfully."%(Path))
    else:
        messagebox.showerror("Error","Select the path first")

def Help_Dialog():
    messagebox.showinfo("How to use it?","1. Insert your data in the data field.\n2. Insert the color in the pattern field.\n Insert the color in the background field\n4. Generate Button : used to generate the preview of the QR.\n5. Clear Button: Used to clear all the input fields.\n6. Save Button : used to save the QR code in the storage in image file.\nNOTE : If you want to open the custom colour selector, just leave the text field empty.",icon='question')

main_window = Tk()
main_window.geometry("400x500")
main_window.title("QR Code Generator")
main_window.configure(bg="#F4F1DE")
main_window.iconbitmap("QR Generator Project\Icons\Simple.ico")
main_window.resizable(width=False,height=False)

Main_Heading = Label(main_window,
                     text=" QR Code Generator ",
                     bd=5,relief="groove",
                     font="CastleTUlt 25",
                     fg="#3D405B",bg="#F4F1DE")
Main_Heading.place(x=35,y=10)

Notice = Label(main_window,
              text="Note: Click on Help Button to know how to use the APP.",
              justify=LEFT,
              bg="#F4F1DE",
              fg="#632413")
Notice.place(x=40,y=65)

Data_text = Label(main_window,
                  text="Data :",
                  bg="#F4F1DE",
                  fg="black")
Data_text.place(x=118,y=110)

Data_Input = Entry(main_window,
                   width=30,
                   bg="#F4F1DE",
                    fg="#632413")
Data_Input.insert(0,"Insert Data")
Data_Input.place(x=160,y=110)


Pattern_text = Label(main_window,
                     text="Pattern colour :",
                     bg="#F4F1DE",
                     fg="black")
Pattern_text.place(x=66,y=135)

Pattern_Input = Entry(main_window,text="Enter the color or choose one",
                        width=30,
                        bg="#F4F1DE",
                        fg="#632413")
Pattern_Input.insert(0,"Insert colour or HEX code")
Pattern_Input.place(x=160,y=135)


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
                         text="Generate QR",
                         width=15,
                         bg="#93BDA9",
                         fg="#000000",
                         command=Generated_QR)
Generate_Button.place(x=20,y=190)

Clear_Button = Button(main_window,
                        text="Clear All",
                        width=10,
                        bg="#93BDA9",
                        fg="#000000",
                        command=Clear_Field)
Clear_Button.place(x=155,y=190)


Save_Button = Button(main_window,
                     text="Save QR",
                     width=10,
                     bg="#93BDA9",
                     fg="#000000",
                     command=Save_QR)
Save_Button.place(x=250,y=190)

Wheel_img = PhotoImage(file="QR Generator Project\Icons\Wheel25.png")

Wheel_Label = Label(image=Wheel_img)


Colour_Button = Button(main_window,
                     text="Help",
                     bg="#93BDA9",
                     fg="#000000",
                     command=Help_Dialog)
Colour_Button.place(x=350,y=190)


label = Label(main_window)
label.place(x=90,y=250)


main_window.mainloop()