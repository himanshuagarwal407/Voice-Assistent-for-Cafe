import pyttsx3
import wikipedia
import webbrowser
import speech_recognition as sr
from time import time
import os
import datetime
from tkinter import *
from PIL import Image,ImageTk
import os

name=''
listen_text=''
time_calc=0

def a():
    global name
    global listen_text
    global time_calc
    root1=Tk()
    def speak(st):
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
       
        root1.after(1000, lambda : s(st))
        def s(text):
             engine = pyttsx3.init()
             engine.setProperty('rate',125)
             engine.say(text)
             engine.runAndWait()

    def listen1():
        global name
        global time_calc
        global listen_text
        img=photos[2] 
        stt='Please speak.....'
        l3=Label(l1,image=img,borderwidth=0)
        l3.place(x=385,y=0)
        w = Canvas(l1, width=735, height=130, bd=0, highlightthickness=0, relief='ridge')
        w.place(x=388,y=231)
        l5=Label(w,image=photos[5],text=stt,font='bold 18',borderwidth=0,compound=CENTER)
        l5.place(x=-1,y=-1)
        time_calc+=1000
        root1.after(time_calc,lambda:l())
        def l():
            global listen_text
            r=sr.Recognizer()
            r.energy_threshold=2000
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                try:
                    audio = r.listen(source)
                    listen_text=listen_text+r.recognize_google(audio, language='en-in')
                except sr.UnknownValueError:
                    speak('Sorry I could not recognize what you said...Can you say that again?')
                    listen1()
                listen_text=listen_text.lower()



    def get_name():
        
        global name
        global time_calc
        global listen_text
        start=int(datetime.datetime.now().strftime('%S'))
        root1.after(time_calc+1000,lambda: speak('What is your name?'))
        end=int(datetime.datetime.now().strftime('%S'))
        time_calc+=3000
        start=int(datetime.datetime.now().strftime('%S'))
        root1.after(time_calc, lambda:listen1())
        end=int(datetime.datetime.now().strftime('%S'))
        time_calc+=end-start+2000
        name1=listen_text.split()
        for i in name1:
            if(i!='myself' and i!='my' and i!='is' and i!='name' and i!='am' and i!='i' and i!='this' and i!='mera' and i!='hai' and i!='naam'):
               name=name+" "+i
        speak('Hello!'+name)
        speak('Is that your name to be printed on the bill?')
        listen1()
        if (listen_text=='yes' or listen_text=='haan' or 'y' in listen_text ):
            name=name
        elif(listen_text=='no' or 'n' in listen_text):
            speak('Can you speak your name again?Please..')
            get_name()
            





    
    x = root1.winfo_screenwidth()
    y = root1.winfo_screenwidth()
    root1.title('Main')
    root1.geometry('%dx%d' % (x, y))
    #root1.wm_attributes('-fullscreen','true')
    
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
    img=photos[2]

    l1 =Label(root1, image=photos[0])
    l1.place(x=0,y=0)

    l2=Label(root1, image=photos[1],borderwidth=0)
    l2.place(x=172,y=500)
    
    l3=Label(l1,image=img,borderwidth=0)
    l3.place(x=385,y=0)
    w = Canvas(l1, width=735, height=130, bd=0, highlightthickness=0, relief='ridge')
    w.place(x=388,y=231)
    l5=Label(w,image=photos[5],text='Welcome to the Cafe...',font='bold 18',borderwidth=0,compound=CENTER)
    l5.place(x=-1,y=-1)
    time=datetime.datetime.now()
    hour=int(time.strftime('%H'))
    time_calc=0
    start=int(datetime.datetime.now().strftime('%S'))
    if hour<12:
        root1.after(1000, lambda: speak("Good Morning"))
    elif hour<16:
        root1.after(1000, lambda: speak('Good Afternoon'))
    else:
        root1.after(1000, lambda: speak('Good Evening'))
    end=int(datetime.datetime.now().strftime('%S'))
    time_calc+=end-start+2500
    start=int(datetime.datetime.now().strftime('%S'))
    root1.after(time_calc,lambda:speak("You are welcome to The AI Cafe...I am Jarvis...I\'ll help you with your order..."))
    end=int(datetime.datetime.now().strftime('%S'))
    time_calc+=end-start+2000
    root1.after(time_calc,lambda:get_name())
    
    
    
    root1.mainloop()
    

    
        

if __name__=='__main__':
    a()