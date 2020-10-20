import adn_string_parsing

if __name__ == "__main__":
    # test 1
    DNA = 'GATGGAACTTGACTACGTAAATT'
    RNA = adn_string_parsing.replace_nuclides(DNA, 'T', 'U')
    assert RNA == 'GAUGGAACUUGACUACGUAAAUU'

    # test 2
    DNA2 = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    count = adn_string_parsing.count_nuclides(DNA2)

    # test 3
    DNA3 = 'AAAACCCGGT'
    rv = adn_string_parsing.reverse_complement(DNA3)
    assert rv == 'ACCGGGTTTT', rv
