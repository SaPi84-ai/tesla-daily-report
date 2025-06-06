import requests
import datetime

# Twelve Data API kulcsod
API_KEY = "5c054bd7f8174d6792a14bee77227fbe"

# 1. Tesla árfolyam lekérése Twelve Data-ból
def get_tesla_price():
    url = f"https://api.twelvedata.com/quote?symbol=TSLA&apikey={API_KEY}"
    response = requests.get(url)
    try:
        data = response.json()
        if "price" not in data or "percent_change" not in data:
            return None, None
        price = float(data["price"])
        change = float(data["percent_change"])
        return price, change
    except Exception as e:
        print("Hiba az adatok feldolgozásakor:", e)
        return None, None

# 2. Egyszerű ajánlás logika
def get_recommendation(change_percent):
    if change_percent <= -5:
        return "A részvény ma sokat esett. Ha hiszel a hosszú távban, akár érdemes lehet venni – de csak óvatosan."
    elif -5 < change_percent < 2:
        return "Most nyugodtabb a piac. Nem kell kapkodni, de ha van részvényed, tartsd meg."
    else:
        return "A részvény emelkedik. Ha van, érdemes lehet tartani. Vásárlással várj, amíg stabilizálódik."

# 3. Jelentés összeállítása
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
