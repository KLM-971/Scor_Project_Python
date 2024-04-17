import pandas as pd
from src.data_import import import_data_from_url, import_data_locally, show_first_20_lines, import_data_commune
from src.data_transformation import show_columns, rename_columns, show_summary_statistics, handle_missing_values, join_dataframes, rename_joined_columns

def main():
    
    # Import part
    # 1_1 - Importing data by storing it locally
    emissions_df = import_data_locally("data/raw/IGT - Pouvoir de réchauffement global.csv")
    show_first_20_lines(emissions_df)
    
    # 1_2 - Importing data by using an URL
    url = "https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert"
    url_df = import_data_from_url(url)
    show_first_20_lines(url_df)

    # 1_3 - Importing data on "communes" 
    communes_data_path = "data/raw/donnees_communes.csv"
    communes_df = import_data_commune(communes_data_path)
    show_first_20_lines(communes_df)

    # Data transformation part
    # 2_1 Renaming columns
    show_columns(emissions_df)
    emissions_df = rename_columns(emissions_df)
    # Show renamed and reformatted columns to verify changes
    show_columns(emissions_df)

    # 2_2 Handling missing values
    # Show summary statistics to understand the data
    show_summary_statistics(emissions_df)
    
    # Handle missing values and create new columns for imputed data
    emissions_df = handle_missing_values(emissions_df)
    
    # Show the DataFrame to verify the new columns with imputed values
    print(emissions_df.head())

    # 2_3 Adding other values
    show_columns(communes_df)

    # Join dataframes
    emissions_communes_df = join_dataframes(emissions_df, communes_df)
    
    # Rename columns in the joined dataframe
    emissions_communes_df = rename_joined_columns(emissions_communes_df)
    
    # Show the first few rows to confirm changes
    print(emissions_communes_df.head())

    # Save the dataframe for future analysis
    emissions_communes_df.to_csv('data/processed/emissions_communes_df.csv', index=False)




if __name__ == "__main__":
    main()
