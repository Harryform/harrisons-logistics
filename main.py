import tkinter.font
from tkinter import *
import random
import pandas

# set up for main tkinter window
root = Tk()
root.title("Harrison's Logistics")
root.geometry('550x400+500+160')
root.config(padx=10, pady=10, bg='white', width=550, height=400)
root.maxsize(width=550, height=500)

canvas = Canvas(width=550, height=500, bg='white', highlightthickness=0)


# creates a new list for items to be picked by giving a bin location and item number for each
def new_list():

    bin_location = pandas.read_csv("bin_locations.txt", header=None)
    random_location = bin_location.sample()
    clean_bin_location = random_location.to_string(justify='left', index=False, header=False)
    location_info.config(text=clean_bin_location)

    item_def = pandas.read_csv("item_names.txt", header=None)
    random_item = item_def.sample()
    clean_random_item = random_item.to_string(justify='left', index=False, header=False)
    item_info.config(text=clean_random_item)

    item_sku_num = pandas.read_csv("item_numbers.txt", header=None)
    random_item_num = item_sku_num.sample()
    clean_random_number = random_item_num.to_string(justify='left', index=False, header=False)
    item_sku.config(text=clean_random_number)

    random_qty_pick = random.randint(30, 69)
    number_to_pick.config(text=random_qty_pick)

    random_qty_box = random.randint(1, 12)
    number_in_box.config(text=random_qty_box)

    number_picked.delete(0, END)
    number_picked.insert(0, 0)


# creates keyboard interface for application
def touch_keyboard():
    # set up for keyboard popup window
    keyboard_gui = Toplevel()
    keyboard_gui.title("Keyboard")
    keyboard_gui.config(padx=8, pady=8, bg='white')
    keyboard_gui.geometry('900x200+350+400')
    keyboard_gui.resizable(0, 0)

    # retrieves text entered with keyboard and inserts into bin location field
    def get_text():
        text = entry.get()
        entry_field_input.insert(0, text)
        keyboard_gui.withdraw()

    # capitalizes entry so it matches bin location
    def auto_capitalize(*args):
        var.set(var.get().upper())

    def select(value):

        if value == "<-":
            char = len(entry.get()) - 1
            entry.delete(char, END)

        elif value == " SPACE ":
            entry.insert(END, ' ')

        elif value == "CLOSE":
            keyboard_gui.withdraw()

        elif value == "ENTER":
            entry.get()

        elif value == "CLEAR":
            entry.delete(0, END)

        elif value == "SHIFT":
            var = entry.get()
            var.trace_add('write', auto_capitalize)

        else:
            entry.insert(END, value)

    buttons = [
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-', '7', '8', '9', '-',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '4', '5', '6', '+',
        'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?', 'SHIFT', '1', '2', '3', '0',
        ' SPACE ', 'CLOSE', 'ENTER', 'CLEAR',
    ]

    var = StringVar(keyboard_gui)
    entry = Entry(keyboard_gui, width=50, fg='black', bg='white', highlightbackground='grey', textvariable=var)
    entry.grid(row=1, columnspan=15)

    var_row = 2
    var_column = 0

    for button in buttons:
        command = lambda x=button: select(x)
        if button != " SPACE ":
            if button != "ENTER":
                if button != "CLEAR":
                    if button != "SHIFT":
                        if button != "CLOSE":
                            Button(keyboard_gui, text=button, width=1, highlightbackground='white', fg='black',
                                   activebackground='black', activeforeground='white', relief='raised', padx=4,
                                   pady=4, bd=4, command=command).grid(row=var_row, column=var_column)

        if button == " SPACE ":
            Button(keyboard_gui, text=button, width=12, highlightbackground='white', fg='black',
                   activebackground='black', activeforeground='white', relief='raised', padx=4,
                   pady=4, bd=4, command=command).grid(row=6, column=0, columnspan=15)

        if button == "CLEAR":
            Button(keyboard_gui, text=button, width=1, highlightbackground='white', fg='black',
                   activebackground='black', activeforeground='white', relief='raised', padx=4,
                   pady=4, bd=4, command=command).grid(row=2, column=var_column - 2)

        if button == "ENTER":
            Button(keyboard_gui, text=button, width=1, highlightbackground='white', fg='black',
                   activebackground='black', activeforeground='white', relief='raised', padx=4,
                   pady=4, bd=4, command=get_text).grid(row=3, column=var_column - 1)

        if button == "CLOSE":
            Button(keyboard_gui, text=button, width=1, highlightbackground='white', fg='black',
                   activebackground='black', activeforeground='white', relief='raised', padx=4,
                   pady=4, bd=4, command=command).grid(row=4, column=var_column)

        if button == "SHIFT":
            Button(keyboard_gui, text=button, width=1, highlightbackground='white', fg='black',
                   activebackground='black', activeforeground='white', relief='raised', padx=4,
                   pady=4, bd=4, command=auto_capitalize).grid(row=var_row, column=var_column)

        var_column += 1
        if var_column > 14 and var_row == 2:
            var_column = 0
            var_row += 1
        if var_column > 14 and var_row == 3:
            var_column = 0
            var_row += 1


