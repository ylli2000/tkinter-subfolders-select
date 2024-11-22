import os
import tkinter as tk
from tkinter import Toplevel, Checkbutton, IntVar, Frame
from tkinter.font import Font

subfolder_dialog_width = 400
subfolder_dialog_base_height = 110
subfolder_dialog_label_height = 26

# opens a dialog to select multiple sub-folders, by default all sub folders are selected
def open_directory_selection_dialog(root, settings, setting_key, folder_path):
    def on_ok():
        selected = [folder for folder, var in folder_vars.items() if var.get() == 1]
        dialog.result = selected if selected else None
        dialog.destroy()

    def select_deselect_all():
        select_all = select_all_var.get()
        for var in folder_vars.values():
            var.set(select_all)

    def update_select_all():
        all_selected = all(var.get() == 1 for var in folder_vars.values())
        select_all_var.set(1 if all_selected else 0)

    dialog = Toplevel(root)
    dialog.title("Directory Selection")
    
    # Calculate the height based on the number of subfolders
    subfolders = [os.path.normpath(folder) for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]
    num_subfolders = len(subfolders)

    # if there is no subfolder, simply return the [folder_path]
    if num_subfolders == 0:
        dialog.result = [folder_path]
        dialog.destroy()
        return dialog.result
    
    dialog_height = subfolder_dialog_base_height + num_subfolders * subfolder_dialog_label_height  # Base height + height per subfolder
    dialog.geometry(f"400x{dialog_height}")

    bold_font = Font(weight="bold")
    select_all_var = IntVar(value=1)  # Default to select all
    select_all_chk = Checkbutton(dialog, text="📁 Select All Subfolders", variable=select_all_var, command=select_deselect_all, font=bold_font)
    select_all_chk.pack(anchor='w', padx=10, pady=10)

    # Create a panel (Frame) to hold the checkboxes
    panel = Frame(dialog, bg="white", relief="sunken", bd=2)
    panel.pack(fill=tk.BOTH, expand=True, padx=10)

    folder_vars = {}
    selected_subfolders = settings.get(setting_key, '').split(', ')

    all_selected = True
    for subfolder in subfolders:
        subfolder_full_path = os.path.normpath(os.path.join(folder_path, subfolder))
        if os.path.isdir(subfolder_full_path):
            is_selected = subfolder_full_path in selected_subfolders
            var = IntVar(value=1 if is_selected else 0)  # Check if the folder is in the settings
            chk = Checkbutton(panel, bg="white", text=subfolder, variable=var, command=update_select_all)  # Indent subfolder names
            chk.pack(anchor='w', padx=20)  # Add indentation before the checkboxes
            folder_vars[subfolder_full_path] = var
            if not is_selected:
                all_selected = False

    # Update the select_all_var based on the all_selected condition
    select_all_var.set(1 if all_selected else 0)

    ok_button = tk.Button(dialog, text="OK", width=20, command=on_ok)
    ok_button.pack(pady=15)

    dialog.bind('<Return>', on_ok)  # Bind Enter key to on_ok
    dialog.bind('<space>', on_ok)   # Bind Space key to on_ok

    dialog.result = None
    dialog.transient(root)
    dialog.grab_set()
    root.wait_window(dialog)

    return dialog.result

