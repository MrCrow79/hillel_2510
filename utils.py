import pathlib
from setting import d_settings

BASE_DIR = pathlib.Path(__file__).parent  # шлях до папки проекту
SCREENSHOTS = pathlib.Path(__file__).parent / 'screenshots'  # шлях до папки проекту


db_connection_str = d_settings.database_url  # d_settings.DATABASE_URL
