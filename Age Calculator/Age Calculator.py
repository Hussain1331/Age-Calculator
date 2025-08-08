import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry
import calendar

def calculate_age():
    try:
        dob_date = dob_entry.get_date()
        dob = datetime(dob_date.year, dob_date.month, dob_date.day)
        today = datetime.today()

        age_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        age_months = (today.year - dob.year) * 12 + (today.month - dob.month)
        if today.day < dob.day:
            age_months -= 1
        age_days = (today - dob).days

        next_birthday_year = today.year if (today.month, today.day) < (dob.month, dob.day) else today.year + 1
        next_birthday = datetime(next_birthday_year, dob.month, dob.day)
        weekday = calendar.day_name[next_birthday.weekday()]

        result_age.config(text=f"AGE : {age_years} Years")
        result_months.config(text=f"MONTHS : {age_months} Months")
        result_days.config(text=f"DAYS : {age_days}")
        result_birthday.config(text=f"Next Birthday On: {weekday}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x350")
root.resizable(False, False)

root.iconbitmap("cake.ico")
root.configure(bg="lightblue")

tk.Label(root, text="AGE CALCULATOR", font=("Arial", 16, 'bold')).pack(pady=10)
tk.Label(root, text="Select your Date of Birth:", font=("Arial", 10)).pack()
dob_entry = DateEntry(root, width=20, font=("Arial", 12), year=2005,
                      background='lightblue', foreground='black', borderwidth=2,
                      date_pattern='dd/mm/yyyy')
dob_entry.pack(pady=5)

tk.Button(root, text="CALCULATE AGE", command=calculate_age,
          bg="lightblue", font=("Arial", 12)).pack(pady=10)

result_age = tk.Label(root, text="", font=("Arial", 12))
result_age.pack(pady=5)
result_months = tk.Label(root, text="", font=("Arial", 12))
result_months.pack(pady=5)
result_days = tk.Label(root, text="", font=("Arial", 12))
result_days.pack(pady=5)
result_birthday = tk.Label(root, text="", font=("Arial", 12, 'italic'))
result_birthday.pack(pady=10)

root.mainloop()
