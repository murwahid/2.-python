from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("checkerBoard.html")

# @app.route('/<color_1>')
# def display_color1(color_1):
#     return render_template("checkerBoard.html", color_1=color_1)

#TWO COLORS
@app.route('/<color_1>/<color_2>/<int:num_1>/<int:num_2>')
def display_color1(color_1, color_2,num_1,num_2):
    new_num1 = int(num_1)
    new_num2 = int(num_2)
    return render_template("checkerBoard.html", color_1=color_1, color_2=color_2, num_1=num_1,num_2=num_2)


# #8x4 board
# @app.route('/4')
# def display_four():
#     return render_template("index.html")

# # @app.route('/<int:x>/<int:y>')
# # def display_x_y(x,y):
# #     return ######## insert template here. 



# @app.route('/<int:x>/<int:y>/')
# def display_x_y(x,y):
#     new_x = int(x)
#     new_y = int(x)
#     return render_template("index.html",x=x,y=y)



# @app.route('/<int:x>/<int:y>/<color_1>/<color_2>')
# def display_x_y(x,y,color_1,color_2):
#     new_x = int(x)
#     new_y = int(y)
#     return render_template("index.html",x=new_x,y=new_y,color_1=color_1,color_2=color_2)


#! MUST BE AT THE BOTTOM ---------------
if __name__ == "__main__":
    app.run(debug=True)
