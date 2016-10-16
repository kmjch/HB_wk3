from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""
    return render_template("index.html")

@app.route("/application")
def application():
    """Show an application form."""
    return render_template("application-form.html")

@app.route('/thanks')
def show_thanks():
    """Thanks the applicant."""
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    salaryreq = request.args.get("salaryreq")
    choosejob = request.args.get("choosejob")

    return render_template("thanks.html", firstname=firstname, lastname=lastname,
                           salaryreq=salaryreq, choosejob=choosejob)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
