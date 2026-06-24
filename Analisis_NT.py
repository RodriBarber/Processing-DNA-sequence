#!/usr/bin/env python3
# Rodrigo Barber, October 2025

# It is created a class named Analisis_cont_NT which models a sequence of DNA
# First it is necessary to crate an object of this class

'''
    Parameters (of the class)
    ----------
    str
        DNA sequence in a single string

    Returns (depend on the method)
    -------
    - content_CG= float, the percentage of C and G nucleotides in the sequence (sum together)
    - content_NT= dictionary, where the key is tHe nucleotide and the value the number of times that appear in the DNA sequence
    - lenght_seq= int, the length of the sequence
'''

class Analisis_cont_NT:

    def __init__(self, sequence):
        self.sequence = sequence

    def content_CG(self):
        # This method calculates the % of C and G of the sequence

        count_CG= 0

        for nt in self.sequence:
            if nt in ("C", "G"):
                count_CG +=1

        percentage_CG= (count_CG/len(self.sequence)) * 100
        return(percentage_CG)

    # This method calculates the total content of each nucleotide

    def content_NT(self):
        A=self.sequence.count("A")
        T=self.sequence.count("T")
        C=self.sequence.count("C")
        G=self.sequence.count("G")
        return { 
            "A": A,
            "T": T,
            "C": C,
            "G": G }
    
    # This method calculates the length of the sequence

    def length_seq(self):
        return(len(self.sequence))
