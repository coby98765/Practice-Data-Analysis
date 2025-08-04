import pandas as pd
import json

class FileHandler:
    # turns a .csv to a pandas DataFrame
    @staticmethod
    def get_df(file_path):
        try:
            df = pd.read_csv(file_path)
            print("CSV file loaded successfully!")
            print(df.info())
            return df
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # export report .json file
    @staticmethod
    def export_json(data):
        file_path = f"results/results.json"
        # adjusting data keys to match JSON prot.
        print(f"Exporting JSON file: {file_path}...")
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"An error occurred: {e}")