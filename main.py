from flask import Flask, render_template
import plots as plt

app = Flask(__name__)


@app.route('/')
def index():
    plot = plt.get_timeseries()
    return render_template('index.html', plot=plot)


if __name__ == '__main__':
    app.run(debug=True)
