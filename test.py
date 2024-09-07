import yfinance as yf

stock = yf.Ticker("A2A.MI")


# Ottieni il balance sheet trimestrale
income_statement_trim = stock.quarterly_financials

# Stampa tutte le voci che sono all'interno di income_statement_trim
for key, value in income_statement_trim.items():
    print(f"Voce: {key}, Valore: {value}")

print(income_statement_trim.keys())


'''
# Seleziona la voce 'Net Debt'
net_debt = income_statement_trim['Net Debt']

# Stampa la voce 'Net Debt' per tutti i quarter
for quarter, value in net_debt.items():
    print(f"Quarter: {quarter}, Net Debt: {value}")

'''
