# tkinter-subfolders-select

### What happened

Tkinter does not support the selection of multiple folders out of the box. 


### Solution

This is the native code to add that missing feature without the need of any third party library.


### How to Use

Now suppose you have something standard like this:


```python
import ... # any necessary libs

setting_mapping_folders = 'my_app:selected_folders'
settings = {} # your settings object

# link this click function to your button
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
