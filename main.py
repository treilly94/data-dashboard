from flask import Flask, render_template
from scripts import plots as plt

app = Flask(__name__)


@app.route('/')
def index():
    plot1 = plt.get_timeseries()
    plot2 = plt.get_week()
    return render_template('index.html', plot1=plot1, plot2=plot2)


if __name__ == '__main__':
    app.run(debug=True)
