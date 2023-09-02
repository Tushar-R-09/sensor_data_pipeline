
import sys
sys.path.append('/Users/4547662/Desktop/Sensor_data_pipeline/venv/lib/python3.8/site-packages')
import os
sys.path.append(os.getcwd())
import pymongo

#sys.path.append(os.getcwd)
from src.kafka_logger.logger import logging

class MongodbOps:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://tusharrohilla70:1234@sensorkafka.dngmycn.mongodb.net/")
        self.database_name = "sensorkafka"
        logging.info(f"database name tracked {self.database_name}")

    def insert_many(self,collection_name:str,records:list):
        #Insert many key value pair
        logging.info("Inserting many records")
        self.client[self.database_name][collection_name].insert_many(records)


    def insert_single(self,collection_name:str,records:dict):
        logging.info("Inserting single records")
        # insert single key value pair
        self.client[self.database_name][collection_name].insert_one(records)


data = {"name":"Taruna"}

MongodbOps().insert_single("single_test",data)
