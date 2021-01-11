from tkinter import filedialog


def dialogue_box():
    """Creates Dialog box"""
    footpath = filedialog.askopenfilename(initialdir="/", title="Select Video file",
                                          filetypes=(("mp4 files", "*.mp4"),))
    longfilename = footpath
    filename = filename_extractor(footpath)
    return filename, longfilename


def filename_extractor(string):
    """Take out file name from complete path"""
    temp_string = ""
    new_string = string[::-1]
    for i in new_string:
        if i == '/':
            break
        temp_string = temp_string + i
    return_string = temp_string[::-1]
    if return_string == "":
        return "No File Selected"
    else:
        return return_string
