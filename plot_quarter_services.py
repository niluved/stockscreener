import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

# Funzione per ottenere i dati dell'EBITDA per un ticker specifico,
# leggendo i dati dal file 'ticker_quarterly_income_data.xlsx'.
# Il metodo restituisce un dataframe con le seguenti colonne:
# - RefQuarter: il trimestre dell'anno a cui si riferiscono i dati
# - EBITDA: il valore dell'EBITDA per il trimestre specifico
# Il dataframe viene ordinato in base al trimestre.


def get_ebitda_data(ticker):
    df = pd.read_excel('ticker_quarterly_income_data.xlsx')
    df = df[df['Ticker'] == ticker]
    df = df[df['YEAR'] == datetime.now().year]
    df = df[['RefQuarter', 'EBITDA']]
    df = df.sort_values('RefQuarter')
    # stampa il df per controllo
    print(df)
    return df

# crea un grafico di tipo 'candlestick' per l'EBITDA


def plot_ebitda(df):
    fig = go.Figure(data=[go.Candlestick(x=df['RefQuarter'],
                                         open=df['EBITDA'],
                                         high=df['EBITDA'],
                                         low=df['EBITDA'],
                                         close=df['EBITDA'])])

    fig.update_layout(title='EBITDA per quarter',
                      yaxis_title='EBITDA')

    fig.show()
