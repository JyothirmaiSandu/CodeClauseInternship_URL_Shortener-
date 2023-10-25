import tkinter as tk
import random
import string

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return "http://short.url/" + short_url

def shorten_url():
    long_url = entry_long_url.get()

    if not long_url:
        result_label.config(text="Please enter a URL", fg="red")
        return

    short_url = generate_short_url()

    entry_short_url.delete(0, tk.END)
    entry_short_url.insert(0, short_url)
    result_label.config(text="URL shortened successfully", fg="green")

def copy_to_clipboard():
    short_url = entry_short_url.get()

    if short_url:
        root.clipboard_clear()
        root.clipboard_append(short_url)
        root.update()
        result_label.config(text="Short URL copied to clipboard", fg="green")
    else:
        result_label.config(text="No short URL available", fg="red")

root = tk.Tk()
root.title("Colorful URL Shortener")
root.configure(bg="#FFDAB9")  # Peach Puff

label_long_url = tk.Label(root, text="Long URL:", bg="#FFDAB9")  # Peach Puff
label_long_url.pack(pady=(10, 0))

entry_long_url = tk.Entry(root, width=50)
entry_long_url.pack(pady=(0, 10))

button_shorten = tk.Button(root, text="Shorten URL", command=shorten_url, bg="#87CEFA")  # Light Sky Blue
button_shorten.pack()

entry_short_url = tk.Entry(root, width=50)
entry_short_url.pack(pady=(10, 0))

button_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#87CEFA")  # Light Sky Blue
button_copy.pack()

result_label = tk.Label(root, text="", fg="green", bg="#FFDAB9")  # Peach Puff
result_label.pack(pady=(10, 0))

root.mainloop()