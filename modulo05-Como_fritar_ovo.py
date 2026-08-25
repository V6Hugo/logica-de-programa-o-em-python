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
def fritar_ovo(tipo_gema):
    print("--- 🍳 Como fritar um Ovo ---")
    print("1. Colocar a frigideira no fogo.")
    print("2. Adicionar uma colher de manteiga ou óleo.")
    print("3. Quebrar o ovo com cuidado e colocar na frigideira.")
    print("4. Adicionar uma pitada de sal.")
    
    # Explicando tomada de decisão (condicional)
    if tipo_gema.lower() == "mole":
        resultado = "Ovo frito com gema mole e bordinha crocante!"
    else:
        resultado = "Ovo frito com gema bem firme!"
        
    return resultado

# Executando a função
meu_almoço = fritar_ovo("mole")
print(f"Resultado: {meu_almoço}")