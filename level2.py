from tkinter import *
root = Tk()
tax=0
sp=0
AFTR=0
root.title('Tax Calculator')
root.geometry("600x400")
root.iconbitmap(r'D:\Documents\programming projects\Tax calculator')
bg = PhotoImage(file='images.png')
canvs=Canvas(root,width=100,height=150)
canvs.pack(fill="both",expand=True)
c=canvs.create_image(0,0,image=bg,anchor='nw')
def tax():
	a=e.get()
	a=int(a)
	b=e1.get()
	c=e2.get()
	b=int(b)
	if a<60 and b==20000:
		canvs.create_text(400,200,text=b,font=("Arial",10))
	elif a<60 and b>20000 and b<=50000:
			tax=0.2
			sp=b*tax
			AFTR=b-sp
			canvs.create_text(400,200,text=AFTR,font=("Arial",10))
	elif a<60 and b>50000 and b<=100000:
			tax=0.3
			sp=b*tax
			AFTR=b-sp
			canvs.create_text(400,200,text=AFTR,font=("Arial",10))
	elif a>=60 and b==20000:
		canvs.create_text(400,200,text=b,font=("Arial",10))
	elif a>=60 and b>20000 and b<=50000:
		tax=0.1
		sp=b*tax
		AFTR=b-sp
		canvs.create_text(400,200,text=AFTR,font=("Arial",10))
	elif a>60 and b>50000 and b<=100000:
	   tax=0.2
	   sp=b*tax
	   AFTR=b-sp
	   canvs.create_text(400,200,text=AFTR,font=("Arial",10))
	   
	    
	elif a>60 and b>100000:
	     tax=0.3
	     sp=b*tax
	     AFTR=b-sp
	     canvs.create_text(400,200,text=AFTR,font=("Arial",10))
	elif a<60 and c=='YES':
		tax=0.075
		sp=b*tax
		AFTR=b-sp
		create_text(400,200,text=AFTR,font=("Arial",10))

canvs.create_text(400,50,text='Tax Calculator',font=("Arial",40))
e=Entry(canvs)
canvs.create_window(400,100,window=e)
e1=Entry(canvs)
e2=Entry(canvs)
canvs.create_window(400,120,window=e1)
canvs.create_text(300,100,text='Enter age',font=("Arial",10))
canvs.create_text(300,120,text='Enter Income',font=("Arial",10))
canvs.create_text(270,140,text='Do you own a business',font=("Arial",10))
canvs.create_window(400,140,window=e2)
b=Button(root,text='Income after taxation',command = lambda :tax())
canvs.create_window(400,160,window=b)
root.mainloop()  
