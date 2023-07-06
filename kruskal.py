import PySimpleGUI as sg
import networkx as nx
import matplotlib.pyplot as plt


def kruskal_inicio(num_vertices, are):
    grafo = nx.Graph()
    grafo.add_nodes_from(range(1, num_vertices + 1))
    grafo.add_weighted_edges_from(are)

    mst = kruskal(grafo)
    percurso = list(mst.edges())

    gera_grafo(grafo, percurso, are)

def kruskal(grafo):
    pais = {}
    ordem = {}

    def find(vert):
        if pais[vert] != vert:
            pais[vert] = find(pais[vert])
        return pais[vert]

    def union(vert1, vert2):
        root1 = find(vert1)
        root2 = find(vert2)

        if root1 != root2:
            if ordem[root1] > ordem[root2]:
                pais[root2] = root1
            else:
                pais[root1] = root2
                if ordem[root1] == ordem[root2]:
                    ordem[root2] += 1

    mst = nx.Graph()
    mst.add_nodes_from(grafo.nodes())

    for verti in grafo.nodes():
        pais[verti] = verti
        ordem[verti] = 0

    sorted_edges = sorted(grafo.edges(data=True), key=lambda x: x[2]['weight'])

    for edge in sorted_edges:
        verti1, verti2, weight = edge
        if find(verti1) != find(verti2):
            union(verti1, verti2)
            mst.add_edge(verti1, verti2, weight=weight['weight'])

    return mst

def gera_grafo(graph, mst_edges, edges):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 6), num='grafo psc')
    nx.draw_networkx(graph, pos=pos, with_labels=True, node_color='lightblue', node_size=500)
    nx.draw_networkx_edges(graph, pos=pos, edgelist=mst_edges, edge_color='blue', width=2)
    labels = {(u, v): f"{peso:.2f}" for (u, v, peso) in edges}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_color='#000000', font_size= 10)
    plt.axis('off')
    plt.show()
