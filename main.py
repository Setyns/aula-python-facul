import os

cadastrar_professor = 's'
nome_arquivo = "professor.txt"
nome_escola = "Estácio"
separador = "-" * len(nome_escola)
cabecalho =  separador + "\n" + nome_escola + "\n" + separador


if not os.path.exists(nome_arquivo):
    nome  = str(input("nome do professor: "))
    disciplina = str(input("Disciplina: "))
    ano = int(input("Ano : "))
    arquivo_cadastro = open(nome_arquivo, 'w+t', encoding="utf-8")
    arquivo_cadastro.write(cabecalho)
    arquivo_cadastro.close()
    
def salvar_professor(professor):
    arquivo_cadastro = open(nome_arquivo, "r", encoding="utf-8")
    posicao_professor = arquivo_cadastro.read().count("Professor") + 1
    arquivo_cadastro.close()
    
    arquivo_cadastro = open(nome_arquivo, 'a+t', encoding="utf-8")
    arquivo_cadastro.write("\nProfessor " + str(posicao_professor) + "\n")
    
    for chave in professor:
        arquivo_cadastro.write("- " + chave + ": " + professor[chave] + "\n")
    
    arquivo_cadastro.write(separador)
    arquivo_cadastro.close()

while cadastrar_professor == 's':
    #cadastro do professor
    professor = {
      "Nome": "",
      "disciplina": "",
      "ano": 0,
      
    }
    
    professor["Nome"] = input("Digite o nome do professor:")
    professor["disciplina"] = input("Digite a Disciplina do professor:")
    professor["ano"] = input("Ano:")
    
   

    salvar_professor(professor)
    
    cadastrar_professor = input("Deseja cadastrar mais um professor? (s ou n)").lower()
