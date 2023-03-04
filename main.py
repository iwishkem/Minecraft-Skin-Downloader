from guizero import App, TextBox, PushButton, Picture
import tkinter as tk
import requests

# Create the GUI app
app = App(title="Minecraft Skin Downloader", width=500, height=500)

# Load the background image
background_image = tk.PhotoImage(file="background.png")

# Create a label to display the background image
background_label = tk.Label(app.tk, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Get the tkinter window object from the app
tk_window = app.tk

# Load the icon file and set it as the window icon
icon = tk.PhotoImage(file="icon.ico")
tk_window.iconphoto(True, icon)

# Create the text box widget
text_box = TextBox(app)

# Create the picture widget
picture = Picture(app)

# Create the button widget
button = PushButton(app, text="Download Skin")

# Define a function to handle the button click event
def on_button_click():
    # Retrieve the user's input from the text box
    user_input = text_box.value
    
    # Construct the URL with the user's input
    image_url = "https://minotar.net/skin/" + user_input

    # Make a GET request to retrieve the image data
    response = requests.get(image_url)

    # Write the image data to a file
    with open(user_input + ".png", "wb") as f:
       f.write(response.content)

# Associate the button with the click event handler
button.update_command(on_button_click)

# Start the GUI event loop
app.display()
