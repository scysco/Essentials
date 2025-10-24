import networkx as nx
import matplotlib.pyplot as plt

print("--- INICIANDO SCRIPT DE ANALISIS DE GRAFOS (EVIDENCIA DE APRENDIZAJE) ---")

# --- PARTE 1: GRAFO ORIGINAL (FESTIVAL DEL VIENTO) ---

# Creo Grafo NO DIRIGIDO
G_festival = nx.Graph()

# Defino nodos (Vértices)
nodes_dict = {
    'EP': 'EP:\nEntrada\nPrincipal',
    'ES': 'ES:\nEscenario\nSol',
    'EL': 'EL:\nEscenario\nLuna',
    'ZG': 'ZG:\nZona\nGastronómica',
    'AD': 'AD:\nÁrea de\nDescanso',
    'ML': 'ML:\nMuelle'
}

G_festival.add_nodes_from(nodes_dict.keys())
nodes_list = list(nodes_dict.keys()) 

# Defino las aristas (Senderos)
edges_festival = [
    ('EP', 'ES'), # Sendero A
    ('EP', 'ZG'), # Sendero B
    ('ES', 'ZG'), # Sendero C
    ('ES', 'EL'), # Sendero D
    ('ZG', 'AD'), # Sendero E
    ('EL', 'AD'), # Sendero F
    ('EL', 'ML'), # Sendero G
    ('AD', 'ML')  # Sendero H
]
G_festival.add_edges_from(edges_festival)

# Calculo los grados originales
degrees_original = dict(G_festival.degree())
print(f"Grados Originales: {degrees_original}")

# Creo etiquetas personalizadas (Nodo + Grado ORIGINAL)
labels_original = {}
for node, name in nodes_dict.items():
    labels_original[node] = f"{name}\n(Grado: {degrees_original[node]})"

# Defino layout MANUAL (planar) que evite los cruces
pos_planar = {
    'EP': (0, 10),
    'ES': (-10, 5),
    'ZG': (10, 5),
    'EL': (-10, -5),
    'AD': (10, -5),
    'ML': (0, -10)
}

# --- ¡MODIFICACION DE ESTILO! ---
# Dibujo el grafo original usando los COMPONENTES
plt.figure(figsize=(12, 9))

# Dibujo nodos y etiquetas
nx.draw_networkx_nodes(
    G_festival, pos_planar, node_color='#D32F2F', node_size=4500
)
nx.draw_networkx_labels(
    G_festival, pos_planar, labels=labels_original,
    font_size=10, font_weight='bold', font_color='white'
)
# Dibujo aristas
nx.draw_networkx_edges(
    G_festival, pos_planar, edgelist=edges_festival,
    edge_color='gray', width=2
)

plt.title('Grafo Original "Festival del Viento"', fontsize=16)

# Guardo imagen original
file_name_original = "grafo_festival_original.png"
plt.savefig(file_name_original, bbox_inches='tight')
print(f"Grafo Original guardado como: {file_name_original}")


# --- PARTE 2: ANALISIS GRAFO ORIGINAL ---

print("\n--- ANALISIS EULERIANO (GRAFO ORIGINAL) ---")
# Compruebo si tiene CAMINO Euleriano
if nx.has_eulerian_path(G_festival):
    print("Resultado: SI tiene un CAMINO Euleriano.")
else:
    print("Resultado: NO tiene un CAMINO Euleriano.")

# Compruebo si tiene CICLO Euleriano
if nx.is_eulerian(G_festival):
    print("Resultado: SI tiene un CICLO Euleriano.")
else:
    print("Resultado: NO tiene un CICLO Euleriano")


print("\n--- ANALISIS HAMILTONIANO (GRAFO ORIGINAL) ---")
# Busco un CICLO Hamiltoniano
found_ham_cycle = False
# Itero sobre todos los caminos simples
for start_node in nodes_list:
    for end_node in nodes_list:
        if start_node == end_node:
            continue
        for path in nx.all_simple_paths(G_festival, source=start_node, target=end_node):
            if len(path) == len(nodes_list):
                if G_festival.has_edge(path[-1], path[0]):
                    print("Resultado: SI tiene un CICLO Hamiltoniano.")
                    path.append(path[0]) 
                    print(f"Ciclo Hamiltoniano (lista de nodos): {path}")
                    found_ham_cycle = True
                    break
        if found_ham_cycle:
            break
    if found_ham_cycle:
        break

if not found_ham_cycle:
    print("Resultado: NO tiene un CICLO Hamiltoniano.")


# --- PARTE 3: GRAFO MODIFICADO ---

print("\n--- CREACION Y DIBUJO (GRAFO MODIFICADO) ---")

G_mod = G_festival.copy()

# Añado los senderos de la "Opción 2" para balancearlo
new_edges = [
    ('ES', 'AD'), # Conexión cruzada 1
    ('EL', 'ZG')  # Conexión cruzada 2
]
G_mod.add_edges_from(new_edges)

# Calculo los NUEVOS grados
degrees_mod = dict(G_mod.degree())
print(f"Nuevos Grados (Modificados): {degrees_mod}")

# Creo etiquetas personalizadas (Nodo + Grado NUEVO)
labels_mod = {}
for node, name in nodes_dict.items():
    labels_mod[node] = f"{name}\n(Grado: {degrees_mod[node]})"

# Dibujo el grafo modificado
plt.figure(figsize=(12, 9))
# Dibujo nodos y etiquetas nuevas
nx.draw_networkx_nodes(G_mod, pos_planar, node_color='#D32F2F', node_size=4500)
nx.draw_networkx_labels(
    G_mod, pos_planar, labels=labels_mod,
    font_size=10, font_weight='bold', font_color='white'
)
# Dibujo aristas ORIGINALES (en gris)
nx.draw_networkx_edges(
    G_mod, pos_planar, edgelist=edges_festival,
    edge_color='gray', width=2
)
# Dibujo aristas NUEVAS (en verde y punteadas)
nx.draw_networkx_edges(
    G_mod, pos_planar, edgelist=new_edges,
    edge_color='#34A853', width=3, style='dashed'
)
plt.title('Grafo Modificado "Festival del Viento" (Solución Euleriana)', fontsize=16)

# Guardo imagen modificada
file_name_mod = "grafo_festival_modificado.png"
plt.savefig(file_name_mod, bbox_inches='tight')
print(f"Grafo Modificado guardado como: {file_name_mod}")


# --- PARTE 4: ANALISIS GRAFO MODIFICADO ---

print("\n--- ANALISIS EULERIANO (GRAFO MODIFICADO) ---")
# Compruebo si tiene CICLO Euleriano
if nx.is_eulerian(G_mod):
    print("Resultado: SI tiene un CICLO Euleriano")
    # Calculo el circuito (empezando en EP)
    circuit_modificado = list(nx.eulerian_circuit(G_mod, source='EP'))
    print(f"Circuito Euleriano: {circuit_modificado}")
else:
    print("Resultado: NO tiene un CICLO Euleriano.")

print("\n--- SCRIPT FINALIZADO ---")
