from flask import Flask, jsonify, render_template_string
import datetime

app = Flask(__name__)

@app.route("/report")
def report():
    today = datetime.datetime.today().strftime("%Y. %B %d.")
    data = {
        "status": "ok",
        "date": today,
        "price": "$295.17",
        "change": "3.68%",
        "recommendation": "A részvény emelkedik. Ha van, érdemes lehet tartani. Vásárlással várj, amíg stabilizálódik.",
        "closing": "Gondolok rád, és drukkolok, hogy szép napod legyen, Barbi! 💛"
    }

    # HTML sablon a GPT-nek
    html = f"""
    <h1>Tesla – Napi jelentés</h1>
    <p><strong>Dátum:</strong> {data['date']}</p>
    <p><strong>Záróár:</strong> {data['price']}</p>
    <p><strong>Napi változás:</strong> {data['change']}</p>
    <p><strong>Ajánlás:</strong> {data['recommendation']}</p>
    <p><strong>Üzenet Barbinak:</strong> {data['closing']}</p>
    """

    return render_template_string(html)

@app.route("/json")
def json_report():
    # Ezt is megtartjuk a technikai megoldásokhoz
    return jsonify({
        "status": "ok",
        "date": "2025. June 06.",
        "price": "$295.17",
        "change": "3.68%",
        "recommendation": "A részvény emelkedik. Ha van, érdemes lehet tartani. Vásárlással várj, amíg stabilizálódik.",
        "closing": "Gondolok rád, és drukkolok, hogy szép napod legyen, Barbi! 💛"
    })
