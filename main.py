from flask import Flask, render_template

from scripts import plots as plt
from scripts.googleAPI import SheetsAPI

app = Flask(__name__)

sheets_api = SheetsAPI()

# Sheet IDs
car_sheet = ""
music_sheet = ""
work_sheet = ""


@app.route("/")
def index():
    plot1 = plt.get_timeseries()
    plot2 = plt.get_week()
    return render_template("index.html", plot1=plot1, plot2=plot2)


@app.route("/car")
def car():
    return render_template("car.html")


@app.route("/music")
def music():
    return render_template("music.html")


@app.route("/work")
def work():
    return render_template("work.html")


@app.route("/fitness")
def fitness():
    return render_template("fitness.html")


if __name__ == '__main__':
    app.run(debug=True)
