import streamlit as st 
import pandas as pd 
import plotly.express as px
from pathlib import Path

@st.cache
def readdata():
    df = pd.read_csv('https://raw.githubusercontent.com/bisdom1/apps/master/assets/owid-covid-data.csv', na_values='nan') # read data in memory
    df.date=pd.DatetimeIndex(df.date)
    df.index=df.date
    df['week'] = df.to_period('W').index.strftime("%Y-%m-%d")
    df = df[df['continent'].notna()]
    df = df[df['total_cases'].notna()]
    return df

df = readdata()

countries = df.location.unique()

st.sidebar.markdown("""### :hammer_and_wrench: Options""")
country = st.sidebar.selectbox("Select country: ", countries)

st.markdown("""## :syringe: COVID-19 stats""")

fig = px.scatter_geo(df, locations="iso_code", color="continent",
                     hover_name="location", size="total_cases",
                     animation_frame="week",
                     projection="equirectangular",
                     title='Total cases per country, coloured by continent',
                     size_max=50,
                     opacity=0.7,
                     template='plotly_white')
fig.update_layout(height=600,showlegend=False)
st.plotly_chart(fig)

fig = px.bar(df[df.location==country], x="date", y="new_cases", title="New cases per day in " + country,template='plotly_white')
st.plotly_chart(fig)

st.markdown(""":link: Data from [ourworldindata.org](https://ourworldindata.org/coronavirus-source-data)""")

st.markdown(Path("assets\\streamlit_source.md").read_text(), unsafe_allow_html=True)