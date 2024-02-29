"""This program counts how many genes are in each category (1.1, 1.2, 2.1 etc.)
based on data from the chr21_genes.txt file."""
import argparse

# Parse command line arguments
PARSER = argparse.ArgumentParser(description='Combine on gene name and count the category occurrence')
PARSER.add_argument('-i1', '--infile1', type=str, help='Path to the gene description file to open')
PARSER.add_argument('-i2', '--infile2', type=str, help='Path to the gene category to open')
ARGS = PARSER.parse_args()

# Define a dictionary to store gene categories and their counts
CATEGORY_COUNTS = {'1.1': 0, '1.2': 0, '2.1': 0, '2.2': 0, '3.1': 0, '3.2': 0, '4.1': 0, '4.2': 0, '4.3': 0, '5': 0}

# Read the gene category file and populate the dictionary
CATEGORY_DESCRIPTIONS = {}
with open(ARGS.infile2, 'r') as f:
    for line in f:
        fields = line.strip().split('\t')
        CATEGORY_DESCRIPTIONS[fields[0]] = fields[1]

# Read the gene description file and update the count dictionary
with open(ARGS.infile1, 'r') as f:
    for line in f:
        fields = line.strip().split('\t')
        if len(fields) >= 3 and fields[2] in CATEGORY_COUNTS:
            CATEGORY_COUNTS[fields[2]] += 1

# Write the output to a file
with open('OUTPUT/categories.txt', 'w') as f:
    f.write('Category\tOccurrence\tDescription\n')
    for category in sorted(CATEGORY_COUNTS.keys()):
        f.write(f'{category}\t{CATEGORY_COUNTS[category]}\t{CATEGORY_DESCRIPTIONS[category]}\n')
