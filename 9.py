import tkinter as tk
import random

def lodicka(x, y):
    plachta = random.randint(-3, 3)
    plachta_id = canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    boat_id = canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)
    return boat_id,plachta_id


plachty = []
boats = []
def start_race():
    global boats,goal_line
    for i in range(1, 16):
        boat_id,plachta_id = lodicka(50, 50 + i * 60)
        boats.append((boat_id,plachta_id))

    goal_line = canvas.create_line(650, 0, 650, 800, fill="red", width=2)
    move_boats()

def move_boats():
    global boats,goal_line,plachty
    for boat_id, plachty_id in boats:
        movement = random.randint(1, 10)
        canvas.move(boat_id, movement, 0)
        canvas.move(plachty_id, movement, 0)
        if canvas.coords(boat_id)[2] >= 650:
            canvas.delete(goal_line)
            canvas.create_text(350, 400, text=f"Lodička č. {boat_id} vyhrala!", font=("Helvetica", 20), fill="blue")
            return

    else:
        canvas.after(100, move_boats)


root = tk.Tk()
root.title("Preteky lodičiek")

canvas = tk.Canvas(root, width=700, height=800)
canvas.pack()

start_button = tk.Button(root, text="Štart", command=start_race)
start_button.pack()

root.mainloop()


