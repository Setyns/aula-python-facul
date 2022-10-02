


nome_arquivo = "alunos.txt"
print("----------------MENU------------------")
print("Cadastrar do aluno: [1]""\n")
print("Remover aluno: [2]""\n")
print("Buscar aluno pela matricula: [3]""\n")
print("Relatórios: [4]""\n")
print("Configurações: [5]""\n")
print("Sair: [6]""\n")
print("-----------------------------------")
menu = input("Selecione uma opção ")
matricula = []
if(menu == "1"):
    for matricula in range (1):
        arquivo_aluno = open("alunos.txt")
        nome = input("infome o nome do aluno: ")
        sexo = input("Sexo do aluno informado: ")
        idade = int(input("Idade do aluno: "))
        nota1 = float(input("digite a primeira nota do aluno: "))
        nota2 = float(input("digite a segunda nota do aluno: "))
        nota3 = float(input("digite a terceira nota do aluno: "))
        media = (nota1+nota2+nota3) / 3
        print("media final: " , media)
        faltas = int(input("quantidade de faltas: "))
        arquivo_aluno.write( str(nome) + str(sexo) + int(nota1) + int(nota2) + int(nota3) + int(media) )
        arquivo_aluno.close()
elif(menu == "2"):
    print("opção 2")
elif(menu == "3"):
    print("Buscar aluno pela matricula")
elif(menu == "4"):
    print("Relatórios")
elif(menu == "5"):
    print("Configurações")
elif(menu == "6"):
    print("fechando a aplicação..")
else:
    print("Opção não existente!")
print(matricula, "\n")        
