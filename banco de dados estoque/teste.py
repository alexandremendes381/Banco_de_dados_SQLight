nome = str(input('Qual o nome do produto : '))
quantidade = int(input('Qual a quantidade do produto : '))
valor  = float(input('Qual valor do produto : '))
 

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()
#cursor.execute("CREATE TABLE estoque (nome text, quantidade interger, valor interger)")

cursor.execute("INSERT INTO estoque VALUES('"+nome+"',"+str(quantidade)+", '"+str(valor)+"')")

banco.commit()

cursor.execute("SELECT * FROM estoque")
print(cursor.fetchall())
   