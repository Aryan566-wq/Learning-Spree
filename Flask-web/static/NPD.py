import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

print("Welcome to ZEN_EX photo editor!")
print("If you face any issues while playing the program send a email to kahanvora2@gmail.com")
print("ZEN_EX version 2.0 REFINED by --Kahan Vora")
def done():
       messagebox.showinfo("Zen_Ex Editor", "Done!")
def save(img):
       fi  = open("uses.txt", "r")
       prev_use = int(fi.read())
       fi.close()
       fil = open("uses.txt", "w")
       fil.write(str(prev_use + 1))
       fil.close()
       name = "ZEN_EX  " + str(prev_use + 1) + ".png"
       img.save(name)
       done()
def rotate():
    img = song_list.get(ACTIVE)
    ask = int(input("By how many degrees do you want to rotate your img? >>"))
    imgc = Image.open(img)
    rotate_img = imgc.rotate(ask)
    save(rotate_img)
def flip():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    flip_bird = ImageOps.flip(imgc)
    save(flip_bird)
def border():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    size = int(input("how many pixels thick do you want your border to be? >>"))
    col = input("what color would you like your border to be? >> ")
    imgb = ImageOps.expand(imgc.copy(),border=size,fill=col)
    save(imgb)
def brightness():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    enhanced_level = float(input("By how much would you like to enhance your picture? >>"))
    imgbright = ImageEnhance.Brightness(imgc).enhance(enhanced_level)
    save(imgbright)
def blur():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    imgBlur = imgc.filter(ImageFilter.BLUR)
    imgBlur.save('Zen_ex.png')
    save(imgBlur)
def contour():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    imgBlur = imgc.filter(ImageFilter.CONTOUR)
    
    save(imgBlur)
def emboss():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    imgBlur = imgc.filter(ImageFilter.EMBOSS)
    
    save(imgBlur)
def detail():
    img = song_list.get(ACTIVE)
    imgc=  Image.open(img)
    imgBlur = imgc.filter(ImageFilter.DETAIL)
    
    save(imgBlur)
def edge():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    imgBlur = imgc.filter(ImageFilter.EDGE_ENHANCE)
    
    save(imgBlur)
def edgem():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    imgBlur = imgc.filter(ImageFilter.EDGE_ENHANCE_MORE)
    
    save(imgBlur)
def finde():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    imgBlur = imgc.filter(ImageFilter.FIND_EDGES)
    
    save(imgBlur)
def smooth():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    imgBlur = imgc.filter(ImageFilter.SMOOTH)
    
    save(imgBlur)
def smmothm():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    imgBlur = imgc.filter(ImageFilter.SMOOTH_MORE)
    
    save(imgBlur)
def sharpen():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    imgBlur = imgc.filter(ImageFilter.SHARPEN)
    
    save(imgBlur)
def colrc():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    try:
        r,g,b = imgc.split()
        img_coor = Image.merge("RGB", (g,b,r))
        save(img_coor)
    except:
        r,g,b,a = imgc.split()
        img_coor = Image.merge("RGBA", (g,b,r,a))
        save(img_coor)
def baw():
    img = song_list.get(ACTIVE)
    imgc = Image.open(img)
    new_img = imgc.convert('L')
    save(new_img)

#tkinter type of functions
def add_photo():
    song = filedialog.askopenfilenames(initialdir='/', title="Choose a song", filetypes=(("png files", "*.png"),("jpeg files", "*.jpeg"),("jpg files", "*.jpg"),('jiff','*.jfif')))
    for s in song:
        song_list.insert(END, s)

        
root = Tk()
root.title(" ZEN_EX ")
root.geometry("600x620")
#root.iconbitmap(r'pics\photo.ico')

song_list = Listbox(root, bg="black", fg="green", width=60, selectbackground="grey", selectforeground="red")
song_list.pack(pady=20)


#menu##
my_menu = Menu(root)
root.config(menu=my_menu)

