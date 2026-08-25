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
# Subfunções auxiliares
def aplicar_shampoo():
    print("   -> Aplicar shampoo no couro cabeludo.")
    print("   -> Massagear suavemente com as pontas dos dedos.")
    print("   -> Enxaguar completamente.")

def aplicar_condicionador():
    print("   -> Aplicar condicionador apenas no comprimento e pontas.")
    print("   -> Deixar agir por 2 minutos.")
    print("   -> Enxaguar bem.")

# Função principal que coordena o processo
def lavar_cabelo(usar_condicionador=True):
    print("\n--- Iniciando: Lavar o Cabelo ---")
    print("1. Entrar no chuveiro e molhar bem o cabelo.")
    
    print("2. Passo do Shampoo:")
    aplicar_shampoo() # Chama a primeira subfunção
    
    if usar_condicionador:
        print("3. Passo do Condicionador:")
        aplicar_condicionador() # Chama a segunda subfunção
        
    print("4. Tirar o excesso de água com a toalha.")
    return "Cabelo limpinho, cheiroso e pronto para pentear!"

# Executando
cabelo_pronto = lavar_cabelo(usar_condicionador=True)
print(f"Resultado: {cabelo_pronto}")