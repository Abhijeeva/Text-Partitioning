# Import the necessary libraries
import re
import csv
import pandas as pd

class TextPartitioner:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def read_file(self):
        with open(self.input_file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def partition_text(self, label):
        text = self.read_file()

        # Use regular expression to split text into sentences
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

        # Initialize variables for tracking the partitions
        partitions = []
        partition_count = 0
        word_count = 0
        current_partition = []

        # Iterate through sentences and form partitions
        for sentence in sentences:
            words = sentence.split()
            word_count += len(words)
            current_partition.append(sentence)

            # Check if the word count for the current partition reaches 100
            if word_count >= 100:
                partitions.append(' '.join(current_partition))
                current_partition = []
                partition_count += 1
                word_count = 0

            # Check if 200 partitions are reached
            if partition_count == 200:
                break

        # Save the partitions to a CSV file with the specified label
        output_file_path = f"output_{label}.csv"
        with open(output_file_path, 'w', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Partitioned Text', 'Label'])

            for i, partition in enumerate(partitions):
                csv_writer.writerow([partition, label])


# Example usage
if __name__ == "__main__":
    file_path_a = r"path_to_your_file.txt"
    partitioner_a = TextPartitioner(file_path_a)
    partitioner_a.partition_text('a')

# Example usage
if __name__ == "__main__":
    file_path_b = r"path_to_your_file.txt"
    partitioner_b = TextPartitioner(file_path_b)
    partitioner_b.partition_text('b')

# Example usage
if __name__ == "__main__":
    file_path_c = r"path_to_your_file.txt"
    partitioner_c = TextPartitioner(file_path_c)
    partitioner_c.partition_text('c')

   
import pandas as pd

# Specify the paths to your CSV files
csv_file_paths = ['output_a.csv', 'output_b.csv', 'output_c.csv']

# Create an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Read each CSV file and concatenate its data to the combined DataFrame
for file_path in csv_file_paths:
    df = pd.read_csv(file_path)
    combined_data = pd.concat([combined_data, df], ignore_index=True)

# Save the combined data to a new CSV file
combined_data.to_csv('combined_dataset.csv', index=False)

# Display the combined data
print(combined_data)