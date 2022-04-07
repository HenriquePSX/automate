from conectaBanco import conectaBanco #Função de conexão ao BD
from enviaEmail import enviaEmail #Função para envio de e-mail
from atualizaDados import atualizaDados #Função para atualizar dado no banco.
#Caso for usar o programa sem o seriviço no windows, vão ser necessárias as bibliotecas abaixo
# from time import sleep 
# from datetime import datetime 
#-------------------------------------------------------------
conexaoMysql = conectaBanco()
codigo = enviaEmail(conexaoMysql)
atualizaDados(conexaoMysql,codigo)
if conexaoMysql.is_connected():
    conexaoMysql.commit() #Aplica os ajustes no banco de dados
    conexaoMysql.close() #Fecha a conexão com o banco de dados
    print("Conexão ao MySQL foi encerrada")
#-------------------------------------------------------------
#Caso for usar o programa sem o seriviço no windows, comente o bloco de código acima e descomente o código abaixo.
#O código abaixo, além de fazer a mesma coisa que o de cima, irá tabém ter uma estruta de repetição continua que
#irá rodar o código de 10 em 10 minutos. Tem uma condição também que faz com que o código também rode das 08:00 as 18:00
#Caso deseje alterar, basta ajustar a hora. Os valores dentro da função Sleep se referem a quantidade de segundos que irá
#Aguardar para prosseguir com o código.
#-------------------------------------------------------------
# confirma = True
# while confirma == True:
#     current_time = datetime.now()
#     hora = current_time.hour
#     if(hora >= 18 or hora <= 8):
#         print('Hora:',hora)
#         sleep(50400)
#     else:
#         conexaoMysql = conectaBanco()   
#         lista = enviaEmail(conexaoMysql)
#         atualizaDados(conexaoMysql,lista)
#         if conexaoMysql.is_connected():
#             conexaoMysql.commit()
#             conexaoMysql.close()
#             print("Conexão ao MySQL foi encerrada")
#         sleep(600)
#-------------------------------------------------------------