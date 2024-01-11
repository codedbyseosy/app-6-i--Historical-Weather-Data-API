from flask import Flask, render_template
import pandas as pd

app = Flask("Website")

@app.route("/") # Domain name/homepage
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>") # '<>' this denotes that the user can enter any value
def about(station, date):
    filename = "/Users/eseoseodion/Documents/Python 2023/Visual Code/UDEMY_PROJECTS/app-6(i)/small_data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df["    DATE"] == date]['   TG'].squeeze() / 10 # to get the value of TG that corresponds to the data 1860-01-05
    return {"station": station,
            "date": date,
            "temperature": temperature}

if __name__ == "__main__":
    app.run(debug=True) # run the Flask app


