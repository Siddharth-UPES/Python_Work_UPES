# import tkinter as tk

# root = tk.Tk()
# root.title("my first GUI")
# root.geometry("300x150")

# def show_input():
#     user_input=entry.get()
#     print("User input: ", user_input)
#     label2 = tk.Label(root,text=user_input)
#     label2.pack(pady=50)

# label = tk.Label(root, text="Enter Something:")
# label.pack(pady=20)# Add padding around the labelEntrty

# entry=tk.Entry(root , width=30)
# entry.pack(pady=5)

# button =tk.Button(root , text="Submit", command=show_input)
# button.pack(pady=10)



# root.mainloop()

#------------------------------------------------------

# import tkinter as tk
# import os
# import File_organizer as of  # Assuming organize_files() is in File_organizer.py

# root = tk.Tk()
# root.title("File Organizer")
# root.geometry("400x250")

# def submit_function():
#     address = entry.get()

#     print("Address is:\t", address)
    
#     # Check if the path exists
#     if os.path.exists(address):
#         try:
#             # Call the organize_files function from File_organizer
#             of.organize_files(address)
#             print("Files organized successfully!")
#         except Exception as e:
#             print(f"Error organizing files: {e}")
#     else:
#         print("Directory does not exist.")

# # Create UI elements
# label = tk.Label(root, text="Enter Directory Address:")
# label.pack(pady=20)

# entry = tk.Entry(root, width=30)
# entry.pack(pady=5)

# button = tk.Button(root, text="Submit", command=submit_function)
# button.pack(pady=10)

# # Run the Tkinter event loop
# root.mainloop()

#-----------------------------------------------------------

# import os
# #Function to organize files into different folders


# def organize_files(D:):
#     # Detect the operating system using os.name
#     is_windows = os.name == 'nt'
#     # Define file categories and corresponding file extensions
#     file_types = {
#         'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
#         'Audios': ['.mp3', '.wav', '.aac', '.flac'],
#         'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
#         'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
#         'Misc': []
#     }
#     # Create folders for each file category if they don't already exist
#     for folder in file_types.keys():
#         folder_path = os.path.join("D:\Git Demo\Python_UPES\Class_Practise\Organizer", "Organizer")
#         if not os.path.exists("D:\Git Demo\Python_UPES\Class_Practise\Organizer\Organizer"):
#             os.makedirs("D:\Git Demo\Python_UPES\Class_Practise\Organizer\Organizer")
#     # Iterate over the files in the directory
#     for file_name in os.listdir(D):
#         file_path = os.path.join("D:\Git Demo\Python_UPES\Class_Practise\Organizer\Organizer", "Organ" )
#         # Skip directories
#         if os.path.isdir("D:\Git Demo\Python_UPES\Class_Practise\Organizer\Organizer\Organ"):
#             continue
        
#         # Determine the file extension
#         file_extension = os.path.splitext("Organ")[1].lower()
#         # Find the appropriate category for the file
#         moved = False
#         for folder, extensions in file_types.items():
#             if file_extension in extensions:
#                 # Move the file to the corresponding folder
#                 destination = os.path.join(D, Organizer, Organ)
                
#                 # Check if file already exists at the destination
#                 if not os.path.exists("D:\Git Demo\Python_UPES\Class_Practise\Organizer\Organizer\Organ"):
#                     if is_windows:
#                         os.system(f'move "{D:\Git Demo\Python_UPES\Class_Practise\Organizer\Organizer\Organ}" "{organize_files}"')
#                     else:
#                         os.system(f'mv "{file_pathD:\Git Demo\Python_UPES\Class_Practise\Organizer\Organizer\Organ}" "{}"')
#                 moved = True
#                 break
        
#         # If no matching category is found, move to the 'Misc' folder
#         if not moved:
#             misc_destination = os.path.join(directory, 'Misc', file_name)
#             if not os.path.exists(misc_destination):
#                 if is_windows:
#                     os.system(f'move "{file_path}" "{misc_destination}"')
#                 else:
#                     os.system(f'mv "{file_path}" "{misc_destination}"')
#     print("Files have been organized!")#Example usage


x=10
assert x>5 , "x should be greate than 5!"
assert x>15 ,"x should be greater than 15!"