import json
from datetime import datetime

# Function to process a JSON file and return unique sorted messages
def process_file(filename, output_file):
    with open(filename, 'r') as f:
        data = json.load(f)

    for item in data:
        item['timestamp'] = datetime.fromisoformat(item['timestamp'].replace("Z", "+00:00"))

    sorted_data = sorted(data, key=lambda x: x['timestamp'])

    unique_data = []
    seen_messages = set()
    for item in sorted_data:
        if item['content'] not in seen_messages:
            unique_data.append(item)
            seen_messages.add(item['content'])

    max_username_length = max(len(item['author']['username']) for item in unique_data)

    # Write to a file
    with open(output_file, 'w') as f:
        for item in unique_data:
            formatted_time = item['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"[{formatted_time}][{item['author']['username']: <{max_username_length}}]: {item['content']}\n")

# Process each file and write to separate output files
process_file('trace2_dc_chat.json', 'sorted_chat_2.log')
process_file('trace3_dc_chat.json', 'sorted_chat_3.log')