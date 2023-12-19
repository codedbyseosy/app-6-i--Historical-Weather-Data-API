from flask import Flask, render_template

app = Flask("Website")

@app.route("/") # Domain name/homepage
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>") # '<>' this denotes that the user can enter any value
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}

if __name__ == "__main__":
    app.run(debug=True) # run the Flask app



