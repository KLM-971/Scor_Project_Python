import pandas as pd

def show_columns(df):
    """Prints the names of all columns in the DataFrame."""
    print(df.columns)

def rename_columns(df):
    """Renames specific columns and converts all column names to lowercase."""
    # Define the new column names mapping
    renaming_dict = {
        'INSEE commune': 'commune_code_insee',
        'Autres transports': 'transports',
        'Autres transports international': 'transports_international',
        'CO2 biomasse hors-total': 'biomasse_co2_hors_total',
        'Industrie hors-énergie': 'industrie_hors_énergie'
    }
    # Rename the columns as specified
    df.rename(columns=renaming_dict, inplace=True)
    # Convert all column names to lowercase
    df.columns = [col.lower() for col in df.columns]
    return df

def show_summary_statistics(df):
    """Displays summary statistics and missing values of the DataFrame."""
    # Display basic descriptive statistics
    print("Summary Statistics:\n", df.describe())
    # Display missing value counts
    print("\nMissing Values Count:\n", df.isnull().sum())

def handle_missing_values(df):
    """Impute missing values and create new columns for the imputed data."""
    # Loop through each column in the DataFrame
    for col in df.columns:
        if df[col].isnull().any():  # Check if there are any missing values
            new_col_name = f"{col}_imputed"  # Define a new column name
            # Impute missing values using the median of the column
            df[new_col_name] = df[col].fillna(df[col].median())
    return df

def join_dataframes(emissions_df, communes_df):
    """Join emissions data with commune data."""
    # Select necessary columns from communes_df
    communes_df = communes_df[['COM', 'DEP', 'PTOT', 'Région', 'REG']]
    # Join dataframes on INSEE commune code
    emissions_communes_df = pd.merge(emissions_df, communes_df, left_on='commune_code_insee', right_on='COM')
    return emissions_communes_df

def rename_joined_columns(df):
    """Rename columns in the joined dataframe."""
    renaming_dict = {
        'PTOT': 'population_totale',
        'DEP': 'departement_code',
        'REG': 'region_code',
        'Région': 'region_name'
    }
    df.rename(columns=renaming_dict, inplace=True)
    return df


