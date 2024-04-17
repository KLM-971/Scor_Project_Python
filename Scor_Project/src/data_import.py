import pandas as pd

def import_data_locally(filepath):
    """Import data from a local CSV file."""
    return pd.read_csv(filepath)

def import_data_from_url(url):
    """Import data directly from a URL."""
    return pd.read_csv(url)

def show_first_20_lines(df):
    """Display the first 20 lines of a DataFrame."""
    print(df.head(20))

def import_data_commune(filepath):
    """Import data from a local CSV file using a specified delimiter."""
    return pd.read_csv(filepath, delimiter=';')  # Added delimiter parameter
