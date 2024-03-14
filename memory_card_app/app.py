from flask import Flask,render_template,request
import sqlite3
import questionsdao

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/editquestion",methods=["GET","POST"])
def editquery():
    question = request.form.get('question')
    answer = request.form.get('answer')

    if request.method=="POST":
        if  len(question.strip()) != 0 and len(answer.strip()) != 0:
            print(f"question {question} and answer {answer}")
            questionsdao.savequestion(question=question,answer=answer)
        else:
            print("pass")


    return render_template("editquery.html")


if __name__=="__main__":
    app.run(debug=True)
    
