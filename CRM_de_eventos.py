clientes = ["cliente1", "cliente2", "cliente3", "cliente4", "cliente5", "cliente6", "cliente7", "cliente8", "cliente9", "cliente10"]
eventos = ["evento1", "evento2", "evento3", "evento4", "evento5", "evento6", "evento7", "evento8", "evento9", "evento10"]

j = 0
i = 0

def add_cliente(clientes):
    
    clientes = input("Digite o cliente que deseja cadastrar: ")
    
    nome = input("Nome: ")
    endereço = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    empresa = input("Empresa: ")
    ramo =  input("Ramo: ")
    cidade = input("Cidade: ")

    clientes = {nome, endereço, telefone, email, empresa, ramo, cidade}
    print(clientes) 
    

def add_evento(eventos):
    
    eventos = input("Digite os dados do evento: ")

    data = input("Data: ")
    horario = input("Endereço: ")
    endereco = input("Telefone: ")
    nome_Acessor = input("Email: ")
    numero_Emergencia = input("Empresa: ")
    descreva_Necessidades =  input("Ramo: ")
 
    eventos[j] = {data, horario, endereco, nome_Acessor, numero_Emergencia, descreva_Necessidades}
    print(eventos[j])
    j = j + 1

addc = input("Deseja adicionar um cliente? [s/n]")

if addc == "sim":
    add_cliente(clientes)
else:   
    print("Seu evendo e cliente foram cadastrados com sucesso!")

addv = input("Deseja adicionar um evento? [s/n]")
if addv == "sim":
    add_evento(eventos)
else :
    print("Seu evendo e cliente foram cadastrados com sucesso!")
