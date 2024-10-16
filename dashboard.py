import streamlit as st
from datetime import datetime, date, timedelta
import pandas as pd


st.set_page_config(
    page_title="Stock Tracking Dashboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

#st.title("Stock Tracking Dashboard")
st.header("STOCK MARKET DASHBOARD")

st.write("MARKET RESEARCH")

url = "https://tradingterminal.com/"
st.write("Market tracker [link](%s)" % url)
    
url = "https://www.sectorspdrs.com/sectortracker"
st.write("SPDR Sectors [link](%s)" % url)

url = "https://docs.google.com/spreadsheets/d/1RpSHUC1gj3bnO4MdmoMgBwdCFIXsCQ-m21ESh63hVaI/edit?usp=sharing"
st.write("PANCHAYAT PORTFOLIO [link](%s)" % url)

option = st.sidebar.selectbox("Watchlist?", ('Daily_review', 'SPYQQ100', 'XLKSMHIGV',  'ETF'))

#timing = st.sidebar.selectbox("What Timeframe?", ('Hourly', 'Daily',  'Weekly', 'Multi'))

timing = st.radio( "Pick Timeframe", ('Hourly', 'Daily',  'Weekly', 'Multi'), horizontal=True)


if option == "SPYQQ100":
    with open('spyqqq100') as f:
        symbols=[i.strip() for i in f.readlines()]

    if timing == "Hourly":
        col1, col2 = st.columns(2)
        for stock in symbols:
            #st.write(stock)
            with col1:
                st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
            with col2:
                st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
    
    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")


    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")

    if timing == "Multi":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=m&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=5&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")

if option == "XLKSMHIGV":
    with open('xlksmhigv') as f:
        symbols=[i.strip() for i in f.readlines()]

    if timing == "Hourly":
        col1, col2 = st.columns(2)
        for stock in symbols:
            #st.write(stock)
            with col1:
                st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
            with col2:
                st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
    
    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")


    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")

    if timing == "Multi":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=m&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=5&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            

if option == "ETF":
    with open('etf') as f:
        symbols=[i.strip() for i in f.readlines()]
        symbols = list(dict.fromkeys(symbols))

    if timing == "Hourly":
        for stock in symbols:
            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")        

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")


    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")

    if timing == "Multi":
        for stock in symbols:
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=m&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=5&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=20&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=40&o[0][oc]=FF8F33C6&o[1][ot]=sma&o[1][op]=30&o[1][oc]=DCB3326D&o[2][ot]=sma&o[2][op]=10&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
            st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")


if option == "Daily_review":

    options = st.radio(
        'Pick the SPDR sectors',
        ['SPY', 'QQQ', 'XLK', 'SMH', 'IGV', 'CIBR', 'XLC', 'XLY', 'XLP', 'XLF', 'XLV', 'XLI', 'XLE', 'XLB', 'XLU', 'XOP', 'XHB', 'XME', 'TAN', 'BLOK', 'AIQ', 'PAVE', 'JETS', 'VTI' ], horizontal=True)
    
    #st.write('You selected:', options)
    
    
    #options = st.checkbox('XLK', 'XLC', 'XLY', 'XLP', 'XLF', 'XLV', 'XLI', 'XLE', 'XLB', 'XLU', 'XOP', 'XHB', 'XME')
    
    
    
    
    SPDR = {
        'SPY' : ['SPY', 'QQQ', 'DIA', 'IWO', 'VTI', 'XLK', 'SMH', 'IGV', 'CIBR', 'SKYY', 'FFTY', 'IBIT', 'RSP', 'QQQE', 'XLG', 'VGT', 'SDS', 'XLC', 'XLY', 'XLP', 'XLF', 'XLV', 'XLI', 'XLE', 'XLB', 'XLU', 'XOP', 'XHB', 'XME', 'XBI', 'KRE', 'IBB', 'XRT', 'TAN', 'BLOK', 'AIQ', 'PAVE', 'JETS',
                   'AAPL', 'AMZN', 'MSFT', 'GOOGL', 'META', 'NVDA', 'AMD', 'COST', 'TSLA', 'NFLX', 'AVGO', 'ADBE', 'ANET', 'ARM', 'ASML', 'LRCX', 'AMAT', 'PANW', 'LLY', 'TSM', 'NOW'],
        #'VTI' : ['XLC', 'XLY', 'XLP', 'XLF', 'XLV', 'XLI', 'XLE', 'XLB', 'XLU', 'XOP', 'XHB', 'XME', 'XBI', 'KRE', 'IBB', 'IBB', 'XRT', 'IYT', 'AIQ', 'BLOK', 'PAVE', 'JETS', 'IVV', 'IJH', 'IJR', 'IAG',
        #            'XLG', 'IDEV', 'IEMG', 'AGG', 'BND', 'TLT', 'GLD', 'SLV', 'TAN', 'ARKK'],
        'QQQ' : ['QQQ', 'TQQQ', 'SQQQ', 'SPY', 'VTI', 'SDS', 'AAPL', 'ABNB', 'ADBE', 'ADI', 'ADP', 'ADSK', 'AEP', 'AMAT', 'AMD', 'AMGN', 'AMZN', 'ANSS', 'ARM', 'ASML', 'AVGO', 'AZN', 'BIIB', 'BKNG', 'BKR', 'CCEP', 'CDNS', 'CDW', 'CEG', 'CHTR', 'CMCSA', 'COST', 'CPRT', 'CRWD', 'CSCO', 'CSGP', 'CSX', 'CTAS', 'CTSH', 'DASH', 'DDOG', 'DLTR', 'DXCM', 'EA', 'EXC', 'FANG', 'FAST', 'FTNT', 'GEHC', 'GFS', 'GILD', 'GOOG', 'GOOGL', 'HON', 'IDXX', 'ILMN', 'INTC', 'INTU', 'ISRG', 'KDP', 'KHC', 'KLAC', 'LIN', 'LRCX', 'LULU', 'MAR', 'MCHP', 'MDB', 'MDLZ', 'MELI', 'META', 'MNST', 'MRNA', 'MRVL', 'MSFT', 'MU', 'NFLX', 'NVDA', 'NXPI', 'ODFL', 'ON', 'ORLY', 'PANW', 'PAYX', 'PCAR', 'PDD', 'PEP', 'PYPL', 'QCOM', 'REGN', 'RIVN', 'ROST', 'SBUX', 'SMCI', 'SNPS', 'TEAM', 'TMUS', 'TSLA', 'TTD', 'TTWO', 'TXN', 'VRSK', 'VRTX', 'WBD', 'WDAY', 'XEL', 'ZS', 'ABBV', 'ABT', 'ACN', 'AIG', 'AMT', 'AXP', 'BA', 'BAC', 'BK', 'BLK', 'BMY', 'BRK-B', 'C', 'CAT', 'CL', 'COF', 'COP', 'CRM', 'CVS', 'CVX', 'DE', 'DHR', 'DIS', 'DOW', 'DUK', 'EMR', 'F', 'FDX', 'GD', 'GE', 'GM', 'GS', 'HD', 'IBM', 'JNJ', 'JPM', 'KO', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDT', 'MET', 'MMM', 'MO', 'MRK', 'MS', 'NEE', 'NKE', 'ORCL', 'PFE', 'PG', 'PM', 'RTX', 'SCHW', 'SO', 'SPG', 'T', 'TGT', 'TMO', 'UNH', 'UNP', 'UPS', 'USB', 'V', 'VZ', 'WFC', 'WMT', 'XOM'],
        'XLK': ['MSFT', 'AAPL', 'AVGO', 'NVDA', 'CRM', 'AMD', 'ADBE', 'ACN', 'ORCL', 'CSCO', 'QCOM', 'INTU', 'IBM', 'AMAT', 'INTC', 'NOW', 'TXN', 'MU', 'LRCX', 'ADI'],
        'XLC': ['META', 'GOOGL', 'GOOG', 'NFLX', 'VZ', 'T', 'TMUS', 'EA', 'DIS', 'CMCSA', 'CHTR', 'TTWO', 'WBD', 'OMC', 'LYV', 'IPG', 'NWSA', 'MTCH', 'FOXA', 'PARA'],
        'XLY': ['AMZN', 'TSLA', 'HD', 'MCD', 'LOW', 'BKNG', 'TJX', 'NKE', 'SBUX', 'CMG', 'ABNB', 'ORLY', 'MAR', 'AZO', 'HLT', 'F', 'GM', 'DHI', 'ROST', 'LULU'],
        'XLP': ['PG', 'COST', 'WMT', 'KO', 'PEP', 'PM', 'MDLZ', 'TGT', 'MO', 'CL', 'STZ', 'KMB', 'MNST', 'GIS', 'SYY', 'KR', 'DG', 'KVUE', 'ADM', 'EL'],
        'XLF': ['BRK-B', 'JPM', 'V', 'MA', 'BAC', 'WFC', 'SPGI', 'GS', 'AXP', 'PGR', 'C', 'MS', 'BLK', 'SCHW', 'CB', 'MMC', 'FI', 'BX', 'ICE', 'CME'],
        'XLV': ['LLY', 'UNH', 'JNJ', 'MRK', 'ABBV', 'TMO', 'ABT', 'DHR', 'PFE', 'AMGN', 'ISRG', 'ELV', 'SYK', 'MDT', 'CI', 'BMY', 'VRTX', 'BSX', 'REGN', 'CVS', 'GEHC'],
        'XLI': ['CAT', 'GE', 'UBER', 'UNP', 'RTX', 'ETN', 'HON', 'UPS', 'DE', 'BA', 'ADP', 'LMT', 'WM', 'PH', 'CSX', 'ITW', 'TT', 'TDG', 'GD', 'EMR'],
        'XLE': ['XOM', 'CVX', 'COP', 'MPC', 'EOG', 'SLB', 'PSX', 'PXD', 'VLO', 'WMB', 'OKE', 'OXY', 'HES', 'HAL', 'FANG', 'KMI', 'BKR', 'DVN', 'TRGP', 'CTRA'],
        'XLB': ['LIN', 'SHW', 'FCX', 'ECL', 'APD', 'NUE', 'NEM', 'DOW', 'CTVA', 'MLM', 'VMC', 'PPG', 'DD', 'LYB', 'STLD', 'IFF', 'BALL', 'AVY', 'PKG', 'CF'],
        'XLU': ['NEE', 'SO', 'DUK', 'CEG', 'SRE', 'AEP', 'D', 'EXC', 'PCG', 'PEG', 'ED', 'XEL', 'EIX', 'WEC', 'AWK', 'DTE', 'ETR', 'ES', 'PPL', 'FE'],
        'XLRE': ['PLD', 'AMT', 'EQIX', 'WELL', 'SPG', 'PSA', 'O', 'CCI', 'DLR', 'CSGP', 'EXR', 'VICI', 'CBRE', 'AVB', 'WY', 'SBAC', 'IRM', 'EQR', 'INVH', 'ARE'],
        'XOP': ['COP', 'EOG', 'PXD', 'FANG', 'OXY', 'HES', 'MRO', 'DVN', 'APA', 'CXO', 'XOM', 'CVX', 'SLB', 'PSX', 'MPC', 'HAL', 'BKR'],
        'XHB': ['WSM', 'CSL', 'OC', 'BLD', 'TT', 'JCI', 'TOL', 'NVR', 'DHI', 'PHM', 'BLDR', 'ALLE', 'LEN', 'FBIN', 'MAS', 'LII', 'LOW', 'TPX', 'CARR', 'FND', 'HD'],
        'XBI': ['EXAS', 'CRNX', 'ROIV', 'EXEL', 'CYTK', 'KRYS', 'NTRA', 'VKTX', 'CERE', 'SRPT', 'ALNY', 'BMRN', 'DYN', 'MRNA', 'NBIX', 'BPMC', 'INSM', 'AMGN', 'VRTX', 'IONS'],
        'XME': ['FCX', 'AA', 'UEC', 'STLD', 'RGLD', 'NUE', 'CLF', 'CMC', 'CRS', 'RS', 'ATI', 'HL', 'MP', 'CEIX', 'X', 'BTU', 'ARCH', 'AMR', 'CDE'],
        'SMH': ['NVDA', 'TSM', 'AVGO', 'ASML', 'MU', 'QCOM', 'TXN', 'LRCX', 'AMAT', 'INTC', 'AMD', 'ADI', 'KLAC', 'SNPS', 'CDNS', 'NXPI', 'MRVL', 'MCHP', 'STM', 'MPWR'],
        'IGV': ['MSFT', 'CRM', 'ORCL', 'ADBE', 'INTU', 'NOW', 'SNPS', 'PANW', 'CDNS', 'CRWD', 'ROP', 'WDAY', 'ADSK', 'FTNT', 'PLTR', 'DDOG', 'HUBS', 'EA', 'FICO', 'TEAM'],
        'CIBR': ['AVGO', 'CSCO', 'CRWD', 'INFY', 'PANW', 'GEN', 'CHKP', 'FFIV', 'LDOS', 'FTNT', 'BAH', 'TENB', 'OTEX', 'CYBR', 'AKAM', 'QLYS', 'NET', 'OKTA', 'SAIC', 'VRNS', 'RPD', 'S', 'ZS'],
        'TAN': ['ENPH', 'SEDG', 'RUN', 'FSLR', 'SOL', 'CSIQ', 'JKS', 'MAXN', 'NOVA', 'SPWR'],
        'BLOK': ['GLXY', 'COIN', 'MSTR', 'BYON', 'PYPL', 'HOOD', 'NU', 'IBM', 'SQ', 'RBLX', 'MARA', 'CLSK', 'CORZ', 'RIOT', 'CME', 'ACN'],
        'AIQ': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'NVDA', 'CRM', 'PYPL', 'ADBE'],
        'PAVE': ['DE', 'CAT', 'UNP', 'EMR', 'JCI', 'NUE', 'FAST', 'VRSK', 'VRSN', 'WAB'],
        'JETS': ['LUV', 'DAL', 'UAL', 'AAL', 'ALK', 'JBLU', 'SAVE', 'HA', 'SKYW', 'MESA'],
        'VTI': ["SPY", "QQQ", "DIA", "VTI", "XLK", "SMH", "IGV", "XLC", "XLY", "XLF", "XLV", "XLP", "XLI", "XLB", "XLU", "XLE", "XLRE", "IBIT", "AIQ", "CIBR", "SKYY", "XME", "VNQ", "GDX", "AMLP", "ITB", "OIH", "KRE", "XRT", "MOO", "FDN", "IBB", "XOP", "PBW", "KIE", "PHO", "TAN", "JETS", "IWB", "IWO", "IWF", "QQQE", "RSP", "SDS", "MDY", "GDXJ", "SLV", "GLD", "IAU", "ERX", "USO", "IEO", "SLX", "IAT", "ONLN", "ARKX", "PPH", "IHI", "XAR", "IJH", "IWM", "RTH", "HACK", "BBH", "IVW", "IHAK", "ARKQ", "CLOU", "IDNA", "IDRV", "IBLC", "ROBO", "IBUY", "XHB", "DRIV", "ARKF", "ARKW", "MSOS", "ARKK", "ARKG", "TNA"]
    }
    
    if options:
        #st.write(options)
        st.header(options)
    
        for sector, symbols in SPDR.items():
            spdr_sector = sector
            if spdr_sector in options:

                #if timing == "Hourly":
                    #for stock in symbols:
                        #st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")

                if timing == "Hourly":
                    col1, col2 = st.columns(2)
                    for stock in symbols:
                    #st.write(stock)
                        with col1:
                            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={spdr_sector}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=ema&o[0][op]=65&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=15&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=30&o[2][oc]=00FF00")
                        with col2:
                            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=ema&o[0][op]=65&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=15&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=30&o[2][oc]=00FF00")
                
                if timing == "Daily":
                    for stock in symbols:
                        st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
                        


                if timing == "Weekly":
                    for stock in symbols:
                        st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=ema&o[0][op]=65&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=15&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=30&o[2][oc]=00FF00")
                        st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
                        st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")

                if timing == "Multi":
                    col1, col2 = st.columns(2)                    
                    for stock in symbols:
                        with col1:
                            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
                        with col2:
                            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
                
