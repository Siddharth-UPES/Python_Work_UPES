import tkinter as tk
from File_download import download_file as dwld


root = tk.Tk()
root.title("File Downloader")
root.geometry("500x200")

def buttonCall():
    url = urlInput.get()
    fname = filenameInput.get()
    print(f"Url: {url}\nFilename: {fname}")
    dwld(url, fname)

# Label for URL
urlLabel = tk.Label(root, text="URL")
urlLabel.grid(row=0, column=0, padx=10, pady=10)

# URL entry
urlInput = tk.Entry(root, width=40)
urlInput.grid(row=0, column=1, padx=10, pady=10)

# Label for Filename
filenameLabel = tk.Label(root, text="Filename")
filenameLabel.grid(row=1, column=0, padx=10, pady=10)

# Filename entry
filenameInput = tk.Entry(root, width=40)
filenameInput.grid(row=1, column=1, padx=10, pady=10)

# Button
downloadButton = tk.Button(root, text="Download", command=buttonCall)
downloadButton.grid(row=2, column=1, pady=10)

root.mainloop()
