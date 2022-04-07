import mysql.connector

def conectaBanco():
    #Variável que recebe os dados do BD------------
    conexaoMysql = mysql.connector.connect(host='Ip do banco de dados',database='nome do BD(Geralmente é glpi)',user='usuário do BD',password='Senha do BD') 
    #----------------------------------------------
    db_info = conexaoMysql.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    return(conexaoMysql)