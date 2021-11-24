from tkinter import *
from tkinter import messagebox
import qrcode
from PIL import Image,ImageTk


root= Tk(className='qrcode-generator')

root.geometry('500x500')
a=StringVar()
def generate():
	if e.get()=='':
		messagebox.showinfo('Error','Enter URL ')
	else:
		
		url=e.get()
		obj=qrcode.QRCode()
		obj.add_data(url)
		
		img=obj.make_image()
		resize_image=img.resize((200,140))
		resize_image.save('D:\\python\\image\\qr.png')
		root.photo=PhotoImage(file='D:\\python\\image\\qr.png')

		

		l2=Label(image=root.photo,width=180,height=130)
		l2.place(x=170,y=120)
		
	
def reset():
	
	a.set('')

	root.photo=PhotoImage(file='')	

l=Label(text='QR Code-Generator',font=('Courier bold',30))
l.place(x=97,y=30)
l1=Label(text='Enter URL:',font=('Courier',20))
l1.place(x=20,y=320)
e= Entry(font=('Arial',15),width=27,textvariable=a)
e.place(x=190,y=320)

b=Button(text='Generate',bg='Green',font=('Terminal'),width=10,command=generate)
b.place(x=150,y=430)

b1=Button(text='Reset',bg='yellow',font=('Terminal'),width=10,command=reset)
b1.place(x=300,y=430)
root.mainloop()