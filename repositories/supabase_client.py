import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        "As variáveis SUPABASE_URL e SUPABASE_KEY não foram definidas.")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
