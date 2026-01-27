#! usr/bin/python 3.15
# Rodrigo Barber, November 2025

# It is imported all de classes required for the aplication

from read_fasta import FastaReader
from menu import Menu

# It is created a class named Aplication with a method that starts the aplication

class Aplication:

    def __init__(self):
        self.lector = FastaReader()
        self.dictionary = None
        self.seq = None
        self.menu = None

    def start(self):
        # This method starts the aplication
        # Step 1: reed the FASTA file
        
        self.dictionary = self.lector.readmultipleFasta()

        # Step 2: select sequence

        self.seq = self.lector.seq_selection(self.dictionary)

        # Step 3: create the menu

        self.menu=Menu(self.seq)

        # Step 4: show options
        
        print(self.menu.options())

        # Step 5: select the option

        result = self.menu.options_selection()
        print(result)

        # Step 6: save the result    

        print(self.menu.save(result))

# The application runs only if you execute the file directly.
if __name__ == "__main__":
    app = Aplication()
    app.start()