#! usr/bin/python 3.15
# Rodrigo Barber, November 2025

# It is created a class named Procesamiento_ADN which models the transcription and translation of a DNA sequence 
# First it is necessary to crate an object of this class

'''
    Parameters (of the class)
    ----------
    str
        DNA sequence in a single string

    Returns (depend on the method)
    -------
    - transcription= str, the mRNA sequence originated by the DNA sequence
    - translation= str, the protein sequence originated by the mRNA 
'''
class Procesamiento_ADN:

    def __init__(self, seq):
        self.seq=seq

    def transcription(self):
        # method that transcribes a DNA sequence of interest

        ARNm= ""
        for nt in self.seq:
            if nt == "T":
                ARNm += "U"
            else:
                ARNm += nt

        result = "" # introduce a line break each 60 lines
        for i in range(0, len(ARNm), 60):
            bloque = ARNm[i:i+60]
            result += bloque + "\n"  

        return result
    
    def translation(self):
        # method that translates a sequence of interest

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

        protein = ""
        for i in range(0, len(self.seq) - 2, 3): # go through a sequence of 3 at a time (until the length of the sequence - two)
            codon = self.seq[i:i+3]
            aminoacid = genetic_code.get(codon, 'X') # if there is no codon, put X
            protein += aminoacid

        result = "" # introduce a line break each 60 lines
        for i in range(0, len(protein), 60):
            bloque = protein[i:i+60]
            result += bloque + "\n"  

        return result