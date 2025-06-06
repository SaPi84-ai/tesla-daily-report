import requests
import datetime
import os

# 1. Tesla árfolyam lekérése, hibakezeléssel
def get_tesla_price():
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=TSLA"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    try:
        data = response.json()
        quote = data.get("quoteResponse", {}).get("result", [])
        if not quote:
            return None, None
        return quote[0]["regularMarketPrice"], quote[0]["regularMarketChangePercent"]
    except Exception as e:
        print("Hiba a Yahoo Finance válasz feldolgozása közben:", e)
        return None, None

# 2. Egyszerű ajánlás logika
def get_recommendation(change_percent):
    if change_percent <= -5:
        return "A részvény ma sokat esett. Ha hiszel a hosszú távban, akár érdemes lehet venni – de csak óvatosan."
    elif -5 < change_percent < 2:
        return "Most nyugodtabb a piac. Nem kell kapkodni, de ha van részvényed, tartsd meg."
    else:
        return "A részvény emelkedik. Ha van, érdemes lehet tartani. Vásárlással várj, amíg stabilizálódik."

# 3. Jelentés összeállítása, eseti hibaüzenettel
def generate_report():
    today = datetime.date.today().strftime("%Y. %B %d.")
    price, change = get_tesla_price()

    if price is None or change is None:
        return f"""TESLA – Napi összefoglaló
📅 {today}

⚠️ Nem sikerült lekérni a Tesla részvényadatokat. Lehet, hogy átmeneti probléma van az adatforrással.
Kérlek, próbáld újra később.
"""

    rec = get_recommendation(change)
    change_str = f"{change:.2f}%"

    return f"""TESLA – Napi összefoglaló
📅 {today}

💵 Aktuális árfolyam: ${price}
📊 Napi változás: {change_str}

💬 Ajánlás:
{rec}
"""

# 4. Futás
if __name__ == "__main__":
    print(generate_report())
