from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")


# @app.route('/about.html')
# def about_me():
#    return render_template('about.html')

# @app.route('/works.html')
# def work():
#    return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#    return render_template('contact.html')

# simply we can one function for all above single specficc functions

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as db:
        email = data['Email']
        sub = data['Subject']
        msg = data['Message']
        csvwriter = csv.writer(db, delimiter=',')
        csvwriter.writerow([email, sub, msg])


@app.route("/details_submit", methods=['POST', 'GET'])
def details_submit():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thanks.html")
        except:
            return "Data not saved to Database"
    else:
        return "Something Went Wrong... Try Again"
