from tkinter import *
from os import system as start

exp_start = lambda: start("start explorer.exe")
cmd_start = lambda: start("start cmd.exe")
task_start = lambda: start("start taskmgr")
reg_start = lambda: start("start regedit")

def call_BSoD():
    #! Bsod
    BSoD = Toplevel(root)
    BSoD.config(bg="blue")
    BSoD.wm_attributes("-fullscreen", True)
    BSoD.wm_attributes("-topmost", True)
        
    BSoD_label = Label(
        BSoD,
        text=":( \nIt BSOD",
        bg="blue",
        fg="white",
        font=("Arial", 25, "bold")
    )
    BSoD_label.pack(expand=1)

root = Tk()

#! Root settings
root.geometry("600x400")
root.title("DesktopOs")
root.config(bg="#222222")
root.wm_attributes("-toolwindow", True)

#! Stage one: Create main menu
main_menu = Menu(root)

#^ Create sub-menu "Пуск"
pysk = Menu(main_menu)

#& Create sub-menu in menu "Пуск"
pysk_open_menu = Menu(pysk)

#* Add cascade to "Пуск"
main_menu.add_cascade(
    label="Пуск",
    menu=pysk,
)

#& Add cascade "Open..." in menu "Пуск"
pysk.add_cascade(
    label="Open...",
    menu=pysk_open_menu,
)
pysk.add_separator()

#~ Add commands to menu "Open..."
# Command "Explorer"
pysk_open_menu.add_command(label="Explorer", command=exp_start)
# Command "CMD"
pysk_open_menu.add_command(label="CMD", command=cmd_start)
# Command "Task manager"
pysk_open_menu.add_command(label="Task manager", command=task_start)
# Command "RegEdit"
pysk_open_menu.add_command(label="RegEdit", command=reg_start)

#& Add command "Call BSoD" in menu "Пуск"
pysk.add_command(
    label="Call BSoD",
    command=call_BSoD,
)

#^ Add command to main menu
main_menu.add_command(label="Выход", command=root.destroy)

#! Stage two: Create interface
#^ Explorer button
Button(
    text="Explorer",
    command=exp_start,
).pack(anchor="nw", ipadx=20, ipady=30, padx=20, pady=20)

#^ CMD button
Button(
    text="CMD",
    command=cmd_start,
).pack(anchor="nw", ipadx=27, ipady=30, padx=20)

#! End
root.config(menu=main_menu)
root.mainloop()
