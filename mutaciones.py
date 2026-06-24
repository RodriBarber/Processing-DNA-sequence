#!/usr/bin/env python3
# Rodrigo Barber, November 2025

# It is created a class named Mutations that creates and evaluates mutations in a DNA Ssequence of interest
# First it is necessary to crate an object of this class

'''
    Parameters 
    ---------- of the class
    str
        DNA sequence in a single string

    --------- of each method
    - puntual_mutation= int, the position of the mutation
                        str, the nucleotide that we want to introduce
    - impact_mutation= int, the position of the mutation
                       str, the nucleotide that we want to introduce

    Returns (depend on the method)
    -------
    - puntual_mutation= str, DNA sequence with the mutation of interest
    - random_mutation= str, DNA sequence with random mutations
                       int, the positions of the mutations
    - impact_mutation= int, the position where the aminoacid changed
                       str, the amonoacid before and after the mutation
'''

class Mutations:

    def __init__(self, seq):
        self.seq = seq

    def puntual_mutation(self):
        # This method introduces a mutation at the desired position

        while True:
            try:
                position = int(input("Introduce la posición del NT a mutar: ")) - 1 #-1 to translate the position to python (the sequence starts in 0)
                if position <= 0 or position >= len(self.seq):
                    print("Error: posición fuera del rango")
                else:
                    break
            except ValueError:
                print("Error: la posición debe ser un número entero")

        while True:
            new_NT = input("Introduce el nuevo nucleótido (A, T, C, G): ").upper()
            if new_NT not in "ATCG":
                print("Error: nucleótido inválido (solo se acepta: A, T, C, G)")
            else:
                break

        DNA_mutated=""
        for pos, nt in enumerate(self.seq):
            if pos == position:
                DNA_mutated += new_NT 
            else:
                DNA_mutated += nt
    
        result = "" # introduce a line break each 60 lines
        for i in range(0, len(DNA_mutated), 60):
            bloque = DNA_mutated[i:i+60]
            result += bloque + "\n"  

        return result

    def random_mutation(self):
        # This method introduces random mutationes (from 1 to 1000 maximum)
        import random
        
        num_mutations= random.randint(1, len(self.seq)) # number of mutations (between 1 and de length of the sequence)
        positions= random.sample(range(len(self.seq)), num_mutations) # position of the mutations
        DNA_mutated=""

        for pos, NT in enumerate(self.seq):
            if pos in positions:
                new_NT = random.choice([nt for nt in "ATCG" if nt != NT])
                DNA_mutated += new_NT
            else:
                DNA_mutated += NT
        new_positions= [p + 1 for p in positions] # Transforms the position to be consistent with the positions of the sequence
        DNA_mutated_result = "" 

        for i in range(0, len(DNA_mutated), 60): # introduce a line break each 60 lines
            bloque = DNA_mutated[i:i+60]
            DNA_mutated_result += bloque + "\n" 

        return DNA_mutated_result, new_positions
    
    def impact_mutation(self):
         # This method requests a specific mutation and then compares the normal protein with the protein obtained from the mutated DNA sequence.

        while True:
            try:
                position = int(input("Introduce la posición del NT a mutar: ")) - 1 #-1 to translate the position to python (the sequence starts in 0)
                if position <= 0 or position >= len(self.seq):
                    print("Error: posición fuera del rango")
                else:
                    break
            except ValueError:
                print("Error: la posición debe ser un número entero")

        while True:
            new_NT = input("Introduce el nuevo nucleótido (A, T, C, G): ").upper()
            if new_NT not in "ATCG":
                print("Error: nucleótido inválido (solo se acepta: A, T, C, G)")
            else:
                break

        muted_DNA=""
        for pos, nt in enumerate(self.seq):
            if pos == position:
                muted_DNA += new_NT 
            else:
                muted_DNA += nt

        genetic_code = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',} # stop codons are marked with an asterisk

        muted_protein = ""
        for i in range(0, len(muted_DNA) - 2, 3): # go through a sequence of 3 at a time (until the length of the sequence - two)
            codon = muted_DNA[i:i+3]
            aminoacid = genetic_code.get(codon, 'X') # if there is no codon, put X
            muted_protein += aminoacid

        muted_protein_result = "" 
        for i in range(0, len(muted_protein), 60): # introduce a line break each 60 lines
            bloque = muted_protein[i:i+60]
            muted_protein_result += bloque + "\n" 

        normal_protein = ""
        for i in range(0, len(self.seq) - 2, 3):
            codon = self.seq[i:i+3]
            aminoacid = genetic_code.get(codon, 'X')
            normal_protein += aminoacid

        normal_protein_result = "" 
        for i in range(0, len(normal_protein), 60):
            bloque = normal_protein[i:i+60]
            normal_protein_result += bloque + "\n" 

        for i in range(len(normal_protein)):
            if normal_protein[i] != muted_protein[i]:
                return i +1, normal_protein[i], muted_protein[i], muted_protein_result, normal_protein_result # + 1 to be consistent with the positions of the sequence
            
        return None
