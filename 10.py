import tkinter as tk
root = tk.Tk()
fr = open('krizovka.txt','r',encoding='utf-8')

WIDTH = 1000
HEIGHT = 500
canvas = tk.Canvas(root,width= WIDTH, height = HEIGHT,bg='white')
canvas.pack()


pozicia = []
slovo = []
for i in fr:
    x = i.strip().split(' ')
    pozicia.append(int(x[0]))
    slovo.append(x[1])

print(slovo)
print(pozicia)
def vykreslenie_prazdnej():
    global dict,slovo,pozicia
    for i in range(len(slovo)):
        for j in range((len(slovo[0])-pozicia[i]),(len(slovo[0])-pozicia[i])+len(slovo[i])):
            if j-(len(slovo[0])-pozicia[i]) == pozicia[i]-1:
                canvas.create_rectangle(100+j*50,100+i*50,50+j*50,50+i*50,outline='black',fill='grey')
            else:
                canvas.create_rectangle(100+j*50,100+i*50,50+j*50,50+i*50,outline='black',fill='white')

def vykreslenie_plnej():
    global dict,slovo,pozicia
    for i in range(len(slovo)):
        for j in range((len(slovo[0])-pozicia[i]),(len(slovo[0])-pozicia[i])+len(slovo[i])):
            if j-(len(slovo[0])-pozicia[i]) == pozicia[i]-1:
                canvas.create_rectangle(600+j*50,100+i*50,550+j*50,50+i*50,outline='black',fill='grey')
                canvas.create_text(575+j*50,75+i*50,text=slovo[i][j-(len(slovo[0])-pozicia[i])])
            else:
                canvas.create_rectangle(600+j*50,100+i*50,550+j*50,50+i*50,outline='black',fill='white')
                canvas.create_text(575+j*50,75+i*50,text=slovo[i][j-(len(slovo[0])-pozicia[i])])
        # for g in range(len(slovo[i])):
        #     canvas.create_text(125+g*50,125+i*50,text=slovo[i][g])

vykreslenie_prazdnej()
vykreslenie_plnej()
root.mainloop()
