import pandas as pd
import os

data_folder = "./data"
output_file = "formatted_data.csv"

processed_dfs = []

for file_name in os.listdir(data_folder):
    if file_name.endswith(".csv"):

        file_path = os.path.join(data_folder, file_name)
        df = pd.read_csv(file_path)

        df = df[df['product'] == 'pink morsel']

        # Removing dollar sign and converting string into float type
        df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)

        df['sales'] = df['price'] * df['quantity'] # Multiplying price with quantity

        df = df[['sales', 'date', 'region']] # Keeping only the required columns

        processed_dfs.append(df)

final_df = pd.concat(processed_dfs, ignore_index=True)

final_df.to_csv(output_file, index=False)

print(f"Success! Processed data saved to {output_file}")