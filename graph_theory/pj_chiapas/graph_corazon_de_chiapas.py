import networkx as nx
import matplotlib.pyplot as plt

# Creo un grafo No Dirigido (simple)
G = nx.Graph()

# Defino los nodos (Vértices)
# Uso abreviaturas para claridad en el gráfico
nodes = {
    'BC': 'Balún Canán',
    'J': 'Jocotal',
    'PL': 'Piedra Larga',
    'RF': 'Río Florido',
    'AC': 'Agua Clara',
    'M': 'Montebello'
}
G.add_nodes_from(nodes.keys())

# Defino las aristas (E) - Conexiones de doble sentido
edges = [
    ('BC', 'J'),   # Balún Canán - Jocotal 
    ('BC', 'AC'),  # Balún Canán - Agua Clara 
    ('BC', 'RF'),  # Balún Canán - Río Florido 
    ('J', 'PL'),   # Jocotal - Piedra Larga 
    ('PL', 'RF'),  # Piedra Larga - Río Florido 
    ('AC', 'M'),   # Agua Clara - Montebello 
    ('RF', 'AC')   # Río Florido - Agua Clara 
]
G.add_edges_from(edges)

# Defino un layout
pos = nx.kamada_kawai_layout(G)

# Dibujo el grafo
plt.figure(figsize=(10, 7))
nx.draw(
    G,
    pos,
    labels=nodes,  # Uso los nombres completos como etiquetas
    with_labels=True,
    node_color='#ff6d00', 
    node_size=2500,
    font_size=6,
    font_weight='bold',
    font_color='black',
    edge_color='gray',
    width=2
)
plt.title('Grafo de la Red "Corazón de Chiapas"')
plt.savefig("grafo_corazon_chiapas.png", bbox_inches='tight')
