
# Scor Python Project

## Project Overview

This project analyzes greenhouse gas emissions data for communes in France, focusing on deriving insights into emission patterns at various administrative levels and investigating the relationship between emissions and population density.

## Data Source

The emissions data used in this project is sourced from [ADEME](https://www.data.gouv.fr/fr/datasets/inventaire-de-gaz-a-effet-de-serre-territorialise/#_), detailing GHG emissions per commune in France.

## Repository Structure

```plaintext
Scor_Project/
│
├── data/
│   ├── processed/
│   │   └── emissions_communes_df.csv
│   └── raw/
│       ├── donnees_communes.csv
│       └── IGT - Pouvoir de réchauffement.csv
│
├── notebooks/
│   ├── 1-Data_import.ipynb
│   ├── 2-Data_preprocessing.ipynb
│   └── 3-Data_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_import.py
│   ├── data_transformation.py
│   └── main.py
│
└── Python_project_TEST.pdf
```

## Repository Structure Justification

This project adheres to a modular structure commonly used in data science workflows, enhancing maintainability and supporting a clear separation of concerns:

- **`data/` Directory**: Differentiates between raw data (`raw/`) and processed data (`processed/`), with the latter being transformed and ready for analysis.

- **`notebooks/` Directory**: Contains sequentially numbered notebooks that detail the data processing steps and exploratory data analysis:
  
  - `1-Data_import.ipynb` outlines the data importation and initial examination.
  - `2-Data_preprocessing.ipynb` describes the data cleaning and transformation process.
  - `3-Data_analysis.ipynb` is dedicated to in-depth analysis and visualization.

- **`src/` Directory**: Houses all source code, including scripts for data import (`data_import.py`), data transformation (`data_transformation.py`), and the main processing script (`main.py`). This separation fosters code reusability and organization.

- **`Python_project_TEST.pdf`**: Provides comprehensive project instructions and documentation.

This structured approach ensures the repository is navigable and understandable, promoting effective collaboration and future development.

## Getting Started

1. Clone the repository to your local machine.
2. Execute the `main.py` script in the `src/` directory to begin preprocessing the data.
3. Open the `3-Data_analysis.ipynb` notebook within the `notebooks/` directory to proceed with the analysis.

## Analysis and Insights

The step-by-step notebooks lead you through the data import and preprocessing to the in-depth analysis:

- `data_import.py` manages the raw data ingestion.
- `data_transformation.py` facilitates data cleaning and transformation.
- `3-Data_analysis.ipynb` enables the statistical analysis and visualization of the emissions data.

## Acknowledgments

- Gratitude to ADEME for providing the emissions dataset.
- Appreciation to ChatGPT for its assistance throughout the project.
```
