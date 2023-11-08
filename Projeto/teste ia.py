if escolha_menu_principal == '1':
    print('Modelos de caminhões disponíveis:')
    numero_modelo = 1
    for guincho_modelos in guinchos.values():
        for modelo in guincho_modelos:
            print(f'{numero_modelo} - {modelo}')
            numero_modelo += 1

    numero_modelo = input('Digite o número do modelo do caminhão: ')
    numero_modelo = int(numero_modelo)

    modelo_caminhao = None
    for guincho_modelos in guinchos.values():
        if 1 <= numero_modelo <= len(guincho_modelos):
            modelo_caminhao = guincho_modelos[numero_modelo - 1]
            break

    if modelo_caminhao:
        guinchos_disponiveis = [guincho for guincho, modelos in guinchos.items() if modelo_caminhao in modelos]

        if guinchos_disponiveis:
            guincho_recomendado = guinchos_disponiveis[0]
            solicitacao = {'modelo_caminhao': modelo_caminhao, 'guincho_recomendado': guincho_recomendado}
            solicitacoes.append(solicitacao)
            print(f'Solicitação realizada com sucesso, para conferir sua solicitação verifique a aba "Verificar solicitações" no menu principal.')
        else:
            print('Não há guincho disponível para o modelo de caminhão selecionado.')
    else:
        print('Número do modelo de caminhão não encontrado na lista!')

elif escolha_menu_principal == '2':
    if solicitacoes:
        print('Solicitações de guincho:')
        for i, solicitacao in enumerate(solicitacoes, 1):
            print(f'{i} - Modelo: {solicitacao["modelo_caminhao"]}, Guincho Recomendado: {solicitacao["guincho_recomendado"]}')
    else:
        print('Não há solicitações de guincho!')

elif escolha_menu_principal == '3':
    guincho_nome = input('Digite o nome do guincho: ')
    guincho_modelos = []
    while True:
        modelo_nome = input('Digite o nome do modelo de caminhão: ')
        if modelo_nome.lower() == 'fim':
            break
        guincho_modelos.append(modelo_nome)

    guinchos[guincho_nome] = guincho_modelos
    print('Guincho criado com sucesso!')

elif escolha_menu_principal == '4':
    guincho_nome = input('Digite o nome do guincho que deseja atualizar: ')
    if guincho_nome in guinchos:
        guincho_modelos = []
        while True:
            modelo_nome = input('Digite o nome do modelo de caminhão: ')
            if modelo_nome.lower() == 'fim':
                break
            guincho_modelos.append(modelo_nome)

        guinchos[guincho_nome] = guincho_modelos
        print('Guincho atualizado com sucesso!')
    else:
        print('Guincho não encontrado!')

elif escolha_menu_principal == '5':
    guincho_nome = input('Digite o nome do guincho que deseja excluir: ')
    if guincho_nome in guinchos:
        del guinchos[guincho_nome]
        print('Guincho excluído com sucesso!')
    else:
        print('Guincho não encontrado!')

elif escolha_menu_principal == '0':
    print('Encerrando atendimento...')
    

else:
    print('Opção inválida! Tente novamente.')