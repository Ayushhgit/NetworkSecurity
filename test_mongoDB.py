from pymongo.mongo_client import MongoClient

# Correct MongoDB connection string
uri = "mongodb+srv://ayush:admin123@<cluster>.mongodb.net/<database>?retryWrites=true&w=majority"

try:
    # Connect to MongoDB
    client = MongoClient(uri, tls=True)
    
    # Ping the server to check connection
    client.admin.command('ping')
    
    print("✅ Successfully connected to MongoDB!")

except Exception as e:
    print("❌ Connection failed:", e)
