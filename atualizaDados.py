def atualizaDados(conexaoMysql,lista):
    #Esta função recebe os ID dos e-mails que foram enviados e altera no BD o flag "is_deleted" para 1
    #para sabermos que o e-mail ja foi enviado.
    cursorMysql = conexaoMysql.cursor()
    for dado in lista:
        cursorMysql.execute(f"UPDATE glpi_queuednotifications SET is_deleted = 1 WHERE id = {str(dado)};")