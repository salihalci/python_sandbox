from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/editquery",methods=["GET","POST"])
def edıtquery():
    question = request.form.get('question')
    print(f"{question} and")
    
    return render_template("editquery.html")


if __name__=="__main__":
    app.run(debug=True)
