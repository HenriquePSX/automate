import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviaEmail(conexaoMysql):
    if conexaoMysql.is_connected():
        cursorMysql = conexaoMysql.cursor() #Criação do cursor para fazer as iterações com o BD
        
        #O Select abaixo está trazendo as informações de e-mail do GLPI. Dentro dessas informações estão contidas:
        #ID (Código do e-mail), name(Título do e-mail), sender(Endereço de e-mail de quem está enviando),
        #recipent(Endereço de e-mail para quem vai receber) e body_html(Todo o corpo do e-mail).
        #Nas condições, filtrei somente a entidade do nosso departamento (Caso não queira filtrar isso, 
        #só apagar a linha "entities_id = 1 AND"), deixei os e-mail que ainda não foram enviados e tirei também
        #os e-mail de pesquisa de satisfação. (Caso queira deixar, só apagar os dados "AND name not like ('%Pesquisa de satisfação%')"). 
        #OBS: Aconselho a não mudar o "is_delete = 0", pois iremos usa-lo para saber quais e-mails ja foram enviados.
        cursorMysql.execute("""SELECT
                               id,name,sender,recipient,body_html
                               FROM glpi_queuednotifications gq WHERE
                               entities_id = 1 AND
                               is_deleted  = 0 AND
                               name not like ('%Pesquisa de satisfação%')""")
        
        codigo = [] #Lista para guardar a informação do id.
        for row in cursorMysql: #Estrutura de repetição que irá ler linha a linha do retono do select.
            informacoes = [elem for elem in row] #Pego as informações da linha atual e guardo em uma lista.
            codigo.append(informacoes[0]) #Guardo a informação do id atual na lista código
            if informacoes == []:
                print('Não há nenhum e-mail a ser enviado')
                return
            else:
                #Aqui começam as config. para envio de e-mail
                host = 'smtp.gmail.com' #Protocolo de envio de e-mail. Ex: smtp.gmail.com,smtp.office365.com
                port = 587 #Porta usada na config dos e-mails. Ex: 587
                user = 'teste@gmail.com' #endereço de e-mail que irá enviar o e-mail. EX: teste@gmail.com
                password = 'senha' #Senha do endereço de e-mail.
                
                #-------------------------------------Configs abaixo não precisam ser alteradas---------------------------
                server = smtplib.SMTP(host, port)
                
                server.ehlo()
                server.starttls()
                server.login(user, password)
                
                message_html = informacoes[4]
                email_msg = MIMEMultipart()
                email_msg['From'] = user
                email_msg['To'] = informacoes[3]
                email_msg['Subject'] = informacoes[1]
                
                email_msg.attach(MIMEText(message_html, 'html'))
                
                server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
                server.quit()
                #--------------------------------------------------------------------------------------------------------        
        cursorMysql.close()
        return(codigo) #Retonar os IDs para serem utilizados.
