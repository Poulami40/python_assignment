# python_assignment
Python assignment for ProgrammingwithMaurya

# CSV Data Visualizer

The CSV Data Visualizer is a command-line tool that allows users to input a dataset in CSV format and generate various visualizations based on the data type of each column. It also provides options to customize the visualizations, calculate statistics, and detect correlations between numeric columns.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Assumptions](#assumptions)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository to your local machine:

  git clone https://github.com/Poulami40/python_assignment.git
  cd data_visualizer.csv

2. Install the required dependencies using pip:

  pip install -r requirements.txt

## Usage

Run the CSV Data Visualizer from the command line by providing the path to your CSV file. Optionally, you can specify customization options:

python data_visualizer.py input_file.csv --color 'blue' --title 'Data Visualization' --stats


The above command will generate visualizations using the specified color, title, and calculate statistics for numeric columns.

## Customization

- `--color`: Specify a color for all visualizations (e.g., 'blue', 'red', '#FF5733').
- `--title`: Provide a custom title for all visualizations.
- `--stats`: Include this flag to calculate and display basic statistics for numeric columns.

## Assumptions

- The CSV file is structured with headers in the first row.
- Numeric columns are identified based on the 'int64' and 'float64' data types.
- Categorical columns are identified based on the 'object' data type.
- Date columns are identified based on the 'datetime64[ns]' data type.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



