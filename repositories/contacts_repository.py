from .supabase_client import supabase


def get_contacts(limit=1):
    response = (supabase.table("contacts").select(
        "*").order("id", desc=False).range(0, limit - 1).execute())
    return response.data or []
