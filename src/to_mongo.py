# Import statments
from base import Base
import pymongo
import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Class Declaration:
class ToMongo(Base):
    '''
    Designed as a class to transport the data from the Base class to a MongoDB instance.
    Initializes an instance of the inherited class.
    
    Defined methods are as follows:
    upload_one_by_one: Uploads pieces of information to a database one by one over an iterable structure.
    upload_collection: upload an entire document of items to MongoDB
    delete_collection: drops an entire collection of data
    '''
    
    def __init__(self):
    # def __init__(self, user=os.getenv('USERNAME'), password=os.getenv('PASSWORD')):
        # Initialize the instance of our inherited class:
        Base.__init__(self)
        
        # Get MongoDB secrets from Streamlit secrets.toml
        host = st.secrets["mongo"]["host"]
        username = st.secrets["mongo"]["username"]
        password = st.secrets["mongo"]["password"]

        # # Load the env variables:
        # load_dotenv()
        # self.user = user
        # self.password = password
        # self.mongo_url = os.getenv('MONGO_URL')
        
        # Using the MongoDB Atlas connection string format
        connection_string = f"mongodb+srv://{username}:{password}@{host}/test?retryWrites=true&w=majority"
        
        # Connect to PyMongo
        self.client = pymongo.MongoClient(connection_string)

        # #Connect to PyMongo
        # self.client = pymongo.MongoClient(self.mongo_url)
        
        # Create a database
        self.db = self.client.db
        # Create a collection:
        self.cards = self.db.cards
        
        # Because there is no ID or index column, set index to the 'country' column
        self.df.set_index('country', inplace=True)

    def upload_one_by_one(self, csv_path):
            '''
            Upload all records from the new CSV file to MongoDB, one-by-one. 
            This method will take longer, but will ensure all data is uploaded correctly!
            '''
            new_data = pd.read_csv(csv_path, usecols=['country', 'totalCases', 'totalDeaths', 'totalRecovered', 'percentDeaths', 'percentRecovered', 'rankPercentRecovered', 'rankPercentDeaths'])
  
            for index, row in new_data.iterrows():
                data_dict = {
                    'country': row['country'],
                    'totalCases': row['totalCases'],
                    'totalDeaths': row['totalDeaths'],
                    'totalRecovered': row['totalRecovered'],
                    'percentDeaths': row['percentDeaths'],
                    'percentRecovered': row['percentRecovered'],
                    'rankPercentRecovered': row['rankPercentRecovered'],
                    'rankPercentDeaths': row['rankPercentDeaths']
                }
                self.cards.insert_one(data_dict)
       

#     def delete_and_upload(self, csv_path):
#         '''
#         Delete all documents in the collection and upload new data from a specified CSV file.
#         '''
#         # Delete all documents in the collection
#         self.cards.delete_many({})
        
#         # Upload new data from the specified CSV file
#         self.upload_one_by_one(csv_path)

# if __name__ == '__main__':
#     c = ToMongo()
#     print('Successful Connection to Client Object')

#     # Specify the path to the new CSV file
#     new_csv_path = os.path.join(os.path.dirname(__file__), 'data', 'covid_data_eng.csv')

#     c.delete_and_upload(new_csv_path)
#     # c.upload_one_by_one(new_csv_path)
#     print('Successfully Uploaded new CSV data one by one to Mongo')
#     # c.upload_one_by_one()
#     # print('Successfully Uploaded all Card Info to Mongo')