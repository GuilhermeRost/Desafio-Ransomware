# Desafio-Ransomware
import  os
importar  pyaes

## abrir o arquivo criptografado
file_name  =  "teste.txt.ransomwaretroll"
file  =  open ( file_name , "rb" )
arquivo_dados  =  arquivo . leia ()
arquivo . fechar ()

## chave para descritografia
key  =  b"testeransomwares"
aes  =  pyaes . AESModeOfOperationCTR ( chave )
decrypt_data  =  aes . descriptografar ( arquivo_dados )

## removedor do arquivo criptografado
os . remover ( nome_do_arquivo )

## criar o arquivo descrito
new_file  =  "teste.txt"
novo_arquivo  =  aberto ( f' { novo_arquivo } ' , "wb" )
novo_arquivo . escrever ( descriptografar_dados )
novo_arquivo . fechar ()
