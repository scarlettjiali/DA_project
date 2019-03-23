import io
from PIL import Image, ImageTk
import tkinter as tk
from urllib.request import urlopen
import numpy as np
import pandas as pd
import json
from time import sleep
import random

def begin_recommend(asin, relation, word_vec, rating):
    raw_list = json.loads(relation[asin].replace("\'", "\""))
    vec = word_vec[asin]
    tuple_list = []
    item_info = dict()
    for item in raw_list:
        try:
            a = np.dot(np.array(word_vec[item]), np.array(vec))
            b = np.linalg.norm(np.array(word_vec[item])) * np.linalg.norm(np.array(vec))
            c = a / b
            tuple_list.append((item, c))
        except:
            continue

    tuple_list.sort(key=lambda k: k[1], reverse=True)
    if len(tuple_list) > 10:
        tuple_list = tuple_list[:10]

    rating_list = []

    for item in tuple_list:
        try:
            rating_list.append((item[0], float(rating[item[0]])))
        except:
            continue

    rating_list.sort(key=lambda k: k[1], reverse=True)
    if len(rating_list) > 5:
        rating_list = rating_list[:5]

    recommendation_list = []
    for item in rating_list:
        recommendation_list.append(item[0])

    item_info[asin] = recommendation_list
    print(item_info)
    return item_info


def process_item(asin, relation, word_vec, rating):
    recommend = begin_recommend(asin, relation, word_vec, rating)
    output_dict = dict()
    for item in recommend[asin]:
        output_dict[item] = get_product_info(item)
    print(output_dict)
    return output_dict


def get_product_info(asin) :
    import requests
    from bs4 import BeautifulSoup
    product_detail = dict()
    product_result = dict()
    url = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + asin
    response = requests.get(url)
    sleep(random.randint(1,3))
    if not response.status_code == 200:
        print(response.status_code)
        return None
    try:
        results_page = BeautifulSoup(response.content,'lxml')
        product_result['product_name'] = results_page.find('h2').get_text()
        count = 0
        for element in results_page.find_all('span', class_="a-size-small a-color-secondary"):
            count+= 1
            if element.get_text() == 'by ':
                product_result['product_author'] = results_page.find_all('span', class_="a-size-small a-color-secondary")[count].get_text()
        detail_url = results_page.find('a', class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal").get('href')
        response1 = requests.get(detail_url)
        if not response1.status_code == 200:
            print(response1.status_code)
            return None
        try:
            results_page1 = BeautifulSoup(response1.content,'lxml')
            detail_code = results_page1.find('div', class_ = 'content').find('ul').find_all('li')
            product_result['product_fig'] = results_page1.find('img',alt = product_result['product_name']).get('src')
        except:
            pass
        return product_result
    except:
        return None




def show(asin):
    a = dict()
    a[asin] = get_product_info(asin)
    return a


# Show the info of the specific product
def get_product():
    global the_asin
    the_asin = e1.get()
    the_asin_info = show(the_asin)
    try:
        pic_url = the_asin_info.get(the_asin).get('product_fig')
        album_nam = the_asin_info.get(the_asin).get('product_name')
        author_nam = the_asin_info.get(the_asin).get('product_author')
    except:
        pic_url = 'https://images-na.ssl-images-amazon.com/images/I/51ZSTKJB%2BcL._SS500.jpg'
        album_nam = 'Something went wrong!'
        author_nam = 'Merry Christmas!'
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


# Show the recommend item info
def recommend_product():
    # show recommend pic1
    item_recommend_relation = begin_recommend(the_asin, r, w, rate)
    item_recommend_info = process_item(the_asin, r, w, rate)
    asin_list = item_recommend_relation.get(the_asin)
    try:
        pic_url = item_recommend_info.get(asin_list[0]).get('product_fig')
        album_nam = item_recommend_info.get(asin_list[0]).get('product_name')
        author_nam = item_recommend_info.get(asin_list[0]).get('product_author')
    except:
        pic_url = 'https://images-na.ssl-images-amazon.com/images/I/51ZSTKJB%2BcL._SS500.jpg'
        album_nam = 'Something went wrong!'
        author_nam = 'Merry Christmas!'
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
    try:
        pic_url = item_recommend_info.get(asin_list[1]).get('product_fig')
        album_nam = item_recommend_info.get(asin_list[1]).get('product_name')
        author_nam = item_recommend_info.get(asin_list[1]).get('product_author')
    except:
        pic_url = 'https://images-na.ssl-images-amazon.com/images/I/51ZSTKJB%2BcL._SS500.jpg'
        album_nam = 'Something went wrong!'
        author_nam = 'Merry Christmas!'
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
    try:
        pic_url = item_recommend_info.get(asin_list[2]).get('product_fig')
        album_nam = item_recommend_info.get(asin_list[2]).get('product_name')
        author_nam = item_recommend_info.get(asin_list[2]).get('product_author')
    except:
        pic_url = 'https://images-na.ssl-images-amazon.com/images/I/51ZSTKJB%2BcL._SS500.jpg'
        album_nam = 'Something went wrong!'
        author_nam = 'Merry Christmas!'
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
    try:
        pic_url = item_recommend_info.get(asin_list[3]).get('product_fig')
        album_nam = item_recommend_info.get(asin_list[3]).get('product_name')
        author_nam = item_recommend_info.get(asin_list[3]).get('product_author')
    except:
        pic_url = 'https://images-na.ssl-images-amazon.com/images/I/51ZSTKJB%2BcL._SS500.jpg'
        album_nam = 'Something went wrong!'
        author_nam = 'Merry Christmas!'
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
    try:
        pic_url = item_recommend_info.get(asin_list[4]).get('product_fig')
        album_nam = item_recommend_info.get(asin_list[4]).get('product_name')
        author_nam = item_recommend_info.get(asin_list[4]).get('product_author')
    except:
        pic_url = 'https://images-na.ssl-images-amazon.com/images/I/51ZSTKJB%2BcL._SS500.jpg'
        album_nam = 'Something went wrong!'
        author_nam = 'Merry Christmas!'
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




# Get the necessary data:
#get the dictionary of overall_rating
df = pd.read_csv("overall_rating.csv")
df.set_index('asin',inplace=True)
rate = dict()
for index in df.index:
    rate[index] = df['overall'].loc[index]

#get the dictionary of word_to_vector
df = pd.read_csv("d2v.csv")
df.set_index('Unnamed: 0',inplace=True)
dvdict = dict()
for index in df.index:
    dvdict[index] = list(df.loc[index])
w = dvdict

#get the dictionary of relation
df = pd.read_csv("meta.csv")
r = dict()
for i in range(len(df)):
    r[df.iloc[i]['asin']] = df.iloc[i]['also_bought']


#Begin the mainpage
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