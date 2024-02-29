"""This program that finds all gene symbols that appear both in the
chr21_genes.txt file and in the HUGO_genes.txt file."""
import argparse

OUTPUT_FILE = "OUTPUT/intersection_output.txt"


def read_genes(filename):
    """
    Reads a gene list file and returns a set of gene symbols.
    """
    genes = set()
    with open(filename, "r") as file:
        # skip header line if exists
        if file.readline().startswith("#"):
            file.readline()
        for line in file:
            gene = line.strip().split("\t")[0]
            genes.add(gene)
    return genes


def find_common_genes(genes1, genes2):
    """
    Finds the common genes between two sets of gene symbols.
    """
    common_genes = genes1.intersection(genes2)
    return common_genes


def write_genes(filename, genes):
    """
    Writes a set of gene symbols to a file in alphabetical order.
    """
    with open(filename, "w") as file:
        for gene in sorted(genes):
            file.write(gene + "\n")


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="Provide two gene list (ignore header line), find intersection")
    PARSER.add_argument("-i1", "--infile1", type=str, required=True, help="Gene list 1 to open")
    PARSER.add_argument("-i2", "--infile2", type=str, required=True, help="Gene list 2 to open")
    ARGS = PARSER.parse_args()

    GENES1 = read_genes(ARGS.infile1)
    GENES2 = read_genes(ARGS.infile2)
    COMMONG_GENES = find_common_genes(GENES1, GENES2)

    NUM_GENES1 = len(GENES1)
    NUM_GENES2 = len(GENES2)
    NUM_COMMON_GENES = len(COMMONG_GENES)

    write_genes(OUTPUT_FILE, COMMONG_GENES)

    print(f"Number of unique gene names in {ARGS.infile1}: {NUM_GENES1}")
    print(f"Number of unique gene names in {ARGS.infile2}: {NUM_GENES2}")
    print(f"Number of common gene symbols found: {NUM_COMMON_GENES}")
    print(f"Output stored in {OUTPUT_FILE}")
