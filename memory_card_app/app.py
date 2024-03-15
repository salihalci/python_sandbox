from flask import Flask,render_template,request
import sqlite3
import questionsdao

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save",methods=["GET","POST"])
def save():
    question = request.form.get('question')
    answer = request.form.get('answer')
    msg=""
  
    print(id)
    if request.method=="POST":
        if  len(question.strip()) != 0 and len(answer.strip()) != 0:
            print(f"question {question} and answer {answer}")
            questionsdao.savequestion(question=question,answer=answer)
            msg="Record Created!"
        else:
            print("pass")
            msg="Record is not created!"


    return render_template("save.html",msg=msg)


@app.route("/list")
def list():
    questions = questionsdao.retrieveQuestions()
    return render_template("list.html",questions=questions)


@app.route("/update")
def update():
    id = request.args.get('Edit')
    questionsdao.retrieveQuestion(id=id)
    
    return render_template("update.html")


@app.route("/delete")
def delete():
    msg=""
    id = request.args.get('Delete')
    print(f"delete id is: {id}")
    msg= questionsdao.deleteQuestion(id)
    
    return render_template("delete.html",msg=msg)


if __name__=="__main__":
    app.run(debug=True)
    
