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
        ['SPY', 'QQQ', 'XLK', 'SMH', 'IGV', 'CIBR', 'XLC', 'XLY', 'XLP', 'XLF', 'XLV', 'XLI', 'XLE', 'XLB', 'XLU', 'XOP', 'XHB', 'XME', 'TAN', 'BLOK', 'AIQ', 'PAVE', 'JETS', 'VTI', 'XLG' ], horizontal=True)
    
    #st.write('You selected:', options)
    
    
    #options = st.checkbox('XLK', 'XLC', 'XLY', 'XLP', 'XLF', 'XLV', 'XLI', 'XLE', 'XLB', 'XLU', 'XOP', 'XHB', 'XME')
    
    
    
    
    SPDR = {
        'SPY' : ['SPY', 'QQQ', 'DIA', 'IWO', 'VTI', 'XLK', 'SMH', 'IGV', 'CIBR', 'SKYY', 'FFTY', 'IBIT', 'RSP', 'QQQE', 'XLG', 'VGT', 'SDS', 'XLC', 'XLY', 'XLP', 'XLF', 'XLV', 'XLI', 'XLE', 'XLB', 'XLU', 'XOP', 'XHB', 'XME', 'XBI', 'KRE', 'IBB', 'XRT', 'TAN', 'BLOK', 'AIQ', 'PAVE', 'JETS',
                   'AAPL', 'AMZN', 'MSFT', 'GOOGL', 'META', 'NVDA', 'AMD', 'COST', 'TSLA', 'NFLX', 'AVGO', 'ADBE', 'ANET', 'PANW', 'CRWD', 'PLTR', 'CRM', 'NOW', 'TEAM', 'ZS', 'COIN', 'MSTR'],
        'XLK': ['AAPL', 'NVDA', 'MSFT', 'AVGO', 'CRM', 'ORCL', 'AMD', 'CSCO', 'ACN', 'ADBE', 'NOW', 'IBM', 'TXN', 'QCOM', 'INTU', 'AMAT', 'PANW', 'MU', 'ADI', 'ANET', 'LRCX', 'INTC', 'KLAC', 'PLTR', 'APH', 'SNPS', 'CDNS', 'MSI', 'CRWD', 'ADSK', 'NXPI', 'ROP', 'FTNT', 'FICO', 'TEL', 'MCHP', 'IT', 'MPWR', 'DELL', 'CTSH', 'GLW', 'HPQ', 'ON', 'ANSS', 'KEYS', 'HPE', 'TYL', 'CDW', 'NTAP', 'GDDY', 'FSLR', 'PTC', 'TDY', 'WDC', 'STX', 'ZBRA', 'TER', 'GEN', 'AKAM', 'TRMB', 'VRSN', 'JBL', 'SWKS', 'FFIV', 'SMCI', 'JNPR', 'ENPH', 'EPAM', 'QRVO'], 
        'SMH': ['NVDA', 'TSM', 'AVGO', 'AMD', 'TXN', 'QCOM', 'AMAT', 'MU', 'ASML', 'ADI', 'INTC', 'LRCX', 'KLAC', 'SNPS', 'CDNS', 'MRVL', 'NXPI', 'MCHP', 'MPWR', 'ON', 'STM', 'TER', 'SWKS', 'OLED', 'QRVO'], 
        'IGV': ['CRM', 'ORCL', 'MSFT', 'NOW', 'ADBE', 'PANW', 'INTU', 'PLTR', 'CDNS', 'SNPS', 'CRWD', 'ADSK', 'ROP', 'WDAY', 'FTNT', 'FICO', 'MSTR', 'DDOG', 'EA', 'TEAM', 'APP', 'HUBS', 'ANSS', 'TTWO', 'TYL', 'PTC', 'ZM', 'ZS', 'DT', 'MANH', 'NTNX', 'GEN', 'GWRE', 'DOCU', 'SNAP', 'IOT', 'DSGX', 'SMAR', 'OTEX', 'BSY', 'S', 'PCOR', 'ESTC', 'CVLT', 'AZPN', 'GTLB', 'CFLT', 'SPSC', 'U', 'DBX', 'ALTR', 'ZETA', 'VRNS', 'BILL', 'PATH', 'ACIW', 'HCP', 'QTWO', 'AUR', 'APPF', 'MARA', 'TENB', 'BOX', 'QLYS', 'DLB', 'CWAN', 'CCCS', 'IDCC', 'WK', 'PEGA', 'YOU', 'NCNO', 'BLKB', 'ENV', 'RNG', 'PRGS', 'TDC', 'BL', 'AI', 'ALRM', 'DV', 'INTA', 'RPD', 'RIOT', 'FIVN', 'AGYS', 'FRSH', 'VERX', 'ALKT', 'LSPD', 'BRZE', 'PD', 'VYX', 'RAMP', 'APPN', 'AVPT', 'ZUO', 'VRNT', 'ADEA', 'SPT', 'BB', 'MTTR', 'ASAN', 'PRO', 'ATEN', 'JAMF', 'NABL', 'CXM', 'ETWO', 'SWI', 'MLNK', 'SEMR', 'USD'], 
        'XLC': ['META', 'GOOGL', 'GOOG', 'NFLX', 'TMUS', 'CHTR', 'CMCSA', 'DIS', 'EA', 'TTWO', 'T', 'VZ', 'OMC', 'LYV', 'WBD', 'IPG', 'NWSA', 'FOXA', 'MTCH', 'PARA', 'FOX', 'NWS'], 
        'XLY': ['AMZN', 'TSLA', 'HD', 'BKNG', 'MCD', 'LOW', 'TJX', 'SBUX', 'NKE', 'CMG', 'ORLY', 'ABNB', 'MAR', 'GM', 'HLT', 'AZO', 'DHI', 'RCL', 'ROST', 'LEN', 'F', 'YUM', 'LULU', 'GRMN', 'EBAY', 'TSCO', 'NVR', 'PHM', 'DECK', 'CCL', 'EXPE', 'DRI', 'ULTA', 'BBY', 'LVS', 'GPC', 'DPZ', 'APTV', 'POOL', 'KMX', 'TPR', 'NCLH', 'LKQ', 'WYNN', 'HAS', 'CZR', 'MGM', 'RL', 'BWA', 'MHK'], 
        'XLP': ['COST', 'PG', 'WMT', 'KO', 'PEP', 'PM', 'MO', 'MDLZ', 'CL', 'TGT', 'KMB', 'KVUE', 'MNST', 'GIS', 'STZ', 'KR', 'SYY', 'KDP', 'KHC', 'ADM', 'HSY', 'CHD', 'K', 'CLX', 'MKC', 'DG', 'TSN', 'EL', 'CAG', 'DLTR', 'SJM', 'BG', 'LW', 'TAP', 'CPB', 'HRL', 'BF.B', 'WBA'], 
        'XLI': ['GE', 'CAT', 'RTX', 'UBER', 'UNP', 'HON', 'ETN', 'ADP', 'LMT', 'BA', 'DE', 'UPS', 'TT', 'PH', 'GEV', 'WM', 'GD', 'TDG', 'ITW', 'CTAS', 'NOC', 'MMM', 'CSX', 'EMR', 'FDX', 'CARR', 'NSC', 'PCAR', 'URI', 'JCI', 'GWW', 'LHX', 'CPRT', 'PWR', 'PAYX', 'CMI', 'FAST', 'AME', 'RSG', 'HWM', 'OTIS', 'VRSK', 'ODFL', 'IR', 'DAL', 'WAB', 'EFX', 'AXON', 'ROK', 'XYL', 'DOV', 'UAL', 'VLTO', 'LDOS', 'FTV', 'BR', 'HUBB', 'BLDR', 'LUV', 'MAS', 'J', 'SNA', 'EXPD', 'IEX', 'PNR', 'TXT', 'JBHT', 'SWK', 'NDSN', 'ROL', 'ALLE', 'CHRW', 'DAY', 'PAYC', 'GNRC', 'AOS', 'HII', 'AMTM'], 
        'XLF': ['BRK-B', 'JPM', 'V', 'MA', 'BAC', 'WFC', 'GS', 'SPGI', 'AXP', 'MS', 'PGR', 'BLK', 'BX', 'C', 'FI', 'MMC', 'SCHW', 'CB', 'KKR', 'ICE', 'CME', 'PYPL', 'AON', 'PNC', 'USB', 'MCO', 'AJG', 'COF', 'TFC', 'BK', 'TRV', 'AFL', 'AMP', 'AIG', 'FIS', 'ALL', 'MSCI', 'MET', 'PRU', 'DFS', 'ACGL', 'HIG', 'MTB', 'NDAQ', 'WTW', 'FITB', 'STT', 'RJF', 'GPN', 'TROW', 'BRO', 'CPAY', 'HBAN', 'CBOE', 'SYF', 'CINF', 'RF', 'NTRS', 'CFG', 'FDS', 'PFG', 'WRB', 'KEY', 'EG', 'L', 'JKHY', 'MKTX', 'ERIE', 'AIZ', 'GL', 'IVZ', 'BEN'], 
        'XLV': ['LLY', 'UNH', 'JNJ', 'ABBV', 'MRK', 'TMO', 'ABT', 'ISRG', 'AMGN', 'DHR', 'PFE', 'SYK', 'BSX', 'VRTX', 'MDT', 'BMY', 'GILD', 'ELV', 'REGN', 'CI', 'ZTS', 'CVS', 'MCK', 'BDX', 'HCA', 'COR', 'A', 'EW', 'GEHC', 'IQV', 'RMD', 'IDXX', 'CNC', 'HUM', 'MTD', 'DXCM', 'CAH', 'BIIB', 'WAT', 'WST', 'STE', 'ZBH', 'COO', 'HOLX', 'MOH', 'LH', 'BAX', 'MRNA', 'DGX', 'PODD', 'RVTY', 'ALGN', 'VTRS', 'UHS', 'INCY', 'TECH', 'CTLT', 'SOLV', 'TFX', 'CRL', 'HSIC', 'DVA'], 
        'XLB': ['LIN', 'SHW', 'APD', 'FCX', 'ECL', 'CTVA', 'NEM', 'MLM', 'VMC', 'DD', 'NUE', 'DOW', 'PPG', 'IFF', 'LYB', 'PKG', 'IP', 'STLD', 'BALL', 'AVY', 'CF', 'AMCR', 'CE', 'ALB', 'EMN', 'MOS', 'FMC'], 
        'XLE': ['XOM', 'CVX', 'COP', 'WMB', 'EOG', 'SLB', 'OKE', 'PSX', 'MPC', 'KMI', 'VLO', 'HES', 'BKR', 'TRGP', 'OXY', 'FANG', 'HAL', 'DVN', 'EQT', 'CTRA', 'MRO', 'APA'], 
        'XLRE': ['PLD', 'AMT', 'EQIX', 'WELL', 'DLR', 'SPG', 'PSA', 'O', 'CCI', 'CBRE', 'IRM', 'EXR', 'VICI', 'AVB', 'CSGP', 'VTR', 'SBAC', 'EQR', 'WY', 'INVH', 'ESS', 'MAA', 'ARE', 'KIM', 'DOC', 'UDR', 'CPT', 'HST', 'REG', 'BXP', 'FRT'],
        'XLU': ['NEE', 'SO', 'DUK', 'CEG', 'AEP', 'SRE', 'D', 'PCG', 'PEG', 'VST', 'EXC', 'XEL', 'ED', 'EIX', 'ETR', 'WEC', 'AWK', 'DTE', 'PPL', 'AEE', 'ES', 'ATO', 'FE', 'CMS', 'CNP', 'NRG', 'NI', 'LNT', 'EVRG', 'AES', 'PNW'],
        'XOP': ['COP', 'EOG', 'FANG', 'OXY', 'HES', 'MRO', 'DVN', 'APA', 'XOM', 'CVX', 'SLB', 'PSX', 'MPC', 'HAL', 'BKR'],
        'XHB': ['WSM', 'CSL', 'OC', 'BLD', 'TT', 'JCI', 'TOL', 'NVR', 'DHI', 'PHM', 'BLDR', 'ALLE', 'LEN', 'FBIN', 'MAS', 'LII', 'LOW', 'TPX', 'CARR', 'FND', 'HD'],
        'XBI': ['EXAS', 'CRNX', 'ROIV', 'EXEL', 'CYTK', 'KRYS', 'NTRA', 'VKTX', 'SRPT', 'ALNY', 'BMRN', 'DYN', 'MRNA', 'NBIX', 'BPMC', 'INSM', 'AMGN', 'VRTX', 'IONS'],
        'XME': ['FCX', 'AA', 'UEC', 'STLD', 'RGLD', 'NUE', 'CLF', 'CMC', 'CRS', 'RS', 'ATI', 'HL', 'MP', 'CEIX', 'X', 'BTU', 'ARCH', 'AMR', 'CDE'],
        'BLOK': ['IBIT', 'MSTR', 'COIN', 'HOOD', 'MARA', 'CLSK', 'SQ', 'RIOT', 'HUT', 'WULF', 'GLXY', 'COIN', 'MSTR', 'BYON', 'PYPL', 'HOOD', 'NU', 'IBM', 'SQ', 'RBLX', 'MARA', 'CLSK', 'CORZ', 'RIOT', 'CME', 'ACN'],
        'FFTY': ['TGTX', 'HIMS', 'MMYT', 'CLS', 'PRCT', 'YOU', 'NVDA', 'PLTR', 'VRT', 'POWL', 'ARM', 'DOCS', 'FIX', 'MNDY', 'TSM', 'ATAT', 'NTRA', 'DUOL', 'IOT', 'NU', 'EME', 'ANET', 'LRN', 'TTD', 'CWAN', 'RCL', 'AXON', 'ALNY', 'AFRM', 'HUT', 'KVYO', 'IBKR', 'TVTX', 'LNTH', 'FOUR', 'FTAI', 'RDDT', 'VIST', 'META', 'VITL', 'AMSC', 'TOST', 'AGX', 'NFLX', 'HWM', 'TXRH', 'ONON', 'ZETA', 'WGS', 'SEZL'],
        'QQQ': ['AAPL', 'NVDA', 'MSFT', 'AMZN', 'AVGO', 'META', 'TSLA', 'COST', 'GOOGL', 'GOOG', 'NFLX', 'TMUS', 'AMD', 'PEP', 'CSCO', 'LIN', 'ADBE', 'TXN', 'QCOM', 'ISRG', 'INTU', 'AMGN', 'CMCSA', 'BKNG', 'AMAT', 'HON', 'VRTX', 'PANW', 'ADP', 'ADI', 'SBUX', 'GILD', 'MU', 'MELI', 'INTC', 'LRCX', 'MDLZ', 'REGN', 'KLAC', 'CTAS', 'CEG', 'PDD', 'SNPS', 'PYPL', 'CDNS', 'MRVL', 'MAR', 'CRWD', 'ORLY', 'CSX', 'ASML', 'ADSK', 'NXPI', 'FTNT', 'ABNB', 'DASH', 'ROP', 'PCAR', 'TTD', 'CHTR', 'AEP', 'FANG', 'MNST', 'WDAY', 'PAYX', 'CPRT', 'ROST', 'FAST', 'KDP', 'ODFL', 'AZN', 'KHC', 'MCHP', 'EA', 'GEHC', 'VRSK', 'DDOG', 'EXC', 'LULU', 'BKR', 'XEL', 'CTSH', 'TEAM', 'CCEP', 'IDXX', 'ON', 'CSGP', 'TTWO', 'DXCM', 'ANSS', 'ZS', 'BIIB', 'CDW', 'ILMN', 'MRNA', 'WBD', 'GFS', 'MDB', 'ARM', 'SMCI', 'DLTR'],
        'CIBR': ['AVGO', 'CSCO', 'CRWD', 'INFY', 'PANW', 'GEN', 'CHKP', 'FFIV', 'LDOS', 'FTNT', 'BAH', 'TENB', 'OTEX', 'CYBR', 'AKAM', 'QLYS', 'NET', 'OKTA', 'SAIC', 'VRNS', 'RPD', 'S', 'ZS'],
        'TAN': ['ENPH', 'SEDG', 'RUN', 'FSLR', 'SOL', 'CSIQ', 'JKS', 'MAXN', 'NOVA', 'SPWR'],
        'AIQ': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'NVDA', 'CRM', 'PYPL', 'ADBE'],
        'PAVE': ['DE', 'CAT', 'UNP', 'EMR', 'JCI', 'NUE', 'FAST', 'VRSK', 'VRSN', 'WAB'],
        'JETS': ['LUV', 'DAL', 'UAL', 'AAL', 'ALK', 'JBLU', 'SAVE', 'HA', 'SKYW', 'MESA'],
        'XLG': ['AAPL', 'NVDA', 'MSFT', 'AMZN', 'META', 'GOOGL', 'GOOG', 'AVGO', 'TSLA', 'LLY', 'JPM', 'UNH', 'XOM', 'V', 'MA', 'HD', 'PG', 'COST', 'JNJ', 'ABBV', 'WMT', 'NFLX', 'CRM', 'BAC', 'ORCL', 'CVX', 'MRK', 'KO', 'AMD', 'PEP', 'CSCO', 'WFC', 'LIN', 'ACN', 'ADBE', 'TMO', 'MCD', 'ABT', 'PM', 'TXN', 'GE', 'CAT', 'QCOM', 'VZ', 'DIS', 'CMCSA', 'DHR', 'PFE', 'NEE', 'AMAT', 'CASH'],
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
                            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
                        with col2:
                        st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=ema&o[0][op]=65&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=15&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=30&o[2][oc]=00FF00")
                
                if timing == "Daily":
                    for stock in symbols:
                        st.image(f"https://charts2-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF8F33C6&o[1][ot]=ema&o[1][op]=10&o[1][oc]=DCB3326D&o[2][ot]=ema&o[2][op]=21&o[2][oc]=DC32B363&o[3][ot]=patterns&o[3][op]=&o[3][oc]=000")
                        


                if timing == "Weekly":
                    for stock in symbols:
                        st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=w&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
                        st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")                        
                        st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=ema&o[0][op]=65&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=15&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=30&o[2][oc]=00FF00")
                        

                if timing == "Multi":
                    col1, col2 = st.columns(2)                    
                    for stock in symbols:
                        with col1:
                            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=d&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
                        with col2:
                            st.image(f"https://charts-node.finviz.com/chart.ashx?cs=l&t={stock}&tf=h2&s=linear&ct=candle_stick&tm=d&o[0][ot]=sma&o[0][op]=50&o[0][oc]=FF0000&o[1][ot]=ema&o[1][op]=10&o[1][oc]=0077B6&o[2][ot]=ema&o[2][op]=21&o[2][oc]=00FF00")
                
