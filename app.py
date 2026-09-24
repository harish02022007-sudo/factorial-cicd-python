from flask import Flask
from factorial import factorial

app = Flask(__name__)

@app.route("/")
def home():
    return "Factorial Application is Running!"

@app.route("/factorial/<int:number>")
def calculate_factorial(number):
    result = factorial(number)
    return f"Factorial of {number} is {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)