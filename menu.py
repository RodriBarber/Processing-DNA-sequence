#! usr/bin/python 3.15
# Rodrigo Barber, October-November 2025

# It is created a class named menu acting as a interface to interact with the user
# First it is require to crate an object of this class

'''
    Parameters (of the class)
    ----------
    str
        DNA sequence in a single string

    In addition, the method options_selection asks for the number of the option (int) and the method save for a string (s/n)

    Returns (depend on the method)
    -------
    - options= str, the different options available to choose
    - option_selection= depend on the method selected (take a look to the info in each script)
    - save= file, a file call resultados.txt with the result of the method selected
'''

class Menu:

    def __init__(self, seq):
        self.seq = seq

    def options(self):
        # This method shows the different options avilable
        return (
        "Elige la opción que quieres utilizar sobre la secuencia previamente cargada (ejemplo: 1.1, 2.3, 5):\n"
        "1. Análisis del contenido de nucleótidos\n"
        "   1.1 Contenido en CG\n"
        "   1.2 Contenido de NT\n"
        "   1.3 Longitud de la secuencia\n"
        "2. Búsqueda de patrones y secuencias de interés\n"
        "   2.1 Búsqueda de genes\n"
        "   2.2 Secuencias repetitivas\n"
        "   2.3 Motivos funcionales\n"
        "3. Traducción del ADN a proteínas\n"
        "   3.1 Transcripción del ADN\n"
        "   3.2 Traducción a proteínas\n"
        "4. Simulación de mutaciones\n"
        "   4.1 Mutación puntual\n"
        "   4.2 Mutaciones aleatorias\n"
        "   4.3 Evaluar impacto mutaciones\n"
        "5. Salir")
    
    def options_selection(self):
        # This method asks for one option and executes it, each option imports a class from another file and calls a specific method
        valid_options=(1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 4.1, 4.2, 4.3, 5)
        while True:
            try:
                selection = float(input("Introduzca número: "))
                if selection in valid_options:
                    break
                else:
                    print("Error: Entrada no válida, introduce un número (ejemplo: 1.1, 2.3, 4.1...)")
                
            except ValueError:
                print("Error: Entrada no válida, introduce un número (ejemplo: 1.1, 2.3, 4.1...)")

        if selection == 1.1:
            from Analisis_NT import Analisis_cont_NT
            ADN= Analisis_cont_NT(self.seq)
            return (f"Porcentaje de CG: {ADN.content_CG()}%")

        elif selection == 1.2:
            from Analisis_NT import Analisis_cont_NT
            ADN= Analisis_cont_NT(self.seq)
            return (f"Contenido de cada nucleótido: {ADN.content_NT()}")
        
        elif selection == 1.3:
            from Analisis_NT import Analisis_cont_NT
            ADN= Analisis_cont_NT(self.seq)
            return (f"Longitud de la cadena: {ADN.length_seq()} nucleótidos")
        
        elif selection == 2.1:
            from Busqueda_seqs import Search
            searcher = Search(self.seq)
            result = searcher.gene_search()

            if len(result) == 2:   # the result is a tuple
                start, end = result
                return(f"Secuencia encontrada desde el NT {start} hasta el NT {end}")
            else:                  # the result is a string so is an error message
                return result
            
        elif selection == 2.2:
            from Busqueda_seqs import Search
            searcher = Search(self.seq)
            result = searcher.repeated_sequences()
            return result

        elif selection == 2.3:
            from Busqueda_seqs import Search
            searcher = Search(self.seq)
            count= searcher.motif_search()
            return(f"El motivo de interes se ha encontrado un total de {count} veces")
        
        elif selection == 3.1:
            from traduccion_transcripcion import Procesamiento_ADN
            Processing1= Procesamiento_ADN(self.seq)
            return (f"ARNm:\n{Processing1.transcription()}")
        
        elif selection == 3.2:
            from traduccion_transcripcion import Procesamiento_ADN
            Processing1= Procesamiento_ADN(self.seq)
            return (f"Proteína:\n{Processing1.translation()}")
        
        elif selection == 4.1:
            from mutaciones import Mutations
            mutation1 = Mutations(self.seq)
            return (f"ADN mutado:\n{mutation1.puntual_mutation()}")
        
        elif selection == 4.2:
            from mutaciones import Mutations
            mutation1 = Mutations(self.seq)
            DNA_mutated_result, new_positions = mutation1.random_mutation()
            return (f"ADN mutado:\n{DNA_mutated_result}\nPosiciones mutadas: {new_positions}")
        
        elif selection == 4.3:
            from mutaciones import Mutations
            mutation1 = Mutations(self.seq)
            resultado = mutation1.impact_mutation()

            if resultado is not None:
                i, normal_protein_aa, muted_protein_aa, muted_protein, normal_protein= resultado
                return (f"Proteína normal:\n{normal_protein}\nProteína mutada:\n{muted_protein}\nCambio en posición {i}: {normal_protein_aa} → {muted_protein_aa}")
            else:
                return ("No se han detectado cambios (mutación silenciosa)")
            
        elif selection == 5:
            exit()

    def save(self, resultado):
        # This method asks if you want to save the result, if so, it creates a file called respuesta.txt
        
        valid_options= ("s", "n")
        while True:
            try:
                option = str(input("Quiere guardar este resultado? (s/n): "))
                if option in valid_options:
                    break
                else:
                    print("Error: entrada no válida. Introduce s/n")
            except ValueError:
                print("Error: entrada no válida. Introduce s/n")
            
        file= "resultado.txt"
        if option == "s":
            with open(file, "w", encoding="utf-8") as f: # The text file does not recognize the arrow
                f.write(f"{resultado}")
            return(f"Resultado guardado en {file} (en el directorio dónde se ejecuta este script)\n"
                   "Si el archivo ya existe se sobreescribe")
        else:
            return("Resultado no guardado")