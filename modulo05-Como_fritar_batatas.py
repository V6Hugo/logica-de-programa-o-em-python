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
import time

def fritar_batata(quantidade_porcoes):
    print(f"\n--- 🍟 Como fritar uma Batatas 🍟 ---")
    print("1. Descascar e cortar as batatas em palito.")
    print("2. Secar bem as batatas.")
    print("3. Aquecer o óleo na temperatura ideal.")
    print("4. Colocar as batatas no óleo quente.")
    
    # Simulando o tempo de fritura com um loop
    minutos = 1
    while minutos <= 3:
        print(f"... Fritando... minuto {minutos}...")
        time.sleep(0.5) # Simula o tempo passando mais rápido
        minutos += 1
        
    print("5. Retirar, escorrer o óleo e colocar sal.")
    return "Batatas fritas douradas e crocantes prontas!"

# Executando
porcao_fds = fritar_batata(2)
print(f"Resultado: {porcao_fds}")