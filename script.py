from time import sleep

nome_arquivo = str(input("[*] Digite o nome do Arquivo .txt: "))
texto_arquivo = str(input("[*] Digite qualquer coisa: "))

print("Gerando Arquivo...")
sleep(3)

gerarArquivo = open(nome_arquivo, 'w')
gerarArquivo.write(texto_arquivo)
gerarArquivo.close()
print("Sucesso !!")