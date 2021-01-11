from threading import Thread
from time import sleep
import cv2
from Project_display import display_image


def video_len(filename):
    """Returns length of a video"""
    cap = cv2.VideoCapture(filename)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    return int(duration)


def time_allocation(vehicle_count, total_time):
    """Returns allocated time"""
    total_vehicles = 0
    time_allocated = ["", "", "", ""]
    for i in range(4):
        total_vehicles += vehicle_count[i]
    for i in range(4):
        if total_vehicles != 0:
            time_allocated[i] = float(vehicle_count[i] / total_vehicles) * int(total_time)
        else:
            time_allocated[i] = 0
    return time_allocated


def countdown(filename, video_len, frame_time, total_time, alloc_time, label, label_tt, canvas):
    """Runs the count down"""
    time_deduction = 0.1
    total_time = round(total_time, 1)

    for i in range(4):
        """Thread for Displaying images"""
        thread_image = Thread(target=display_image, args=[filename[i], video_len[i], frame_time, alloc_time[i], i])
        alloc_time[i] = round(alloc_time[i], 1)
        canvas[i]['bg'] = "green"
        canvas[i].update()
        thread_image.start()
        while round(alloc_time[i], 1) > 0:
            total_time -= round(time_deduction, 1)
            alloc_time[i] -= round(time_deduction, 1)
            label_tt['text'] = 'Total Time = ' + str(abs(round(total_time, 1)))
            label[i]['text'] = 'Time Allocated is : ' + str(abs(round(alloc_time[i], 1)))
            label_tt.update()
            label[i].update()
            sleep(time_deduction)
        canvas[i]['bg'] = "red"
        canvas[i].update()
