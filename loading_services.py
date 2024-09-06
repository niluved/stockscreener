import os
import pandas as pd
import get_financials as gf

# carica i dati 'info' dal file o scarica i nuovi dati da yfinance


def load_or_download_info(tickers, filename='ticker_info_data.xlsx'):
    if os.path.exists(filename):
        while True:
            choice = input(
                f"Il file {filename} esiste già. Vuoi usare i dati esistenti (E) o scaricare nuovi dati (N)? ").lower()
            if choice in ['e', 'n']:
                break
            print("Scelta non valida. Per favore, inserisci 'E' per usare i dati esistenti o 'N' per scaricare nuovi dati.")

        if choice == 'e':
            print(f"Caricamento dei dati generali dal file {filename}...")
            return pd.read_excel(filename)

    print("Scaricamento di nuovi dati...")
    all_data = []
    counter = 0
    for ticker in tickers:
        try:
            data = gf.get_info_data(ticker)
            all_data.append(data)
            # stampa percentuale di progressione
            counter += 1
            percentuale = round(counter / len(tickers) * 100, 1)
            print(f"loading {str(percentuale)}%")
        except Exception as e:
            print(f"Errore nell'ottenere i dati per {ticker}: {e}")

    df = pd.DataFrame(all_data)

    df.to_excel(filename, index=False, engine='openpyxl')
    print(f"I nuovi dati generali sono stati salvati in {filename}")
    return df

# carica i dati 'conto economico trimestrale' dal file o scarica i nuovi dati da yfinance


def load_or_download_quarterly_income_statement(tickers, filename='ticker_quarterly_income_data.xlsx'):
    if os.path.exists(filename):
        while True:
            choice = input(
                f"Il file {filename} esiste già. Vuoi usare i dati esistenti (E) o scaricare nuovi dati (N)? ").lower()
            if choice in ['e', 'n']:
                break
            print("Scelta non valida. Per favore, inserisci 'E' per usare i dati esistenti o 'N' per scaricare nuovi dati.")

        if choice == 'e':
            print(f"Caricamento dei dati trimestrali dal file {filename}...")
            return pd.read_excel(filename)

    print("Scaricamento di nuovi dati...")
    all_data = []
    counter = 0
    for ticker in tickers:
        try:
            data = gf.get_quarterly_income_statement(ticker)
            # Usiamo extend invece di append perché ora riceviamo una lista di dizionari
            all_data.extend(data)
            # stampa percentuale di progressione
            counter += 1
            percentuale = round(counter / len(tickers) * 100, 1)
            print(f"loading {str(percentuale)}%")
        except Exception as e:
            print(f"Errore nell'ottenere i dati per {ticker}: {e}")

    df = pd.DataFrame(all_data)

    # Riordina le colonne come richiesto
    columns_order = ['Ticker', 'Long name', 'Industry', 'Sector', 'FullTimeEmployees',
                     'Country', 'Currency', 'Exchange', 'Website', 'QUARTER', 'YEAR']
    remaining_columns = [col for col in df.columns if col not in columns_order]
    df = df[columns_order + remaining_columns]

    df.to_excel(filename, index=False, engine='openpyxl')
    print(f"I nuovi dati trimestrali sono stati salvati in {filename}")
    return df
