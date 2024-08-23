# Biblioteca usada para se conectar ao bd
import pyodbc

# Os dados usados para se conectar ao banco de dados 
connection_string = (
    "Driver={ODBC Driver 17 for SQL Server};" # Driver utilizado pelo Pyodbc
    "Server=tcp:green-plus-server.database.windows.net,1433;" # Endereço do servidor utilizado para a conexão
    "Database=Green Plus;" # Nome do banco de dados
    "UID=greenplusadmin;" # O ID de usuário usado para se conectar no banco de dados
    "PWD=554HLLST@;" # A senha do usuário
    "Encrypt=yes;" # Não sei
    "TrustServerCertificate=no;" # Não sei
    "ConnectionTimeout=30") # Não sei

connection = pyodbc.connect(connection_string) # Instância de conexão do servidor
cursor = connection.cursor() # Comando utilizado para começar uma query
cursor.execute("""INSERT INTO Teste VALUES ('Testinalvo', 'Silva');""") # Comando que executa a query
cursor.commit() # Comando que manda as informações para o Banco de Dados
connection.close() # Comando que fecha a conexão com o Banco de Dados