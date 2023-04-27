import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello Memecakes")

# Set the window size
root.geometry("60x400")

# Create a maximized button (disabled)
button = tk.Button(root, text="Hello Memecakes", state="disabled")
button.pack(fill=tk.BOTH, expand=True)

# Create a small window
small_window = tk.Toplevel(root)
small_window.title("Little Bitty Window")
small_window.geometry("100x100")

# Start the main loop
root.mainloop()

##  FCP Foundation 20XX [C] 20XX - 4.27.X  - 4.27.X
