from flask import Flask, render_template, request

# jab public variable bnanay hoon tu without 'underscore' bnatay hain ???
# oop say related kuch batain chal rahi theen yahan
app = Flask(__name__)


# ye home page ban gaya, or home oage par kia show krna hay vo ban gaya
@app.route("/")
# @: generator. see generator vs decorator
# /: means user will write nothing. landing pg bnay ga
# jesay hi server pr click kia jaye tu os bnday ko kahan lay k aan hay
def home():
    name = input("Kindly tell me your name: ")
# sending data from backend to frontend
    return render_template("home.html", data = {'name': name})
# hmaisha response (eg: here it was 'name'), json format/dictionary ki form main jaye ga



# ye aik naya route/address/page ban gaya or os page par kia show krna hay vo bhi
@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        

        return render_template("about.html", result = {"sum": result})
    else:
        return render_template("about.html", result = {"sum": ""})


if __name__ == "__main__":
    
    app.run(debug = True, port = 5000)
# by defaulr port = 5000 hi hoti hay, aap chaho tu isay change bhi kr sktay ho yahan say