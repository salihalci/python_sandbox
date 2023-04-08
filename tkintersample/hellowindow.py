import tkinter

window = tkinter.Tk()

window.title("Memory Cards!")
window.minsize(width=500,height=300)




lbl_Question=tkinter.Label(text="Question Label",
                           font=("Arial",14,"bold")
                           )
lbl_Question.pack()


def btn_showAnswerClicked():
    print("Clicked")

btn_ShowAnswer = tkinter.Button(text="Answer",
                                font=("Arial",14,"bold"),
                                command=btn_showAnswerClicked
                                )
btn_ShowAnswer.pack()



lbl_Answer=tkinter.Label(text="Answer Label",
                           font=("Arial",14,"bold")
                           )
lbl_Answer.pack()


window.mainloop()