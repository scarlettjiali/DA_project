import io
from PIL import Image, ImageTk
import tkinter as tk
from urllib.request import urlopen
from time import sleep
import random

def create_dict():
    item_B0000000ZW = dict()
    item_B0000000ZW['product_name'] = 'Changing Faces'
    item_B0000000ZW['product_author'] = 'Changing Faces'
    item_B0000000ZW['product_fig'] = 'https://images-na.ssl-images-amazon.com/images/I/51K2YJvd79L._SS500.jpg'

    item_B000BNTM32 = dict()
    item_B000BNTM32['product_name'] = 'The Breakthrough'
    item_B000BNTM32['product_author'] = 'Mary J. Blige'
    item_B000BNTM32['product_fig'] = 'https://images-na.ssl-images-amazon.com/images/I/41EXE2SLIJL._SS500.jpg'

    item_B00004WIZA = dict()
    item_B00004WIZA['product_name'] = 'TP-2.com'
    item_B00004WIZA['product_author'] = 'R. Kelly'
    item_B00004WIZA['product_fig'] = 'https://images-na.ssl-images-amazon.com/images/I/51VpbU%2BxDfL._SY300_QL70_.jpg'

    item_B000002OME = dict()
    item_B000002OME['product_name'] = "What's The 411?"
    item_B000002OME['product_author'] = 'Mary J. Blige'
    item_B000002OME['product_fig'] = 'https://images-na.ssl-images-amazon.com/images/I/41IfZ3Ax-HL._SS500.jpg'

    item_B00096S3PY = dict()
    item_B00096S3PY['product_name'] = 'The Way It Is'
    item_B00096S3PY['product_author'] = 'Keyshia Cole'
    item_B00096S3PY['product_fig'] = 'https://images-na.ssl-images-amazon.com/images/I/51wOqmuNvVL._SS500.jpg'

    item_B00000050T = dict()
    item_B00000050T['product_name'] = '12 Play'
    item_B00000050T['product_author'] = 'R. Kelly'
    item_B00000050T['product_fig'] = 'https://images-na.ssl-images-amazon.com/images/I/41aeEtXcUwL._SS500.jpg'

    item_B00000053B = dict()
    item_B00000053B['product_name'] = 'R. Kelly'
    item_B00000053B['product_author'] = 'R. Kelly'
    item_B00000053B['product_fig'] = 'https://images-na.ssl-images-amazon.com/images/I/51wP-Kt-g6L._SS500.jpg'

    item_B00004UARR = dict()
    item_B00004UARR['product_name'] = 'Who Is Jill Scott? Words and Sounds'
    item_B00004UARR['product_author'] = 'Jill Scott'
    item_B00004UARR['product_fig'] = 'https://images-na.ssl-images-amazon.com/images/I/51crOiHih4L._SX300_QL70_.jpg'

    item_B0000000ZW = dict()
    item_B0000000ZW['product_name'] = 'Changing Faces'
    item_B0000000ZW['product_author'] = 'Changing Faces'
    item_B0000000ZW['product_fig'] = 'https://images-na.ssl-images-amazon.com/images/I/51K2YJvd79L._SS500.jpg'

    item_B00006ISBT = dict()
    item_B00006ISBT['product_name'] = 'Voyage To India'
    item_B00006ISBT['product_author'] = 'India.Arie'
    item_B00006ISBT['product_fig'] = 'https://images-na.ssl-images-amazon.com/images/I/413K1gCKLCL._SS500.jpg'

    item_B0000AGWFA = dict()
    item_B0000AGWFA['product_name'] = "Comin' From Where I'm From"
    item_B0000AGWFA['product_author'] = 'Anthony Hamilton'
    item_B0000AGWFA['product_fig'] = 'https://images-na.ssl-images-amazon.com/images/I/51b1imyagkL._SS500.jpg'

    global item_info
    item_info = dict()

    item_info['B0000000ZW'] = item_B0000000ZW
    item_info['B000BNTM32'] = item_B000BNTM32
    item_info['B00004WIZA'] = item_B00004WIZA
    item_info['B000002OME'] = item_B000002OME
    item_info['B00096S3PY'] = item_B00096S3PY
    item_info['B00000050T'] = item_B00000050T
    item_info['B00000053B'] = item_B00000053B
    item_info['B00004UARR'] = item_B00004UARR
    item_info['B0000000ZW'] = item_B0000000ZW
    item_info['B00006ISBT'] = item_B00006ISBT
    item_info['B0000AGWFA'] = item_B0000AGWFA

    global item_recommend
    item_recommend = dict()
    item_recommend['B0000000ZW'] = ['B000BNTM32', 'B00004WIZA', 'B000002OME', 'B00096S3PY', 'B00000050T']
    item_recommend['B000BNTM32'] = ['B00000053B', 'B00004UARR', 'B0000000ZW', 'B00006ISBT', 'B0000AGWFA']

    print(item_info)
    print(item_recommend)

