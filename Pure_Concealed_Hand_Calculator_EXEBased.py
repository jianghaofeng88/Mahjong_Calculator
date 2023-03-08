from tkinter import *

# Core functions


def sublist(a, b):
    c = b.copy()
    for item in a:
        if item in c:
            c.remove(item)
        else:
            return False
    return True


def find_quetou(hand14):
    result = []
    for i in range(10):
        if(sublist([i, i], hand14)):
            result.append(i)
    return result


def hu(h):
    huxing = []
    quetou_list = find_quetou(h)
    for quetou in quetou_list:
        huxing.append([quetou, quetou])
        hand12 = h.copy()
        hand12.remove(quetou)
        hand12.remove(quetou)
        hand12.sort()

        while(1):
            i = hand12[0]
            if(sublist([i, i, i], hand12)):
                hand12.remove(i)
                hand12.remove(i)
                hand12.remove(i)
                huxing.append([i, i, i])
            elif(sublist([i, i + 1, i + 2], hand12)):
                hand12.remove(i)
                hand12.remove(i + 1)
                hand12.remove(i + 2)
                huxing.append([i, i + 1, i + 2])
            else:
                huxing = []
                break
            if(len(hand12) == 0):
                return True, huxing
    return False, []


def callback(P):
    error3.place_forget()
    current_hand.place_forget()
    winnings.place_forget()
    window.focus_get().config(fg='black', highlightthickness=1, highlightcolor='blue', highlightbackground=original_highlightbackground, validatecommand=(vcmd, '%P'))
    if (str.isdigit(P) and int(P) in range(1, 10)) or str(P) == "":
        return True
    else:
        error3.place(x=window_x / 2, y=450, anchor="center")
        window.focus_get().config(highlightthickness=2, highlightcolor='red')
        return False


def clear():
    error1.place_forget()
    error2.place_forget()
    error3.place_forget()
    current_hand.place_forget()
    winnings.place_forget()
    for i in range(13):
        tiles[i].config(fg='black', highlightthickness=1, highlightcolor='blue', highlightbackground=original_highlightbackground)
        tiles[i].delete(0, 'end')
    tiles[0].focus_set()
    return


def calculate():
    error1.place_forget()
    error2.place_forget()
    error3.place_forget()
    current_hand.place_forget()
    winnings.place_forget()
    inspector = 0
    hand = []
    for i in range(13):
        tiles[i].config(fg='black', highlightthickness=0, highlightbackground=original_highlightbackground)
        if (tiles[i].get() == ""):
            tiles[i].config(highlightthickness=2, highlightbackground='red')
            inspector = 1
            error1.place(x=window_x / 2, y=450, anchor="center")
        elif(not(str.isdigit(tiles[i].get()) and int(tiles[i].get()) in range(1, 10))):
            tiles[i].config(highlightthickness=2, highlightbackground='red')
            inspector = 1
            error3.place(x=window_x / 2, y=450, anchor="center")
        else:
            hand.append(int(tiles[i].get()))

    if (inspector == 1):
        error1.place(x=window_x / 2, y=450, anchor="center")
        return

    for i in range(1, 10):
        indices = [n for n, x in enumerate(hand) if x == i]
        if len(indices) >= 5:
            error2.place(x=window_x / 2, y=450, anchor="center")
            for j in indices:
                tiles[j].config(fg='red', highlightthickness=2, highlightbackground='red')
            return

    assert(len(hand) == 13)
    hand.sort()
    current_hand.config(text=f"Current tiles on your hand are {hand}")
    current_hand.place(x=100, y=450)
    result = []
    winning_text = ""
    for i in range(1, 10):
        if (sublist([i, i, i, i], hand)):
            continue
        hu_or_not = hu(hand + [i])
        if (hu_or_not[0]):
            winning_text += (f"Winning tile is {i}, melds are {hu_or_not[1]}\n")
            result.append(i)
    if (result == []):
        winnings.config(text="No winning tiles!")
    else:
        winnings.config(text=winning_text)
    winnings.place(x=100, y=500)

    return


def leftKey():
    current = tiles.index(window.focus_get())
    if (current != 0):
        tiles[current - 1].focus_set()
    else:
        tiles[12].focus_set()


def rightKey():
    current = tiles.index(window.focus_get())
    if (current != 12):
        tiles[current + 1].focus_set()


# UI Window
# Window setup
window = Tk()
window.title('Mahjong Calculator')
window.geometry("1080x800+10+10")
window.update()
window_x = window.winfo_width()
window_y = window.winfo_height()
tile_height = 80
tile_width = 60
tile_y = 200

tile_locations = []
tile_locations.append(150)
for i in range(12):
    tile_locations.append(tile_locations[-1] + tile_width)

# Labels
head1 = Label(window, text="Mahjong Calculator for Winning Tiles on Pure Concealed Hand", font=("Arial", 20))
head2 = Label(window, text="Developed by Haofeng Jiang  |  June 06, 2022", font=("Arial", 12))
head3 = Label(window, text="-" * 120, font=("Arial", 16))
head4 = Label(window, text="Please enter the 13 tiles on your hand:", font=("Arial", 16))
head1.place(x=100, y=50)
head2.place(x=100, y=90)
head3.place(x=100, y=120)
head4.place(x=100, y=150)

error1 = Label(window, text="All 13 tiles should be entered!", fg='red', font=("Arial", 20))
error2 = Label(window, text="The same tile can only appear at most 4 times!", fg='red', font=("Arial", 20))
error3 = Label(window, text="Your input must be integers from 1 to 9 inclusive!", fg='red', font=("Arial", 20))

current_hand = Label(window, text="", font=("Arial", 16))
winnings = Label(window, text="", font=("Arial", 16))


# Entries and their validation
vcmd = window.register(callback)
tiles = []
for i in range(13):
    tiles.append(Entry(font=("Arial", 24), highlightthickness=1, highlightcolor='blue', justify='center', validate='all', validatecommand=(vcmd, '%P')))
    tiles[-1].place(x=tile_locations[i], y=tile_y, width=tile_width, height=tile_height)

original_highlightbackground = tiles[0].cget("highlightbackground")
tiles[0].focus_set()

# Buttons
calculate_btn = Button(window, text='Find the winning tiles!', font=("Arial", 16), command=calculate)
calculate_btn.place(x=window_x / 2, y=350, width=300, height=50, anchor="center")
clear_btn = Button(window, text='Clear all', font=("Arial", 16), command=clear)
clear_btn.place(x=870, y=700, width=120, height=40, anchor="center")

# Keyboard binding
window.bind('<Return>', lambda event: calculate())
window.bind('<Delete>', lambda event: clear())
window.bind('<Left>', lambda event: leftKey())
window.bind('<Right>', lambda event: rightKey())
for i in range(1, 10):
    window.bind(str(i), lambda event: rightKey())

window.mainloop()
