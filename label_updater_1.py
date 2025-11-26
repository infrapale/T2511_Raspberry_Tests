import tkinter as tk
from threading import Thread
import time

def update_loop(root, labels):
    """Loop that updates labels from outside the window"""
    counter = 0
    while True:
        labels[0].config(text=f"Counter: {counter}")
        labels[1].config(text=f"Double: {counter * 2}")
        labels[2].config(text=f"Square: {counter ** 2}")
        labels[3].config(text=f"Time: {time.time():.2f}")
        counter += 1
        time.sleep(1)

root = tk.Tk()
root.title("Label Updater")
root.geometry("300x200")

# Create 4 labels
labels = []
for i in range(4):
    label = tk.Label(root, text="Updating...", font=("Arial", 12))
    label.pack(pady=10)
    labels.append(label)

# Start update loop in a separate thread
thread = Thread(target=update_loop, args=(root, labels), daemon=True)
thread.start()

root.mainloop()