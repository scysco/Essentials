import networkx as nx
import matplotlib.pyplot as plt

# Creo Grafo DIRIGIDO
G_sprint = nx.DiGraph()

# Defino nodos (Vértices)
nodes_sprint = {
    'B': 'B:\nPila', 
    'P': 'P:\nPlanificación',
    'D': 'D:\nDesarrollo', 
    'CR': 'CR:\nRevisión\nCódigo',
    'T': 'T:\nPruebas', 
    'Dep': 'Dep:\nDespliegue',
    'R': 'R:\nRetrospectiva'
}
G_sprint.add_nodes_from(nodes_sprint.keys())

# Defino las aristas (Flujo de trabajo)
edges_sprint = [
    ('B', 'P'), 
    ('P', 'D'), 
    ('D', 'CR'), 
    ('CR', 'D'), 
    ('CR', 'T'),
    ('T', 'Dep'), 
    ('Dep', 'R'), 
    ('R', 'B'), 
    ('P', 'CR'), 
    ('D', 'T'),
    ('T', 'R')
]
G_sprint.add_edges_from(edges_sprint)

# Defino layout (circular)
pos_sprint = nx.circular_layout(G_sprint)

# Dibujo el grafo
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(
    G_sprint, pos_sprint, node_size=3000, node_color='#4285F4')

nx.draw_networkx_edges(
    G_sprint,
    pos_sprint, 
    node_size=3000, 
    arrowstyle='-|>',
    arrowsize=20, 
    edge_color='gray', 
    width=2,
    connectionstyle='arc3,rad=0.1' # para arcos en aristas paralelas (CR <-> D)
)

nx.draw_networkx_labels(
    G_sprint,
    pos_sprint, 
    labels=nodes_sprint, 
    font_size=8,
    font_color='white', 
    font_weight='bold'
)

plt.title('Grafo Dirigido: Flujo de Sprint', fontsize=16)
plt.axis('off')

# Guardo imagen
plt.savefig("grafo_sprint.png", bbox_inches='tight')