def next_item():
    new_list()


# confirms your choice to skip
def skip_answer():
    answer = Toplevel()
    answer.title('Skip?')
    answer.config(padx=40, pady=40, bg='white', width=400, height=300)
    answer.geometry('300x200+600+300')

    master = Canvas(answer, width=400, height=300, bg='white', highlightthickness=0)

    answer_label = Label(answer, text='Are you sure you want to skip?', bg='white', fg='black')
    answer_label.grid(column=0, row=0, columnspan=2)

    def yes():
        answer.destroy()
        skip_reason()

    def no():
        answer.destroy()

    answer_yes_img = PhotoImage(master=master, file='/Users/harryform/Downloads/answer_yes.png')
    answer_yes = Button(answer, image=answer_yes_img, highlightbackground='white', bg='white',
                        borderwidth=0, command=yes)
    answer_yes.grid(column=0, row=1, pady=(30, 0))

    answer_no_img = PhotoImage(master=master, file='/Users/harryform/Downloads/answer_no.png')
    answer_no = Button(answer, image=answer_no_img, highlightbackground='white', bg='white',
                       borderwidth=0, command=no)
    answer_no.grid(column=1, row=1, pady=(30, 0))

    answer.mainloop()


# asks the reason for skipping to the next item in the pick list with a drop down options list
def skip_reason():

    skip_win = Toplevel()
    skip_win.title('Skip')
    skip_win.config(padx=30, pady=30, bg='white', width=300, height=300)
    skip_win.geometry('300x300+600+200')

    picture = Canvas(skip_win, width=300, height=300, bg='white', highlightthickness=0)

    question_label = Label(skip_win, text='What is the reason for skipping?', bg='white', fg='black')
    question_label.grid(column=0, row=0, columnspan=2, pady=(0, 30))

    def submit():
        skip_win.destroy()
        next_item()

    def cancel():
        skip_win.destroy()

    options = [
        '',
        'Bin is Empty',
        'Damaged Items',
        'Wrong Items',
        'Not Enough Items',
    ]

    variable = StringVar(skip_win)
    variable.set(options[0])

    menu = OptionMenu(skip_win, variable, *options)
    menu.grid(column=0, row=1, columnspan=2, padx=(15, 0), pady=(10, 30))
    menu.config(bg='white', fg='black')

    submit_img = PhotoImage(master=picture, file='/Users/harryform/Downloads/submit_button.png')
    submit = Button(skip_win, image=submit_img, highlightbackground='white', bg='white',
                    borderwidth=0, command=submit)
    submit.grid(column=0, row=2, pady=(20, 20))

    cancel_img = PhotoImage(master=picture, file='/Users/harryform/Downloads/cancel_button.png')
    cancel = Button(skip_win, image=cancel_img, highlightbackground='white', bg='white',
                    borderwidth=0, command=cancel)
    cancel.grid(column=1, row=2, pady=(20, 20))

    skip_win.mainloop()


# function designed to simulate scanning a label to pick the current item in the pick list
def scan():
    num_picked = int(number_picked.get())
    if entry_field['text'] == 'Label Scan':
        if num_picked < number_to_pick['text'] - 1:
            num_picked += 1
            number_picked.delete(0, END)
            number_picked.insert(0, num_picked)
        else:
            next_item()
            entry_field.config(text='Bin Location:')
    else:
        wrong_bin_error.config(text='Please verify bin first!')


