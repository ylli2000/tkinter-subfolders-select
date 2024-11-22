# tkinter-subfolders-select

### What happened

Tkinter does not support the selection of multiple folders out of the box. 


### Solution

This is the native code to add that missing feature without the need of any third party library.


### How to Use

Now suppose you have something standard like this:


```python
import ... # any necessary libs

# This is your settings object, to memorize the subfolder you selected last time
# I have provided you a settings object here, in a practical project you can write your settings into a 
# settings.txt as persistent memory.
selected_folders_key = 'my_app:selected_folders'
settings = {} 
settings[selected_folders_key] = ''

# link this click function to your button
# selected_folders_label: where you store the list of subfolders, separated by commas
# hint: the title of the dialog box
def browse_folder_click(selected_folders_label, hint):
    folder_path = filedialog.askdirectory(title=hint)
    if folder_path:
        selected_folders = open_directory_selection_dialog(root, settings, selected_folders_key, folder_path)
        if selected_folders and len(selected_folders) > 0:
            selected_folders_label.config(text=", ".join(selected_folders))
            settings[selected_folders_key] = ",".join(selected_folders)
    root.update()
```

Where `open_directory_selection_dialog` is your entrance function. Check out the code from this repository.
