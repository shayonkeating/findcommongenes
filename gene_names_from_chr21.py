"""This program will ask the user to enter a gene symbol and then prints
the description for that gene based on data from the chr21_genes.txt file."""
import argparse


# Open the file and read all lines into a list
def read_genes(infile):
    """Reads the infile and will read each line
    in the infile and split it then store in a dictionary"""
    gene_dict = {}
    with open(infile, 'r') as file:
        for line in file:
            gene_info = line.strip().split('\t')
            gene_dict[gene_info[0].lower()] = gene_info[1]
    return gene_dict


# Parse command line arguments
PARSER = argparse.ArgumentParser(description='Open chr21_genes.txt, \
                                 and ask user for a gene name')
PARSER.add_argument('-i', '--infile', help='Path to the file to open', required=True)
ARGS = PARSER.parse_args()

# Read gene names and descriptions from file into dictionary
GENE_DICT = read_genes(ARGS.infile)


# Ask user for gene names and print descriptions until "quit" or "exit" is entered
while True:
    GENE_NAME = input(f'Enter gene name of interest. Type quit or exit to exit: ').lower()
    if GENE_NAME in ('quit', 'exit'):
        print(f'Thanks for querying the data. See you again soon :)')
    elif GENE_NAME in GENE_DICT:
        print(f'{GENE_NAME.upper()} found! Here is the description: {GENE_DICT[GENE_NAME]}')
    else:
        print(f'Not a valid gene name.')
