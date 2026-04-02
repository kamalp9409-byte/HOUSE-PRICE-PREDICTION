from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = "kamal123"


# ------------ USER DATABASE (file based) ---------------
def save_user(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")


def check_user(username, password):
    if not os.path.exists("users.txt"):
        return False

    with open("users.txt", "r") as f:
        for line in f:
            user, pwd = line.strip().split(",")
            if username == user and password == pwd:
                return True
    return False



# ------------ PRICE PREDICTION ---------------
def predict_price(area, bedrooms, age, bathrooms, metro, parking, rating, city):
    
    city_factor = {
        "Delhi": 1.3,
        "Mumbai": 1.5,
        "Bangalore": 1.2,
        "Pune": 1.1
    }

    base = (area * 2500) + (bedrooms * 400000) + (bathrooms * 150000)
    base -= (age * 10000)
    base -= (metro * 2000)

    if parking == "yes":
        base += 50000

    base += (rating * 10000)

    multiplier = city_factor.get(city, 1)

    return round(base * multiplier, 2)



# ---------------- ROUTES -----------------

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def do_login():
    username = request.form["username"]
    password = request.form["password"]

    if check_user(username, password):
        session["user"] = username
        return redirect("/home")
    else:
        return render_template("login.html", error="Invalid username/password!")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def do_register():
    username = request.form["username"]
    password = request.form["password"]

    save_user(username, password)
    return render_template("login.html", success="Account created! Please login.")


@app.route("/home")
def home():
    if "user" not in session:
        return redirect("/")
    return render_template("index.html")


# PREDICTION ROUTE
@app.route("/predict", methods=["POST"])
def predict():

    area = int(request.form["area"])
    bedrooms = int(request.form["bedrooms"])
    age = int(request.form["age"])
    bathrooms = int(request.form["bathrooms"])
    metro = int(request.form["metro"])
    parking = request.form["parking"]
    rating = int(request.form["rating"])
    city = request.form["city"]

    price = predict_price(area, bedrooms, age, bathrooms, metro, parking, rating, city)

    return render_template("result.html", price=price)



if __name__ == "__main__":
    app.run(debug=True)
