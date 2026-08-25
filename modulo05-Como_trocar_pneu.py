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
def trocar_pneu(lado_pneu):
    print(f"\n--- 🛞 Como troca do pneu {lado_pneu} 🛞 ---")
    print("1. Estacionar o carro em local plano e puxar o freio de mão.")
    print("2. Pegar o estepe, o macaco e a chave de roda no porta-malas.")
    print("3. Afrouxar um pouco os parafusos do pneu (ainda no chão).")
    print("4. Posicionar o macaco e levantar o carro.")
    print("5. Remover completamente os parafusos e o pneu furado.")
    print("6. Colocar o pneu reserva (estepe).")
    print("7. Enroscar os parafusos levemente.")
    print("8. Descer o carro com o macaco.")
    print("9. Apertar os parafusos firmemente com o carro no chão.")
    print("10. Guardar as ferramentas e o pneu furado.")
    
    return f"Pneu {lado_pneu} trocado com segurança! Viagem liberada."

# Executando
status_carro = trocar_pneu("traseiro direito")
print(f"Resultado: {status_carro}")