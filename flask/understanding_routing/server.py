from flask import Flask, render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/hello')
def hello():
    return render_template('index.html')


@app.route('/say/<name>')
def say_name(name):
    is_num = False
    try:
        int(name)
        print("*******")
        print(f"successful there is a number {name}")
        return f"Please enter a string/name"
    except:
        print("*******")
        print(f"unsuccessful we have string {name}")
        print("********")
        print(type(name))
        return f"Hi {name}!"


@app.route('/repeat/<word>/<multiple>')
def repeat(word,multiple):
    try:
        print("*******")
        int(word)
        print("*******")
        print(f"successful there is a number {word}")
        return f"Please enter a string/word"
    except:
        print("Word is word.")
        try:
            return word*int(multiple)
        except:
            return f"please enter a number since you entered a string. It was {multiple}"
            

    



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


