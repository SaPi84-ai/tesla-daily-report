from flask import Flask, jsonify
import requests
import datetime

app = Flask(__name__)

API_KEY = "5c054bd7f8174d6792a14bee77227fbe"  # Twelve Data kulcs

def get_tesla_data():
    url = f"https://api.twelvedata.com/quote?symbol=TSLA&apikey={API_KEY}"
    response = requests.get(url)
    try:
        data = response.json()
        if "close" not in data or "percent_change" not in data:
            return None
        return {
            "price": float(data["close"]),
            "percent_change": float(data["percent_change"]),
            "date": datetime.date.today().strftime("%Y. %B %d.")
        }
    except Exception as e:
        return None

def create_report():
    tesla = get_tesla_data()
    if not tesla:
        return {
            "status": "error",
            "message": "Nem sikerült lekérni a Tesla adatokat."
        }
    
    price = tesla["price"]
    change = tesla["percent_change"]
    date = tesla["date"]

    if change <= -5:
        recommendation = "A részvény ma sokat esett. Ha hiszel a hosszú távban, akár érdemes lehet venni – de csak óvatosan."
    elif -5 < change < 2:
        recommendation = "Most nyugodtabb a piac. Nem kell kapkodni, de ha van részvényed, tartsd meg."
    else:
        recommendation = "A részvény emelkedik. Ha van, érdemes lehet tartani. Vásárlással várj, amíg stabilizálódik."

    closing = "Gondolok rád, és drukkolok, hogy szép napod legyen, Barbi! 💛"

    return {
        "status": "ok",
        "date": date,
        "price": f"${price:.2f}",
        "change": f"{change:.2f}%",
        "recommendation": recommendation,
        "closing": closing
    }

@app.route("/")
def root():
    return "Tesla Daily Report API – működik."

@app.route("/report")
def report():
    return jsonify(create_report())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
