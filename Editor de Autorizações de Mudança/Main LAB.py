import datetime
import os
import sys
from Script.Edit_Save_PDF import Edit_Save_PDF
from Script.HorariosMudança import Horarios
from Script.Condominio_OPT import cond_opt
from Script.Converter_Mes import convert_mes


#__________________________________________________KEYS_VALIDADE___________________________________________________________________________________
data_key = datetime.datetime.now()
ano_key = data_key.year
    
if ano_key == 2024:  
    print("Loading Key...\n")  
    pass
else: 
    print("Sessão Expirada!! Entre em Contato com Desenvolvedor!!")  
    sys.exit()    

#_______________________________________CONDOMINIO___________________________________________________________________________________________________

print("Digite o número correspondente ao condomínio desejado")
print("")
print("1)Reserva Sul Resort\t\t\t12)Portal dos Pinheiros\n2)Jardim Paulista\t\t\t13)Recreio Panorama\n3)Edificio Damasco\t\t\t14)Recreio Humaita\n4)Edificio Ecoville\t\t\t15)Valencia Turia\n5)Edificio Alleanza\t\t\t16)Santa Angela\n6)Edificio Figueira\t\t\t17)Santa Helena\n7)Edificio Itaporai\t\t\t18)Santa Monica 1\n8)Edificio Marcela e Monica\t\t19)Santa Monica 2\n9)Edificio Oliveira\t\t\t20)Villa Florença\n10)Haras Country Village\t\t21)Vivendas do Sul\n11)Edificio Prime Office\n")
print("")

condominio_usuario = input()
os.system("cls")
#___________________________OPÇÃO CORRESPONDENTE AO NUMERO DO CONDOMINIO________________________________________________________

condominio_usuario= cond_opt(condominio_usuario)

#_____________________________________CONDIÇÃO_BLOCO_CONDOMINIO________________________________________________________________________

bloco_usuario = 0
if condominio_usuario == "Reserva Sul Resort" or condominio_usuario == "Jardim Paulista":
    print("Digite o Bloco:")
    bloco_usuario = input()
#_________________________________________DIGITAR_UNIDADE________________________________________________________________________

print("Digite a Unidade:")
unidade_usuario = input()
#________________________________________OPÇÃO_ENTRADA/SAIDA________________________________________________________________________

print()
entrada_saida_usuario = input("Digite 1)Entrada 2)Saida\n")

while True:
    if  entrada_saida_usuario == "1":
                entrada_saida_usuario = "Entrada"   
                break       
    elif   entrada_saida_usuario == "2":
                entrada_saida_usuario = "Saida" 
                break
    else: print("***************************************************\n \t     Opção Inválida!! \nDigite 1 ou 2 de acordo com as opções apresentadas\n***************************************************")             
    entrada_saida_usuario = input("Digite 1)Entrada 2)Saida\n")     

#________________________________________DIGITAR_NOME_MORADOR________________________________________________________________________

print("Nome Completo do Morador")
nome_usuario = input()

#____________________________________OPÇÃO_INQUILINO/PROPRIETARIO________________________________________________________________________
    
status_usuario = input("Digite 1)Inquilino 2)Proprietario\n ")
        
while True:
    if status_usuario == "1":
        status_usuario = "Inquilino"
        break
    elif status_usuario == "2":
        status_usuario = "Proprietario"
        break
    else:
        print("***************************************************\n \t     Opção Inválida!! \nDigite 1 ou 2 de acordo com as opções apresentadas\n***************************************************")
        status_usuario = input("Digite 1)Inquilino 2)Proprietario\n")

#__________________________________________DIGITAR_DIA_E_MÊS________________________________________________________________________

dia_usuario = input("Digite Dia da Mudança em forma numerica: \n")

mes_usuario = input("Digite o Mês da Mudança em forma numerica: \n")

#____________________________________________CONVERSÃO_MÊS_________________________________________________________________________

mes_usuario = convert_mes(mes_usuario)

#________________________________________OBTER_DATA/MES_ATUAL___________________________________________________________________

data_hora_atual = datetime.datetime.now()

#_______________________________________EXTRAIR_DATA/MES/ANO_ATUAL__________________________________________________________________

dia_atual = data_hora_atual.day

#___________________________________________CONVERSÃO_MÊS_ATUAL_________________________________________________________________________

mes_atual = str(data_hora_atual.month)

mes_atual = convert_mes(mes_atual)
  
ano_atual = data_hora_atual.year

#_________________________________VARIAVEIS_RECEBENDO_DADOS_TRATADOS___________________________________________________________

condominio = str(condominio_usuario)
motivo = str(entrada_saida_usuario)    
unidade = str(unidade_usuario)
nome = str(nome_usuario)
dia = str(dia_usuario)
mes = str(mes_usuario)
morador = str(status_usuario)
dataatual = str(dia_atual)
mesatual = str(mes_atual)
bloco = str(bloco_usuario)
horario= Horarios(condominio) #METODO "Horarios" (ALOCA O HORARIO DO CONDOMINIO CORRETO NA VARIAVEL)

#__________________________________RELATORIO_DOS_DADOS_PREENCHIDOS_______________________________________________________________________
os.system("cls")
print("Condomínio:", condominio)
print("Bloco:", bloco_usuario)
print("Unidade:", unidade_usuario)
print("Entrada/Saída:", entrada_saida_usuario)
print("Nome do Morador:", nome_usuario)
print("Status (Inquilino/Proprietário):", status_usuario)
print("Dia da Mudança:", dia_usuario)
print("Mes da Mudança:", mes_usuario)
print(f"Dia atual: {dia_atual}")
print(f"Mês atual: {mes_atual}")
print(f"Ano atual: {ano_atual}")
input("Press ENTER")

#_________________________________ENVIANDO_VARIAVEIS_PARA_O_METODO__________________________________________________________________

Edit_Save_PDF(
    "auto.docx",
    "001",
    "002",
    "003",  
    "004",
    "005",
    "006",
    "007",
    "008",
    "009",
    "DATA1",
    "DATA2",
    "bloco",
    condominio, motivo, unidade, nome, dia, mes, morador,horario, dataatual, mesatual, bloco
    )









