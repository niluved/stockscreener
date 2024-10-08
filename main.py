import loading_services as ls
import ticker_list as tl
import plot_quarter_services as qs


# main function
def main():
    # Carica i dati 'info' dal file o scarica i nuovi dati da yfinance
    df_info = ls.load_or_download_info(tl.tickers)
    print(df_info.head())
    # stampa il numero di valori unici nella colonna Ticker rispetto al numero totale di ticker iniziali
    print(
        f"{df_info['Ticker'].nunique()} ticker scaricati / {len(tl.tickers)} ticker iniziali")

    # Carica i dati 'conto economico trimestrale' dal file o scarica i nuovi dati da yfinance
    df_income_trim = ls.load_or_download_quarterly_income_statement(tl.tickers)
    print(df_income_trim.head())
    # stampa il numero di valori unici nella colonna Ticker rispetto al numero totale di ticker iniziali
    print(
        f"{df_income_trim['Ticker'].nunique()} ticker scaricati / {len(tl.tickers)} ticker iniziali")

    # chiedo all'utente di scegliere un ticker
    ticker = ls.choose_ticker(tl.tickers)

    # stampo il grafico del trend di EBITDA
    df_ebitda_trend = qs.get_ebitda_data(ticker)
    qs.plot_ebitda(df_ebitda_trend)


# Chiamata alla funzione principale
if __name__ == '__main__':
    main()
