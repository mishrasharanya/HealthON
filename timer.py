from tkinter import *
import datetime
import time


def timer(duration):
	while True:
		
		current=datetime.datetime.now()
		now=current.strftime("%H:%M:%S")
		date=current.strftime("%d/%m/%Y")
		
		if now==duration:
			print("NEXT WORKOUT")
			
			break
		
def time():
	duration=f"{hour.get()}:{min.get()}:{sec.get()}"
	timer(duration)

workout_timer=Tk()

workout_timer.title("WORKOUT TIMER")
workout_timer.geometry("400x200")
time_format=Label(workout_timer, text="Enter time in 24 hour format!",fg='red',bg='black',font='Arial').place(x=60,y=120)
addTime=Label(workout_timer,text='hour min sec',font=60).place(x=110)
set_timer=Label(workout_timer,text="Enter end time of workout",fg='blue',relief='solid',font=("Helevetica",7,'bold')).place(x=0,y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

h_time=Entry(workout_timer,textvariable=hour,bg='pink',width=15).place(x=125,y=30)
m_time=Entry(workout_timer,textvariable=min,bg='pink',width=15).place(x=150,y=30)
s_time=Entry(workout_timer,textvariable=sec,bg='pink',width=15).place(x=210,y=30)

submit=Button(workout_timer,text='SET TIMER',fg='red',width=10,command=time).place(x=110,y=70)

workout_timer.mainloop()


