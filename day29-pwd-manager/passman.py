import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from passgen import generate_password


app_dir = "day29-pwd-manager"
is_duplicate = True

# === Generate Password === #
def load_pass_to_Entry():
    pass_entry.delete(0, tk.END)
    new_password = generate_password()
    pass_entry.insert(0, new_password)

def check_duplicate_password_username(pwd_file, new_website, new_email_user, new_password,  detail_info):
    global is_duplicate
    found = False
    pass_data_list = []
    pass_data = ""
    # Read to check if there is a duplicate website, 

    # Read to check if there is a duplicate, 
    with open(f"{app_dir}/{pwd_file}", "r") as pass_data:
        pass_data_list = pass_data.readlines()


        if not pass_data_list:
            print("The list is empty")

        for pass_detail in pass_data_list:
            website , email_user, password  =  pass_detail.split("|")
            password = password.strip() # remove newline 

            # check already existing website and username
            if website == new_website and email_user == new_email_user and password== new_password:
                messagebox.showwarning("Multiple Info", f"Detail info Already Exist, Try different Detail")
                is_duplicate = True # don't allow duplicate
                return
            
            elif website == new_website and email_user == new_email_user:
                answer = messagebox.askquestion("Duplicate", "Duplicate Found, Do you want to Continue?")
                if answer == "yes":
                    found = True
                    break
                else:
                    print("Exiting Save data")
                    return

            # Read to check if there is a duplicate website only   
            elif website == new_website and email_user != new_email_user:
                 if website == new_website:
                    found = True
                    break
                 
    if found:
        pass_data_list.insert(pass_data_list.index(pass_detail)+1, detail_info)
        return pass_data_list
    else:
        is_duplicate = False
        return
    

  

def save_data():
    # open file
    new_website =  website_entry.get()
    new_email_user = email_entry.get()
    new_password = pass_entry.get()

    detail_info = f"{new_website}|{new_email_user}|{new_password}\n"
    

    new_list = check_duplicate_password_username("pwd.txt", new_website, new_email_user, new_password, detail_info)

    if new_list:
        with open(f"{app_dir}/pwd.txt", "w") as passwords_data:
            passwords_data.write(f"{''.join(new_list)}\n")

    elif is_duplicate != True:
        with open(f"{app_dir}/pwd.txt", "a+") as passwords_data:
            messagebox.showinfo("Add Password", f"The follow Details will be added\nWebsite: {new_website}\nEmail\\Username: {new_email_user}\nPassword: {new_password}")
            passwords_data.write(detail_info)


        

# === UI Setup === #

win  = tk.Tk()
win.title("Passman - Keeping your password safe")
win.config(padx=50, pady=20)
win.resizable(0, 0)



logo_img = ImageTk.PhotoImage(Image.open(f"{app_dir}/paswa.png"))

logo_cvs = tk.Canvas(win, height=100, width=100)
logo_cvs.create_image(50, 50, image=logo_img)
logo_cvs.grid(row=0, column=1, sticky=tk.N)

# Website field
website_label = ttk.Label(win, text="Website: " )
website_entry = ttk.Entry(win, width=30)
search_btn = ttk.Button(win, text="Search" )

website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, sticky=tk.W)
search_btn.grid(row=1, column=2, sticky=tk.NSEW)

# Email/Username field
email_label = ttk.Label(win, text="Email: " )
email_entry = ttk.Entry(win, width=45)

email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2, sticky=tk.NSEW)


# Password field
pass_label = ttk.Label(win, text="Password")
pass_entry = ttk.Entry(win, width=30)
gen_pass_btn = ttk.Button(win, text="Gen. Password", command=load_pass_to_Entry)

pass_label.grid(row=3, column=0)
pass_entry.grid(row=3, column=1)
gen_pass_btn.grid(row=3, column=2)

# Saved Field
save_btn = ttk.Button(win, text="Add Password", padding=(5, 5), command=save_data)
save_btn.grid(row=4, column=1, pady=20)

win.mainloop()