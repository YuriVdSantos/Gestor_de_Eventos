dnovo = 's'

while dnovo == 's':
    
    i = 0
    c = input("Digite o cliente que deseja cadastrar: ")



    nome = input("Nome: ")
    endereço = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    empresa = input("Empresa: ")
    ramo =  input("Ramo: ")
    cidade = input("Cidade: ")

    c = {nome, endereço, telefone, email, empresa, ramo, cidade}
    print(c)

    dnovo = input("Deseja cadastrar outro cliente? (s/n) ")