from operator import index
from numpy import average
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf



with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html= True)
####Stock Data Download ########
stock_list = [
    'JD','AMZN','DDOG','MSFT','CWEB','KWEB','BTC-USD','BAC','TSLA','FVRR','RBLX','CRM','PLTR','ETH-USD','OLPX','SQ','CRWD','BIRD','ATVI','SBUX','NFLX','ABNB','FWONK','AER','CPANEL.BK','SPXU','APP','BYDDY','ORGN','NET','COIN','SIS.BK','NET','COIN','^IXIC' , '^DJI' , '^GSPC'
]
@st.cache
def data_for_app(list):
    stock_data = yf.download(list ,start = '2022-07-22')
    since_inception = (stock_data['Close'].fillna(method='ffill').iloc[-1] - stock_data['Close'].iloc[0]).div(stock_data['Close'].iloc[0]).mul(100).sort_values(ascending = False)
    pct = stock_data['Close'].pct_change().round(2) 
    return since_inception ,stock_data,pct




since_inception ,stock_data ,pct = data_for_app(stock_list)
avg = since_inception.drop(['^IXIC','^DJI','^GSPC']).mean()
count_stock = since_inception.drop(['^IXIC','^DJI','^GSPC']).count()
nasdaq = since_inception['^IXIC'].round(2)
dji = since_inception['^DJI'].round(2)
sp500 = since_inception['^GSPC'].round(2)
#####
st.title('Stock Competition Dashboard')

col1 ,col2 ,col3,col4,col5= st.columns(5)
col1.metric('Stock in this competition' , '{x}'.format(x=count_stock))
col2.metric('Average return','{x}%'.format(x=round( avg , 2)))
col3.metric('DJI Return','{x} %'.format(x=dji))
col4.metric('S&P500 Return','{x} %'.format(x=sp500))
col5.metric('Nasdaq Return','{x} %'.format(x=nasdaq))



st.write(
    '''## The following stock are selected by each player in competition.
    Number in the middle represent return percentage since inception.
    Number at the bottom represent daily percentage change''')



##### Stock Movement Daily#######
stock1 ,stock2 ,stock3 ,stock4 ,stock5= st.columns(5, gap = 'small')
stock6,stock7,stock8,stock9,stock10= st.columns(5, gap = 'small')
stock11 ,stock12 ,stock13 ,stock14 ,stock15= st.columns(5, gap = 'small')
stock16,stock17,stock18,stock19,stock20= st.columns(5, gap = 'small')
stock21 ,stock22 ,stock23 ,stock24 ,stock25= st.columns(5, gap = 'small')
stock26,stock27,stock28,stock29,stock30= st.columns(5, gap = 'small')
#######row1#########
stock1.metric(since_inception.index[0] , '{x} %'.format(x=since_inception.loc[since_inception.index[0]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[0]))
stock2.metric(since_inception.index[1] , '{x} %'.format(x=since_inception.loc[since_inception.index[1]].round(1)) ,'{x}%'.format(x=pct.iloc[-2].iloc[1]))
stock3.metric(since_inception.index[2] , '{x} %'.format(x=since_inception.loc[since_inception.index[2]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[2]))
stock4.metric(since_inception.index[3] , '{x} %'.format(x=since_inception.loc[since_inception.index[3]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[3]))
stock5.metric(since_inception.index[4] , '{x} %'.format(x=since_inception.loc[since_inception.index[4]].round(1)) ,'{x}%'.format(x=pct.iloc[-2].iloc[4]))
####### Row 2######

stock6.metric(since_inception.index[5] , '{x} %'.format(x=since_inception.loc[since_inception.index[5]].round(1)) ,'{x}%'.format( x=pct.iloc[-2].iloc[5]))
stock7.metric(since_inception.index[6] , '{x} %'.format(x=since_inception.loc[since_inception.index[6]].round(1)) ,'{x}%'.format( x=pct.iloc[-2].iloc[6]))
stock8.metric(since_inception.index[7] , '{x} %'.format(x=since_inception.loc[since_inception.index[7]].round(1)) ,'{x}%'.format( x=pct.iloc[-2].iloc[7]))
stock9.metric(since_inception.index[8] , '{x} %'.format(x=since_inception.loc[since_inception.index[8]].round(1)) ,'{x}%'.format( x=pct.iloc[-2].iloc[8]))
stock10.metric(since_inception.index[9] , '{x} %'.format(x=since_inception.loc[since_inception.index[9]].round(1)) ,'{x}%'.format( x=pct.iloc[-2].iloc[9]))

#######row3#########
stock11.metric(since_inception.index[10] , '{x} %'.format(x=since_inception.loc[since_inception.index[10]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[10]))
stock12.metric(since_inception.index[11] , '{x} %'.format(x=since_inception.loc[since_inception.index[11]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[12]))
stock13.metric(since_inception.index[12] , '{x} %'.format(x=since_inception.loc[since_inception.index[12]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[12]))
stock14.metric(since_inception.index[13] , '{x} %'.format(x=since_inception.loc[since_inception.index[13]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[13]))
stock15.metric(since_inception.index[14] , '{x} %'.format(x=since_inception.loc[since_inception.index[14]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[14]))

####### Row 4######

stock16.metric(since_inception.index[15] , '{x} %'.format(x=since_inception.loc[since_inception.index[15]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[15]))
stock17.metric(since_inception.index[16] , '{x} %'.format(x=since_inception.loc[since_inception.index[16]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[16]))
stock18.metric(since_inception.index[17] , '{x} %'.format(x=since_inception.loc[since_inception.index[17]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[17]))
stock19.metric(since_inception.index[18] , '{x} %'.format(x=since_inception.loc[since_inception.index[18]].round(1)) ,'{x}%'.format( x=pct.iloc[-2].iloc[18]))
stock20.metric(since_inception.index[19] , '{x} %'.format(x=since_inception.loc[since_inception.index[19]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[19]))

#######row5#########
stock21.metric(since_inception.index[20] , '{x} %'.format(x=since_inception.loc[since_inception.index[20]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[20]))
stock22.metric(since_inception.index[21] , '{x} %'.format(x=since_inception.loc[since_inception.index[21]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[22]))
stock23.metric(since_inception.index[22] , '{x} %'.format(x=since_inception.loc[since_inception.index[22]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[22]))
stock24.metric(since_inception.index[23] , '{x} %'.format(x=since_inception.loc[since_inception.index[23]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[23]))
stock25.metric(since_inception.index[24] , '{x} %'.format(x=since_inception.loc[since_inception.index[24]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[24]))

####### Row 6######

stock26.metric(since_inception.index[25] , '{x} %'.format(x=since_inception.loc[since_inception.index[25]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[25]))
stock27.metric(since_inception.index[26] , '{x} %'.format(x=since_inception.loc[since_inception.index[26]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[26]))
stock28.metric(since_inception.index[27] , '{x} %'.format(x=since_inception.loc[since_inception.index[27]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[27]))
stock29.metric(since_inception.index[28] , '{x} %'.format(x=since_inception.loc[since_inception.index[28]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[28]))
stock30.metric(since_inception.index[29] , '{x} %'.format(x=since_inception.loc[since_inception.index[29]].round(1)) , '{x}%'.format(x=pct.iloc[-2].iloc[29]))
