import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# --- CONFIGURACIÓN GENERAL ---
def guardar_imagen(titulo, nombre_archivo):
    plt.title(titulo, fontsize=12, fontweight='bold', pad=12)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(nombre_archivo, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"✅ Imagen generada: {nombre_archivo}")

# ==========================================
# DEFINICIÓN DEL MODELO
# ==========================================
def crear_grafo_villabonita():
    G = nx.DiGraph() # Grafo DIRIGIDO

    # Nodos (Refugios)
    nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    G.add_nodes_from(nodos)

    # Aristas con PESOS 
    rutas = [
        ('A', 'B', 20), ('A', 'C', 15), ('A', 'D', 45),
        ('B', 'C', 10), ('B', 'E', 30),
        ('C', 'D', 10), ('C', 'E', 35), ('C', 'F', 12), ('C', 'A', 18),
        ('D', 'A', 40),
        ('E', 'F', 5),  ('E', 'G', 20),
        ('F', 'G', 15), ('F', 'B', 25),
        ('G', 'A', 30)
    ]
    G.add_weighted_edges_from(rutas)
    return G

# ==========================================
# GRAFOS
# ==========================================
def generar_graficos():
    G = crear_grafo_villabonita()

    # Posición manual para claridad (A en el centro o arriba)
    pos = {
        'A': (0, 6),   # Centro Acopio (Norte)
        'B': (-4, 4),  'C': (0, 2),   'D': (4, 4),
        'F': (-2, 0),  'E': (2, 0),
        'G': (0, -3)   # Sur
    }

    TAMANO_NODO = 1500

    # --- GRAFO COMPLETO ---
    plt.figure(figsize=(10, 8))
    # Aristas curvas para evitar superposición en rutas de ida/vuelta
    nx.draw_networkx_edges(G, pos, node_size=TAMANO_NODO, connectionstyle='arc3, rad=0.1', arrowstyle='-|>', arrowsize=20, edge_color='gray')
    nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='#FFC000', edgecolors='black')
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='white')

    # Etiquetas de pesos (tiempos)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.3)

    guardar_imagen("Red Logística de Emergencia (Villabonita)", "1_grafo_villabonita.png")

    # --- ÁRBOL DIJKSTRA (DESDE A) ---
    # Calculo rutas más cortas desde A
    path_lengths, paths = nx.single_source_dijkstra(G, source='A')

    plt.figure(figsize=(10, 8))
    nx.draw_networkx_edges(G, pos, node_size=TAMANO_NODO, connectionstyle='arc3, rad=0.1', edge_color='lightgray', arrowstyle='-|>', arrowsize=10)

    # Resaltar aristas del árbol de caminos mínimos
    aristas_dijkstra = []
    for destino, ruta in paths.items():
        if len(ruta) > 1:
            for i in range(len(ruta)-1):
                aristas_dijkstra.append((ruta[i], ruta[i+1]))

    nx.draw_networkx_edges(G, pos, node_size=TAMANO_NODO, edgelist=aristas_dijkstra, connectionstyle='arc3, rad=0.1', edge_color='blue', width=2.5, arrowstyle='-|>', arrowsize=25)
    nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='#FFC000', edgecolors='black')
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_color='white')

    # Resaltar ruta A -> G 
    ruta_AG = paths['G']
    aristas_AG = [(ruta_AG[i], ruta_AG[i+1]) for i in range(len(ruta_AG)-1)]
    nx.draw_networkx_edges(G, pos, node_size=TAMANO_NODO, edgelist=aristas_AG, connectionstyle='arc3, rad=0.1', edge_color='red', width=3, arrowstyle='-|>', arrowsize=25)

    guardar_imagen("Árbol de Caminos Mínimos desde A (Ruta A->G en Rojo)", "2_arbol_dijkstra.png")

    return paths, path_lengths


if __name__ == "__main__":
    print("--- Generando análisis Villabonita ---")
    rutas, tiempos = generar_graficos()