def get_product():
    sleep(random.randint(1, 3))
    global the_asin
    the_asin = e1.get()
    pic_url = item_info.get(the_asin).get('product_fig')
    album_nam = item_info.get(the_asin).get('product_name')
    author_nam = item_info.get(the_asin).get('product_author')
    image_bytes = urlopen(pic_url).read()
    # internal data file
    data_stream = io.BytesIO(image_bytes)
    # open as a PIL image object
    pil_image = Image.open(data_stream)
    pil_image = pil_image.resize((250, 300), Image.ANTIALIAS)
    # optionally show image info
    # get the size of the image
    #w, h = pil_image.size
    # split off image file name
    # convert PIL image object to Tkinter PhotoImage object
    tk_image = ImageTk.PhotoImage(pil_image)
    canvas = tk.Canvas(window, height=300, width=250)
    canvas.create_rectangle(0, 0, 250, 300, fill="white")
    canvas.pack()
    canvas.place(x=55, y=170)
    canvas.image = tk_image
    canvas.create_image(125, 6, anchor='n',image=tk_image)

    album_label = tk.Label(window, text=album_nam, font=("Helvetica", 20, "bold italic"))
    album_label.place(x=55, y=490)

    author_label = tk.Label(window, text=author_nam,font=("Times", 17, "italic"))
    author_label.place(x=55, y=530)

    #print(e1.get())


