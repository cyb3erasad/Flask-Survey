from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:cyb3r%40db%280101%29@localhost/survey_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class SurveyResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    q1 = db.Column(db.String(200))
    q2 = db.Column(db.String(200))
    q3 = db.Column(db.String(200))
    q4 = db.Column(db.String(200))
    q5 = db.Column(db.String(200))

with app.app_context():
    db.create_all()


@app.route("/")
def survey():
    return render_template("survey.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    q1 = request.form["q1"]
    q2 = request.form.getlist("q2")
    q2=", ".join(q2)
    q3 = request.form["q3"]
    q4 = request.form["q4"]
    q5 = request.form["q5"]

    response = SurveyResponse(
        name=name,
        email=email,
        q1=q1,
        q2=q2,
        q3=q3,
        q4=q4,
        q5=q5
    )
    db.session.add(response)
    db.session.commit()

    return redirect("/success")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/results")
def results():
    all_responses = SurveyResponse.query.all()
    return render_template("results.html", responses = all_responses)


if __name__ == "__main__":
    app.run(debug=True)