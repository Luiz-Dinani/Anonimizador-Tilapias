import csv
import services_references.openMapAPI as mapa

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    csvLido = csv.reader(arquivo)
    return csvLido

def anonimizarDados(nomeCompletoCliente, cpf):    
    cpf_oculto = cpf[:3] + "*" * (len(cpf)-4) + cpf[len(cpf)-1:]    
    nomesCliente = nomeCompletoCliente.split()
    
    if len(nomesCliente) <= 2:
        nomesCliente[-1] = len(nomesCliente[-1]) * "*"
    else:
        i = 0
        for nome in nomesCliente:
            if nome != nomesCliente[0] and nome != nomesCliente[-1]:
                nomesCliente[i] = len(nome) * "*"
            i += 1
    nome_oculto = " ".join(nomesCliente)
    
    dados_ocultos = [nome_oculto, cpf_oculto]
    return dados_ocultos

def main():
    nomeArquivo = "clientes_exposto.csv"
    arquivo = lerArquivo(nomeArquivo)
    next(arquivo) #Pula o cabeçalho

    with open("arquivoAnonimizado.csv", mode="w", newline='') as anonimizadoCsv:
        writer = csv.writer(anonimizadoCsv, delimiter=";")
        writer.writerow(["NomeCliente","CPF"])

        for linha in arquivo:
            nomeCompletoCliente, cpf= linha[0], linha[1]
            dados_ocultos = anonimizarDados(nomeCompletoCliente, cpf)
            writer.writerow(dados_ocultos)                
            
main()