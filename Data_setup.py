import os
from supabase import create_client, Client

def create_table():
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_KEY')
    
    supabase: Client = create_client(supabase_url, supabase_key)
    
    # Table creation is handled through Supabase dashboard or migrations
    # This function is kept for compatibility
    pass

if __name__ == "__main__":
    create_table()