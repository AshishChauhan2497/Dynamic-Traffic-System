import time
import cv2
from PIL import ImageTk, Image
from File_handler import dialogue_box
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def frame1(frame):
    frame.tkraise()


def frame2(frame):
    frame.tkraise()


def frame3(frame):
    frame.tkraise()


def display_image(file_name, video_length, frame_time, waiting_time, itr):
    """Display image called by Countdown"""
    if waiting_time > 0:
        window_name = "img" + str(itr + 1)
        vid_cap = cv2.VideoCapture(file_name)
        frame_time = frame_time % video_length
        vid_cap.set(cv2.CAP_PROP_POS_MSEC, frame_time * 1000)   # Current Position(millisec)
        success, image = vid_cap.read()
        if success:
            image = cv2.resize(image, (750, 490))
            cv2.imshow(window_name, image)
            cv2.moveWindow(window_name, 770 * ((itr + 1) % 2), 215)
        cv2.waitKey(int(waiting_time) * 1000)
        cv2.destroyWindow(window_name)


def run_video(canvas, c_height, c_width, button):
    """Display Video with Boxes"""
    _, file_path = dialogue_box()
    if file_path != "":
        button.place(relwidth=0, relheight=0, relx=0, rely=0)
        vehicle_cascade = cv2.CascadeClassifier('classifier/cascade.xml')
        cap = cv2.VideoCapture(file_path)
        while cap.isOpened():
            _, img = cap.read()
            vehicles = vehicle_cascade.detectMultiScale(img, 1.1, 5)
            for (x, y, w, h) in vehicles:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (int(c_width), int(c_height)))
            photo = ImageTk.PhotoImage(image=Image.fromarray(img))
            canvas.create_image(c_width / 2, c_height / 2, image=photo)
            canvas.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.05)
            canvas.update()
        canvas.destroy()
    button.place(relheight=0.10, relwidth=0.24, relx=0.37, rely=0.90)


def graph(df1, canvas, timing):
    """Display graph"""
    figure1 = plt.Figure(figsize=(5, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, canvas)
    bar1.get_tk_widget().place(relwidth=1, relheight=1, relx=0, rely=0)
    df1 = df1[['File Name', 'Vehicle Count']].groupby('File Name').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('File name vs Vehicle Count @ time = '+str(timing))
    canvas.update()


def show_data(canvas, button):
    """Create DataFrames"""
    filename = ["", "", "", ""]
    veh_cnt = ["", "", "", ""]
    itr = 0
    if filename != "":
        button.place(relwidth=0, relheight=0, relx=0, rely=0)
        for i in range(4):
            filename[i], _ = dialogue_box()
        while itr < 30:
            for i in range(4):
                veh_cnt[i] = veh_count(filename[i], itr)
            data = {'File Name': filename,
                    'Vehicle Count': veh_cnt
                    }
            data_frame = DataFrame(data, columns=['File Name', 'Vehicle Count'])
            graph(data_frame, canvas, itr)
            canvas.update()
            itr += 2
            time.sleep(2)
    button.place(relheight=0.1, relwidth=0.1, relx=0.90, rely=0.5)


def veh_count(filename, timed):
    vehicle_cascade = cv2.CascadeClassifier('classifier/cascade.xml')
    vid_cap = cv2.VideoCapture(filename)
    vid_cap.set(cv2.CAP_PROP_POS_MSEC, timed * 1000)
    success, image = vid_cap.read()
    if success:
        vehicles = vehicle_cascade.detectMultiScale(image, 1.1, 5)
        return len(vehicles)
    else:
        return 0
