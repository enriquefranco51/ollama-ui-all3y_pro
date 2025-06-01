import json

def create_code_cell(code: str) -> dict:
    """Returns a dictionary representing a Jupyter notebook code cell."""
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + '\n' for line in code.splitlines()]
    }

def create_markdown_cell(markdown: str) -> dict:
    """Returns a dictionary representing a Jupyter notebook markdown cell."""
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + '\n' for line in markdown.splitlines()]
    }

def save_notebook(notebook_content: dict, filename: str = "generated_notebook.ipynb"):
    """Saves the notebook content to a .ipynb file."""
    if not filename.endswith(".ipynb"):
        filename += ".ipynb"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(notebook_content, f, indent=2)
    print(f"Notebook saved as {filename}")

def initialize_notebook():
    """Initializes the basic structure of a Jupyter notebook."""
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.0" # Example, can be adjusted
            }
        },
        "cells": []
    }

# We will call initialize_notebook() and add cells in subsequent steps.
# For now, this sets up the function that creates the basic notebook structure.

def add_data_loading_cleaning_section(notebook_cells):
    """Adds the data loading and cleaning section to the notebook cells list."""
    notebook_cells.append(create_markdown_cell(
        """# 1. Data Loading and Cleaning
This section focuses on loading your dataset into the notebook and performing initial cleaning steps.
Proper data cleaning is crucial for accurate analysis and reliable model building.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Import necessary libraries
import pandas as pd
import numpy as np

# Display pandas DataFrames nicely
from IPython.display import display
pd.options.display.max_columns = None # Show all columns
pd.options.display.max_rows = 100    # Show up to 100 rows
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 1.1. Load Data
Replace `'your_dataset.csv'` with the actual path or URL to your dataset.
You can upload your dataset to the Colab environment or load it from a URL.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Load the dataset
# Example: Load a CSV file
try:
    # Try to load a common sample dataset, or replace with user's data path
    # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/auto-mpg.csv')
    # For local uploads in Colab:
    # from google.colab import files
    # uploaded = files.upload()
    # import io
    # df = pd.read_csv(io.BytesIO(uploaded['your_file_name.csv']))

    # Placeholder: User needs to replace this with their actual data loading
    print("Please replace 'your_dataset.csv' with the path to your data.")
    print("Example: df = pd.read_csv('your_dataset.csv')")
    # Create a dummy DataFrame for demonstration if no data is loaded
    data = {'col1': [1, 2, np.nan, 4, 5], 'col2': ['A', 'B', 'A', np.nan, 'C'], 'col3': [np.nan, np.nan, 7, 8, 9]}
    df = pd.DataFrame(data)
    print("\nUsing a dummy DataFrame for demonstration purposes:")
    display(df.head())
except FileNotFoundError:
    print("FileNotFoundError: Make sure 'your_dataset.csv' is accessible or the URL is correct.")
    print("Creating a dummy DataFrame for demonstration purposes:")
    data = {'col1': [1, 2, np.nan, 4, 5], 'col2': ['A', 'B', 'A', np.nan, 'C'], 'col3': [np.nan, np.nan, 7, 8, 9]}
    df = pd.DataFrame(data)
    display(df.head())
except Exception as e:
    print(f"An error occurred: {e}")
    print("Creating a dummy DataFrame for demonstration purposes:")
    data = {'col1': [1, 2, np.nan, 4, 5], 'col2': ['A', 'B', 'A', np.nan, 'C'], 'col3': [np.nan, np.nan, 7, 8, 9]}
    df = pd.DataFrame(data)
    display(df.head())
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 1.2. Initial Data Inspection
Let's take a first look at the data.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Display the first few rows of the DataFrame
print("First 5 rows of the DataFrame:")
display(df.head())

# Get a summary of the DataFrame's structure
print("\nDataFrame Info:")
df.info()

# Get descriptive statistics for numerical columns
print("\nDescriptive Statistics:")
display(df.describe(include='all'))
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 1.3. Handle Missing Values
Missing data can significantly impact your analysis. Here are some common strategies:
*   **Identify missing values:** Count them per column.
*   **Remove missing values:** Drop rows or columns with missing data (use with caution).
*   **Impute missing values:** Fill them with a specific value (e.g., mean, median, mode, or a constant).
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Check for missing values
print("Missing values per column:")
display(df.isnull().sum())

# Example: Fill missing numerical values with the mean
# Ensure you only select numerical columns for mean imputation
# For demonstration, we'll try to fill NaNs in 'col1' and 'col3' from our dummy data
for col in ['col1', 'col3']:
    if col in df.columns and df[col].isnull().any() and pd.api.types.is_numeric_dtype(df[col]):
        print(f"\nFilling missing values in '{col}' with its mean.")
        df[col].fillna(df[col].mean(), inplace=True)

# Example: Fill missing categorical values with the mode
# For demonstration, we'll try to fill NaNs in 'col2' from our dummy data
for col in ['col2']:
    if col in df.columns and df[col].isnull().any(): # Check if it's object or category later
        print(f"\nFilling missing values in '{col}' with its mode.")
        df[col].fillna(df[col].mode()[0], inplace=True) # mode() can return multiple values if they have same frequency

# Display DataFrame after handling missing values
print("\nDataFrame after attempting to handle missing values:")
display(df.head())
print("\nMissing values per column after handling:")
display(df.isnull().sum())

# Example: Drop rows with any remaining missing values (use cautiously)
# df.dropna(inplace=True)
# print("\nDataFrame after dropping rows with any NaN values (if any were left):")
# display(df.head())
# display(df.isnull().sum())
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 1.4. Handle Duplicates
Duplicate rows can skew your analysis.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Check for duplicate rows
duplicate_rows = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_rows}")

# Remove duplicate rows (keeping the first occurrence)
if duplicate_rows > 0:
    df.drop_duplicates(keep='first', inplace=True)
    print("Duplicate rows removed.")
    print(f"Number of duplicate rows after removal: {df.duplicated().sum()}")
else:
    print("No duplicate rows to remove.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 1.5. Data Type Conversion
Ensure columns have the correct data types (e.g., numbers as numeric, dates as datetime objects).
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Display current data types
print("Current data types:")
display(df.dtypes)

# Example: Convert a column to numeric (if applicable)
# if 'column_to_numeric' in df.columns:
#     df['column_to_numeric'] = pd.to_numeric(df['column_to_numeric'], errors='coerce') # 'coerce' turns errors into NaT/NaN

# Example: Convert a column to datetime (if applicable)
# if 'date_column' in df.columns:
#     df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')

# Example: Convert a column to category (if applicable for memory efficiency and some libraries)
# if 'categorical_column' in df.columns:
#     df['categorical_column'] = df['categorical_column'].astype('category')

print("\nData types after potential conversions (examples are commented out):")
display(df.dtypes)
        """
    ))

