from flask import Flask, render_template
import pandas as pd

app = Flask("Website")

stations = pd.read_csv("/Users/eseoseodion/Documents/Python 2023/Visual Code/UDEMY_PROJECTS/app-6(i)/small_data/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]
@app.route("/") # Domain name/homepage
def home():
    return render_template("home.html", data=stations.to_html())

# return the temperature for a particular date
@app.route("/api/v1/<station>/<date>") # '<>' this denotes that the user can enter any value
def about(station, date):
    filename = "/Users/eseoseodion/Documents/Python 2023/Visual Code/UDEMY_PROJECTS/app-6(i)/small_data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df["    DATE"] == date]['   TG'].squeeze() / 10 # to get the value of TG that corresponds to the data 1860-01-05
    return {"station": station,
            "date": date,
            "temperature": temperature}

# return the data for a particular station
@app.route("/api/v1/<station>")
def all_data(station):
    filename = "/Users/eseoseodion/Documents/Python 2023/Visual Code/UDEMY_PROJECTS/app-6(i)/small_data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20,  parse_dates=['    DATE'])
    result = df.to_dict(orient="records") # changes dict into a list of multiple dicts, with eahc dict representing a row of the dataframe
    return result

# return the data for a particular year
@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "/Users/eseoseodion/Documents/Python 2023/Visual Code/UDEMY_PROJECTS/app-6(i)/small_data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient='records') # filter out the data for a particular year and changes dict into a list of multiple dicts, with eahc dict representing a row of the dataframe
    return result

if __name__ == "__main__":
    app.run(debug=True) # run the Flask app


