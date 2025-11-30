from dotenv import load_dotenv
import os

# load_dotenv(override=True)

load_dotenv(override=True)
API_KEY = os.getenv("API_KEY")
USER = os.getenv("USERNAME")
ADRESS = os.getenv("ADRESS")
print(API_KEY)
print(USER)
print(ADRESS)
