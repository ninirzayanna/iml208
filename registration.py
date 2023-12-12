import tkinter as tk
from tkinter import messagebox
from tkinter import font 

def register():
    username = entry_username.get()
    email = entry_email.get()
    vehicle = entry_vehicle.get()
    password = entry_password.get()

    if not username or not email or not vehicle or not password:
        messagebox.showerror("Error", "All fields are required.")
    else:
        user_info = f"Username: {username}, Email: {email}, Vehicle: {vehicle}, Password: {password}"
        listbox_users.insert(tk.END, user_info)
        clear_entries()
        messagebox.showinfo("Sucessfull", "You are registered.")

def update_selected():
    selected_indices = listbox_users.curselection()
    if not selected_indices:
        messagebox.showerror("Error", "Please select a user to update.")
        return

    updated_username = entry_username.get()
    updated_email = entry_email.get()
    updated_vehicle = entry_vehicle.get()
    updated_password = entry_password.get()

    if not updated_username or not updated_email or not updated_vehicle or not updated_password:
        messagebox.showerror("Error", "All fields are required.")
    else:
        for selected_index in selected_indices:
            user_info = f"Username: {updated_username}, Email: {updated_email}, Vehicle: {updated_vehicle}, Password: {updated_password}"
            listbox_users.delete(selected_index)
            listbox_users.insert(int(selected_index), user_info)
        clear_entries()
    

def delete_selected():
    selected_index = listbox_users.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a user to delete.")
        return

    listbox_users.delete(selected_index)
    clear_entries()

def clear_entries():
    entry_username.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_vehicle.delete(0, tk.END)
    entry_password.delete(0, tk.END)

root = tk.Tk()
root.title("Student Vehicle Sticker Registration Form")
root.geometry("600x400")
root.configure(bg="#8B7355")  

label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, sticky="e", padx=10, pady=10)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, sticky="e", padx=10, pady=10)

entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

label_vehicle = tk.Label(root, text="Vehicle:")
label_vehicle.grid(row=2, column=0, sticky="e", padx=10, pady=10)

entry_vehicle = tk.Entry(root)
entry_vehicle.grid(row=2, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=3, column=0, sticky="e", padx=10, pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=3, column=1, padx=10, pady=10)

button_create = tk.Button(root, text="Create", command=register, bg="#EEC591")  
button_create.grid(row=4, column=0, padx=5, pady=10)

button_update = tk.Button(root, text="Update", command=update_selected, bg="#FFD39B")  
button_update.grid(row=4, column=1, padx=5, pady=10)

button_delete = tk.Button(root, text="Delete", command=delete_selected, bg="#8B2323")  
button_delete.grid(row=4, column=2, padx=5, pady=10)

listbox_users = tk.Listbox(root, width=50, height=8)
listbox_users.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()