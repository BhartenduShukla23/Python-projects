from tkinter import Tk,Label,StringVar, OptionMenu,Frame,Entry
from tkinter import ttk
import time
root=Tk()
root.state("zoomed")
root.config(bg='powder blue')
root.resizable(width=False,height=False)
root.title('@ Bhartendu Tech')

root.iconbitmap("logo1.1.ico")
lbl_title=Label(root,text="Banking Simulation",font=('arial',50,'bold'),bg='powder blue')
lbl_title.pack()
lbl_date=Label(root,text=time.strftime("%d-%m-%Y"),fg='blue', font=('arial',20,'bold'),bg='powder blue')
lbl_date.pack(pady=15)

# ---------------- Main Form Frame ----------------
form_frame = Frame(root, bg='powder blue')
form_frame.pack(pady=50)

# Control column spacing
form_frame.columnconfigure(0, weight=0)
form_frame.columnconfigure(1, weight=0)

# ===== Row 1 : Role =====
lbl_role = Label(form_frame, text="Select Role:",font=('arial', 12, 'bold'),bg='powder blue')
lbl_role.grid(row=0, column=0, padx=3, pady=5, sticky="e")

selected_role = StringVar()

role_combo = ttk.Combobox(form_frame,textvariable=selected_role,font=('arial', 12),width=22,state="readonly")
role_combo['values'] = ("Admin", "User")
role_combo.grid(row=0, column=1, padx=3, pady=5, sticky="w")

# ===== Row 2 : Account Number =====
acn_label = Label(form_frame, text="A.C.Number:",font=('arial', 12, 'bold'),bg='powder blue')
acn_label.grid(row=1, column=0, padx=3, pady=5, sticky="e")

entry1 = Entry(form_frame, font=('arial', 12), width=25)
entry1.grid(row=1, column=1, padx=3, pady=5, sticky="w")

name_label = Label(form_frame, text="Your Name:",font=('arial', 12, 'bold'),bg='powder blue')
name_label.grid(row=2, column=0, padx=3, pady=5, sticky="e")

entry2 = Entry(form_frame, font=('arial', 12), width=25)
entry2.grid(row=2, column=1, padx=3, pady=5, sticky="w")

pasw_label = Label(form_frame, text="Password:",font=('arial', 12, 'bold'),bg='powder blue')
pasw_label.grid(row=3, column=0, padx=3, pady=5, sticky="e")

entry3 = Entry(form_frame, font=('arial', 12), width=25,show='*')
entry3.grid(row=3, column=1, padx=3, pady=5, sticky="w")
#====== Buttons :- (Login Reset and Forget password)================
login_btn = ttk.Button(form_frame, text='Login', width=15)
login_btn.grid(row=4, column=1, padx=5, pady=15, sticky="e")

reset_btn = ttk.Button(form_frame, text='Reset', width=15)
reset_btn.grid(row=4, column=1, padx=5, pady=15, sticky="w")
# ===== Row 5 : Forget Password =====
forget_btn = ttk.Button(form_frame,
                        text="Forget Password",
                        width=38)
forget_btn.grid(row=5, column=1, columnspan=2, pady=5)

footer = Label(root,
               text="© 2026 Developed By Bhartendu Shukla | All Rights Reserved",
               font=('arial', 9),
               bg='#1f1f1f',
               fg='white')
footer.pack(side="bottom", fill="x")

root.mainloop()