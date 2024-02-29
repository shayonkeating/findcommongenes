"""This program will serve if i need to pull old code to solve new code problems"""
import sys


def get_filehandle(file=None, mode=None):
    "this function will get the file handle and toss errors if it arises"
    try:
        fobj = open(file, mode)
        return fobj
    except OSError:
        print(f"Could not open the file: {file} for type '{mode}'", file=sys.stderr)
        raise
    except ValueError:
        print(f"Could not open the file: {file} for type '{mode}'", file=sys.stderr)
        raise


def get_fasta_lists(fh_in):
    """list, list: get_fasta_lists(fh_in)"""

    header_list = []
    seq_list = []
    current_seq = ''

    for line in fh_in:
        if line[0] == ">":
            header_list.append(line[1:].rstrip('\n'))
            if current_seq != '':
                seq_list.append(current_seq)
            current_seq = ''
        else:
            current_seq += line.rstrip('\n')

    if current_seq:
        seq_list.append(current_seq)

    _verify_lists(header_list=header_list, seq_list=seq_list)

    return header_list, seq_list


def _verify_lists(header_list=None, seq_list=None):
    """This function will verify if the lists are the same size and toss an error if not"""
    size1 = len(header_list)
    size2 = len(seq_list)
    if size1 != size2:
        sys.exit("Header and sequence sizes do not match!")
    else:
        return True
