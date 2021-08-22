from tkinter import *


i=0
e=0
initial_texts={}
end_texts={}
window = Tk()
window.title("Dissapearing text")

#A function wich compares the present text with the one written 5 seconds ago. If it is the same text, then deletes text.
def compare_text():
    global e, initial_texts
    end_texts[e]=area.get("1.0", "end-1c")
    if initial_texts[e]==end_texts[e]:
        area.delete("1.0", "end-1c")
    e += 1





#Function bind on any key
def func(event):
    global initial_texts, i
    #Each key press will make a new entry in the dictionary
    initial_texts[i]=area.get("1.0", "end-1c")
    i += 1
    #Waits 5 seconds for every key press
    window.after(5000, compare_text)

window.bind('<Key>', func)



area=Text(window, height=20, width=150)
area.pack()

window.mainloop()