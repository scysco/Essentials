import networkx as nx
import matplotlib.pyplot as plt

print("--- INICIANDO SCRIPT DE ANALISIS DE GRAFOS (ACTIVIDAD 3) ---")

# --- PARTE 1: GRAFO ORIGINAL ---

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
file_name_original = "grafo_sprint_original.png"
plt.savefig(file_name_original, bbox_inches='tight')
print(f"Grafo Original guardado como: {file_name_original}")


# --- PARTE 2: ANALISIS GRAFO ORIGINAL ---

print("\n--- ANALISIS EULERIANO (GRAFO ORIGINAL) ---")
# Compruebo si tiene CAMINO Euleriano
if nx.has_eulerian_path(G_sprint):
    print("Resultado: SI tiene un CAMINO Euleriano.")
    # Calculo el camino
    path_original = list(nx.eulerian_path(G_sprint))
    print(f"Camino Euleriano (lista de aristas): {path_original}")
else:
    print("Resultado: NO tiene un CAMINO Euleriano.")

# Compruebo si tiene CICLO Euleriano
if nx.is_eulerian(G_sprint):
    print("Resultado: SI tiene un CICLO Euleriano.")
else:
    print("Resultado: NO tiene un CICLO Euleriano.")


print("\n--- ANALISIS HAMILTONIANO (GRAFO ORIGINAL) ---")
nodes = list(G_sprint.nodes())
found_ham_path = False
# Busco todos los caminos simples de B a R
for path in nx.all_simple_paths(G_sprint, source='B', target='R'):
    # Compruebo si el camino visita todos los nodos
    if len(path) == len(nodes):
        print("Resultado: SI tiene un CAMINO Hamiltoniano.")
        print(f"Camino Hamiltoniano (lista de nodos): {path}")
        found_ham_path = True
        break # Encontramos uno

if not found_ham_path:
    print("Resultado: NO tiene un CAMINO Hamiltoniano.")


# --- PARTE 3: GRAFO MODIFICADO ---

print("\n--- CREACION Y DIBUJO (GRAFO MODIFICADO) ---")
# Creo una copia del grafo original
G_mod = G_sprint.copy()

# Añado la arista R -> P para balancearlo
edge_nueva = ('R', 'P')
G_mod.add_edge(*edge_nueva)

# Dibujo el grafo modificado
plt.figure(figsize=(10, 8))
# Dibujo nodos
nx.draw_networkx_nodes(G_mod, pos_sprint, node_size=3000, node_color='#4285F4')
# Dibujo aristas ORIGINALES (en gris)
nx.draw_networkx_edges(
    G_mod, pos_sprint, edgelist=edges_sprint, node_size=3000,
    arrowstyle='-|>', arrowsize=20, edge_color='gray', width=2,
    connectionstyle='arc3,rad=0.1'
)
# Dibujo arista NUEVA (en rojo)
nx.draw_networkx_edges(
    G_mod, pos_sprint, edgelist=[edge_nueva], node_size=3000,
    arrowstyle='-|>', arrowsize=20, edge_color='red', width=3,
    connectionstyle='arc3,rad=0.2'
)
# Dibujo etiquetas
nx.draw_networkx_labels(
    G_mod, pos_sprint, labels=nodes_sprint,
    font_size=8, font_color='white', font_weight='bold'
)
plt.title('Grafo Modificado (Euleriano)', fontsize=16)
plt.axis('off')

# Guardo imagen modificada
file_name_mod = "grafo_sprint_modificado.png"
plt.savefig(file_name_mod, bbox_inches='tight')
print(f"Grafo Modificado guardado como: {file_name_mod}")


# --- PARTE 4: ANALISIS GRAFO MODIFICADO ---

print("\n--- ANALISIS EULERIANO (GRAFO MODIFICADO) ---")
# Compruebo si tiene CICLO Euleriano
if nx.is_eulerian(G_mod):
    print("Resultado: SI tiene un CICLO Euleriano.")
    # Calculo el circuito
    circuit_modificado = list(nx.eulerian_circuit(G_mod, source='B'))
    print(f"Circuito Euleriano (lista de aristas): {circuit_modificado}")
else:
    print("Resultado: NO tiene un CICLO Euleriano.")

print("\n--- SCRIPT FINALIZADO ---")
