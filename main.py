from dotenv import load_dotenv
import os
import mysql.connector
load_dotenv()


conexao = mysql.connector.connect(
    host='localhost',
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    database='bd_crudpy',
)
cursor = conexao.cursor()

#CREATE

nomefii= "MXRF11"
pvp = 9.12
cota = 0.09
divyield = 12.72
valorizacao = -5.98

comando = f'INSERT INTO fundosfii (name_fii, pvp, cota,div_yield, valorizacao) VALUES("{nomefii}",{pvp},{cota},{divyield},{valorizacao})'
cursor.execute(comando)
conexao.commit()


#READ
'''
comando = f'SELECT * FROM fundosfii'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)
'''


cursor.close()
conexao.close()