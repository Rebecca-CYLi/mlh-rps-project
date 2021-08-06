import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# MONGODB_URI = (
#     "mongodb://"
#     "{user}:{password}@{hostname}:{port}/{db}?authSource={authSource}".format(
#         user=os.environ.get("MONGO_USER"),
#         password=os.environ.get("MONGO_PASSWORD"),
#         hostname=os.environ.get("HOSTNAME"),
#         port=27017,
#         db=os.environ.get("DB"),
#         authSource=os.environ.get("AUTH_SOURCE"),
#     )
# )

MONGODB_URI = "mongodb://" "{hostname}:{port}/{db}".format(
    hostname="localhost",
    port=27017,
    db="DB",
    authSource="admin",
)


client = MongoClient(MONGODB_URI)
