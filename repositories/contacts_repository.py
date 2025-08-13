from .supabase_client import supabase


def get_contacts(limit=3):
    response = supabase.table("contacts").select("*").limit(limit).execute()
    return response.data or []