# This function will be called later when assembling the notebook.
# Example:
# notebook = initialize_notebook()
# add_data_loading_cleaning_section(notebook["cells"])
# save_notebook(notebook, "my_data_notebook.ipynb")

def add_eda_section(notebook_cells):
    """Adds the Data Exploration (EDA) section to the notebook cells list."""
    notebook_cells.append(create_markdown_cell(
        """# 2. Data Exploration (Exploratory Data Analysis - EDA)
EDA is the process of analyzing datasets to summarize their main characteristics, often using visual methods.
This step is crucial for understanding the data, identifying patterns, anomalies, and forming hypotheses.
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 2.1. Re-confirm Data Overview
It's good practice to look at the data again after cleaning.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Display the first few rows again
print("Cleaned DataFrame - First 5 rows:")
if 'df' in globals():
    display(df.head())
else:
    print("DataFrame 'df' not found. Please ensure data loading and cleaning steps were successful.")

# Display DataFrame info again
print("\nCleaned DataFrame Info:")
if 'df' in globals():
    df.info()
else:
    print("DataFrame 'df' not found.")

# Display descriptive statistics again
print("\nCleaned DataFrame Descriptive Statistics:")
if 'df' in globals():
    display(df.describe(include='all'))
else:
    print("DataFrame 'df' not found.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 2.2. Univariate Analysis (Analyzing individual columns)
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """### 2.2.1. Value Counts for Categorical Columns
Understand the distribution of categories in your categorical features.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Value counts for categorical columns
if 'df' in globals():
    print("Value counts for categorical columns:")
    for col in df.select_dtypes(include=['object', 'category']).columns:
        print(f"\n--- {col} ---")
        display(df[col].value_counts(dropna=False)) # dropna=False to see missing value counts if any
else:
    print("DataFrame 'df' not found.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """### 2.2.2. Distribution of Numerical Columns
Understand the spread and central tendency of numerical features. Histograms are great for this.
(More detailed plotting will be in the 'Plotting' section)
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Basic distribution for numerical columns (histograms will be more detailed in Plotting section)
if 'df' in globals():
    print("Distribution of numerical columns (summary):")
    for col in df.select_dtypes(include=np.number).columns:
        print(f"\n--- {col} ---")
        display(df[col].describe())
else:
    print("DataFrame 'df' not found.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 2.3. Bivariate Analysis (Analyzing relationships between two columns)
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """### 2.3.1. Correlation Matrix for Numerical Columns
A correlation matrix helps understand linear relationships between numerical variables.
Values range from -1 (strong negative correlation) to +1 (strong positive correlation). 0 indicates no linear correlation.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Correlation matrix for numerical columns
if 'df' in globals():
    numerical_df = df.select_dtypes(include=np.number)
    if not numerical_df.empty:
        print("Correlation Matrix:")
        correlation_matrix = numerical_df.corr()
        display(correlation_matrix)
        # For a heatmap visualization (more in plotting section):
        # import seaborn as sns
        # import matplotlib.pyplot as plt
        # plt.figure(figsize=(10, 8))
        # sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        # plt.title("Correlation Heatmap")
        # plt.show()
    else:
        print("No numerical columns found to calculate correlation matrix.")
else:
    print("DataFrame 'df' not found.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """### 2.3.2. Grouping by Categorical Columns
Explore how numerical features vary across different categories.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Example: Group by a categorical column and calculate mean of numerical columns
if 'df' in globals():
    # Select first available categorical and numerical column for demonstration
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    numerical_cols = df.select_dtypes(include=np.number).columns

    if len(categorical_cols) > 0 and len(numerical_cols) > 0:
        cat_col_example = categorical_cols[0]
        num_col_example = numerical_cols[0] # or all numerical_cols

        print(f"Example: Grouping by '{cat_col_example}' and showing mean of '{num_col_example}':")
        try:
            display(df.groupby(cat_col_example)[num_col_example].mean().reset_index())
        except Exception as e:
            print(f"Could not perform groupby operation for demonstration: {e}")
            print(f"Categorical column '{cat_col_example}' values: {df[cat_col_example].unique()}")
            print(f"Numerical column '{num_col_example}' dtype: {df[num_col_example].dtype}")


        # Example: Group by 'col2' (categorical from dummy) and show mean of 'col1' (numerical from dummy)
        if 'col2' in df.columns and 'col1' in df.columns:
            print("\nExample using dummy data columns ('col2', 'col1'):")
            try:
                display(df.groupby('col2')['col1'].mean().reset_index())
            except Exception as e:
                 print(f"Could not perform groupby for dummy data: {e}")
    else:
        print("Not enough categorical or numerical columns for a groupby demonstration.")
else:
    print("DataFrame 'df' not found.")
        """
    ))

# This function will be called later when assembling the notebook.

def add_plotting_section(notebook_cells):
    """Adds the Plotting section to the notebook cells list."""
    notebook_cells.append(create_markdown_cell(
        """# 3. Plotting and Visualization
Visualizations are key to understanding data distributions, relationships, and outliers.
This section uses Matplotlib and Seaborn for creating common plots.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Import plotting libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Set some default styling for plots
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6) # Default figure size
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 3.1. Histogram
Shows the distribution of a single numerical variable.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Histogram for a numerical column
if 'df' in globals():
    numerical_cols = df.select_dtypes(include=np.number).columns
    if len(numerical_cols) > 0:
        col_to_plot = numerical_cols[0] # Plot the first numerical column
        plt.figure(figsize=(10,6))
        sns.histplot(df[col_to_plot], kde=True, bins=30) # kde for kernel density estimate
        plt.title(f'Histogram of {col_to_plot}')
        plt.xlabel(col_to_plot)
        plt.ylabel('Frequency')
        plt.show()
    else:
        print("No numerical columns available in the DataFrame for a histogram.")
else:
    print("DataFrame 'df' not found. Please ensure data loading and cleaning steps were successful.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 3.2. Bar Chart
Shows the distribution of a categorical variable or compares a numerical variable across categories.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Bar chart for a categorical column (count of categories)
if 'df' in globals():
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(categorical_cols) > 0:
        col_to_plot = categorical_cols[0] # Plot the first categorical column
        plt.figure(figsize=(10,6))
        sns.countplot(y=df[col_to_plot], order = df[col_to_plot].value_counts().index) # Order by frequency
        plt.title(f'Bar Chart of {col_to_plot}')
        plt.xlabel('Count')
        plt.ylabel(col_to_plot)
        plt.show()
    else:
        print("No categorical columns available in the DataFrame for a bar chart.")
else:
    print("DataFrame 'df' not found.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 3.3. Scatter Plot
Shows the relationship between two numerical variables.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Scatter plot for two numerical columns
if 'df' in globals():
    numerical_cols = df.select_dtypes(include=np.number).columns
    if len(numerical_cols) >= 2:
        col_x = numerical_cols[0]
        col_y = numerical_cols[1]
        plt.figure(figsize=(10,6))
        sns.scatterplot(x=df[col_x], y=df[col_y])
        plt.title(f'Scatter Plot: {col_x} vs {col_y}')
        plt.xlabel(col_x)
        plt.ylabel(col_y)
        plt.show()
    else:
        print("At least two numerical columns are needed for a scatter plot.")
else:
    print("DataFrame 'df' not found.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 3.4. Box Plot
Displays the distribution of a numerical variable, showing median, quartiles, and potential outliers.
Can also be used to compare distributions across different categories.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Box plot for a numerical column
if 'df' in globals():
    numerical_cols = df.select_dtypes(include=np.number).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    if len(numerical_cols) > 0:
        num_col_to_plot = numerical_cols[0]

        plt.figure(figsize=(10,6))
        sns.boxplot(x=df[num_col_to_plot])
        plt.title(f'Box Plot of {num_col_to_plot}')
        plt.xlabel(num_col_to_plot)
        plt.show()

        # Box plot of a numerical column grouped by a categorical column
        if len(categorical_cols) > 0:
            cat_col_to_group = categorical_cols[0]
            plt.figure(figsize=(12,7))
            sns.boxplot(x=df[cat_col_to_group], y=df[num_col_to_plot])
            plt.title(f'Box Plot of {num_col_to_plot} grouped by {cat_col_to_group}')
            plt.xlabel(cat_col_to_group)
            plt.ylabel(num_col_to_plot)
            plt.xticks(rotation=45, ha='right') # Rotate x-axis labels if they overlap
            plt.tight_layout() # Adjust layout to prevent labels from being cut off
            plt.show()
        else:
            print("\nNo categorical columns available for a grouped box plot.")

    else:
        print("No numerical columns available for a box plot.")
else:
    print("DataFrame 'df' not found.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 3.5. Correlation Heatmap
Visualizes the correlation matrix (calculated in EDA section) as a heatmap.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Correlation Heatmap
if 'df' in globals():
    numerical_df = df.select_dtypes(include=np.number)
    if not numerical_df.empty and len(numerical_df.columns) > 1:
        correlation_matrix = numerical_df.corr()
        plt.figure(figsize=(12, 10))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
        plt.title('Correlation Heatmap of Numerical Features')
        plt.show()
    elif not numerical_df.empty and len(numerical_df.columns) <=1:
        print("Not enough numerical columns (need at least 2) to generate a meaningful correlation heatmap.")
    else:
        print("No numerical columns found to calculate correlation matrix for heatmap.")
else:
    print("DataFrame 'df' not found.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 3.6. Pair Plot (Optional)
Visualizes pairwise relationships between numerical variables. Can be computationally intensive for datasets with many features.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Pair Plot (optional, can be slow for many columns)
if 'df' in globals():
    numerical_df = df.select_dtypes(include=np.number)
    if not numerical_df.empty and len(numerical_df.columns) > 1 :
        # Consider using a subset of columns if too many, e.g., numerical_df.iloc[:, :5] for first 5
        print(f"Generating pair plot for {len(numerical_df.columns)} numerical columns. This might take a moment...")
        # Add a categorical hue if available and not too many unique values
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns
        hue_col = None
        if len(categorical_cols) > 0:
            # Select a categorical column with a manageable number of unique values for hue
            for col in categorical_cols:
                if df[col].nunique() < 10: # Arbitrary threshold for 'manageable'
                    hue_col = col
                    break

        if hue_col:
            print(f"Using '{hue_col}' as hue.")
            sns.pairplot(numerical_df, hue=df[hue_col] if hue_col else None, diag_kind='kde', corner=True)
        else:
            print("No suitable categorical column for hue, or too many numerical columns for default pairplot.")
            print("Plotting without hue or for a subset of columns for performance.")
            # If too many columns, it's better to select a few important ones or skip
            if len(numerical_df.columns) > 5:
                print(f"Plotting for the first 5 numerical columns: {list(numerical_df.columns[:5])}")
                sns.pairplot(numerical_df.iloc[:,:5], diag_kind='kde', corner=True)
            else:
                sns.pairplot(numerical_df, diag_kind='kde', corner=True)

        plt.suptitle('Pair Plot of Numerical Features', y=1.02) # Adjust title position
        plt.show()
    elif not numerical_df.empty and len(numerical_df.columns) <=1:
        print("Not enough numerical columns (need at least 2) to generate a pair plot.")
    else:
        print("No numerical columns available for a pair plot.")
else:
    print("DataFrame 'df' not found.")
        """
    ))

# This function will be called later when assembling the notebook.

def add_q_and_a_section(notebook_cells):
    """Adds the Q&A on Data section to the notebook cells list."""
    notebook_cells.append(create_markdown_cell(
        """# 4. Q&A on Data (Querying and Filtering)
This section allows you to ask specific questions about your data by filtering and querying the DataFrame.
While true natural language Q&A often requires advanced tools (like LLMs), you can achieve a lot with Pandas.
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 4.1. Filtering Data with Pandas
You can select subsets of your data based on conditions.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Example: Filter data based on a condition
if 'df' in globals():
    # Ensure the dummy dataframe's 'col1' is numeric for this example
    if 'col1' in df.columns and pd.api.types.is_numeric_dtype(df['col1']):
        print("Example: Filtering 'col1' where values are greater than the mean of 'col1'")
        # Calculate mean, ensuring it's not NaN
        mean_col1 = df['col1'].mean()
        if pd.notna(mean_col1):
            filtered_df_gt_mean = df[df['col1'] > mean_col1]
            display(filtered_df_gt_mean)

            if filtered_df_gt_mean.empty:
                print(f"No data in 'col1' is greater than its mean ({mean_col1:.2f}).")
        else:
            print("Mean of 'col1' could not be calculated (possibly all NaNs before cleaning).")

    else:
        print("Column 'col1' not found or not numeric, skipping this filtering example.")

    # Example with a categorical column from dummy data
    if 'col2' in df.columns:
        # Find the most frequent category in 'col2'
        if not df['col2'].empty and df['col2'].mode().shape[0] > 0:
            most_frequent_category_col2 = df['col2'].mode()[0]
            print(f"\nExample: Filtering 'col2' for the most frequent category ('{most_frequent_category_col2}')")
            filtered_df_category = df[df['col2'] == most_frequent_category_col2]
            display(filtered_df_category)
        else:
            print("\nColumn 'col2' is empty or mode could not be determined, skipping categorical filter example.")
    else:
        print("\nColumn 'col2' not found, skipping categorical filter example.")

    print("\n# --- Your Turn! ---")
    print("# Ask your own questions by modifying the conditions below:")
    print("# Example: df_your_condition = df[df['your_column_name'] == 'some_value']")
    print("# display(df_your_condition)")
    print("\n# Example: df_multiple_conditions = df[(df['col_A'] > X) & (df['col_B'] == 'Y')]")
    print("# display(df_multiple_conditions)")
else:
    print("DataFrame 'df' not found. Please ensure data loading and cleaning steps were successful.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 4.2. Using `query()` method
Pandas' `query()` method allows you to filter DataFrames using a string expression.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Example: Using the query() method
if 'df' in globals():
    if 'col1' in df.columns and pd.api.types.is_numeric_dtype(df['col1']):
        mean_col1 = df['col1'].mean() # Recalculate or use from previous cell if stored
        if pd.notna(mean_col1):
            print(f"Example: Querying 'col1' for values greater than its mean ({mean_col1:.2f}) using query()")
            try:
                queried_df = df.query(f"col1 > {mean_col1}") # f-string for variable injection
                display(queried_df)
                if queried_df.empty:
                    print(f"No data in 'col1' is greater than its mean ({mean_col1:.2f}) using query().")
            except Exception as e:
                print(f"Error during query: {e}. This can happen if column names have spaces or special characters not suited for unquoted query strings.")
        else:
            print("Mean of 'col1' could not be calculated for query example.")
    else:
        print("Column 'col1' not found or not numeric, skipping query() example.")

    print("\n# --- Your Turn with query() ---")
    print("# Example: queried_df_custom = df.query('your_column > 100 and another_column == "Category A"')")
    print("# display(queried_df_custom)")
    print("# Note: Column names with spaces or special characters might need backticks: `My Column Name`")
else:
    print("DataFrame 'df' not found.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 4.3. Advanced Q&A and Natural Language Processing (NLP)
For more complex Q&A or using natural language:
*   **PandasAI:** A library that allows you to ask questions to your Pandas DataFrames in natural language. It uses LLMs in the background. You would typically need to install it (`pip install pandasai`) and have an LLM API key (e.g., for OpenAI's GPT).
    ```python
    # Example of how PandasAI might be used (requires setup and API key):
    # from pandasai import SmartDataframe
    # from pandasai.llm import OpenAI # Or other supported LLMs
    #
    # # This is a conceptual example - YOU NEED TO SET UP YOUR API KEY
    # # llm = OpenAI(api_token="YOUR_API_KEY")
    # # smart_df = SmartDataframe(df, config={"llm": llm})
    # # response = smart_df.chat("What is the average value of col1?")
    # # print(response)
    # # response_plot = smart_df.chat("Plot a histogram of col1") # Can sometimes generate plots
    # # print(response_plot)
    ```
*   **LangChain or LlamaIndex:** These are more general frameworks for building LLM-powered applications, including Q&A over structured data. They offer more flexibility but also have a steeper learning curve.

**Note:** Using LLM-based tools usually involves API costs and requires careful consideration of data privacy if you are sending your data to an external API.
        """
    ))

# This function will be called later when assembling the notebook.

def add_predictive_modeling_section(notebook_cells):
    """Adds the Predictive Modeling section to the notebook cells list."""
    notebook_cells.append(create_markdown_cell(
        """# 5. Predictive Modeling
This section introduces basic predictive modeling concepts using Scikit-learn.
We'll cover a simple regression and a simple classification example.
Remember, effective modeling requires careful feature engineering, model selection, and hyperparameter tuning.
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 5.1. Setup for Modeling
Import necessary libraries and prepare data.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Import libraries for modeling
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression # Logistic for classification
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

import warnings
warnings.filterwarnings('ignore', category=FutureWarning) # Ignore some sklearn warnings for cleaner output

if 'df' not in globals():
    print("DataFrame 'df' not found. Using a placeholder for modeling demonstration.")
    # Create a more suitable dummy DataFrame for modeling
    data_model = {
        'feature1': np.random.rand(100),
        'feature2': np.random.rand(100) * 10,
        'feature3_cat': np.random.choice(['A', 'B', 'C'], 100),
        'target_regression': 2 * np.random.rand(100) + 3 * (np.random.rand(100) * 10) + np.random.normal(0, 1, 100),
        'target_classification': np.random.choice([0, 1], 100)
    }
    df_model = pd.DataFrame(data_model)
else:
    # Use a copy of the original df for modeling to avoid changing it
    df_model = df.copy()

print("Using the following DataFrame for modeling examples (first 5 rows):")
display(df_model.head())
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """### 5.1.1. Feature Selection and Preprocessing
*   **Select Features (X) and Target (y):** Identify which columns will be your input features and which one is your target variable.
*   **Handle Categorical Features:** Convert them to numerical format (e.g., one-hot encoding, label encoding).
*   **Handle Numerical Features:** Scale or normalize them if necessary (e.g., StandardScaler).
*   **Split Data:** Divide your data into training and testing sets.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# --- Placeholder: Define your features (X) and target (y) ---
# This is highly dataset-dependent. You need to choose based on your data and problem.

# Example:
# numerical_features = df_model.select_dtypes(include=np.number).columns.tolist()
# categorical_features = df_model.select_dtypes(include=['object', 'category']).columns.tolist()

# For Regression:
# target_reg = 'target_regression' # Replace with your regression target column name
# if target_reg in numerical_features: numerical_features.remove(target_reg)
# if target_reg in categorical_features: categorical_features.remove(target_reg) # Should not happen

# For Classification:
# target_clf = 'target_classification' # Replace with your classification target column name
# if target_clf in numerical_features: numerical_features.remove(target_clf)
# if target_clf in categorical_features: categorical_features.remove(target_clf)


# For demonstration with the dummy df_model:
numerical_features_demo = ['feature1', 'feature2']
categorical_features_demo = ['feature3_cat']
target_reg_demo = 'target_regression'
target_clf_demo = 'target_classification'

# Remove target columns from feature lists if they were accidentally included
if target_reg_demo in numerical_features_demo: numerical_features_demo.remove(target_reg_demo)
if target_reg_demo in categorical_features_demo: categorical_features_demo.remove(target_reg_demo)
if target_clf_demo in numerical_features_demo: numerical_features_demo.remove(target_clf_demo)
if target_clf_demo in categorical_features_demo: categorical_features_demo.remove(target_clf_demo)


print(f"Demo Numerical Features: {numerical_features_demo}")
print(f"Demo Categorical Features: {categorical_features_demo}")
print(f"Demo Regression Target: {target_reg_demo}")
print(f"Demo Classification Target: {target_clf_demo}")

# Create preprocessing pipelines for numerical and categorical features
numerical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')), # Handle any lingering NaNs
    ('scaler', StandardScaler())
])

categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')), # Handle any lingering NaNs
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Create a column transformer to apply different transformations to different columns
# Ensure the columns listed actually exist in df_model
existing_num_feats = [f for f in numerical_features_demo if f in df_model.columns]
existing_cat_feats = [f for f in categorical_features_demo if f in df_model.columns]

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_pipeline, existing_num_feats),
        ('cat', categorical_pipeline, existing_cat_feats)
    ],
    remainder='passthrough' # Keep other columns (if any) not specified
)

print("\nPreprocessor created.")
print("Ensure your df_model, feature lists, and target names are correctly defined for your actual dataset.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 5.2. Regression Example (e.g., Linear Regression)
Predict a continuous numerical value.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Regression Task
if target_reg_demo in df_model.columns and (len(existing_num_feats) + len(existing_cat_feats) > 0):
    print(f"--- Regression using '{target_reg_demo}' as target ---")
    X_reg = df_model[existing_num_feats + existing_cat_feats]
    y_reg = df_model[target_reg_demo]

    # Handle potential NaNs in target before split
    if y_reg.isnull().any():
        print(f"Warning: Target column '{target_reg_demo}' has NaNs. Removing rows with NaN target for regression.")
        valid_indices = y_reg.notnull()
        X_reg = X_reg[valid_indices]
        y_reg = y_reg[valid_indices]

    if len(X_reg) > 1 and len(y_reg) > 1: # Need enough data to split
        X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

        # Create a full pipeline with preprocessor and model
        # Using RandomForestRegressor as a more robust default than LinearRegression for diverse data
        # regression_model = LinearRegression()
        regression_model = RandomForestRegressor(random_state=42)

        full_pipeline_reg = Pipeline(steps=[('preprocessor', preprocessor),
                                          ('regressor', regression_model)])

        print(f"Training a {type(regression_model).__name__} model...")
        full_pipeline_reg.fit(X_train_reg, y_train_reg)

        print("\nModel training complete.")
        y_pred_reg = full_pipeline_reg.predict(X_test_reg)

        # Evaluate the model
        mse = mean_squared_error(y_test_reg, y_pred_reg)
        r2 = r2_score(y_test_reg, y_pred_reg)
        print(f"\nRegression Model Evaluation ({type(regression_model).__name__}):")
        print(f"Mean Squared Error (MSE): {mse:.4f}")
        print(f"R-squared (R2 Score): {r2:.4f}")

        # Plot actual vs. predicted
        plt.figure(figsize=(8,6))
        plt.scatter(y_test_reg, y_pred_reg, alpha=0.7)
        plt.plot([y_test_reg.min(), y_test_reg.max()], [y_test_reg.min(), y_test_reg.max()], '--k', lw=2) # Diagonal line
        plt.xlabel('Actual Values')
        plt.ylabel('Predicted Values')
        plt.title(f'Regression: Actual vs. Predicted ({type(regression_model).__name__})')
        plt.show()
    else:
        print(f"Not enough data or valid target values in '{target_reg_demo}' for regression example after NaN handling.")
else:
    print(f"Regression target '{target_reg_demo}' not in DataFrame columns or no features defined. Skipping regression example.")
        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 5.3. Classification Example (e.g., Logistic Regression or Random Forest)
Predict a categorical class label.
        """
    ))

    notebook_cells.append(create_code_cell(
        """# Classification Task
if target_clf_demo in df_model.columns and (len(existing_num_feats) + len(existing_cat_feats) > 0):
    print(f"\n--- Classification using '{target_clf_demo}' as target ---")
    X_clf = df_model[existing_num_feats + existing_cat_feats]
    y_clf = df_model[target_clf_demo]

    # Handle potential NaNs in target before split
    if y_clf.isnull().any():
        print(f"Warning: Target column '{target_clf_demo}' has NaNs. Removing rows with NaN target for classification.")
        valid_indices_clf = y_clf.notnull()
        X_clf = X_clf[valid_indices_clf]
        y_clf = y_clf[valid_indices_clf]

    # Ensure target is integer type for some classifiers if it's like 0.0, 1.0
    if pd.api.types.is_float_dtype(y_clf) and y_clf.apply(lambda x: x.is_integer()).all():
        y_clf = y_clf.astype(int)


    if len(X_clf) > 1 and len(y_clf) > 1 and y_clf.nunique() > 1: # Need enough data and at least 2 classes
        X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42, stratify=y_clf if y_clf.nunique() > 1 else None)

        # Create a full pipeline with preprocessor and model
        # Using RandomForestClassifier as a robust default
        # classification_model = LogisticRegression(random_state=42, max_iter=1000)
        classification_model = RandomForestClassifier(random_state=42)

        full_pipeline_clf = Pipeline(steps=[('preprocessor', preprocessor),
                                          ('classifier', classification_model)])

        print(f"Training a {type(classification_model).__name__} model...")
        full_pipeline_clf.fit(X_train_clf, y_train_clf)

        print("\nModel training complete.")
        y_pred_clf = full_pipeline_clf.predict(X_test_clf)
        y_pred_proba_clf = full_pipeline_clf.predict_proba(X_test_clf)[:, 1] # Probability for class 1

        # Evaluate the model
        accuracy = accuracy_score(y_test_clf, y_pred_clf)
        print(f"\nClassification Model Evaluation ({type(classification_model).__name__}):")
        print(f"Accuracy: {accuracy:.4f}")
        print("\nClassification Report:")
        print(classification_report(y_test_clf, y_pred_clf))
        print("\nConfusion Matrix:")
        cm = confusion_matrix(y_test_clf, y_pred_clf)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.title('Confusion Matrix')
        plt.show()
    else:
        print(f"Not enough data, valid target values in '{target_clf_demo}', or not enough classes for classification example after NaN handling.")

else:
    print(f"Classification target '{target_clf_demo}' not in DataFrame columns or no features defined. Skipping classification example.")

        """
    ))

    notebook_cells.append(create_markdown_cell(
        """## 5.4. Further Steps in Modeling
*   **Hyperparameter Tuning:** Use techniques like GridSearchCV or RandomizedSearchCV to find the best settings for your model.
*   **Cross-Validation:** Get a more robust estimate of model performance.
*   **Try Different Models:** Experiment with various algorithms suitable for your problem (e.g., SVM, Gradient Boosting, Neural Networks).
*   **Feature Engineering:** Create new features from existing ones to potentially improve model performance.
*   **Interpretability:** Understand why your model makes certain predictions (e.g., using SHAP or LIME).
        """
    ))

# This function will be called later when assembling the notebook.

def add_introductory_cells(notebook_cells):
    """Adds introductory markdown cells to the notebook_cells list."""
    notebook_cells.append(create_markdown_cell(
        """# AI-Generated Data Analysis & Modeling Notebook
This Colab notebook provides a comprehensive template for a typical data science workflow, including:
1.  **Data Loading and Cleaning**: Importing data and handling common issues like missing values and duplicates.
2.  **Exploratory Data Analysis (EDA)**: Understanding data characteristics through statistics and preliminary checks.
3.  **Plotting and Visualization**: Creating various plots to uncover insights and trends.
4.  **Q&A on Data**: Querying and filtering data to answer specific questions.
5.  **Predictive Modeling**: Building and evaluating basic regression and classification models.

**How to Use This Notebook:**
*   **Replace Placeholders**: Look for comments like `# Replace with your data...` or instructions to modify code for your specific dataset.
*   **Upload Your Data**: If using Colab, you can upload your data files to the session storage (use the file explorer pane on the left) or load data from a URL.
*   **Run Cells Sequentially**: Execute cells one by one, especially during the initial run, to ensure dependencies are met.
*   **Adapt and Extend**: This is a template. Feel free to add more specific analyses, plots, or models relevant to your project.
*   **Install Libraries**: If any `ImportError` occurs, you might need to install libraries. In a Colab code cell, you can run `!pip install library_name`. Common libraries used here (pandas, numpy, matplotlib, seaborn, scikit-learn) are pre-installed in Colab environments.

Let's get started!
        """
    ))
    # Add an empty code cell at the beginning for any initial user setup if they prefer
    notebook_cells.append(create_code_cell("# You can add any initial setup code here (e.g., !pip install some_package)"))


def add_concluding_cells(notebook_cells):
    """Adds concluding markdown cells to the notebook_cells list."""
    notebook_cells.append(create_markdown_cell(
        """# 6. Conclusion and Next Steps
This notebook has walked through a foundational data science workflow:
*   Loading and meticulously cleaning a dataset.
*   Performing exploratory data analysis to understand its nuances.
*   Visualizing data to identify patterns and relationships.
*   Querying the data to answer specific questions.
*   Building and evaluating baseline predictive models for both regression and classification tasks.

**Next Steps for Your Project:**
*   **Deep Dive into Your Data**: Spend more time on EDA and feature engineering specific to your dataset's domain.
*   **Advanced Modeling**: Explore more complex models, hyperparameter tuning (e.g., GridSearchCV, RandomizedSearchCV), and ensemble methods.
*   **Cross-Validation**: Implement robust cross-validation strategies for more reliable model evaluation.
*   **Interpretability**: Use tools like SHAP or LIME to understand your model's predictions.
*   **Deployment**: If applicable, consider how you might deploy your trained model (e.g., using Flask, FastAPI, or cloud services).
*   **Iterate**: Data science is an iterative process. Revisit earlier steps as you learn more or as project requirements evolve.

Happy analyzing and modeling!
        """
    ))
    notebook_cells.append(create_code_cell(
        """# Thank you for using the AI-Generated Notebook!
# Feel free to share feedback or suggest improvements.
        """
    ))

# These functions will be called when assembling the full notebook.

def main():
    """Main function to generate the notebook."""
    notebook = initialize_notebook()
    cells = notebook['cells'] # Get a reference to the cells list

    # Add all sections
    add_introductory_cells(cells)
    add_data_loading_cleaning_section(cells)
    add_eda_section(cells)
    add_plotting_section(cells)
    add_q_and_a_section(cells)
    add_predictive_modeling_section(cells)
    add_concluding_cells(cells)

    # Save the notebook
    notebook_filename = "AI_Generated_Data_Notebook.ipynb"
    save_notebook(notebook, notebook_filename)
    print(f"Successfully generated and saved '{notebook_filename}'")

if __name__ == "__main__":
    main()
