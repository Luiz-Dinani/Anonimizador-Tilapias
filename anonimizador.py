import csv
import services_references.openMapAPI as mapa

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    csvLido = csv.reader(arquivo)
    return csvLido

def anonimizarDados(cpf, rg, nomeCompletoCliente, cep):
    #endereco = mapa.procurar(nomeEscola)
    cpf_oculto = cpf[:3] + "*" * (len(cpf)-4) + cpf[len(cpf)-1:]
    rg_oculto = rg[:2] + "*" * (len(rg)-3) + rg[len(rg)-1:]
    nomesCliente = nomeCompletoCliente.split()
    cep_oculto = cep[:2] + "*" * (len(cep)-2) + cep[len(cep)-1:]

    if len(nomesCliente) <= 2:
        nomesCliente[-1] = len(nomesCliente[-1]) * "*"
    else:
        i = 0
        for nome in nomesCliente:
            if nome != nomesCliente[0] and nome != nomesCliente[-1]:
                nomesCliente[i] = len(nome) * "*"
            i += 1
    nome_oculto = " ".join(nomesCliente)
    
    dados_ocultos = [nome_oculto, cpf_oculto, rg_oculto, cep_oculto]
    return dados_ocultos

def main():
    nomeArquivo = "clientes_exposto.csv"
    arquivo = lerArquivo(nomeArquivo)
    next(arquivo) #Pula o cabeçalho

    with open("arquivoAnonimizado.csv", mode="w", newline='') as anonimizadoCsv:
        writer = csv.writer(anonimizadoCsv, delimiter=";")
        writer.writerow(["NomeCliente","CPF","RG","CEP"])

        for linha in arquivo:
            nomeCompletoCliente, cpf, rg, cep = linha[0], linha[1], linha[2], linha[3]
            dados_ocultos = anonimizarDados(cpf, rg, nomeCompletoCliente, cep)

            writer.writerow(dados_ocultos)    
        
    
main()