import customtkinter
from tkinter import *
from translate import Translator
root=customtkinter.CTk()
root.geometry("800x500")
root.resizable(0,0)
root.title("Text Translator")
root.config(bg="#202630")

Font1=('Arial',18,'bold')
lang=['English','French','German']
variable1=StringVar()
variable2=StringVar()
variable3=StringVar()
variable4=StringVar()

label1=customtkinter.CTkLabel(root,font=Font1,text="From Language:", text_color="#FFFFFF",width=20, bg_color="#06021a")
label1.place(x=20,y=30)

label2=customtkinter.CTkLabel(root,font=Font1,text="To Language:", text_color="#FFFFFF",width=20, bg_color="#06021a")
label2.place(x=500,y=30)

combobox1=customtkinter.CTkComboBox(root,values=lang,variable=variable1,font=Font1,dropdown_hover_color="#00ff00",fg_color="#FFFFFF",text_color="#ed0707",width=150,height=40)
combobox1.place(x=20,y=70)

combobox2=customtkinter.CTkComboBox(root,values=lang,variable=variable2,font=Font1,dropdown_hover_color="#00ff00",fg_color="#FFFFFF",text_color="#ed0707",width=150,height=40)
combobox2.place(x=500,y=70)

Entry1=customtkinter.CTkEntry(root,textvariable=variable3,text_font=Font1,fg_color="#FFFFFF",border_color="#06021a",text_color="#000000",width=300,height=60)
Entry1.place(x=20,y=140)

Entry2=customtkinter.CTkEntry(root,textvariable=variable4,font=Font1,fg_color="#FFFFFF",border_color="#06021a",text_color="#000000",width=300,height=60)
Entry2.place(x=500,y=140)


root.mainloop()