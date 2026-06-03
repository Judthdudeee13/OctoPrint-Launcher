
'''
IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT 
TO CLOSE OCTOPRINT IF CONTROLLER IS CLOSED RUN THIS IN TERMINAL
pkill -f octoprint
IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT
'''


import tkinter as tk
import subprocess
import webbrowser
import time
import os

process = None

OCTOPRINT_PYTHON = "/Users/family/Octoprint/venv/bin/python"


root = tk.Tk()
root.title("OctoPrint Controller")
root.geometry("300x200")
connected = 'Not connected'
tk.Label(root, text="OctoPrint Control", font=("Arial", 16)).pack(pady=10)
state = tk.Label(root, text=f"{connected}", font=("Arial", 16), bg = '#ff0000')
state.pack(pady=5)

#root.attributes("-topmost", True)
def start_octoprint():
    global process
    global connected
    global state
    if process is None:
        process = subprocess.Popen(
    [OCTOPRINT_PYTHON, "-m", "octoprint", "serve"]
)
        time.sleep(3)
        connected = 'Connected'
        state.configure(text=f"{connected}", bg='#00ff00')
        #webbrowser.open("http://localhost:5000")

def stop_octoprint():
    global process
    global connected
    global state
    if process is not None:
        process.terminate()
        process = None
        connected = 'Not connected'
        state.configure(text=f"{connected}", bg='#ff0000')



tk.Button(root, text="Start OctoPrint", command=start_octoprint, width=20).pack(pady=5)
tk.Button(root, text="Stop OctoPrint", command=stop_octoprint, width=20).pack(pady=5)


root.mainloop()
