from tkinter import *
from PIL import ImageTk, Image
import requests
import json
from io import BytesIO
import urllib.request
from resizeimage import resizeimage




def api_call():
    '''Calls the Waifu API, converts link to an image, resizes the image,
    and then updates the label in Tkinter with the new image'''
    global im
    endpoint = f'https://waifu.pics/api/sfw/{clicked.get()}'


    #the actual API call
    response = requests.get(endpoint)
    response.raise_for_status()
    data = response.json()
    global url
    url = data['url']

    #takes the image, opens it up, gets width and height (for later)
    image = Image.open(requests.get(url, stream=True).raw)
    width, height = image.size
    print(width, height)

    #resizes the image and changes the background color
    operation1 = resizeimage.resize_width(image, 300)
    image = resizeimage.resize_contain(operation1, [450, 400], bg_color=(255, 250, 205))

    #converts the image into an ImageTk so it can be configured onto the label
    im = ImageTk.PhotoImage(image)
    starter_label.config(image=im)



    


    


#creates window, adds title, and padding/bg color
window = Tk()
window.title('Waifu Generator')
window.config(padx=20, pady=20, bg='#FFFACD')

#label creation
welcome_label = Label(text='Welcome to the Waifu Generator!', bg='#FFFACD',
font=('Arial', 15, 'bold'))
welcome_label.grid(row=0, column=0, columnspan=2)

choose_label = Label(text='さあ。。。ワイフを選んで下さい♡', bg='#FFFACD',
font=('Arial', 12, 'italic'))
choose_label.grid(row=1, column=0, columnspan=2)

#button creation
finalize_button = Button(text='Finalize choice', command=api_call)
finalize_button.grid(row=3, column=1)


#dropdown creation
options=['waifu', 'neko', 'megumin', 'bully', 'cuddle',
'hug', 'kiss', 'pat', 'smug', 'bonk', 'smile', 'blush',
'wave', 'kill', 'happy', 'wink', 'dance']
clicked = StringVar()
clicked.set('Type Selector')

#dropdown command + feis
drop = OptionMenu(window, clicked, *options)
drop.grid(row=3, column=0)

#initial image
#or at least that's what it was supposed to be
#now it gets the initial image, but starter_image is also what gets updated
nino_filepath = 'OneDrive/Desktop/Personal/waifu_generator/images/nino_template2.jpg'
starter_image = ImageTk.PhotoImage(Image.open(nino_filepath))
starter_label = Label(window, image=starter_image)
starter_label.config(bg='#FFFACD', highlightthickness=0)
starter_label.grid(row=2, column=0, columnspan=2)








window.mainloop()

