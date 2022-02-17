from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("mainpage.html")

@app.route("/about")
def about():
    return render_template("about/_0_about.html")

@app.route("/about/details")
def ad():
    return render_template("about/_1_mainabout.html")

@app.route("/about/details/<type>")
def type(type):
    if type == "love":
        return render_template("about/love.html")
    elif type == "core":
        return render_template("about/core.html")
    elif type == "details":
        return render_template("about/details.html")
     
@app.route("/skills")
def skills():
    return render_template("skills/_0_skills.html")

@app.route("/wp")
def wp():
    return render_template("wp/_0_wp.html")

app.run(debug=True)