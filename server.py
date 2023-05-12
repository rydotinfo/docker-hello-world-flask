from flask import Flask

PORT = 8000

if (2023 % 400 == 0) and (2023 % 100 == 0):
    print("{0} is a leap year".format(2023))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (2023 % 4 ==0) and (2023 % 100 != 0):
    print("{0} is a leap year".format(2023))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(2023))

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
