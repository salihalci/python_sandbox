import tkinter

window = tkinter.Tk()

window.title("Memory Cards!")
window.minsize(width=500,height=300)



#Write core here!
lbl_Question=tkinter.Label(text="Question Label",
                           font=("Arial",14,"bold")
                           )
lbl_Question.pack()

btn_ShowAnswer = tkinter.Button(text="Answer",
                                font=("Arial",14,"bold"))
btn_ShowAnswer.pack()
#Write core here!
lbl_Answer=tkinter.Label(text="Answer Label",
                           font=("Arial",14,"bold")
                           )
lbl_Answer.pack()


window.mainloop()