#add songs to menu

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Photo", menu=add_song_menu)
#add_song_menu.add_command(label="Add a Song to the playlist", command = lambda: add_song())
#many song
add_song_menu.add_command(label="Add many Photos to the Account list", command = lambda: add_photo())

fr1 = Frame(root, bg="#0000ff")
fr1.pack(fill=X)
#b1_status
b11 = Button(fr1, bg ="#00ddff", text = "Rotate", command=rotate, padx=49,  pady=5, bd=5)
b12 = Button(fr1, bg ="#00ddff", text = "Flip", command=flip, padx=50, pady=5,bd=5)
b13 = Button(fr1, bg="#00ddff", text = "Border", command=border, padx=48, pady=5,bd=5)
b14 = Button(fr1, bg="#00ddff", text = "Brighten", command=brightness, padx=45, pady=5,bd=5)

#spacing_label
paddy = 10
paddx = 25


b11.grid(row=0, column=1, padx=paddx, pady=paddy)
b12.grid(row=0, column=2, padx=paddx, pady=paddy)
b13.grid(row=0, column=3, padx=paddx, pady=paddy)
b14.grid(row=4, column=1, padx=paddx, pady=paddy)

#b2_status
b21 = Button(fr1, bg ="#00ddff", text = "Blur", command=blur, padx=53,  pady=5,bd=5)
b22 = Button(fr1, bg ="#00ddff", text = "Contour", command=contour, padx=40, pady=5,bd=5)
b23 = Button(fr1, bg="#00ddff", text = "Detail", command=detail, padx=48, pady=5,bd=5)
b24 = Button(fr1, bg="#00ddff", text = "Emboss", command=emboss, padx=48, pady=5,bd=5)


b21.grid(row=1, column=1, padx=paddx, pady=paddy)
b22.grid(row=1, column=2, padx=paddx, pady=paddy)
b23.grid(row=1, column=3, padx=paddx, pady=paddy)
b24.grid(row=4, column=2, padx=paddx, pady=paddy)

#b3_status

b31 = Button(fr1, bg ="#00ddff", text = "Edge 1x", command=edge, padx=48,  pady=5,bd=5)
b32 = Button(fr1, bg ="#00ddff", text = "Edge 2x", command=edgem, padx=46, pady=5,bd=5)
b33 = Button(fr1, bg="#00ddff", text = "Find Edges", command=finde, padx=43, pady=5,bd=5)
b34 = Button(fr1, bg="#00ddff", text = "Smoothen 1x", command=smooth, padx=37, pady=5,bd=5)

b31.grid(row=2, column=1, padx=paddx, pady=paddy)
b32.grid(row=2, column=2, padx=paddx, pady=paddy)
b33.grid(row=2, column=3, padx=paddx, pady=paddy)
b34.grid(row=4, column=3, padx=paddx, pady=paddy)

b41 = Button(fr1, bg ="#00ddff", text = "Smoothen 2x", command=smmothm, padx=30,  pady=5,bd=5)
b42 = Button(fr1, bg ="#00ddff", text = "Color Change", command=colrc, padx=30, pady=5,bd=5)
b43 = Button(fr1, bg="#00ddff", text = "Black & White", command=baw, padx=30, pady=5,bd=5)


b41.grid(row=3, column=1, padx=paddx, pady=paddy)
b42.grid(row=3, column=2, padx=paddx, pady=paddy)
b43.grid(row=3, column=3, padx=paddx, pady=paddy)

#spacing
b44 = Button(fr1, bg="#00ddff", text = "Sharpen", command=sharpen, padx=46, pady=5,bd=5)
b44.grid(row=5, column=2, padx=paddx, pady=paddy)

f23 = Frame(root)
f23.pack()

version_name = Label(f23, text="Version 2.0 REFINED", font=40, foreground="#df0000")
by_name=  Label(f23, text="|   --By Kahan Vora", font=40, foreground="#df0000")

version_name.grid(row=0, column=1)
by_name.grid(row=0, column=2)
root.mainloop() 

#If you find a bug please report it to kahanvora2@gmail.com, @bug_bounty
#if you find a place of improvement report it to kahanvora2@gmail.com, @improvements
