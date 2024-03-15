from flask import Flask,render_template,request
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


@app.route("/update",methods=["POST","GET"])
def update():
    id = request.args.get('Edit')
    question =questionsdao.retrieveQuestion(id=id)
  
    print(question)
    
    if request.method=="GET":
        return render_template("update.html",question=question)
    
    if request.method =="POST": #comes from update button of submit form
        id = request.form.get("id")
        question = request.form.get("question")
        answer = request.form.get("answer")
        msg = questionsdao.updateQuestion(id=id,question=question,answer=answer) 
        return render_template("update.html",msg=msg, question=question)
    
    


@app.route("/delete",methods=["POST","GET"])
def delete():
    msg=""
    id = request.args.get('Delete')
    print(f"delete id is: {id}")
    msg= questionsdao.deleteQuestion(id)
    
    return render_template("delete.html",msg=msg)


if __name__=="__main__":
    app.run(debug=True)
    
