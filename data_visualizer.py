
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    #command line inputs from user parsed
    parser = argparse.ArgumentParser(description='CSV File Reader')
    parser.add_argument('input_file', type=str, help='/Users/poulami/Documents/creditcard.csv')
    parser.add_argument('--color', type=str, default='blue', help='Color for visualizations')
    parser.add_argument('--title', type=str, default='Data Visualization', help='Title for visualizations')
    parser.add_argument('--stats', action='store_true', help='Calculate and display basic statistics')
    args = parser.parse_args()
    
    # Check if the input file exists
    if not os.path.isfile(args.input_file):
        print(f"File not found: {args.input_file}")
        return
    
    # Read the CSV file
    try:
        df = pd.read_csv(args.input_file)
        
        # Detect data types of each column
        data_types = df.dtypes
        
        # Lists to store the filenames of saved images
        saved_image_filenames = []
        
        # Loop through each column and its data type
        for column, data_type in data_types.items():
            plt.figure()
            plt.title(args.title)  # Use custom title before creating the plot
            plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[args.color])  # Use custom color
            
            # Generate different types of plots based on data type
            if data_type == 'int64' or data_type == 'float64':
                if args.stats:
                    calculate_and_display_statistics(df[column])
                df[column].plot(kind='hist', title=f'Histogram of {column}')
            elif data_type == 'object':
                df[column].value_counts().plot(kind='bar', title=f'Bar Plot of {column}')
            elif data_type == 'datetime64[ns]':
                if len(df[column]) > 1:
                    plt.plot(df[column], df[column].index)
                    plt.title(f'Time Series Plot of {column}')
                else:
                    print(f"Not enough data points to generate a time series plot for {column}.")
            
            # Save the visualization as a PNG file
            image_filename = f'{column}_plot.png'
            plt.savefig(image_filename)
            saved_image_filenames.append(image_filename)
            
        # Generate an HTML report
        generate_html_report(saved_image_filenames, args.title)  # Pass the custom title
        
    except pd.errors.EmptyDataError:
        print("The file is empty or contains no valid data.")
    except Exception as e:
        print(f"An error occurred: {e}")

def calculate_and_display_statistics(column_data):
    mean = column_data.mean()
    median = column_data.median()
    mode = column_data.mode().iloc[0]
    print(f"Statistics:\nMean: {mean}\nMedian: {median}\nMode: {mode}\n")

#generating the HTML report with embedded visualizations
def generate_html_report(image_filenames, title):
    with open('report.html', 'w') as f:
        f.write('<html><head><title>{}</title>'.format(title))
        f.write('<style>body { font-family: Arial, sans-serif; }</style></head><body>')
        
        for image_filename in image_filenames:
            f.write('<h2>{}</h2>'.format(image_filename))
            f.write('<img src="{}" alt="{}">'.format(image_filename, image_filename))
            f.write('<hr>')  # Add a horizontal rule between sections
        
        f.write('</body></html>')

if __name__ == '__main__':
    main()



