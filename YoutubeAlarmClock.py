import tkinter as tk
import time
import webbrowser
from datetime import datetime
import threading


# URL of the video you want to play
URL = "https://www.youtube.com/watch?v=Gu9HhYv0C7E"

# Function to set an alarm
# Validation for input fields
def setAlarm():
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())

    # Validate the hour
    if hour < 0 or hour > 23:
        raise ValueError("The time must be between 0 and 23.")

    # Validate the minute
    if minute < 0 or minute > 59:
        raise ValueError("The minute must be between 0 and 59.")

    return datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour, minute)

# Function to play alarm URL
def startAlarm():
    webbrowser.open(URL)

# Function to check if it is alarm time
def checkAlarm():
    try:
        alarm = setAlarm()
    except ValueError as e:
        result_label.config(text=e.args[0])
        return

    while True:
        now = datetime.now()
        if now >= alarm:
            result_label.config(text="The alarm was activated.")
            startAlarm()  # Function call to play URL
            break
        else:
            result_label.config(text="Waiting for the alarm...")
            time.sleep(10)  # Wait 10 seconds between checks

# Create interface
window = tk.Tk()
window.title("YouTube Alarm Clock")
window.geometry("600x400")  # Window size

# Labels and input fields
hour_label = tk.Label(window, text="Hour (0-23):")
hour_label.pack()
hour_entry = tk.Entry(window)
hour_entry.pack()

minute_label = tk.Label(window, text="Minute (0-59):")
minute_label.pack()
minute_entry = tk.Entry(window)
minute_entry.pack()

# Function to start alarm checking
def initCheckAlarm():
    thread = threading.Thread(target=checkAlarm)
    thread.daemon = True  # The thread will stop when the application is closed
    thread.start()

# Button to set the alarm
set_button = tk.Button(window, text="Set Alarm", command=initCheckAlarm)
set_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Show current time in real time
def showCurrentTime():
    current_time = time.strftime("%H:%M:%S")
    current_time_label.config(text=f"Current time: {current_time}")
    window.after(1000, showCurrentTime)

current_time_label = tk.Label(window, text="", font=("Helvetica", 12))
current_time_label.pack()
showCurrentTime()

window.mainloop()







