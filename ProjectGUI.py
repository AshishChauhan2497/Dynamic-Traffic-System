from threading import Thread
from tkinter import Tk, Menu, Canvas, Label, Button, Entry, Frame
from ProjectGUI_function import get_total_time, quit_it
from Project_display import frame1, frame2, frame3, run_video, show_data


def GUI():
    global window_main
    window_main = Tk()
    window_main.title('GUI Dynamic Traffic System')
    window_height = window_main.winfo_screenheight() - 100
    window_main.iconbitmap()
    window_width = window_main.winfo_screenwidth() - 100
    window_main.configure(background='yellow')
    window_main.resizable = False
    window_main.attributes("-fullscreen", True)

    def thread_video(canvas, c_height, c_width, button):
        """Thread for video tab"""
        thread_2 = Thread(target=run_video, args=(canvas, c_height, c_width, button))
        thread_2.start()

    def thread_data(canvas, button):
        """Thread for graph tab"""
        thread_3 = Thread(target=show_data, args=(canvas, button))
        thread_3.start()

    # Menu Bar
    menu_bar = Menu(window_main)
    menu_bar.add_command(label='Quit', command=lambda: quit_it(window_main))
    menu_bar.add_command(label='Reset', command=lambda: refresh())
    menu_bar.add_command(label='MainPage', command=lambda: frame1(frame_main))
    menu_bar.add_command(label='Video', command=lambda: frame2(frame_video))
    menu_bar.add_command(label='Data', command=lambda: frame3(frame_data))

    window_main.configure(width=window_width, height=window_height, background='yellow', menu=menu_bar)

    # frames
    frame_main = Frame(window_main)
    frame_video = Frame(window_main, bg="light blue")
    frame_data = Frame(window_main, bg="magenta")

    # Canvases
    canvas_background = Canvas(frame_main, bg='#333333')
    canvas_1 = Canvas(canvas_background, bg='red')
    canvas_2 = Canvas(canvas_background, bg='red')
    canvas_3 = Canvas(canvas_background, bg='red')
    canvas_4 = Canvas(canvas_background, bg='red')
    canvases = [canvas_1, canvas_2, canvas_3, canvas_4]
    canvas_video = Canvas(frame_video, bg="blue")

    canvas_data = Canvas(frame_data, bg="red")

    # Labels
    label_heading = Label(canvas_background)
    label_heading['text'] = 'Dynamic Traffic System'
    label_heading['bg'] = 'red'
    label_heading['fg'] = 'white'
    label_heading['font'] = "Algerian 32 bold"
    label_heading['borderwidth'] = 10
    label_heading['relief'] = 'ridge'
    label_time_cycle = Label(canvas_background)
    label_time_cycle['text'] = 'Enter Time per Cycle (x15): '
    label_time_cycle['bg'] = '#333333'
    label_time_cycle['fg'] = "white"
    label_time_cycle['font'] = "Arial 20"
    label_time_cycle['borderwidth'] = 2

    # Button
    button_video = Button(frame_video, text='browse', bg='green', font='Times 20 bold', border=10, relief='raised')
    button_entry = Button(canvas_background, text="OK !", bg='green', fg='white',
                          font='Times 20', border=10, relief="raised")
    button_data_browse = Button(frame_data, text='browse', bg='green', font='Times 20 bold', border=10, relief='raised')

    # Button Command
    button_data_browse['command'] = lambda: thread_data(canvas_data, button_data_browse)
    button_video['command'] = lambda: thread_video(canvas_video, window_height, window_width, button_video)
    button_entry['command'] = lambda: get_total_time(total_time.get(), button_entry, total_time, label_time_cycle,
                                                     canvas_1, canvas_2, canvas_3, canvas_4, canvas_background)

    # Input Box
    tot_time = 0
    total_time = Entry(canvas_background, font="Times 20")

    # Placement
    frame_main.place(relheight=1, relwidth=1, relx=0, rely=0)
    canvas_background.place(relheight=0.98, relwidth=0.98, relx=0.01, rely=0.01)
    label_heading.place(relheight=0.10, relwidth=0.90, relx=0.05, rely=0.02)
    canvas_1.place(relheight=0.30, relwidth=0.40, relx=0.05, rely=0.230)
    canvas_2.place(relheight=0.30, relwidth=0.40, relx=0.55, rely=0.230)
    canvas_3.place(relheight=0.30, relwidth=0.40, relx=0.05, rely=0.555)
    canvas_4.place(relheight=0.30, relwidth=0.40, relx=0.55, rely=0.555)
    label_time_cycle.place(relheight=0.08, relwidth=0.25, relx=0.05, rely=0.13)
    total_time.place(relheight=0.07, relwidth=0.06, relx=0.30, rely=0.13)
    button_entry.place(relheight=0.10, relwidth=0.24, relx=0.37, rely=0.13)

    frame_video.place(relheight=1, relwidth=1, relx=0, rely=0)
    canvas_video.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.05)
    button_video.place(relheight=0.10, relwidth=0.24, relx=0.37, rely=0.90)

    frame_data.place(relheight=1, relwidth=1, relx=0, rely=0)
    canvas_data.place(relheight=0.9, relwidth=0.8, relx=0.1, rely=0.05)
    button_data_browse.place(relheight=0.1, relwidth=0.1, relx=0.90, rely=0.5)

    # Begin
    frame1(frame_main)

    # The End
    window_main.mainloop()

    # border types:flat, raised, sunken, ridge, solid, groove


if __name__ == '__main__':
    def refresh():
        window_main.destroy()
        GUI()

    GUI()
