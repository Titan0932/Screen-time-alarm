from tkinter import *
import time
from tkinter import font,messagebox
from PIL import ImageTk,Image
import tkinter.ttk as ttk





seconds=0
label2=None
done=False
def alarm(id):
    global start_time,label,alarm_on
    start_time=0
    root.after_cancel(id)
    messagebox.showinfo("ALARM!!!.", "GET OFF YOUR COMPUTER!!!")
    label.config(text="\t  GO!! STRETCH TIME!!!\t\t")
    alarm_on=True
    

def check():
    global after_id,seconds,u_time
    
    utime=u_time.get()
    
    check_time=time.time()
    seconds=int(((check_time-start_time)))
   
    label.config(text=f'\t Ok, Timer started! Start working!!  {seconds}\t')
    after_id=root.after(1000,check)
    
    if seconds!=int(utime):
        pass
    else:
        alarm(after_id)
    


def work_start():
    global start_time,label,seconds,label2,alarm_on
    try:
        input_val=int(u_time.get())     #this variable is not used but it detects errors!!
        alarm_on=False
        start_time=time.time()
        if label2 is not None:
            label2.destroy()
        label=Label(canvas,text='Ok, Timer started! Start working!!',font=25,fg='red',pady=5,borderwidth=3,relief='solid',padx=5)
        label.place(x=180,y=380)
       
        check()
    except:
        pass

            

    
def break_time():
    global label,label2,start_time,seconds,check_time,done,input_val
    try:  
        input_val=int(u_time.get())
        messagebox.showinfo("Greattt!!!!",'Good jobb!!',icon="question")
       
        
        start_time=time.time()
        seconds=0
        if alarm_on==True:
            work_start() 
        
    except: 
        label2=Label(canvas,text="\t Start Working Now??\t",font=25,fg='red',pady=5,borderwidth=3,relief='solid',padx=5)
        label2.place(x=180,y=380)
    


def end_time():
    global label,label2
    try:  
        root.after_cancel(after_id)
        label.config(text="\t Done for the Day, huh?\t\t")
    except NameError: 
        label2=Label(canvas,text="\t Start Working First??\t",font=25,fg='red',pady=5,borderwidth=3,relief='solid',padx=5)
        label2.place(x=180,y=380)







root=Tk()
root.minsize(width=700, height=500)
root.resizable(width=False,height=False)
root.title('Screen Time Notifier')
#root['background']='pink'

canvas = Canvas(root, width=600, height=500)
canvas.pack(fill=BOTH, expand=True)
my_img=ImageTk.PhotoImage(Image.open('C:/Users/anjis/Desktop/eXtraWorks/Python/screen_time/images/background.jpg'))
canvas.create_image(0, 0, image=my_img, anchor='nw')


heading=Label(canvas,text="Press 'start working' and I'll remind you to stretch periodically!! \nHappy working!! ",borderwidth=3,relief="solid",padx=5,pady=7)

heading.place(x=100,y=180)

heading['font']=font.Font(size=13)


ttk.Style().configure("TEntry", padding=(30,0 ,0 ,0) , relief="flat")
u_time=ttk.Entry(canvas,font=10)
u_time.insert(3,'Enter time in seconds')

u_time.place(x=220,y=280)

start=Button(canvas,text='Start Working',command=work_start,padx=4,pady=5,bg="#856ff8",fg='ivory',font=5)
start.place(x=140,y=320)
relax=Button(canvas,text='I took a Break!',command=break_time,padx=4,pady=5,bg='#856ff8',fg='ivory',fon=5)
relax.place(x=290,y=320)
finished=Button(canvas,text='Finished Working!!',command=end_time,padx=4,pady=5,bg='#856ff8',fg='ivory',font=5)
finished.place(x=450,y=320)



root.mainloop()
