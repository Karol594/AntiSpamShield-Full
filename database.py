import os
import logging
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://username:password@cluster.mongodb.net/antispam")

logger = logging.getLogger(__name__)

def get_database():
    try:
        client = MongoClient(MONGO_URI)
        db = client.antispam_karakalpak
        logger.info("Connected to MongoDB successfully")
        return db
    except Exception as e:
        logger.error(f"Error connecting to MongoDB: {e}")
        return None

def setup_database():
    db = get_database()
    if db:
        try:
            db.users.create_index("user_id", unique=True)
            db.groups.create_index("group_id", unique=True)
            logger.info("Database indexes created successfully")
        except Exception as e:
            logger.error(f"Error creating database indexes: {e}")
    else:
        logger.warning("Using fallback storage as MongoDB connection failed")