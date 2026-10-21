from tkinter import *
from tkinter import ttk
import psutil
from psutil._common import BatteryTime

vent = Tk()
vent.geometry("500x250")
vent.config(bg='black')

style = ttk.Style(vent)
style.layout('ProgressBarStyle',
            [('Horizontal.Progressbar.trough',{
                    'children':[('Horizontal.Progressbar.pbar',
                                {'side': 'right','sticky':'ns'})],
                                'sticky':'nsew'}),
                                ('Horizontal.Progressbar.label',{'sticky': ''})])


bar = ttk.Progressbar(vent,maximum=100, style='ProgressBarStyle')
bar.place(relx=0.5,rely=0.2,anchor=CENTER)

battery_life = Label(vent, font='arial 15 bold', bg= 'black', fg='white')
battery_life.place(relx=0.5,rely=0.5,anchor=CENTER)

def converTime(seconds):
    minutes, seconds =  divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return str(hours)+ ":"+ str(minutes) +":"+ str(seconds)

def getBatteryLife():
    battery = psutil.sensors_battery()
    bar['value'] = battery.percent
    style.configure('ProgressBarStyle', text=str(battery.percent)+"%")
    battery_left = converTime(battery.secsleft)
    if battery.secsleft == BatteryTime.POWER_TIME_UNLIMITED:
        battery_life['text'] = "Desconecta tu bateria y vuelve a ejecutar el codigo"
    elif battery.secsleft == BatteryTime.POWER_TIME_UNKNOWN:
        battery_life['text'] = "No se detecto la duracion de la bateria, porfavor ejecuta el codigo otra vez"
    else:
        battery_life['text']="Duracion de la bateria " + battery_left
        vent.after(1000,getBatteryLife)

getBatteryLife()

vent.mainloop()