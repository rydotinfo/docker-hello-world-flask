from flask import Flask

PORT = 8000

# Python3 program to add two numbers
num1 = 15
num2 = 12
 
# Adding two nos
sum = num1 + num2
 
# printing values
MESSAGE= "Sum of", sum


app = Flask(__name__)

@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