def recommend_product():
    # show recommend pic1
    asin_list = item_recommend.get(the_asin)
    sleep(random.randint(1, 2))
    pic_url = item_info.get(asin_list[0]).get('product_fig')
    album_nam = item_info.get(asin_list[0]).get('product_name')
    author_nam = item_info.get(asin_list[0]).get('product_author')

    # pic_url = "https://images-na.ssl-images-amazon.com/images/I/51%2BxK8PMPkL._SS500.jpg"
    # album_nam = 'Reputation'
    # author_nam = 'Taloy Swift'
    image_bytes = urlopen(pic_url).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    pil_image = pil_image.resize((63, 75), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(pil_image)
    canvas1 = tk.Canvas(window, height=75, width=62.5)
    canvas1.create_rectangle(0, 0, 62.5, 75, fill="#476042")
    canvas1.pack()
    canvas1.place(x=470, y=120)
    canvas1.image = tk_image
    canvas1.create_image(31.25, 1.5, anchor='n',image=tk_image)

    album_label1 = tk.Label(window, text=album_nam, font=("Helvetica", 13, "bold italic"))
    album_label1.place(x=540, y=130)

    author_label1 = tk.Label(window, text=author_nam,font=("Times", 11, "italic"))
    author_label1.place(x=540, y=160)

    # show recommend pic2:
    sleep(random.randint(1, 2))
    pic_url = item_info.get(asin_list[1]).get('product_fig')
    album_nam = item_info.get(asin_list[1]).get('product_name')
    author_nam = item_info.get(asin_list[1]).get('product_author')

    image_bytes = urlopen(pic_url).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    pil_image = pil_image.resize((63, 75), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(pil_image)
    canvas2 = tk.Canvas(window, height=75, width=62.5)
    canvas2.create_rectangle(0, 0, 62.5, 75, fill="#476042")
    canvas2.pack()
    canvas2.place(x=470, y=210)
    canvas2.image = tk_image
    canvas2.create_image(31.25, 1.5, anchor='n',image=tk_image)

    album_label2 = tk.Label(window, text=album_nam,font=("Helvetica", 13, "bold italic"))
    album_label2.place(x=540, y=220)

    author_label2 = tk.Label(window, text=author_nam,font=("Times", 11, "italic"))
    author_label2.place(x=540, y=250)

    #show recommend pic3
    pic_url = item_info.get(asin_list[2]).get('product_fig')
    album_nam = item_info.get(asin_list[2]).get('product_name')
    author_nam = item_info.get(asin_list[2]).get('product_author')

    image_bytes = urlopen(pic_url).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    pil_image = pil_image.resize((63, 75), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(pil_image)
    canvas3 = tk.Canvas(window, height=75, width=62.5)
    canvas3.create_rectangle(0, 0, 62.5, 75, fill="#476042")
    canvas3.pack()
    canvas3.place(x=470, y=300)
    canvas3.image = tk_image
    canvas3.create_image(31.25, 1.5, anchor='n',image=tk_image)

    album_label3 = tk.Label(window, text=album_nam,font=("Helvetica", 13, "bold italic"))
    album_label3.place(x=540, y=310)

    author_label3 = tk.Label(window, text=author_nam,font=("Times", 11, "italic"))
    author_label3.place(x=540, y=340)

    #show recommend pic4
    pic_url = item_info.get(asin_list[3]).get('product_fig')
    album_nam = item_info.get(asin_list[3]).get('product_name')
    author_nam = item_info.get(asin_list[3]).get('product_author')

    image_bytes = urlopen(pic_url).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    pil_image = pil_image.resize((63, 75), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(pil_image)
    canvas4 = tk.Canvas(window, height=75, width=62.5)
    canvas4.create_rectangle(0, 0, 62.5, 75, fill="#476042")
    canvas4.pack()
    canvas4.place(x=470, y=390)
    canvas4.image = tk_image
    canvas4.create_image(31.25, 1.5, anchor='n',image=tk_image)
    album_label4 = tk.Label(window, text=album_nam,font=("Helvetica", 13, "bold italic"))
    album_label4.place(x=540, y=400)
    author_label4 = tk.Label(window, text=author_nam,font=("Times", 11, "italic"))
    author_label4.place(x=540, y=430)

    #show recommend pic5
    pic_url = item_info.get(asin_list[4]).get('product_fig')
    album_nam = item_info.get(asin_list[4]).get('product_name')
    author_nam = item_info.get(asin_list[4]).get('product_author')

    image_bytes = urlopen(pic_url).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    pil_image = pil_image.resize((63, 75), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(pil_image)
    canvas5 = tk.Canvas(window, height=75, width=62.5)
    canvas5.create_rectangle(0, 0, 62.5, 75, fill="#476042")
    canvas5.pack()
    canvas5.place(x=470, y=480)
    canvas5.image = tk_image
    canvas5.create_image(31.25, 1.5, anchor='n',image=tk_image)
    album_label5 = tk.Label(window, text=album_nam,font=("Helvetica", 13, "bold italic"))
    album_label5.place(x=540, y=490)
    author_label5 = tk.Label(window, text=author_nam,font=("Times", 11, "italic"))
    author_label5.place(x=540, y=520)



create_dict()
sleep(random.randint(1, 3))
window = tk.Tk()
window.title('Welcome to our project!')

window.geometry('800x600')
window.resizable(False, False)
canvas = tk.Canvas(window, height=600, width=1000)
canvas.pack()
image = Image.open('./background.jpg')
image = image.resize((800, 600), Image.ANTIALIAS)
photo_image = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, image=photo_image, anchor="nw")

canvas_header = canvas.create_text(110, 40, anchor="nw")
title_ = 'Welcome to our Music Video Recommendation System'
canvas.itemconfig(canvas_header, text=title_, width=800)
canvas.itemconfig(canvas_header, font=('Times', 25, 'bold'))
canvas.insert(canvas_header, 0, '')

canvas_author = canvas.create_text(420, 85, anchor="nw")
text_ = 'Author: Yaojun Qin, Yunzhu Liu, Chen Ke, Jiali Sun'
canvas.itemconfig(canvas_author, text=text_, width=800)
canvas.itemconfig(canvas_author, font=('Times', 16, 'italic'))
canvas.insert(canvas_author, 0, '')

asin_label = tk.Label(window, text="Asin")
asin_label.place(x=40, y=120)

e1 = tk.Entry(window)
e1.place(x=80, y=120)

show_asin = tk.Button(window, text='Show', command=get_product)
show_asin.place(x=280, y=120)


process_bt = tk.Button(window, text='Process', font=('Times', 18,"bold italic"), width=12, height=3,command=recommend_product)
process_bt.place(x=330, y=300)


window.mainloop()