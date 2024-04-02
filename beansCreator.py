import os
import tkinter as tk
from tkinter import messagebox

def create_folders_and_files():
    base_path = 'BeansFolders'
    os.makedirs(base_path, exist_ok=True)
    
    for folder_num in range(1, 1001):
        folder_path = os.path.join(base_path, f'Beans_{folder_num}')
        os.makedirs(folder_path, exist_ok=True)
        os.system('cls')
        print(f"[{folder_num}/1000]")
        
        for file_num in range(1, 1001):
            file_path = os.path.join(folder_path, f'Beans_{file_num}.txt')
            with open(file_path, 'w') as file:
                file.write('Beans\n' * 10000)
                #print(f"Created file: \n Number: {file_num} \n Path: '{file_path}'")
    
    messagebox.showinfo("Success", "Folders and files have been created successfully!")

# Set up the UI
root = tk.Tk()
root.title('Beans Creator')

create_button = tk.Button(root, text='Create Folders and Files', command=create_folders_and_files)
create_button.pack(pady=20)

root.mainloop()
