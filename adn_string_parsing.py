#An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
#Given a DNA string t corresponding to a coding strand,
# its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
#Given: A DNA string t having length at most 1000 nt.
#Return: The transcribed RNA string of t.

ADN = 'GATGGAACTTGACTACGTAAATT'

def sequence_occurence (ADN, nucleide1, nucleide2):
    #the method replace ALL the occurences of T to U
    nucleide1 = 'T'
    bucleide2 = 'U'
    RNA = sequence.replace(nucleide1,nucleide2)
    print (RNA)

#The output :

# RNA = GAUGGAACUUGACUACGUAAAUU
#___________________________________________________________#

#A string is simply an ordered collection of symbols selected from
# some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
#An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
#Given: A DNA string s of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

ADN = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

def count_occurences(ADN):

    occurence_A = ADN.count('A')

    occurence_T = ADN.count('T')

    occurence_C = ADN.count('C')

    occurence_D = ADN.count('D')

    return (ADN.count('A') + '' + ADN.count('T') + '' + ADN.count('C') + ADN.count('D'))

#Output : 20 12 17 21

#_________________________________________________________#

#In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
#The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
# then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
#Given: A DNA string s of length at most 1000 bp.
#Return: The reverse complement sc of s.

ADN = 'AAAACCCGGT'

def reverse_complement(ADN, nucleide1,nucleide2,nucleide3, nucleide4):

    #define nucleides

    nucleide1 = 'A'
    nucleide2 = 'T'
    nucleide3 = 'C'
    nucleide4 = 'G'
    #first step is to reverse the ADN:

    reversed_ADN = ADN[::-1]

#((((DO A FOR LOOP))))
    #second step: use the function sequence occurence to change the values of A,T,C,G
    changed_ADN = sequence_occurence(ADN,nucleide1 ,nucleide2 )

    final_ADN = sequence_occurence(ADN,nucleide3 ,nucleide3 )

    return final_ADN

#_________________________________________________#
