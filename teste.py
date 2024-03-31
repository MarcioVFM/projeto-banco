from models.cliente import Cliente
from models.conta import Conta

Marcio: Cliente = Cliente('Marcio Vinicius', 'algumemail.com', '123.123.123-12', '12/12/1212')
Daniel: Cliente = Cliente('daniel da silva', 'algumemail1.com', '123.123.123.23', '12/12/1212')

#print(Marcio)
#print(Daniel)

conta1 = Conta(Marcio)
conta2 = Conta(Daniel)

print(conta1)
print(conta2)