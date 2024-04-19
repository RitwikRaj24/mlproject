# A file named data_ingestion.py is likely a Python script used in a data science project to handle bringing in data for analysis. Here's what it typically does:

# Reads data from various sources: This script can read data from different locations like files (CSV, Excel, JSON etc.), databases, APIs, or even web scraping.
# Data format handling: It might preprocess the data to ensure it's in a usable format for further analysis. This could involve cleaning, transforming, or structuring the data.
# Loading data for further processing: The script likely prepares the data for use in other parts of your data science project. This might involve loading it into memory or storing it in a suitable format for later stages of analysis.
# Here are some contexts where you might find a data_ingestion.py script:

# Machine Learning Pipeline: In a machine learning project, this script might be the first step in the pipeline, responsible for ingesting the training and testing data.
# Data Warehousing: It could be used to populate a data warehouse with data from various sources.
# Data Analysis: For general data analysis, this script might be used to read data from various sources for further exploration and visualization.
# By separating data ingestion logic into a dedicated script, you improve the modularity and reusability of your data science project.

# Main aim : To read the dataset from some specific data source , which might be created from the big data team , cloud team who may be 
# reading from the livestream etc . Job is to read the data , split it into train / test , after which data_transformation will happen in the other file 

import os 
import sys 
from src.exception import CustomException
from src.logger import logging 
import pandas as pd 

from sklearn.model_selection import train_test_split 
from dataclasses import dataclass 
# 'dataclass' a way to create classes specifically for holding data. They simplify the process by using a decorator and type 
# hints to automatically generate common methods like __init__ and __repr__.

@dataclass # dont need __init__ or need to define the class variable
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')  # All the outputs will be stored in the artifacts folder 
    test_data_path: str=os.path.join('artifacts','test.csv')  
    raw_data_path: str=os.path.join('artifacts','data.csv')  

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self): 
        logging.info("Entered the data ingestion method or component")
        try: 
            df = pd.read_csv('notebook/data/stud.csv')  # can also be read from databases like mongodb , mysql etc.
            logging.info("Read the dataset as a dataframe")

            # Making directories for train data 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) 
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True) # raw_data -> csv file

            logging.info("Train Test split initiated")
            train_set, test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header=True)
            logging.info("Ingestion of the data is now complete.")

            return(
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
            )
        except Exception as e: 
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()