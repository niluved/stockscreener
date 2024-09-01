import yfinance as yf


def get_info_data(ticker):

    # Scarica i dati per il ticker specificato
    stock = yf.Ticker(ticker)

    # Ottieni i dati finanziari chiave e le previsioni degli analisti
    info = stock.info

    # Crea un dizionario con i dati
    data = {
        # info anagrafiche
        'Ticker': ticker,
        'Long name': info.get('longName', None),
        'Industry': info.get('industry', None),
        'Sector': info.get('sector', None),
        'FullTimeEmployees': info.get('fullTimeEmployees', None),
        'Country': info.get('country', None),
        'Currency': info.get('currency', None),
        'Exchange': info.get('exchange', None),
        'Website': info.get('website', None),

        # info bilancio (ratio)
        'ROE': info.get('returnOnEquity', None),
        'ROA': info.get('returnOnAssets', None),
        'Beta': info.get('beta', None),
        'EnterpriseToEbitda': info.get('enterpriseToEbitda', None),
        'EnterpriseToRevenue': info.get('enterpriseToRevenue', None),
        'EPS': info.get('trailingEps', None),
        'P/E Ratio': info.get('trailingPE', None),

        # info bilancio (valori)
        'TotalRevenue': info.get('totalRevenue', None),
        'Ebitda': info.get('ebitda', None),
        'DebtToEquity': info.get('debtToEquity', None),
        'TotalDebt': info.get('totalDebt', None),
        'Free Cash Flow': info.get('freeCashflow', None),
        'Gross Margins': info.get('grossMargins', None),
        'Operating Margins': info.get('operatingMargins', None),
        'Profit Margins': info.get('profitMargins', None),

        # info finanziarie prezzo e valutazione
        'PreviousClose': info.get('previousClose', None),
        'PriceChange(YoY)': info.get('52WeekChange', None),
        'Dividend Yield': info.get('dividendYield', None),
        'ForwardEps': info.get('forwardEps', None),
        'ForwardPE': info.get('forwardPE', None),
        'RecommendationKey': info.get('recommendationKey', None),
        'MarketCap': info.get('marketCap', None),
        'EnterpriseValue': info.get('enterpriseValue', None),

        # info di trend
        'EarningsGrowth(YoY)': info.get('earningsGrowth', None),
        'EarningsQuarterlyGrowth': info.get('earningsQuarterlyGrowth', None),
        'Revenue Growth': info.get('revenueGrowth', None),

    }

    return data
