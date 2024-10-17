from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

alphaVantageApiKey = "429VFIKMPXLL67PU"
baseUrl = "https://www.alphavantage.co/query"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/stock/<symbol>")
def getStockData(symbol):
    url = f"{baseUrl}?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={alphaVantageApiKey}"
    print(f"Generated URL: {url}")  # Debugging
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data from Alpha Vantage"}), response.status_code
    data = response.json()
    if "Time Series (5min)" not in data:
        return jsonify({"error": "Invalid symbol or data not available"}), 400
    return render_template("stock.html", symbol=symbol, stock_data=data)

@app.route("/test")
def test():
    return "Test route is working"

if __name__ == '__main__':
    app.run(debug=True, port=5002)
