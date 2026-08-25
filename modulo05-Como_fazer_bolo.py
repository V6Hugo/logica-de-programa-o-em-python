'''
Modulo 05 - Funções e Modulos
Modulo 06 - Manipulação de arquivos

"O resumo deve abranger os módulos 1, 2, 3, 4, 5 e 6 (ou seja, do módulo 1 ao 6) 
e precisa ser realizado com o auxílio de inteligência artificial. A entrega poderá 
ser feita em um dos seguintes formatos: apresentação de slides, infográfico ou audiocast. 
Recomendo que vocês utilizem o NotebookLM para coletar as informações da IA e transformá-las em um desses produtos finais."

Precisa ser entregue nesta quarta-feira, dia 19/07/2026, às 23h59min. 
A entrega deve ser feita no whatsapp, na aba "Atividades", com o nome do arquivo no seguinte formato.


COMO FRITAR UM OVO;
COMO FAZER UM BOLO;
COMO FRITAR BATATA FRITA;
COMO TROCAR UM PNEU;
COMO FAZER UM HAMBURGUER;
COMO LAVAR O CABELO.


'''
def fazer_bolo(sabor, usar_cobertura=True):
    print(f"\n🥮 Iniciando: Bolo de {sabor.capitalize()}🥮")
    print("1. Bater os ovos, açúcar e manteiga.")
    print("2. Adicionar a farinha e o leite aos poucos.")
    print(f"3. Misturar o ingrediente principal: {sabor}.")
    print("4. Adicionar o fermento delicadamente.")
    print("5. Assar no forno a 180°C por 40 minutos.")
    
    if usar_cobertura:
        print("6. Adicionar uma cobertura caprichada por cima!")
        
    return f"Bolo de {sabor} quentinho e pronto para o café!"

# Criando bolos diferentes usando a mesma função
bolo_da_tarde = fazer_bolo("chocolate", usar_cobertura=True)
print(f"Resultado: {bolo_da_tarde}")

bolo_da_vovo = fazer_bolo("fubá", usar_cobertura=False)
print(f"Resultado: {bolo_da_vovo}")