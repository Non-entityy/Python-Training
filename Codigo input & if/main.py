nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")
carteira = input("Possui carteira de motorista (Sim/Não): ")
beb = input("Ingeriu bebidas alcoólicas? (Sim/Não): ")

if carteira == "Sim" and beb == "Não" and idade >= "18":
 print("Apto a dirigir.")
else:
 print("Não pode dirigir.")

