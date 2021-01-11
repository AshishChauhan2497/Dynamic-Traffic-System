import _tkinter
from tkinter import Label, Button
from File_handler import dialogue_box
from Project_algo import time_allocation, countdown, video_len
from Project_display import veh_count


def get_total_time(tot_time, button, entry, label, canvas_1, canvas_2, canvas_3, canvas_4, canvas_background):
    """Takes time per cycle as input from Entry widget"""
    # Removing widgets
    button.place(relheight=0, relwidth=0, relx=0, rely=0)
    entry.place(relheight=0, relwidth=0, relx=0, rely=0)
    label.place(relheight=0, relwidth=0, relx=0, rely=0)

    # Checking value of input
    if tot_time.isdigit():
        if int(tot_time) == 0:
            tot_time = 60
        else:
            tot_time = abs(int(tot_time) * 15)
    else:
        tot_time = 60

    # Calling browse button
    button_browse = Button(canvas_background,  text='Browse',  bg='dark green',
                           fg='white', font='Times 20 bold', border=10, relief='raised')

    button_browse['command'] = lambda: browsing(button_browse, canvas_1, canvas_2, canvas_3, canvas_4,
                                                tot_time, canvas_background)
    button_browse.place(relheight=0.10, relwidth=0.24, relx=0.37, rely=0.13)


def quit_it(window):
    """Closes window"""
    try:
        window.destroy()
    except _tkinter.TclError:
        pass


def browsing(button_browse, canvas_1, canvas_2, canvas_3, canvas_4, total_time, canvas_background):
    """Call dialog box and create Begin button"""
    filename = ['', '', '', '']
    filepath = ['', '', '', '']
    canvas = [canvas_1, canvas_2, canvas_3, canvas_4]

    for i in range(4):
        filename[i], filepath[i] = dialogue_box()
        label_filename = Label(canvas[i], text=str(filename[i]), font='algerian 15 bold')
        label_filename.place(relheight=0.10, relwidth=0.90, relx=0.05, rely=0.10)

    """Creating Begin Button"""
    button_begin = Button(canvas_background, text='Begin', bg='black', fg='white',
                          font='Broadway 15', border=10, relief='raised')
    button_begin['command'] = lambda: begin(button_begin, button_browse, filepath,
                                            canvas, canvas_background, total_time)

    """Checks for presence of File"""
    checker = True
    for i in range(4):
        if filename[i] == "No File Selected":
            checker = False
    if checker:
        button_begin.place(relheight=0.10, relwidth=0.30, relx=0.35, rely=0.88)
        button_begin.update()
    else:
        button_begin.place(relheight=0.0, relwidth=0.0, relx=0., rely=0.)


def begin(button_begin, btn_browse, filepath, canvas, canvas_bg, get_tot_time):
    """Main..."""
    try:
        v_count = ['', '', '', '']
        label_veh_count = ['', '', '', '']
        label_time_alloc = ['', '', '', '']
        vid_duration = ['', '', '', '']
        frame_time = 1
        button_begin.place(relheight=0.0, relwidth=0.0, relx=0.0, rely=0.0)
        btn_browse.place(relheight=0.0, relwidth=0.0, relx=0.0, rely=0.0)
        button_begin.update()
        btn_browse.update()

        for i in range(4):
            vid_duration[i] = video_len(filepath[i])

        while True:
            label_total_time = Label(canvas_bg, text='Total Time: ' + str(get_tot_time), font='Algerian 20 bold')
            label_total_time.place(relheight=0.10, relwidth=0.50, relx=0.25, rely=0.12)

            for i in range(4):
                """Get Vehicle count"""
                v_count[i] = veh_count(filepath[i], frame_time)
                label_veh_count[i] = Label(canvas[i], text='Vehicle Count : ' + str(v_count[i]), font='Times 20 bold')
                label_veh_count[i].place(relheight=0.25, relwidth=0.80, relx=0.10, rely=0.25)
            """Allocates time"""
            time_allocated = time_allocation(v_count, get_tot_time)

            for i in range(4):
                label_time_alloc[i] = Label(canvas[i], text='Time Allocated = ' + str(round(time_allocated[i], 1)),
                                            width=30,
                                            font='Times 20 bold')
                label_time_alloc[i].place(relheight=0.25, relwidth=0.80, relx=0.10, rely=0.60)
            """Runs the GUI"""
            countdown(filepath, vid_duration, frame_time, int(get_tot_time), time_allocated, label_time_alloc,
                      label_total_time, canvas)

            frame_time += 5     #get_tot_time
    except _tkinter.TclError as e:
        # print("Premature Closing Result: " + str(e))
        pass
