# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# Given a DNA string t corresponding to a coding strand,
# its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.


# the method replace ALL the occurences of T to U
# Proper documentation
def replace_nuclides(DNA, nuclide1, nuclide2):
    RNA = DNA.replace(nuclide1, nuclide2)
    return RNA

# A string is simply an ordered collection of symbols selected from
# some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
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

def reverse_complement(DNA):
    # first step is to reverse the ADN
    reversed_DNA = DNA[::-1]
    # second step:
    final_DNA = ''

    for c in reversed_DNA:
        if(c == 'G'):
            final_DNA += 'C'
        elif(c == 'C'):
            final_DNA += 'G'
        elif(c == 'A'):
            final_DNA += 'T'
        else:
            final_DNA += 'A'

    return final_DNA

