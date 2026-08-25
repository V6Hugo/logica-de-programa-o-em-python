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
def fazer_hamburguer(ponto_carne, adicionais):
    print("\n--- 🍔 Como fazer um Hambúrguer 🍔 ---")
    print("1. Cortar o pão ao meio e selar na chapa.")
    print(f"2. Grelhar o hambúrguer até o ponto: {ponto_carne}.")
    print("3. Colocar o queijo por cima para derreter.")
    
    # Adicionando ingredientes dinamicamente
    print("4. Montando a base e adicionando os opcionais:")
    for ingrediente in adicionais:
        print(f"   -> Adicionando: {ingrediente}")
        
    print("5. Fechar com a metade superior do pão.")
    return f"Hambúrguer montado ({ponto_carne}) com os adicionais selecionados!"

# Criando um pedido personalizado
meu_pedido = fazer_hamburguer("ao ponto", ["Alface", "Tomate", "Bacon", "Molho Especial"])
print(f"Resultado: {meu_pedido}")