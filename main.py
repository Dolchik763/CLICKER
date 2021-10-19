from tkinter import *
from time import time
from tkinter import messagebox as mb

def cliker():
    counter = 0
    start = time()
    def check_record (name: str,score: int) -> None:
        with open("clicker_records.txt", "r+", ) as f:
            record_list = f.readlines()

            new_record = [line.strip("\n").split(" ") for line in record_list]

            for index, line_num in enumerate(new_record):
                if score > int(line_num[2]):
                    new_record.insert(index, [str(index + 1), name, str(score)])
                    break
            for line_num in range(index + 1, len(new_record)):
                new_record[line_num][0] = str(line_num + 1)
            record_list = [" ".join(i) + "\n" for i in new_record]
            f.seek(0)
            f.writelines(record_list)
            print(new_record)
    def click():
        nonlocal counter,start
        if time()-start<3:
            counter += 1
            lbl.config(text=f"tap\n{counter}")
        else:
            confirm = mb.showerror(message=f"хватит жать кнопку\nваш результат{counter}")
            if confirm == "ok":
                start = time()
                counter == 0
                confirm ==0
                lbl.config(text=f"tap\n{0}")



    root =  Tk()
    root.geometry("600x600")
    root.resizable(False,False)
    icon_img = PhotoImage(file="164659.png")
    root.iconphoto(False,icon_img)

    btn = Button(text = "tap"
                 ,font = ("Comic Sans",15),
                 width = 10,
                 height = 2,
                 bg = "orange",
                 fg = "black",
                 relief=RAISED,
                 bd = 10,
                 command = click
                 )
    lbl = Label(text = "tap\n0"
                 ,font = ("Comic Sans",15),
                 width = 12,
                 height = 2,
                 bg = "orange",
                 fg = "black",
                justify = CENTER
                )

    lbl.pack()
    btn.pack()
    root.mainloop()
if __name__ == "__main__":
     cliker()






