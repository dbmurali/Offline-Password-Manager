import json
from tkinter import *
import  random_password
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
rp=random_password.ran()
def password():
    entry_password.delete(0,END)
    entry_password.insert(0, rp)

def copy_to_clip():
    pyperclip.copy(entry_password.get())

def clear_entry():
    entry_web.delete(0,END)
    entry_email.delete(0,END)
    entry_password.delete(0,END)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    data_list = []
    web=entry_web.get()
    p_word=entry_password.get()
    email=entry_email.get()
    my_dict={"web":web,"email":email,"password":p_word}

    # CHECK FIELDS ARE FILLED------------------------------- #
    if len(p_word)>0 and len(email)>0 and len(web)>0:
       try:
          with open("data_file.json",mode="r")as file:
            """is_ok=messagebox.askokcancel(title="Inputs Given",message=f"website: {entry_web.get()}\nEmail: {entry_email.get()}\nPassword:{entry_password}")
            if is_ok:"""
            data=json.load(file)
            data_list.append(data)

       except FileNotFoundError:
            with open("data_file.json",mode="w")as file:
                data_list.append(my_dict)
                json.dump(data_list,file,indent=4)
                clear_entry()
       else:
           with open("data_file.json",mode="w")as file:
               data_list.append(my_dict)
               json.dump(data_list, file, indent=4)
               clear_entry()
    else:
        print("invalid input")

# ---------------------------- UI SETUP ------------------------------- #
FONT=("Segoe UI",15,"bold")
BG_COLOR="#FFFDD0"
window=Tk()
window.title("Password manager")
window.config(padx=20,pady=20,background=BG_COLOR)

#CANVAS
canvas=Canvas(window,width=251,height=190,bg=BG_COLOR,highlightbackground=BG_COLOR)
img=PhotoImage(file="lock.png")
canvas.create_image(125,95,image=img)
canvas.grid(row=0,column=1)

#LABLES
web_txt=Label(text="website/user_ID:",bg=BG_COLOR,font=FONT)
web_txt.grid(row=1,column=0)

email_txt=Label(text="Email:",bg=BG_COLOR,font=FONT)
email_txt.grid(row=2,column=0)

password_txt=Label(text="Password:",bg=BG_COLOR,font=FONT)
password_txt.grid(row=3,column=0)

#ENTRY
entry_web=Entry(width=35)
entry_web.grid(row=1,column=1,columnspan=2)

entry_email=Entry(width=35)
entry_email.grid(row=2,column=1,columnspan=2)

entry_password=Entry(width=17)
entry_password.grid(row=3,column=1)

#BUTTONS
pass_btn=Button(text="Generate password",command=password)
pass_btn.grid(row=3,column=2)

add_btn=Button(text="Add",width=36,command=save_pass)
add_btn.grid(row=4,column=1,columnspan=2)

copy_pass=Button(text="copy",width=10,command=copy_to_clip)
copy_pass.grid(row=3,column=3)
window.mainloop()