import os

def criar_comando_aldeao():
    # Criação do comando
    comando = "/summon Villager ~1 ~ ~ {"
    comando += "\n    Profession: 1,"
    
    # Adiciona o nome personalizado
    nome_aldeao = input("Digite o nome do aldeão: ")
    comando += f'\n    CustomName: "{nome_aldeao}",'
    comando += "\n    CustomNameVisible: 1,"
    
    # Adiciona a carreira e o nível de carreira
    comando += "\n    Career: 1,"
    comando += "\n    CareerLevel: 42,"
    
    # Configurações adicionais
    comando += "\n    CanPickUpLoot: 0,"
    comando += "\n    PersistenceRequired: 1,"
    comando += "\n    Invulnerable: 1,"
    
    # Atributos de saúde
    comando += "\n    Attributes: ["
    comando += "\n        {"
    comando += '\n            Name: "generic.maxHealth",'
    comando += "\n            Base: 99999"
    comando += "\n        }"
    comando += "\n    ],"
    
    # Trocas
    comando += "\n    Offers: {"
    comando += "\n        Recipes: ["
    
    while True:
        # Adiciona uma nova troca
        comando += criar_comando_troca()
        
        # Pergunta se deseja adicionar mais trocas
        adicionar_mais = input("Deseja adicionar mais trocas? (s/n): ").lower()
        if adicionar_mais != 's':
            break
    
    comando += "\n        ]"
    comando += "\n    }"
    
    # Fecha o comando
    comando += "\n}"
    
    # Salva o comando em um arquivo
    salvar_comando_em_arquivo(comando, nome_aldeao)


def criar_comando_troca():
    # Inicia o comando da troca
    comando_troca = "\n            {"
    
    # Itens de compra
    items_compra = criar_lista_itens("Digite os itens para compra (separados por vírgula): ")
    comando_troca += f'\n                buy: {{ {items_compra} }},'
    
    # Limite de usos
    max_uses = input("Digite o limite de usos para a troca (0 para ilimitado): ")
    comando_troca += f'\n                maxUses: {max_uses},'
    
    # Item de venda
    item_venda = criar_item("Digite o item para venda: ")
    comando_troca += f'\n                sell: {{ {item_venda} }},'
    
    # Experiência
    reward_exp = input("A troca deve recompensar experiência? (s/n): ").lower()
    comando_troca += f'\n                rewardExp: {reward_exp == "s"}'
    
    # Fecha o comando da troca
    comando_troca += "\n            },"
    
    return comando_troca


def criar_lista_itens(mensagem):
    while True:
        itens = input(mensagem).split(',')
        itens = [item.strip() for item in itens]
        
        # Verifica se não há itens duplicados
        if len(set(itens)) == len(itens):
            for i in itens:
                if i not in ["dirt", "emerald", "emerald_block", "diamond_block", "gold_block"]:
                    break
            else:
                return ', '.join(itens)
            print("Por favor, escolha um item válido.") 
        else:
            print("Por favor, remova itens duplicados.")


def criar_item(mensagem):
    while True:
        item = input(mensagem).strip()
        
        # Verifica se o item está na lista de itens permitidos
        itens_permitidos = ["dirt", "emerald", "emerald_block", "diamond_block", "gold_block"]
        if item in itens_permitidos:
            return f'id: "{item}", Count: 1'
        else:
            print("Por favor, escolha um item válido.")


def salvar_comando_em_arquivo(comando, nome_aldeao):
    # Verifica se o arquivo já existe
    numero = 0
    nome_arquivo = f"{nome_aldeao}.txt"
    while os.path.exists(nome_arquivo):
        numero += 1
        nome_arquivo = f"{nome_aldeao}{numero:02d}.txt"

    # Salva o comando no arquivo
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(comando)

    print(f"\nComando do Aldeão salvo em '{nome_arquivo}'.")


# Executa o código
criar_comando_aldeao()
