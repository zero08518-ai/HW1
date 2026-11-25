
import sqlite3
import requests

connection = sqlite3.connect("weather.sl3", 5)

cur = connection.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS weather (
    date_time TEXT,
    temperature REAL
);
""")

url = "https://api.open-meteo.com/v1/forecast?latitude=51.4982&longitude=31.2893&current=temperature_2m&timezone=Europe%2FKyiv"

response = requests.get(url)
data = response.json()

date_time = data["current"]["time"]
temperature = data["current"]["temperature_2m"]

cur.execute(
    "INSERT INTO weather (date_time, temperature) VALUES (?, ?);",
    (date_time, temperature)
)

connection.commit()

cur.execute("SELECT date_time, temperature FROM weather;")

res = cur.fetchall()
print(res)

connection.close()
