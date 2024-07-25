import pandas as pd
import json

# Load the Excel file into a DataFrame
excel_file_path = './LinkedIn_post.xlsx'
df = pd.read_excel(excel_file_path)

# Open the JSONL file for writing
jsonl_file_path = './output.jsonl'
with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        # Create the JSON object
        json_object = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": row["prompt"]},
                {"role": "assistant", "content": row["completion"]}
            ]
        }
        # Write the JSON object to the file
        jsonl_file.write(json.dumps(json_object, ensure_ascii=False) + '\n')
print(f"Excel file converted to JSONL and saved to {jsonl_file_path}")
