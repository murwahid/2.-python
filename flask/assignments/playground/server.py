from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello"

#PLAY FUNCTION
@app.route('/play')
def display():
    return render_template('blueBoxes.html')

#PLAY W/ NUMBERS FUNCTION
#AMAZING LOOP
@app.route('/play/<int:num>/<string:boxColor>')
def display_boxes(num,boxColor):
    times = int(num)
    return render_template('blueBoxes.html', num=num,boxColor=boxColor)

#! MUST BE AT THE BOTTOM ---------------
if __name__ == "__main__":
    app.run(debug=True)
