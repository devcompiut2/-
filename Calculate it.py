import json
import os
import customtkinter as ctk
from tkinter import messagebox

# إعدادات الواجهة
ctk.set_appearance_mode("System")  # وضع الواجهة (System, Dark, Light)
ctk.set_default_color_theme("blue")  # السمات المتاحة: blue, green, dark-blue

# دالة لحفظ البيانات في ملف JSON
def save_data(user_name):
    data = {"user_name": user_name}
    with open(f"{user_name}.json", "w") as file:
        json.dump(data, file)
    messagebox.showinfo("Success", f"Data saved for {user_name}!")

# دالة للتحقق من وجود المستخدم
def check_user():
    user_name = entry.get()
    if user_name.strip() == "":
        messagebox.showwarning("Error", "Please enter your name!")
        return
    if os.path.exists(f"{user_name}.json"):
        messagebox.showinfo("Info", f"Welcome back, {user_name}!")
    else:
        save_data(user_name)

# إنشاء واجهة المستخدم
root = ctk.CTk()
root.title("User Account")
root.geometry("400x200")  # حجم النافذة

# تسمية الحقل
label = ctk.CTkLabel(root, text="Enter your name:", font=("Arial", 16))
label.pack(pady=10)

# حقل إدخال النص
entry = ctk.CTkEntry(root, width=200, font=("Arial", 14))
entry.pack(pady=10)

# زر الإرسال
button = ctk.CTkButton(root, text="Submit", command=check_user, font=("Arial", 14))
button.pack(pady=10)

# تشغيل الواجهة
root.mainloop()
