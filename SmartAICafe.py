import pyttsx3
import wikipedia
import webbrowser
import speech_recognition as sr
import time
import os
import pandas as pd
import datetime
from tkinter import *
from PIL import Image,ImageTk
import os

name=''
listen_text=''
time_calc=0
ph_number=0
num_people=0

def a():
    global name
    global listen_text
    global time_calc
    global ph_number
    global num_people
    root=Tk()
    print('tk created')
    def speak(st):
        def s(text):
            engine = pyttsx3.init()
            engine.setProperty('rate',125)
            engine.say(text)
            engine.runAndWait()
        img=photos[3]
        stt=''
        l3=Label(l1,image=img,borderwidth=0)
        l3.place(x=385,y=0)
        if(len(st)>61):
            l=1
            for i in range(0,len(st)):
                stt=stt+st[i]
                if (i%60==0 and i!=0):
                    stt=stt+"\n"
                    l+=1
                if(l==4):
                    break
        else:
            stt=st
        w = Canvas(l1, width=735, height=130, bd=0, highlightthickness=0, relief='ridge')
        w.place(x=388,y=231)
        l5=Label(w,image=photos[5],text=stt,font='bold 18',borderwidth=0,compound=CENTER)
        l5.place(x=-1,y=-1)
        root.update()
        s(st)
       

    def listen1():
        def l():
            global listen_text
            r=sr.Recognizer()
            r.energy_threshold=2000
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                try:
                    audio = r.listen(source)
                    listen_text=listen_text+r.recognize_google(audio)
                except sr.UnknownValueError:
                    speak('Sorry I could not recognize what you said...Can you say that again?')
                    listen1()
                listen_text=listen_text.lower()
        global name
        global time_calc
        global listen_text
        listen_text=''
        img=photos[2]
        l3=Label(l1,image=img,borderwidth=0)
        l3.place(x=385,y=0)
        w = Canvas(l1, width=735, height=130, bd=0, highlightthickness=0, relief='ridge')
        w.place(x=388,y=231)
        l5=Label(w,image=photos[5],text='Please Speak...',font='bold 18',borderwidth=0,compound=CENTER)
        l5.place(x=-1,y=-1)
        root.update()
        #time_calc+=1000
        #root1.after(time_calc,lambda:l())
        l()
       



    def get_name():
       
        global name
        global time_calc
        global listen_text
        start=int(datetime.datetime.now().strftime('%S'))
        name=""
       
        speak('What is your name?')
 
        listen1()
     
        name1=listen_text.split()
        for i in name1:
            if(i!='myself' and i!='my' and i!='is' and i!='name' and i!='am' and i!='i' and i!='this' and i!='mera' and i!='hai' and i!='naam'):
                name=name+" "+i
        speak('Hello!'+name)
       # time.sleep(2)
        speak('Is that your name to be printed on the bill?')
       # time.sleep(2)
        listen1()
        if (listen_text=='yes' or listen_text=='haan' or 'y' in listen_text ):
            pass
        elif(listen_text=='no' or 'n' in listen_text):
            get_name()
           
    def get_num():
        global ph_number
        global listen_text
        speak('Can I have your number?')
        listen1()
        listen_text.lower()
        if (listen_text=='yes' or listen_text=='haan' or 'y' in listen_text ):
            speak('Please speak your contact number to be printed on bill...')
            listen1()
            ph_number=listen_text
           
    def get_people():
        global listen_text
        global num_people
        speak('How many people are you accompanied with?')
        listen1()
        num_people=listen_text
       
    def order():
        top= Toplevel()
        x1 = top.winfo_screenwidth()
        y1 = top.winfo_screenwidth()
        top.title('ORDER')
        top.geometry('%dx%d' % (x1, y1))
       

        photos1=[]
        photo1=Image.open('order1.png')
        photo1=photo1.resize((1530,795),Image.ANTIALIAS)
        photos1.append(ImageTk.PhotoImage(photo1))
        photos2=[]
        photo2=Image.open('11.png')
        photo2=photo2.resize((650,750),Image.ANTIALIAS)
        photos2.append(ImageTk.PhotoImage(photo))
        photo2=Image.open('12.png')
        photo2=photo2.resize((650,750),Image.ANTIALIAS)
        photos2.append(ImageTk.PhotoImage(photo))
        photo2=Image.open('13.png')
        photo2=photo2.resize((650,750),Image.ANTIALIAS)
        photos2.append(ImageTk.PhotoImage(photo))
        photo2=Image.open('14.png')
        photo2=photo2.resize((650,750),Image.ANTIALIAS)
        photos2.append(ImageTk.PhotoImage(photo))
        photo2=Image.open('15.png')
        photo2=photo2.resize((650,750),Image.ANTIALIAS)
        photos2.append(ImageTk.PhotoImage(photo))
        photo2=Image.open('16.png')
        photo2=photo2.resize((650,750),Image.ANTIALIAS)
        photos2.append(ImageTk.PhotoImage(photo))
        photo2=Image.open('17.png')
        photo2=photo2.resize((650,750),Image.ANTIALIAS)
        photos2.append(ImageTk.PhotoImage(photo))
        photo2=Image.open('18.png')
        photo2=photo2.resize((650,750),Image.ANTIALIAS)
        photos2.append(ImageTk.PhotoImage(photo))

        L1=Label(top,image=photos1[0])
        L1.place(x=0,y=0)
        category=['Starters and Soups','Main Course','South Indian','Italian','Chinese','fast Food','Drinks','Desserts','Add ons']
        now1 = datetime.datetime.now()
        date1=now1.strftime("%d-%m-%Y %H:%M")
        Label(top,text=date1,font='bold 18',bg='white',fg='black').place(x=1333,y=760)
        top.update()
        active=True
        while active:
            speak('In which category mentioned here do you want to order food?')
            listen1()
            for i in range(0,9):
                if(listen_text==i):
                    top1=Toplevel()
                    top1.minsize(650,750)
                    top1.maxsize(650,750)
                    top1.title(category[i])
                    l=Label(top1,image=photos[i])
                    l.place(x=0,y=0)
                    top1.update()
                    ord=True
                    while ord:
                        speak('Please select the dish you want to order from the list....')
                        listen1()
                        df=pd.read_csv('menu_xls.csv')
                        #df1 = pd.DataFrame(data1, columns=['Category', 'Name', 'Price']
                        #df = df.append(df1, ignore_index=True)
                        #df.to_csv('menu_xls.csv', index=False)
                        list_menuname=[""]
                        list_menuprice=['']
                        for k,p in df['Name'],df['Price']:
                            if listen_text == k:
                                list_menuname.append(k)
                                list_menuprice.append(p)                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                speak('Please tell the number of plates you wanr to order of'+k)
                                listen1()
                                list_quanity.append(listen_text)
                                list_sum.append(len(list_quantity)*len(list_menuprice))
                                speak('Do you want to order more from this category?')
                                listen1()
                                if(listen_text=='yes'):
                                    ord=True
                                elif(listen_text=='no'):
                                    ord=False
               
               
                       
                   
                        top1.mainloop()
                   
                speak('Do you want to order from another category as well?')
                listen1()
                   

        top.mainloop()
   
                   
   
    x = root.winfo_screenwidth()
    y = root.winfo_screenwidth()
    root.title('SMART AI CAFE')
    root.geometry('%dx%d' % (x, y))
    #root1.wm_attributes('-fullscreen','true')
    print('win created')
   
    photos=[]
    photo=Image.open('cafe.png')
    photo=photo.resize((1600,850), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(photo))


    photo=Image.open('2.png')
    photo=photo.resize((290,225), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(photo))

    photo=Image.open('3.png')
    photo=photo.resize((740,240), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(photo))
   

    photo=Image.open('4.png')
    photo=photo.resize((740,240), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(photo))
   
    photo=Image.open('5.png')
    photo=photo.resize((740,240), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(photo))

    photo=Image.open('7.png')
    photo=photo.resize((735,130), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(photo))
    img=photos[3]
    print('photos added')
    l1 =Label(root, image=photos[0])
    l1.place(x=0,y=0)

    l2=Label(root, image=photos[1],borderwidth=0)
    l2.place(x=172,y=500)
   
    l3=Label(l1,image=img,borderwidth=0)
    l3.place(x=385,y=0)
    w = Canvas(l1, width=735, height=130, bd=0, highlightthickness=0, relief='ridge')
    w.place(x=388,y=231)
    l5=Label(w,image=photos[5],text='Welcome to the Cafe...',font='bold 18',borderwidth=0,compound=CENTER)
    l5.place(x=0,y=0)
    root.update()

    time1=datetime.datetime.now()
    hour=int(time1.strftime('%H'))


    #time_calc=0
    #start=int(datetime.datetime.now().strftime('%S'))
    print('func call starts')
    if hour<12:
        #root1.after(1000, lambda: speak("Good Morning"))
        speak("Good Morning")
    elif hour<16:
        #root1.after(1000, lambda: speak('Good Afternoon'))
        speak('Good Afternoon')
    else:
        #root1.after(1000, lambda: speak('Good Evening'))
        speak('Good Evening')
    speak("You are welcome to The AI Cafe...I am Jarvis...I\'ll help you with your order...")
   

    print('tk printed')
    get_name()
    get_num()
    get_people()
    order()

   
    root.mainloop()

           
   

if __name__=='__main__':
    a()
