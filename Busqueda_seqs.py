#! usr/bin/python 3.15
# Rodrigo Barber, November 2025

# It is created a class named Search that finds in a DNA equence different inputs (short sequences,repetitive sequences and motifs)
# First it is necessary to crate an object of this class

'''
    Parameters
    ---------- of the class
    str
        DNA sequence in a single string

    ---------- of each method
    - gene_search= str, DNA sequence in a single string (gene)
    - motif_seacrh= str, DNA sequence in a single string (motif)
    
    Returns (depend on the method)
    -------
    - gene_search= int, the position of the firts and the last nucleotide of the sequence of interest (regarding the DNA sequence)
    - repeated_sequences= dictionary, the key is the number of NT repeated and the value is the another dicctionary with the subsequence and thenumber of times it is repeated.
    - motif_seacrh= int, the frecuence of the sequence of interest (regarding the DNA sequence)
'''
class Search:

    def __init__(self, seq):
        self.seq = seq
  
    def gene_search(self):
       # Method that search the position of a specific sequence in the DNA sequence

        while True:
            gene = input("Introduzca secuencia de interés en mayúsculas: ")

            if not gene:
                print("Error: la secuencia está vacía")
            elif not all(nt in "ATCG" for nt in gene):
                print("Error: la secuencia contiene algún carácter inválido. Solo se permiten A, T, C, G")
            else:
                break  
       
        if gene not in self.seq:
          return("La secuencia de interes no esta en las ecuencia de ADN")
       
        else:
          start = self.seq.find(gene) + 1 # +1, to start the count in 1 and not in 0
          end = start + len(gene)
          return start, end
       
    def repeated_sequences(self, k_min=10, k_max=20):
       # Method that search in the DNA sequence for repeated subsequences (between 10 and 20 nucleotides long)

        result = {}
    
        for k in range(k_min, k_max +1): # +1, to start the count in 1 and not in 0
            counted = {}
            for i in range(len(self.seq) - k + 1):
                sub = self.seq[i:i+k]
                counted[sub] = counted.get(sub, 0) + 1
        
            repeated_subseq = {}
            for sub, count in counted.items(): 
                if count > 1:  # Filter only those that appear more than once
                    repeated_subseq[sub] = count
        
            if repeated_subseq:
                result[k] = repeated_subseq
        if not result:
            return("No hay secuencias repetidas de una longitud de entre 10 y 20 NT")
        else:
            return result

    def motif_search(self):
        # Method that search the frecuence of a specific motif in the DNA sequence

        while True:
            motif = input("Introduzca secuencia de interés: ").upper()

            if not motif:
                print("Error: la secuencia está vacía")
            elif not all(nt in "ATCG" for nt in motif):
                print("Error: la secuencia contiene algún carácter inválido. Solo se permiten A, T, C, G")
            else:
                break  

        count = self.seq.count(motif)
        return count
