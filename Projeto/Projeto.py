guinchos = {

    'Guincho 1 (para veículos simples)': ['3 / 4 ou VUC'],

    'Guincho 2 (para veículos de porte médio)': ['Toco'],

    'Guincho 3 (para veículos de 5 a 10 toneladas)': ['Truck', 'Cavalo Mecânico Trucado (carreta 2 eixos)'],

    'Guincho 4 (para veículos de 10 a 20 toneladas)': ['Carreta', 'Carreta de 3 eixos', 'Bitrem ou Romeu e Julieta', 'Treminhão', 'Tritrem', 'Rodotrem']

}



solicitacoes = []



while True:

    print('-----Auto Help Porto-----')

    print('1 - Solicitar Guincho')

    print('2 - Verificar solicitações')

    print('0 - Encerrar atendimento')



    escolha_menu_principal = input('Escolha uma opção do menu: ')



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



    elif escolha_menu_principal == '0':

        print('Atendimento encerrado! Conte sempre conosco!')

        break