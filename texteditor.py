import tkinter as tk
from tkinter import messagebox, filedialog
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")
#create textarea
text=tk.Text(
    root,
    wrap=tk.WORD,
    font=("Arial", 18)
)

text.pack(expand=True, fill="both")
#main logic
#function 1 : To create a new file

def new_file():
    if text.get("1.0", tk.END).strip():
        if messagebox.askyesno("Save Changes", "Do you want to save changes?"):
            save_file()
    text.delete("1.0", tk.END)
    root.title("Untitled - Simple Text Editor")

# function 2 : To open an existing file
def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path,"r") as file:
            text.delete("1.0",tk.END)
            text.insert(tk.END,file.read())

#function 3 : To save the current file
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path,"w")as file:
            file.write(text.get("1.0", "tk.END"))
        messagebox.showinfo("Save File", "File saved successfully!")

#function 4 : To exit the application
def exit_app():
    if text.get("1.0", "tk.END").strip():
        if messagebox.askyesno("Save Changes", "Do you want to save changes?"):
            save_file()
    root.destroy()

#create menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
#file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

root.mainloop()