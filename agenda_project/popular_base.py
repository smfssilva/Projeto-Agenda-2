import sqlite3
from faker import Faker
import random
from datetime import datetime

fake = Faker()



conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()


# for linha in range(10000):
# 	nome = fake.name().split()[0]
# 	sobrenome = fake.name().split()[1]
# 	telefone = fake.phone_number()
# 	conteudo = fake.text()
# 	categoria = random.choice([1, 2, 3])
# 	email = f"{nome}@yahoo.com"
# 	data = datetime.today()
# 	comando = f"INSERT INTO contatos_contato (nome, sobrenome, email, data_criacao, descricao, telefone, categoria_id) VALUES ('{nome}', '{sobrenome}', '{email}', '{data}', '{conteudo}', '{telefone}','{categoria}')"
# 	print(comando)
# 	cursor.execute(comando)
# 	conexao.commit()


cursor.execute("SELECT * FROM contatos_contato where mostra = 0")
for linha in cursor.fetchall():
    print(linha)




cursor.close()
conexao.close()