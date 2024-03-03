# Import module 
from tkinter import *

# Create object 
root = Tk() 

# Load your custom icon
custom_icon = PhotoImage(file="Tesla-logo.png")
root.iconphoto(False, custom_icon)


# Adjust size 
root.geometry("400x400") 

# Define a font with the desired size
custom_font = ("Roboto", 35)

# Add image file 
bg = PhotoImage(file = "modalS.png") 

x = (500 - bg.width()) / 2
y = (500 - bg.height()) / 2
# Create a vertical scrollbar and associate it with the Text widget
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Create Canvas 
canvas1 = Canvas( root, width = 600, 
				height = 400) 

canvas1.pack(fill = "both", expand = True) 

# Display image 
canvas1.create_image( x, y, image = bg, 
					anchor = "nw") 

# Add Text 
canvas1.create_text( 200, 250, text = "Modal 3", font=custom_font) 

# Create Buttons 
button1 = Button( root, bg="gray", fg="black",  relief="flat", borderwidth=0, text = "CUSTOM ORDER") 

button2 = Button( root, bg="white", fg="black",  relief="flat", borderwidth=0, text = "EXITING INVETORY") 

# Display Buttons 
button1_canvas = canvas1.create_window( 0, 0, 
									anchor = "nw", 
									window = button1) 


button2_canvas = canvas1.create_window(0,0, side=LEFT, padx=5, pady=5) 



# Execute tkinter 
root.mainloop() 
