#Autor: Anthony Terán Arellano
#Version 1.0

# Calcular el indice de masa moscular

nombre = input("Introduzca su nombre: ");
peso = int(input("Introduzca su peso(Kg): "));
estatura = float(input("Introduzca su estatura: "));
imc = round((peso / estatura ** 2), 2);
print(f"{nombre} su indice de masa moscular es: {imc}")