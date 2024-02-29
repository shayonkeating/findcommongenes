"""test for io_utils.py"""
import sys
import pytest


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


def test_get_filehandle(tmp_path):
    """test will run for test_get_filehandle"""
    # Test successful file opening
    test_file = tmp_path / 'test.txt'
    test_file.write_text('test')
    fobj = get_filehandle(file=str(test_file), mode='r')
    assert isinstance(fobj, type(sys.stdin))

    # Test file not found error
    with pytest.raises(OSError):
        get_filehandle(file='invalid_file.txt', mode='r')

    # Test invalid mode error
    with pytest.raises(ValueError):
        get_filehandle(file=str(test_file), mode='invalid')


def test_get_fasta_lists():
    """test will run for test_get_fasta_lists"""
    # Test successful parsing
    fasta_input = '>header1\nseq1\n>header2\nseq2\n'
    expected_header_list = ['header1', 'header2']
    expected_seq_list = ['seq1', 'seq2']
    fh_in = fasta_input.splitlines()
    header_list, seq_list = get_fasta_lists(fh_in)
    assert header_list == expected_header_list
    assert seq_list == expected_seq_list

    # Test empty file input
    fh_in = []
    header_list, seq_list = get_fasta_lists(fh_in)
    assert header_list == []
    assert seq_list == []

    # Test invalid FASTA format error
    fh_in = ['>header1\nseq1\ninvalid\n>header2\nseq2\n']
    with pytest.raises(SystemExit):
        get_fasta_lists(fh_in)


def test__verify_lists():
    """Test matching list sizes"""
    header_list = ['header1', 'header2']
    seq_list = ['seq1', 'seq2']
    assert _verify_lists(header_list, seq_list)

    # Test mismatching list sizes error
    header_list = ['header1', 'header2']
    seq_list = ['seq1']
    with pytest.raises(SystemExit):
        _verify_lists(header_list, seq_list)
