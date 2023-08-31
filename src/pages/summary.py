# Import
import streamlit as st

# Create a title
st.title("Summary Page for Covid Country Data Streamlit App")

st.image('https://i.imgur.com/cwi2uq0.jpg',width=680)

st.write("")

st.text("""
        Summary of COVID Country Data Streamlit App:

        My Streamlit application presents an intuitive and interactive platform for 
        
        analyzing COVID-19 statistics by country, sourced from the World Health 
        
        Organization via Collect API. Key features and data insights include:

        Authoritative Data Source: All information is reliably sourced from the 
        
        World Health Organization, ensuring users access accurate and up-to-date 
        
        statistics.

        
        Comprehensive Metrics: The platform displays crucial metrics for each country 
        
        including total cases, total deaths, and total recoveries.


        Engineered Columns for Deeper Analysis:

        Percent Deaths: This represents the proportion of total deaths with respect 
        
        to total cases, giving users a clearer perspective on fatality rates.


        Percent Recovered: Similarly, this metric offers insights into the recovery 
        
        rate by calculating the proportion of total recoveries against total cases.
        

        Country Rankings: Our application goes beyond presenting raw data. We've 
        
        ranked countries based on the engineered metrics of percent deaths and percent 
        
        recovered, allowing users to quickly gauge and compare the performance of 
        
        countries in managing and recovering from the pandemic.


        Interactive Visualizations: Engage with dynamic charts and graphs that shed 
        
        light on the trends, patterns, and state of the pandemic globally.

        Regular Updates: The app routinely fetches the latest data, ensuring users are 
        
        always informed with the most recent figures.

        
        User-Friendly Interface: Whether you're accessing from desktop or mobile, the 
        
        app offers a seamless experience.

        
        Our goal is to keep users informed and aware of the global situation, aiding in 
        
        research, decision-making, and understanding the pandemic's broader impact.

        """)

st.write("")

st.write("""
        Technologies used:

        Python: The primary programming language used to drive the application.
         
        Streamlit: For building the interactive web application interface.
            
        Pandas: Employed for data manipulation and analysis.
         
        MongoDB & PyMongo: Utilized for database storage, management, and retrieval
        of the COVID-19 datasets.
        
        Plotly Express: Integrated for dynamic data visualizations.
        
        Requests: Used for making HTTP requests to fetch data or interact with APIs.
        
        OS & Pathlib: For interacting with the system and managing file paths.
        
        ToMongo: A utility to facilitate data transfers to MongoDB.
            
        Virtual Environment (venv): Ensures a contained environment for the application, 
        isolating dependencies.
         """)

