from tkinter import *
from time import time
import global_vars
from tkinter import messagebox as mb

def show_help():
    mb.showerror(message = "tap the button")
def show_records():
    records1 = ""
    with open("clicker_records.txt", "r", ) as f:
        record_list = f.readlines()
        records1 = "".join(record_list)
    mb.showerror(message = records1 )
def show_about():
    pass
def cliker():

    def check_record (name: str,score: int) -> None:
        with open("clicker_records.txt", "r+", ) as f:
            record_list = f.readlines()

            new_record = [line.strip("\n").split(";") for line in record_list]

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

        if global_vars.cc == 0 :
            global_vars.sc = time()
        if time()-global_vars.sc<3:
            global_vars.cc += 1
            lbl.config(text=f"tap\n{global_vars.cc}")
        else:
            confirm = mb.showerror(message=f"хватит жать кнопку\nваш результат{global_vars.cc}")
            if confirm == "ok":
                global_vars.sc = time()
                global_vars.cc == 0
                confirm ==0
                lbl.config(text=f"tap\n{0}")



    root =  Tk()
    root.geometry("600x600")
    root.resizable(False,False)
    icon_img = PhotoImage(file="164659.png")
    root.iconphoto(False,icon_img)
    """
    создаём понель меню под заголовком
    """
    mainmenu = Menu(root)
    root.config(menu = mainmenu)
     #mainmenu.add_command(label = "info",command = root.)
     #mainmenu.add_command(label="Exit",command = root.destroy)
    filemenu = Menu(mainmenu,tearoff = 0)
    filemenu.add_command(label="Exit", command=root.destroy)
    refmenu = Menu(mainmenu,tearoff = 1)
    refmenu.add_command(label="Help", command=show_help)
    refmenu.add_command(label="records", command=show_records)
    refmenu.add_command(label="about", command=show_about)

    mainmenu.add_cascade(label = "file", menu=filemenu)
    mainmenu.add_cascade(label="referc", menu=refmenu)

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






