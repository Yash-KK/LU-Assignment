from PIL import Image
from PIL import ImageDraw, ImageFont

# Opening the Image 
"""
This Image contains the Text: What is your Name: _____
"""

def write_name(name):
    img = Image.open('ques.jpeg')   # This image contains the Text: What is your Name: ______
    img2 = ImageDraw.Draw(img)
    
    font = ImageFont.truetype("arial.ttf", 40, encoding="unic") # Setting up the Font     
    
    img2.text((600,250),name, fill=(0,0,0),font=font,stroke_width=1,stroke_fill="black") # Adding Text to the Image


    img = img.save(f"{name}.jpg")   # saves the File in the present directory as the name of the User


   
ask_user = input("Enter your Name: ")      # Asking the User to write his/her Name
if len(ask_user) ==0:
    raise Exception("Empty String!")       # If Empty String, raise an Exception
else:
    write_name(ask_user)                   # Call the function 
    
    
