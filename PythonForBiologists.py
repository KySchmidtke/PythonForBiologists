# This script contains all exercises from Python for Biologists





print("NEW SECTION: REPLACEMENT METHOD FOR STRINGS")
# This section below is an example of the REPLACEMENT Method for STRINGS
protein = "vlspadktnv"
# replace valine with tyrosine
print("This is our protein with the V replaced by Y: " + protein.replace("v", "y"))
# we can replace more than one characters
print("This is our protein with the VLS replaced by YMW: " + protein.replace("vls", "ymw"))
# the origina variable is not affected
print("This is our original protein: " + protein)



print("                                  ")
print("NEW SECTION: EXTRACTING SUBSTRINGS")
# This section below is an example of EXTRACTING part of the string - SUBSTRING - 
protein = "vlspadktnv"
# print positions three to five
print(protein[3:5])
print("Python begins counting from position 0 rather than 1")
# positions start at zero, not one
print(protein[0:6])
print("Positions are inclusive with the start, but excluse with the stop. This means that the string that is returned starts from 0 and stops prior to printing the 6 character")
# if we use a stop position beyond the end, it's the same as using the end 
print(protein[0:60])

first_residue = protein[0]
print(first_residue)



print("                                  ")
print("NEW SECTION: COUNTING AND FINDING SUBSTRINGS") # REPLACE COUNT FIND
# This section below is an example of the COUNT METHOD which is used to count how many times a string occurs
protein = "vlspadktnv"
# count amino acid residues 
valine_count = protein.count('v')
lsp_count = protein.count('lsp')
tryptophan_count = protein.count('w')

# now print the counts. Must convert to strings because we CANNOT print counts
print("valines: " + str(valine_count))
print("lsp: " + str(lsp_count))
print("tryptophan: " + str(tryptophan_count))

# Find Method - returns the number in which the position of that substring is - This is called the index 
protein = "vlspadktnv"
print(str(protein.find('p')))
print(str(protein.find('kt')))
print(str(protein.find('w'))) # the output for searching for a substring that doesn't exist is -1

# my_dna.count(my_motif) != my_motif.count(my_dna)

print("                                  ")
print("EXERCISE 1")
print("                                  ")
print("                                  ")

print("Exercise 1.1: Calculate the AT Content within the DNA Sequence")
print("                                  ")

dna_sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAAT" 
print("This is the DNA Sequence: " + dna_sequence)
at_count = dna_sequence.count('AT')
print("This is the AT count in the DNA Sequence: " + str(at_count))

print("                                  ")




print("Exercise 1.2: Write a program that will print the complement of the DNA sequence") # EXERCISE 1.2
print("                                  ")

# We want the complement DNA Sequence so we are replacing these combinations in the original dna_sequence
# A = T
# G = C
# C = G
# T = A


dna_sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAAT" 
print("This is the original sequence: " + dna_sequence)

dna_sequence_comp = dna_sequence.replace('T', 'X')
dna_sequence_comp_1 = dna_sequence_comp.replace('A', 'T')
dna_sequence_comp_2 = dna_sequence_comp_1.replace('X', 'A')
dna_sequence_comp_3 = dna_sequence_comp_2.replace('G', 'Y')
dna_sequence_comp_4 = dna_sequence_comp_3.replace('C', 'G')
dna_sequence_comp_5 = dna_sequence_comp_4.replace('Y', 'C')

print("This is the complement sequence: " + dna_sequence_comp_5)