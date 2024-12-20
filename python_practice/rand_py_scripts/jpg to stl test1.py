# Python script with a full GUI for Windows
# that prompts the user to select a JPG file
# and converts it to an STL and prompts
# the user for a destination folder

from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Create the Window
window = Tk()
window.title("Image to STL Converter")

# Create a label to explain the program
explain = Label(window, text = "Please select an image to convert to an STL file")
explain.pack()

# Function to open a file dialog and store the result
def openDialog():
    file_name =  filedialog.askopenfilename(initialdir =  "/", 
                                           title = "Select a file", 
                                           filetypes = (("JPG files","*.jpg"),("all files","*.*")))
    if file_name != '':
        # Store the file name in a variable
        file_loc = file_name

# Create a button to open the file dialog
selectButton = Button(window, text = "Select Image", command = openDialog)
selectButton.pack()

# Function to open a folder dialog and store the result
def saveDialog():
    destination = filedialog.askdirectory(initialdir = "/", title = "Select a destination folder")
    if destination != '':
        # Store the file name in a variable
        save_loc = destination

# Create a button to open the folder dialog
saveButton = Button(window, text = "Select Destination", command = saveDialog)
saveButton.pack()

# Function to convert JPG to STL
def convertImage():
    #convert to numpy array
    arr = np.array(file_loc)

    #convert to stl
    stl_file = np.asstl(img_array)
    stl_file.write(arr.tostring())
    stl_file.close()
    print("Converting Image...")

# Create a button to call the convertImage function
convertButton = Button(window, text = "Convert", command = convertImage)
convertButton.pack()

# Execute the window
window.mainloop()



