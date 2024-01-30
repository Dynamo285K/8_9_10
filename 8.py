import tkinter as tk
import random

root = tk.Tk()
alph = 'ABCDEFGHIJ'
canvas = tk.Canvas(root,width=1000,height=300,bg='white')
canvas.pack()

dict = {}
for i in range(10):
    x = canvas.create_oval(i*100,100,100+i*100,25,fill='blue')
    dict[alph[i]] = x
for i in range(10):
    canvas.create_text(i*100+50,60,text=alph[i],fill='black',font= 'Arial 20')
print(dict)

puknuty = random.choice(list(dict.values()))
print(puknuty)

zle_kliky = []
def on_canvas_click(event):
    x, y = event.x, event.y
    item_ids = canvas.find_overlapping(x, y, x, y)
    if item_ids[0] == puknuty:
        print('nasiel si ho')
        print('predtym si klikol aj tieto',zle_kliky)
        zle_str = ''.join(zle_kliky)
        canvas.create_text(500,230, text=f'Nasiel si ho a bolo to {alph[item_ids[0]-1]}', font='Arial 20 ',fill='Blue')
        canvas.create_text(500,260, text=f'Predtym si klikol aj na {zle_str}', font='Arial 20 ',fill='red')
    else:
        zle_kliky.append(alph[item_ids[0]-1])


canvas.bind("<Button-1>", on_canvas_click)

root.mainloop()
