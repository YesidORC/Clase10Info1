from reglas import *
from reglas import solicitar_variables_unicaentre as sv
import random

while True:
  menu = input("""
  1- Suma 34
  2- resta
  3- multiplkicación
  4- división
  5- Salir 
  """)
  x=random.randint(2,49)
  y=sv()
  if menu == "1":
    print(suma(x,y))
  elif menu == "2":
    print(resta(x,y))
  elif menu == "3":
    print(mult(x,y))
  elif menu == "4":
    print(division(x,y))
  elif menu == "5":
    break
  else:
    print("INGRESE VALOR CORRECTO!!!!")