from time import sleep

nome_arquivo = input("[*] Digite o nome do Arquivo .txt: ")
texto_arquivo = input("[*] Digite qualquer coisa: ")

print("Gerando Arquivo...")
sleep(3)

gerarArquivo = open(nome_arquivo, 'w')
gerarArquivo.write(texto_arquivo)
gerarArquivo.close()
print("Sucesso !!")
