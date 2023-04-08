import tkinter,sqlite3

conn = sqlite3.connect('memorycards.db')
c=conn.cursor()

record = c.execute("SELECT  * FROM questions where id=1")


fetched_record = record.fetchone()

#controls is record properly
if fetched_record is not None:
    print(fetched_record[1])



#print(record[0])
conn.commit()
conn.close()
window = tkinter.Tk()

window.title("Memory Cards!")
window.minsize(width=500,height=300)




lbl_Question=tkinter.Label(text=fetched_record[1],
                           font=("Arial",14,"bold")
                           )
lbl_Question.pack()


btn_ShowAnswer = tkinter.Button(text="Answer",
                                font=("Arial",14,"bold"))
btn_ShowAnswer.pack()



lbl_Answer=tkinter.Label(text="Answer Label",
                           font=("Arial",14,"bold")
                           )
lbl_Answer.pack()


window.mainloop()