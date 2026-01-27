#! usr/bin/python 3.15
# Rodrigo Barber, October 2025

# It is created a class named FastaReader with a method that can read a FASTA file and return the sequence
# First it is necessary to crate an object of this class

''' Parameters
    ------ of each method
    - readmultipleFasta= str, path of the FASTA file
    - seq_selection=  str, ID of the sequence in the FASTA file

    Returns (depend on the method)
    ------- 
    - readmultipleFasta= dictionary, with the ID of each sequence as key and the sequence as value
    - seq_selection= str, the sequence of the FASTA file with the ID selected
'''
class FastaReader:
    
    def __init__ (self):
        self.sequence= ""
        
    def readmultipleFasta(self):
        # Method that reads a FASTA file with multiple sequences and obtain the ID and the sequence for each one
        
       while True:
            file= input("Introduce el path del fichero FASTA que quieres leer: ")
            try:
                dictionary = {}
                with open(file, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith('>'):
                            identificador = line[1:].split()[0]
                            dictionary[identificador] = ''
                        else:
                            dictionary[identificador] += line
                    return dictionary
            
            except FileNotFoundError:
                print ("Archivo no encontrado")
            except PermissionError:
                print ("No tienes los permisos para abrir este archivo")
            except IsADirectoryError:
                print ("La ruta es un directorio, no un archivo")
            except Exception:
                print("Error al abrir el fichero")

    def seq_selection(self, dictionary):
        # Method that asks the user to choose one sequence of the FASTA file

        while True:
            selection= input("Itroduce el ID de la secuencia que quieres analizar (la primera cadena de texto despues del '>' y hasta el primer espacio): ")
            if selection in dictionary:
                return dictionary[selection]
            else:
                print("No se ha encontrado ese identificador")