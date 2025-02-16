import streamlit as st
import pandas as pd
import plotly.express as px




def Visualisation():
    st.markdown("<h1 style='text-align: center;'>📊 Data Visualisation</h1>", unsafe_allow_html=True)

  
    @st.cache_data
    def load_data():
        return pd.read_csv("./data/save_data_clean.tsv", sep="\t")

    df = load_data()

    st.title("Some advanced Data around films and series 🎬")

    st.subheader("Number of films/series per year")
    year_counts = df["startYear"].value_counts().sort_index()
    fig_years = px.line(year_counts, x=year_counts.index, y=year_counts.values, 
                        labels={"x": "Year", "y": "Number of film/series"},
                        title="Evolution of the number of films/series per year")
    st.plotly_chart(fig_years)

    st.subheader("Distribution of durations in minutes")
    fig_runtime = px.histogram(df, x="runtimeMinutes", nbins=50, title="Reparition of the duration")
    st.plotly_chart(fig_runtime)

    st.subheader("Genres distribution")
    genres = pd.concat([df["genre_1"], df["genre_2"], df["genre_3"]]).dropna()
    fig_genres = px.bar(genres.value_counts(), x=genres.value_counts().index, y=genres.value_counts().values, 
                        labels={"x": "Genre", "y": "Number of films/series"},
                        title="Distribution of genres")
    st.plotly_chart(fig_genres)

    st.subheader("Average rating distribution")
    fig_ratings = px.histogram(df, x="averageRating", nbins=20, title="Distribution of average ratings")
    st.plotly_chart(fig_ratings)

    st.subheader(" Correlation between votes and average rating")
    fig_votes = px.scatter(df, x="numVotes", y="averageRating", 
                        title="Correlation between votes and average rating", 
                        log_x=True, opacity=0.5)
    st.plotly_chart(fig_votes)

    