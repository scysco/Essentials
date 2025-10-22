import networkx as nx
import matplotlib.pyplot as plt

# Creo un grafo No Dirigido (simple)
G = nx.Graph()

# Defino los nodos (Vértices)
# Uso abreviaturas para claridad en el gráfico
nodes_simple = {
    'BC': 'Balún Canán',
    'J': 'Jocotal',
    'PL': 'Piedra Larga',
    'RF': 'Río Florido',
    'AC': 'Agua Clara',
    'M': 'Montebello'
}
G.add_nodes_from(nodes_simple.keys())

# Defino las aristas (E) - Conexiones de doble sentido
edges_list = [
    ('BC', 'J'),   # Balún Canán - Jocotal e1
    ('BC', 'AC'),  # Balún Canán - Agua Clara e2
    ('BC', 'RF'),  # Balún Canán - Río Florido e3
    ('J', 'PL'),   # Jocotal - Piedra Larga e4
    ('PL', 'RF'),  # Piedra Larga - Río Florido e5
    ('AC', 'M'),   # Agua Clara - Montebello e6
    ('RF', 'AC')   # Río Florido - Agua Clara e7
]
G.add_edges_from(edges_list)

# Calculo los grados
degrees = dict(G.degree())

# Etiquetas personalizadas
custom_labels = {}
for node, name in nodes_simple.items():
    custom_labels[node] = f"{name}\n(Grado: {degrees[node]})"

edge_labels = {
    ('BC', 'J'): '$e_1$',
    ('BC', 'AC'): '$e_2$',
    ('BC', 'RF'): '$e_3$',
    ('J', 'PL'): '$e_4$',
    ('PL', 'RF'): '$e_5$',
    ('AC', 'M'): '$e_6$',
    ('AC', 'RF'): '$e_7$'  # Se usa el orden alfabético ('AC', 'RF')
}

# Defino un layout
pos = nx.kamada_kawai_layout(G)

# Dibujo el grafo
plt.figure(figsize=(14, 9))
nx.draw(
    G,
    pos,
    labels=custom_labels,  
    with_labels=True,
    node_color='#ff6d00', 
    node_size=4500,
    font_size=10,
    font_weight='bold',
    font_color='black',
    edge_color='gray',
    width=2
)

# Dibujo las etiquetas de las aristas
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_color='blue',
    font_size=18,
    font_weight='bold',
    bbox=dict(facecolor='white', alpha=0.5, edgecolor='none', pad=0.1) 
)

plt.title('Grafo de la Red "Corazón de Chiapas"', fontsize=16)
plt.savefig("grafo_corazon_chiapas.png", bbox_inches='tight')
