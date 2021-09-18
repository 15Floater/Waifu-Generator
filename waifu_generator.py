from tkinter import *
from PIL import ImageTk, Image
import requests
import json
from io import BytesIO
import urllib.request
from resizeimage import resizeimage



#api
def api_call():
    global im
    endpoint = f'https://waifu.pics/api/sfw/{clicked.get()}'



    response = requests.get(endpoint)
    response.raise_for_status()
    data = response.json()
    global url
    url = data['url']
    print(url)

    image = Image.open(requests.get(url, stream=True).raw)
    image = resizeimage.resize_contain(image, [200, 300], bg_color=(255, 255, 255, 0))

    im = ImageTk.PhotoImage(image)
    

    starter_label.config(image=im)



    


    


#window creation
window = Tk()
window.title('Waifu Generator')

#label creation
welcome_label = Label(text='Welcome to the Waifu Generator!')
welcome_label.grid(row=0, column=0, columnspan=3)

choose_label = Label(text='さあ。。。ワイフを選んで下さい♡')
choose_label.grid(row=1, column=0, columnspan=3)

starter_label = Label(text='Here\'s Nino (best girl)!')
starter_label.grid(row=2, column=0)

#button creation
finalize_button = Button(text='Finalize choice', command=api_call)
finalize_button.grid(row=4, column=1)


#dropdown creation
options=['waifu', 'neko', 'megumin', 'bully', 'cuddle',
'hug', 'kiss', 'pat', 'smug', 'bonk', 'smile', 'blush',
'wave', 'kill', 'happy', 'wink', 'dance']
clicked = StringVar()
clicked.set('Type Selector')

drop = OptionMenu(window, clicked, *options)
drop.grid(row=2, column=2)

#initial image
nino_filepath = 'OneDrive/Desktop/Personal/waifu_generator/images/nino_template2.jpg'
starter_image = ImageTk.PhotoImage(Image.open(nino_filepath))
starter_label = Label(window, image=starter_image)
#starter_label.config(bg='#Fdfcfa', highlightthickness=0)
starter_label.grid(row=2, column=1)








window.mainloop()

