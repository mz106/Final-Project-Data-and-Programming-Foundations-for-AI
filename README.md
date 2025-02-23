# Final-Project-Data-and-Programming-Foundations-for-AI

## Overview

This project analyzes Netflix movie and series data to explore patterns in genres and runtime distributions. Using Python and various data processing, transformation, visualization, and statistical analysis techniques, we aim to uncover insights about Netflix content.

Features

Data Processing: Cleans and prepares the dataset.

Data Transformation: Standardizes text, fills missing values, and splits multi-genre entries.

Data Visualization: Generates charts to display genre distribution.

Statistical Analysis: Performs a Chi-Square test to analyze relationships between genres and runtime.

Repository Structure

```
.
├── data_processor.py # Handles data loading and initial processing
├── data_transformer.py # Applies transformations like text standardization and missing value handling
├── data_visualizer.py # Creates visual representations of data
├── data_stats.py # Conducts statistical analysis
├── dataset_converted.csv # Processed dataset (not included in repo for privacy)
├── netflix_final.ipynb # Jupyter Notebook with analysis and visualizations
└── README.md # Project documentation
```

Setup Instructions

Prerequisites

Ensure you have Python installed along with the required dependencies.

Clone the repository:

```
git clone https://github.com/mz106/Final-Project-Data-and-Programming-Foundations-for-AI.git
cd Final-Project-Data-and-Programming-Foundations-for-AI
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the Jupyter Notebook:

```
jupyter notebook netflix_final.ipynb
```

Usage

Load and process the dataset using DataProcessor.

Apply transformations such as text standardization and missing value imputation using DataTransformer.

Visualize genre distributions with DataVisualizer.

Perform statistical tests using DataStats to analyze relationships in the data.

Modify and extend the analysis as needed.

Results

Genre Distribution: Bar plots showcasing the most common Netflix genres.

Genre-Runtime Analysis: Statistical insights into whether movie/series runtimes are significantly different across genres.

Genre-IMDb Votes Analysis: Statistical insights into whether movie/series IMDb Votes are significantly different across genres.

Potential Improvements

Add more data visualizations (e.g., boxplots for runtime per genre).

Expand the statistical analysis to include correlation tests.

Improve Markdown documentation within the notebook.

License

This project is for educational purposes. You are free to modify and use the code.

Contact

For questions or contributions, please reach out via GitHub Issues.

Happy coding! 🚀
