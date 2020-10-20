# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# Given a DNA string t corresponding to a coding strand,
# its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

ADN = 'GATGGAACTTGACTACGTAAATT'

# the method replace ALL the occurences of T to U
# Proper documentation
# Output : RNA = GAUGGAACUUGACUACGUAAAUU
def swap_nuclides(DNA, nucleide1, nucleide2):
    RNA = DNA.replace(nucleide1, nucleide2)
    return RNA

# A string is simply an ordered collection of symbols selected from
# some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
# Output : 20 12 17 21
def count_nuclides(DNA):
    occurence_A = DNA.count('A')
    occurence_T = DNA.count('T')
    occurence_C = DNA.count('C')
    occurence_G = DNA.count('G')
    print('Nuclide A count: ' + str(occurence_A) + '\n' +
            'Nuclide T count: ' + str(occurence_T) + '\n' +
            'Nuclide C count: ' + str(occurence_C) + '\n' +
            'Nuclide G count: ' + str(occurence_G))



# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
# then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

DNA = 'AAAACCCGGT'

def reverse_complement(DNA):
    # first step is to reverse the ADN
    reversed_DNA = ADN[::-1]

    #second step: use the function swap_nuclides to change the values of A,T,C,G
    complement_DNA = swap_nuclides(reversed_DNA, 'A', 'T')
    final_DNA = swap_nuclides(complement_DNA, 'C', 'G')

    return final_DNA


