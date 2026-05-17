import yfinance as yf
from google import genai

client = genai.Client(api_key = "")

def get_stock_data(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)
        history = ticker.history(period="3y")
        if history.empty:
            print("No ticker found, is this correct?")
        current = history["Close"].iloc[-1]
        return history, current
    except Exception as e:
        return None, str(e)

def ai_projections(ticker_symbol, history, current_price):
    recent_trends = history.tail(20)[['Open', 'High', 'Low', 'Close', 'Volume']]
    prompt = f"Analyze {ticker_symbol}. Current price: ${current_price:.2f}. Trend:\n{recent_trends}\nProvide a projection for 2026 and 2027."
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    return response.text

stock_ticker = input('What is the stock ticker you want to project? ')
history, price = get_stock_data(stock_ticker)
if history is not None:
    print(f"Current Price: ${price:.2f}")
    analysis = ai_projections("GOOGL", history, price)
    print(analysis)
