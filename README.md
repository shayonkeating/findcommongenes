## 🚀 Finding common genes?

This project is meant to find common gene names from various text files and can be ran in a linux terminal 
console and can be executed for data text file. All of these programs can be ran on the command line.
gene_names_from_chr21.py will take the gene names from the chr21_genes text file. 
find_common_cats.py will find for common gene categories in it. intersection_of_gene_names.py
will compare two texts files for similar genes.

io_utils.py can be used as well for getting the filehandle or other functions that exist in it


## 🚦 Running the Project

Everything is to be ran in a linux CLI.

```shell
python3 gene_names_from_chr21.py -i data/chr21_genes.txt
python3 find_common_cats.py -i1 data/chr21_genes.txt -i2 data/chr21_genes_categories.txt
python3 intersection_of_gene_names.py -i1 data/chr21_genes.txt -i2 data/HUGO_genes.txt
```

## 🛠️ Technologies

- `Python`
- `Bioinformatics`

## 💡 Improvements

- Adding a main file to automate the entire workflow (I'll get around to it one day)

## 🐞 Issues

- None (so far)