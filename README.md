**Introduction**

The Stock Market Tracker is a web application that fetches and displays real-time stock market data using the Alpha Vantage API. Users can input a stock symbol, and the application will retrieve the latest stock price information.

This is the first project I have created in Python. 

**Features**

  Fetch real-time stock market data using Alpha Vantage.
  
  User-friendly interface built with Flask.
  
  Display stock information such as symbol, price, and other relevant data.
  
  Extensible for adding more features like historical stock data and graphs.

**Installation**

To get the project up and running locally, follow these steps:

  1. Clone the repository:
     
       git clone https://github.com/your-username/StockMarketTracker.git
     
       cd StockMarketTracker
  
  2. Set up a virtual environment (optional but recommended):
     
       python3 -m venv venv
     
       source venv/bin/activate  # On Windows: venv\Scripts\activate

  3. Install the required dependencies:
     
       pip install -r requirements.txt

  4. Set up your environment variables:
     
     You need to add your Alpha Vantage API key in an .env file or export it directly in your environment:
     
       Create a .env file in the project root:
     
         ALPHA_VANTAGE_API_KEY=your_api_key_here

  5. Run the application:
    
      flask run
   
      The app will be available at http://127.0.0.1:5000/.

**Usage**

  Open your browser and go to http://127.0.0.1:5000/.
  
  Enter a stock symbol (e.g., AAPL for Apple, TSLA for Tesla) in the input field.
  
  The app will display the stock’s latest price information retrieved from the Alpha Vantage API.
  
  API Integration
  
  This application integrates with the Alpha Vantage API. You will need an API key to fetch stock market data. Visit the Alpha Vantage website to obtain your key.

**Technologies**

  Flask: Web framework
  
  Python: Core programming language
  
  HTML/CSS: For the front-end interface
  
  Alpha Vantage API: For stock market data
  
  dotenv: For handling environment variables
