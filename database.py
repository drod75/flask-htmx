### Supabase file for flask
from supabase import create_client, Client
import os
from dotenv import load_dotenv

class Database():
    def __init__(self):
        load_dotenv()
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_KEY")
        
        self.supabase: Client = create_client(self.supabase_url, self.supabase_key)

    