import datetime
import tkinter as tk
from tkinter import messagebox


def get_weekday_for_july_14(year: int) -> str:
    date = datetime.date(year, 7, 14)
    return date.strftime("%A")


def show_weekday():
    year_text = year_entry.get().strip()
    if not year_text:
        messagebox.showwarning("입력 필요", "년도 입력이 필요합니다.")
        return

    try:
        year = int(year_text)
        weekday = get_weekday_for_july_14(year)
        result_label.config(text=f"{year}년 7월 14일은 {weekday}입니다.")
    except ValueError:
        messagebox.showerror("입력 오류", "올바른 숫자 형태의 년도를 입력해주세요.")
    except Exception as e:
        messagebox.showerror("오류", f"오류가 발생했습니다: {e}")


root = tk.Tk()
root.title("7월 14일 요일 찾기")
root.resizable(False, False)
root.geometry("320x160")

frame = tk.Frame(root, padx=16, pady=16)
frame.pack(fill="both", expand=True)

label = tk.Label(frame, text="년도를 입력하세요:", font=("Arial", 12))
label.pack(anchor="w")

year_entry = tk.Entry(frame, font=("Arial", 12))
year_entry.pack(fill="x", pady=(4, 10))

go_button = tk.Button(frame, text="확인", font=("Arial", 12), command=show_weekday)
go_button.pack(pady=(0, 10))

result_label = tk.Label(frame, text="", font=("Arial", 12), fg="blue")
result_label.pack()

root.mainloop()
