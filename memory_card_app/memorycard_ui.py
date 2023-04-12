import tkinter,sqlite3

# model class for questions---------------------------
class QuestionModel:
    question=""
    answer=""
    index=0

    def __init__(self,index,question,answer):
        self.question=question
        self.answer = answer
        self.index=index

# db operations--------------------------------------
conn = sqlite3.connect('./memorycards.db')
c=conn.cursor()

records = c.execute("SELECT  * FROM questions")

items = c.fetchall()

#print(record[0])
conn.commit()
conn.close()

#-----------------------------------------------------
question_list = [] # contains questions array

for x in items:
    temp_item = QuestionModel(x[0],x[1],x[2])
    question_list.append(temp_item)



question_index = 0  #initial

def increment_questionindex():
    return question_index+1

window = tkinter.Tk()
def set_answer():

    lbl_Answer['text']=question_list[question_index].answer
    
    # this is an other way to set label TODO test it 
    # lbl_Answer.config(text=fetched_record[2])
def next_activity():
    print("Next executed!")
    global question_index
    question_index +=1
    print(question_index)
    lbl_Question['text'] = question_list[question_index].question
    lbl_Answer['text']=""

window.title("Memory Cards!")
window.minsize(width=500,height=300)

lbl_Question=tkinter.Label(text=question_list[question_index].question,
                           font=("Arial", 14, "bold")
                           )
lbl_Question.pack()

btn_ShowAnswer = tkinter.Button(text="Answer",
                                font=("Arial", 14, "bold"),
                                command=set_answer
                                )
btn_ShowAnswer.pack()

lbl_Answer=tkinter.Label(text="Answer Label",
                           font=("Arial",14,"bold")
                           )
lbl_Answer.pack()

btn_Next = tkinter.Button(text="Next ->",
                                font=("Arial", 14, "bold"),
                                command=next_activity
                                )
btn_Next.pack()

window.mainloop()