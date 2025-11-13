from supabase import create_client, Client, ClientOptions
from config import settings
import httpx

# Configure httpx client with timeouts and no proxy
http_client = httpx.Client(
    timeout=30.0,
    proxies=None,  # Explicitly disable proxies for Supabase connection
    follow_redirects=True
)

# Initialize Supabase client with custom options
options = ClientOptions(
    schema="public",
    headers={},
    auto_refresh_token=True,
    persist_session=True
)

supabase: Client = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_SERVICE_KEY,
    options=options
)


def get_supabase() -> Client:
    """Get Supabase client instance"""
    return supabase
