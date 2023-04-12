import tkinter
from tkinter import Entry, Text

from prompt_toolkit.key_binding.bindings.named_commands import self_insert

window = tkinter.Tk()

window.title("Memory Cards!")
window.minsize(width=500,height=300)

lbl_Question=tkinter.Label(text="Question Label",
                           font=("Arial",14,"bold")
                           )
lbl_Question.pack()

def btn_showAnswerClicked():
    print("Clicked")
    print(txt_input.get())
    lbl_Answer.config(text=txt_input.get()) # change text when button clicked.
    lbl_Question.config(text=txt_box.get("1.0","2.100"))

btn_ShowAnswer = tkinter.Button(text="Answer",
                                font=("Arial",14,"bold"),
                                command=btn_showAnswerClicked
                                )
btn_ShowAnswer.pack()


lbl_Answer=tkinter.Label(text="Answer Label",
                           font=("Arial",14,"bold")
                           )
lbl_Answer.pack()

#Simple text input
txt_input = Entry(width=50)
txt_input.insert(0,"Sample Text") # add default text
txt_input.pack()

#Text Entry box
txt_box = Text(background="yellow",width=20,height=2)
txt_box.focus()
txt_box.pack()


window.mainloop()