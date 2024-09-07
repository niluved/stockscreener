import yfinance as yf
from datetime import datetime

# scarico i dati GENERALI  per il ticker specificato


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

# scarica i dati 'conto economico trimestrale' per il ticker specificato


def get_quarterly_income_statement(ticker):
    # Scarica i dati per il ticker specificato
    stock = yf.Ticker(ticker)

    # Ottieni i dati finanziari
    info = stock.info
    income_statement_trim = stock.quarterly_financials

    # Crea una lista per contenere tutti i dati trimestrali
    all_quarterly_data = []

    # Ottieni l'anno corrente
    current_year = datetime.now().year
    previous_year = current_year - 1

    # Itera attraverso tutti i trimestri disponibili
    for date in income_statement_trim.columns:
        # Filtra solo i dati dell'anno corrente e dell'anno precedente
        if date.year in [current_year, previous_year]:
            quarter = (date.month - 1) // 3 + 1
            year = str(date.year)[-2:]  # Get the last two digits of the year
            quarter_data = {
                # Add the new column
                'RefQuarter': f'Q{quarter}-{year}',
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
                # Calcola il trimestre basato sul mese
                'QUARTER': quarter,
                'YEAR': date.year,
            }

            # Aggiungi informazioni del bilancio (quarterly income statement) al dizionario 'quarter_data'
            for item in income_statement_trim.index:
                if item in income_statement_trim.index:
                    quarter_data[item] = income_statement_trim.loc[item, date]
                else:
                    quarter_data[item] = None

            all_quarterly_data.append(quarter_data)

    return all_quarterly_data