# confirms bin location entry so you can start scanning the current item in the pick list
def submit_entry():
    location = location_info['text']
    entry = str(entry_field_input.get()).upper()
    label_entry = "Label Scan"
    if entry == location:
        entry_field.config(text=label_entry)
        entry_field_input.delete(0, END)
        wrong_bin_error.config(text='')
    else:
        entry_field_input.delete(0, END)
        wrong_bin_error.config(text='Incorrect Bin Location!')


# Label section for main window
item = Label(text='Item Descrip:', bg='white', fg='black')
item.grid(pady=2, column=0, row=0)

item_info = Label(text='', bg='white', fg='black')
item_info.grid(pady=2, padx=(0, 70), column=1, row=0, columnspan=4, stick='ew')

item_num = Label(text='Item Number:', bg='white', fg='black')
item_num.grid(pady=2, column=0, row=1)

item_sku = Label(text='', bg='white', fg='black')
item_sku.grid(pady=2, column=1, row=1, padx=(0, 30))

fc = Label(text='FC:', bg='white', fg='black')
fc.grid(pady=2, column=0, row=2)

fc_answer = Label(text='Yes', bg='white', fg='black')
fc_answer.grid(pady=2, column=1, row=2, padx=(20, 70))

zone = Label(text='Zone:', bg='white', fg='black')
zone.grid(pady=2, column=0, row=3)

bin_label = Label(text='Bin Loc.:', bg='white', fg='black')
bin_label.grid(pady=2, column=0, row=4)

location_info = Label(text='', bg='white', fg='black')
location_info.grid(column=1, row=4, padx=(20, 30))

box_quantity = Label(text='Qty/Pack:', bg='white', fg='black')
box_quantity.grid(pady=2, column=0, row=5)

number_in_box = Label(text='', bg='white', fg='black')
number_in_box.grid(column=1, row=5, padx=(20, 83))

pick_quantity = Label(text='Qty to Pick:', bg='white', fg='black')
pick_quantity.grid(pady=2, column=0, row=6)

number_to_pick = Label(text='', bg='white', fg='black')
number_to_pick.grid(column=1, row=6, padx=(20, 83))

already_picked = Label(text='Qty Picked:', bg='white', fg='black')
already_picked.grid(pady=2, column=0, row=7)

entry_field = Label(text='Bin Location:', bg='white', fg='black')
entry_field.grid(column=0, row=8)

wrong_bin_error = Label(text='', bg='white', fg='red')
wrong_bin_error.grid(column=0, columnspan=2, row=9, pady=(10, 30))

# Input section for main window
number_picked = Entry(width=5, fg='black', bg='white', highlightbackground='grey')
number_picked.grid(column=1, row=7, padx=(0, 44), pady=2)
number_picked.insert(0, 0)

entry_field_input = Entry(width=10, fg='black', bg='white', highlightbackground='grey')
entry_field_input.grid(column=1, row=8)

# Button section for main window
back_button_img = PhotoImage(file="/Users/harryform/Downloads/back_button.png")
back_button = Button(root, image=back_button_img, highlightbackground='white', bg='white', fg='white',
                     command=root.destroy, borderwidth=0)
back_button.grid(column=0, row=10, padx=(15, 2))

scan_button_img = PhotoImage(file="/Users/harryform/Downloads/scan_button.png")
scan_button = Button(root, image=scan_button_img, highlightbackground='white', bg='white', fg='white',
                     command=scan, borderwidth=0)
scan_button.grid(column=1, row=10)

keyboard_img = PhotoImage(file="/Users/harryform/Downloads/keyboard_button.png")
keyboard_button = Button(image=keyboard_img, highlightbackground='white', fg='white',
                         borderwidth=0, command=touch_keyboard)
keyboard_button.grid(column=2, row=10, padx=(0, 30))

submit_button_img = PhotoImage(file="/Users/harryform/Downloads/submit_button.png")
submit_button = Button(root, image=submit_button_img, highlightbackground='white', fg='white',
                       borderwidth=0, command=submit_entry)
submit_button.grid(column=3, row=10, padx=(0, 20))

skip_button_img = PhotoImage(file="/Users/harryform/Downloads/skip_button.png")
skip_button = Button(root, image=skip_button_img, highlightbackground='white', bg='white', fg='white',
                     borderwidth=0, command=skip_answer)
skip_button.grid(padx=(0, 50), column=4, row=10)


new_list()
root.mainloop()
