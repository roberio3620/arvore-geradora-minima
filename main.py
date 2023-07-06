import PySimpleGUI as sg
import networkx as nx
import matplotlib.pyplot as plt
import kruskal as k

def cria_graf():
    sg.theme_background_color('#1C1C1C')
    sg.theme_text_color('#FFD700')
    sg.theme_button_color(('#273755', '#fad029'))

    layout1 = [
        [sg.Text('Árvore Geradora Mínima', background_color='#1C1C1C', font='Ubuntu', pad=(200,7) )],
        [sg.Text('Número de Vértices:', background_color='#1C1C1C', font='Ubuntu')],
        [sg.InputText(key='num_vertices')],
        [sg.Text('Número de Arestas:', background_color='#1C1C1C', font='Ubuntu')],
        [sg.InputText(key='num_arestas')],
        [sg.Button('Salvar', font='Ubuntu')]
    ]

    window1 = sg.Window('Trabalho Grafo', layout1)

    while True:
        event, values = window1.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Salvar':
            num_vertices = int(values['num_vertices'])
            num_arestas = int(values['num_arestas'])
            window1.close()
            cria_input(num_vertices, num_arestas)

    window1.close()

def cria_input(num_vertices, num_arestas):
    layout2 = [
        [sg.Text('Aresta {}/{}'.format(1, num_arestas), key='label_edge',background_color='#1C1C1C', pad=(200,7),font='Ubuntu')],
        [sg.Text('Vértice 1:',background_color='#1C1C1C',font='Ubuntu')],
        [sg.InputText(key='v1')],
        [sg.Text('Vértice 2:',background_color='#1C1C1C',font='Ubuntu')],
        [sg.InputText(key='v2')],
        [sg.Text('Peso:     ',background_color='#1C1C1C',font='Ubuntu')],
        [sg.InputText(key='peso')],
        [sg.Button('Próxima Aresta',font='Ubuntu')]
    ]

    window2 = sg.Window('Entrada de Grafos', layout2)

    arestas = []
    arestas_criadas = []
    aresta_atual = 1

    while True:
        event, values = window2.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Próxima Aresta':
            vert1 = int(values['v1'])
            vert2 = int(values['v2'])
            peso = int(values['peso'])

            if ((vert1,vert2) in arestas_criadas) or ((vert2,vert1) in arestas_criadas):
                print('ERRO')
                sg.popup('CONJUNTO DE ARESTA JÁ UTILIZADO',background_color='#1C1C1C', font='Ubuntu')
            else:
                arestas.append((vert1, vert2, peso))

                arestas_criadas.append((vert1,vert2))

                aresta_atual += 1

            if aresta_atual <= num_arestas:
                window2['label_edge'].update('Aresta {}/{}'.format(aresta_atual, num_arestas))
                window2['v1'].update('')
                window2['v2'].update('')
                window2['peso'].update('')
            else:
                window2.close()
                k.kruskal_inicio(num_vertices, arestas)

    window2.close()


cria_graf()