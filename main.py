import requests
import datetime
import os

# 1. Tesla árfolyam lekérése
def get_tesla_price():
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=TSLA"
    response = requests.get(url)
    data = response.json()
    quote = data["quoteResponse"]["result"][0]
    return quote["regularMarketPrice"], quote["regularMarketChangePercent"]

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
    rec = get_recommendation(change)
    change_str = f"{change:.2f}%"
    
    report = f"""TESLA – Napi összefoglaló
📅 {today}

💵 Aktuális árfolyam: ${price}
📊 Napi változás: {change_str}

💬 Ajánlás:
{rec}
"""
    return report

# 4. Tesztfutás (Render.com futtatáskor ez fog lefutni)
if __name__ == "__main__":
    print(generate_report())
