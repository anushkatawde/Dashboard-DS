import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

#st.set_page_config(page_title="Dashboard", page_icon=":tada:", layout="centered")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.title("CO2 Emission in India")
# Loading DATASET
CO2_emission = pd.read_csv(r"CO2_emission.csv")
#print(data_set)

#DATAFRAME FORMATION
df = pd.DataFrame(CO2_emission)

dataName = st.sidebar.selectbox("Select Year", ("Home", "1990", "2000", "2010", "2019"))

def get_dataset(dataName):
    if dataName == "Home":
        st.title("CO2 Emission Worldwide")
        if st.checkbox("View Dataset"):
            data = st.dataframe(CO2_emission)
        # Plotting Geographical map
        df1 = px.data.gapminder()
        map_fig = px.scatter_geo(df1,
                                 locations='iso_alpha',
                                 projection='orthographic',
                                 color='continent',
                                 opacity=.8,
                                 hover_name='country',
                                 hover_data=['lifeExp', "pop"]
                                 )
        st.plotly_chart(map_fig)


        st.write("## Joint-plots")
        p = sns.jointplot(CO2_emission['Region'])
        p.fig.suptitle("Continents' Joint-plot",size=18)
        st.pyplot()

        st.text("")
        st.text("")

        p = sns.jointplot(CO2_emission['1990'], CO2_emission['2000'], kind="kde")
        p.fig.suptitle("1990 vs 2000",size=18)
        st.pyplot()
        st.text("")
        st.text("")

        p = sns.jointplot(CO2_emission['2000'], CO2_emission['2010'], kind="hex")
        p.fig.suptitle("2000 vs 2010", size=18)
        st.pyplot()
        st.text("")
        st.text("")

        p = sns.jointplot(CO2_emission['2010'], CO2_emission['2019'], kind="kde")
        p.fig.suptitle("2010 vs 2019", size=18)
        st.pyplot()


    elif dataName == "1990":
        st.title("CO2 Emission in 1990")
        d1 = df["1990"]
        st.dataframe(d1)

        st.write("## Count-plot:")
        sns.countplot(d1)
        plt.xlabel("1990")
        plt.ylabel("CO2 Emission")
        st.pyplot()
        st.text(
            ""
        )

        st.write("## Scatter-plot:")
        sns.scatterplot(x=df.index, y=df["1990"])
        st.pyplot()
        st.text("")

        st.write("## Histogram:")
        plt.hist(df["1990"])
        plt.xlabel("Countries", size=12)
        plt.ylabel("Year 1990", size=12)
        plt.title("CO2 emission worldwide in 1990 ", size=15)
        st.pyplot()

        st.text("")
        st.write("## Joint-plot")
        sns.jointplot(CO2_emission['1990'])
        st.pyplot()

    elif dataName == "2000":
        st.title("CO2 Emission in 2000")
        d1 = df["2000"]
        st.dataframe(d1)
        st.text("")

        st.write("## Count-plot:")
        sns.countplot(d1)
        plt.xlabel("2000")
        plt.ylabel("CO2 Emission")
        st.pyplot()

        st.text("")
        st.write("## Scatter-plot")
        sns.scatterplot(x=df.index, y=df["2000"])
        st.pyplot()

        st.text("")
        st.write("## Histogram:")
        plt.hist(df["2000"])
        plt.xlabel("Countries", size=12)
        plt.ylabel("Year 2000", size=12)
        plt.title("CO2 emission worldwide in 2000", size=15)
        st.pyplot()

        st.text("")
        st.write("## Joint-plot")
        sns.jointplot(CO2_emission['2000'])

        st.pyplot()


    elif dataName == "2010":
        st.title("CO2 Emission in 2010")
        d1 = df["2010"]
        st.dataframe(d1)

        st.write("## Count-plot:")
        sns.countplot(d1)
        plt.xlabel("2010")
        plt.ylabel("CO2 Emission")
        st.pyplot()

        st.text("")
        st.write("## Scatter-plot:")
        sns.scatterplot(x=df.index, y=df["2010"])
        st.pyplot()

        st.text("")
        st.write("## Histogram:")
        plt.hist(df["2010"])
        plt.xlabel("Countries", size=12)
        plt.ylabel("Year 2010", size=12)
        plt.title("CO2 emission worldwide in 2010 ", size=15)
        st.pyplot()
        st.text("")

        st.write("## Joint-plot:")
        sns.jointplot(CO2_emission['2010'])
        st.pyplot()


    else:
        st.title("CO2 Emission in 2019")
        d1 = df["2019"]
        st.dataframe(d1)

        st.write("## Count-plot:")
        sns.countplot(d1)
        plt.xlabel("2019")
        plt.ylabel("CO2 Emission")
        st.pyplot()

        st.text("")
        st.write("## Scatter-plot:")
        sns.scatterplot(x=df.index, y=df["2019"])
        st.pyplot()

        st.text("")
        st.write("## Histogram:")
        plt.hist(df["2019"])
        plt.xlabel("Countries", size=12)
        plt.ylabel("Year 2019", size=12)
        plt.title("CO2 emission worldwide in 2019 ", size=15)
        st.pyplot()
        st.text("")

        st.write("## Joint-plot")
        sns.jointplot(CO2_emission['2019'])
        st.pyplot()


Dataset = get_dataset(dataName)







