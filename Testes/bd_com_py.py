import cx_Oracle
import easygui

def create_connection():
    # Ajuste as informações de conexão conforme sua configuração Oracle
    dsn_tns = cx_Oracle.makedsn('<host>', '<port>', service_name='<service_name>')
    conn = cx_Oracle.connect(user='<username>', password='<password>', dsn=dsn_tns)
    return conn

def close_connection(conn):
    conn.close()

def select_report():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM <table_name> WHERE <column_name> = :value"
        value = easygui.enterbox('Digite o valor a ser filtrado:')
        cursor.execute(query, {'value': value})
        rows = cursor.fetchall()
        if rows:
            easygui.msgbox('\n'.join([str(row) for row in rows]))
        else:
            easygui.msgbox('Nenhum registro encontrado.')
    except cx_Oracle.DatabaseError as e:
        easygui.exceptionbox('Erro ao executar consulta.', e)
    finally:
        close_connection(conn)

def main():
    while True:
        choices = ['Insert', 'Update', 'Delete', 'Select', 'Exit']
        choice = easygui.choicebox('Selecione uma opção:', 'CRUD', choices)
        if choice == 'Insert':
            # Implementar lógica de insert
            pass
        elif choice == 'Update':
            # Implementar lógica de update
            pass
        elif choice == 'Delete':
            # Implementar lógica de delete
            pass
        elif choice == 'Select':
            select_report()
        elif choice == 'Exit':
            break

if __name__ == '__main__':
    main()