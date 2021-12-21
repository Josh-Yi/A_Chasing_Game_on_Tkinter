import io
import tkinter as tk

import PIL
from PIL import ImageTk, Image
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from player import player
from env import environment

root = tk.Tk()
root.title('Chase 1.0')
# canvas = tk.Canvas(root, width=600, height=600)
# canvas.grid(columnspan=3)
my_text = tk.Label(root, text='Chase', bg='royalblue', font=('Arial', 20), width=30, height=2)
my_text.grid(column=0, row=0)
btn = tk.Button(root,text='New Game',command=lambda:func('x'),font = 'Raleway',bg='black',fg='blue',height=2,width=15)
btn.grid(column=0,row=1)
# canva = tk.Canvas(root,bg = 'white')

env = environment(40, 40)
env.add_trap(80)
player1 = player([1, 1], 2)
player2 = player([2, 2], 1)
env.add_player(player1)
env.add_player(player2)


def func(event):
    if event == 'x':
        pass
    else:
        if event.keysym == 'w':
            env.player_list[0].move([-1, 0])
        elif event.keysym == 'a':
            env.player_list[0].move([0, -1])
        elif event.keysym == 's':
            env.player_list[0].move([1, 0])
        elif event.keysym == 'd':
            env.player_list[0].move([0, 1])
        elif event.keysym == 'Up':
            env.player_list[1].move([-1, 0])
        elif event.keysym == 'Left':
            env.player_list[1].move([0, -1])
        elif event.keysym == 'Down':
            env.player_list[1].move([1, 0])
        elif event.keysym == 'Right':
            env.player_list[1].move([0, 1])

    x, end = env.check_state()
    if end:
        quit()
    plt.matshow(x)
    plt.axis('off')
    buffer_ = io.BytesIO()
    plt.savefig(buffer_, format="png", pad_inches=0.0, bbox_inches='tight')
    buffer_.seek(0)
    logo = Image.open(buffer_)
    logo = ImageTk.PhotoImage(logo)
    buffer_.close()
    logo_label = tk.Label(image=logo)
    logo_label.image = logo  # Necessary, rubbish tkinker
    logo_label.grid(columnspan=1, column=0, row=1)


def quit():
    import sys
    sys.exit()


root.bind('w', func)
root.bind('a', func)
root.bind('s', func)
root.bind('d', func)
root.bind('<Escape>', quit)
root.bind('<Left>', func)
root.bind('<Right>', func)
root.bind('<Up>', func)
root.bind('<Down>', func)

root.mainloop()
