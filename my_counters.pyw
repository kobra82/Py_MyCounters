from tkinter import *
from datetime import date, datetime

def conmon():
    max_balance=50
    current_balance=float(first_counter_entry.get())
    start_date=date(datetime.now().year,datetime.now().month,13)
    today_date=date.today()
    current_period=(today_date-start_date).days+1
    if current_period < 0:
        current_period+=30
    going=float(max_balance/30)*current_period
    net=round((going-current_balance),2)
    first_counter_label2=Label(frame1, text="Active Balance EU: "+str(net))
    first_counter_label2.grid(row=3, column=0, padx=10, sticky="WE")

def balmon():
    max_balance=-600
    current_balance=float(second_counter_entry.get())
    start_date=date(datetime.now().year,1,1)
    end_date=date(datetime.now().year,12,31)
    today_date=date.today()
    days_by_period=(end_date-start_date).days+1
    current_period=(today_date-start_date).days+1
    going=(int(max_balance)/days_by_period)*current_period
    net=round((current_balance-going),2)
    third_counter_label2=Label(frame2, text="Active Balance EU: "+str(net))
    third_counter_label2.grid(row=3, column=1, padx=10, sticky="WE")

root=Tk()
root.resizable(False, False)
root.title("Gestione Contatori")
frame1=LabelFrame(root, text="Cell Internet", padx=10, pady=5)
frame1.grid(row=0, column=0)
frame2=LabelFrame(root, text="Money", padx=10, pady=5)
frame2.grid(row=0, column=1)

first_counter_entry=Entry(frame1)
first_counter_entry.grid(row=1, column=0, padx=10, pady=5, sticky="WE")
first_counter_entry.focus()
first_counter_button=Button(frame1, text="Calcola", command=conmon)
first_counter_button.grid(row=2, column=0, padx=10, pady=10, sticky="WE")
first_counter_label2=Label(frame1, text="")
first_counter_label2.grid(row=3, column=0, padx=10, sticky="WE")

second_counter_entry=Entry(frame2)
second_counter_entry.grid(row=1, column=1, padx=10, pady=5, sticky="WE")
second_counter_button=Button(frame2, text="Calcola", command=balmon)
second_counter_button.grid(row=2, column=1, padx=10, pady=10, sticky="WE")
second_counter_label2=Label(frame2, text="")
second_counter_label2.grid(row=3, column=1, padx=10, sticky="WE")

root.mainloop()
