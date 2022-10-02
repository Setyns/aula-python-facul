import os

cadastrar_aluno = 's'
nome_arquivo = "aluno.txt"
nome_escola = "Estácio"
separador = "-" * len(nome_escola)
cabecalho =  separador + "\n" + nome_escola + "\n" + separador


if not os.path.exists(nome_arquivo):
    nome = str(input("nome do aluno: "))
    matricula = int(input("matricula: "))
    nota1 = int(input("Nota1: "))
    nota2 = int(input("Nota2: "))
    nota3 = int(input("Nota3: "))
    faltas = int(input("Faltas no ano: "))
    arquivo_cadastro = open(nome_arquivo, 'w+t', encoding="utf-8")
    arquivo_cadastro.write(cabecalho)
    arquivo_cadastro.close()
    
def salvar_aluno(aluno):
    arquivo_cadastro = open(nome_arquivo, "r", encoding="utf-8")
    posicao_aluno = arquivo_cadastro.read().count("Aluno") + 1
    arquivo_cadastro.close()
    
    arquivo_cadastro = open(nome_arquivo, 'a+t', encoding="utf-8")
    arquivo_cadastro.write("\nAluno " + str(posicao_aluno) + "\n")
    
    for chave in aluno:
        arquivo_cadastro.write("- " + chave + ": " + aluno[chave] + "\n")
    
    arquivo_cadastro.write(separador)
    arquivo_cadastro.close()

while cadastrar_aluno == 's':
    #cadastro do aluno
    aluno = {
      "Nome": "",
      "matricula": 0,
      "nota1": 0,
      "nota2": 0,
      "nota3": 0,
      "faltas": 0,
      
    }
    
    aluno["Nome"] = input("Digite o nome do aluno:")
    aluno["matricula"] = input("Digite a matricula do aluno:")
    aluno["nota1"] = input("nota1:")
    aluno["nota2"] = input("nota2:")
    aluno["nota3"] = input("nota3:")
    aluno["faltas"] = input("faltas no semestre:")
    
   

    salvar_aluno(aluno)
    
    cadastrar_aluno = input("Deseja cadastrar mais um aluno? (s ou n)").lower()
