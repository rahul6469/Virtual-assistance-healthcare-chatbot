from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form.get('input_text')
    # your existing code goes here to process the input_text
    output = 'output text'  # replace with your actual output

    return jsonify({'output': output})


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        input_text = request.form['input_text']
        # Your code to process the input and generate output goes here
        output = "Your output goes here"
        return output
    return '''
        <form method="post">
            <label for="input_text">Enter your input:</label>
            <input type="text" name="input_text">
            <br>
            <input type="submit" value="Submit">
        </form>
    '''
