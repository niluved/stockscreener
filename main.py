import loading_services as ls
import ticker_list as tl


# main function
def main():
    # Carica i dati 'info' dal file o scarica i nuovi dati da yfinance
    df = ls.load_or_download_info(tl.tickers)
    print(df.head())


# Chiamata alla funzione principale
if __name__ == '__main__':
    main()
