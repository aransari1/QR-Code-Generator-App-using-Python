import tkinter
import customtkinter as ctk
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
                                        initialdir="Saved QR Codes",
                                        title="Save"
                                        )
    if Path:
        img.save(Path)
        messagebox.showinfo("Success", "QR code is saved in %s successfully."%(Path))
    else:
        messagebox.showerror("Error","Select the path first")

def Help_Dialog():
    messagebox.showinfo("How to use it?","1. Insert your data in the data field.\n2. Insert the color in the pattern field.\n Insert the color in the background field\n4. Generate Button : used to generate the preview of the QR.\n5. Clear Button: Used to clear all the input fields.\n6. Save Button : used to save the QR code in the storage in image file.\nNOTE : If you want to open the custom colour selector, just leave the text field empty.",icon='question')


#GUI Programming starts from here.

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()
app.geometry("700x400")
app.title("QR Code Generator")
app.iconbitmap("Icons\Simple.ico")

Main_Heading_Label = ctk.CTkLabel(app, text="Welcome to QR Generator", fg_color="transparent")
Main_Heading_Label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

Notice_Label = ctk.CTkLabel(app, text="Note: Click on Help Button to know how to use the APP.", fg_color="transparent")
Notice_Label.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

Data_Label = ctk.CTkLabel(app, text="Data :", fg_color="transparent")
Data_Label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

Pattern_Label = ctk.CTkLabel(app, text="Pattern colour :", fg_color="transparent")
Pattern_Label.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

Background_Label = ctk.CTkLabel(app, text="Background colour :", fg_color="transparent")
Background_Label.place(relx=0.5, rely=3, anchor=tkinter.CENTER)


Generate_Button = ctk.CTkButton(master=app, text="Generate QR", command=Generated_QR)
Generate_Button.place(relx=0.15, rely=0.9, anchor=tkinter.CENTER)

Clear_Button = ctk.CTkButton(master=app, text="Clear All", command=Clear_Field)
Clear_Button.place(relx=0.38, rely=0.9, anchor=tkinter.CENTER)

Save_Button = ctk.CTkButton(master=app, text="Save QR", command=Save_QR)
Save_Button.place(relx=0.62, rely=0.9, anchor=tkinter.CENTER)

Help_Button = ctk.CTkButton(master=app, text="Help💡", command=Help_Dialog)
Help_Button.place(relx=0.85, rely=0.9, anchor=tkinter.CENTER)

app.mainloop()