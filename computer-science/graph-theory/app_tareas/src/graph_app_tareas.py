import networkx as nx
import matplotlib.pyplot as plt

def generar_graficos():
    # DEFINICIÓN DE ACTIVIDADES
    actividades = {
        'A': {'dur': 3, 'pred': []},
        'B': {'dur': 2, 'pred': ['A']},
        'C': {'dur': 5, 'pred': ['B']},
        'D': {'dur': 2, 'pred': ['B']},
        'E': {'dur': 4, 'pred': ['C']},
        'F': {'dur': 3, 'pred': ['C']},
        'G': {'dur': 6, 'pred': ['E', 'D']},
        'H': {'dur': 5, 'pred': ['F', 'D']},
        'I': {'dur': 4, 'pred': ['G', 'H']},
        'J': {'dur': 3, 'pred': ['C']},
        'K': {'dur': 3, 'pred': ['I', 'J']},
        'L': {'dur': 4, 'pred': ['K']},
        'M': {'dur': 3, 'pred': ['K']},
        'N': {'dur': 3, 'pred': ['L', 'M']},
        'O': {'dur': 2, 'pred': ['N']},
        'P': {'dur': 1, 'pred': ['O']},
        'Q': {'dur': 2, 'pred': ['P']}
    }

    # 2. CÁLCULOS CPM
    # Paso Adelante (ES, EF)
    for id_act, datos in actividades.items():
        if not datos['pred']:
            datos['ES'] = 0
        else:
            datos['ES'] = max([actividades[p]['EF'] for p in datos['pred']])
        datos['EF'] = datos['ES'] + datos['dur']

    duracion_proyecto = max([a['EF'] for a in actividades.values()])

    # Paso Atrás (LS, LF)
    sucesores = {k: [] for k in actividades}
    for id_act, datos in actividades.items():
        for p in datos['pred']:
            sucesores[p].append(id_act)

    for id_act in list(actividades.keys())[::-1]:
        datos = actividades[id_act]
        if not sucesores[id_act]:
            datos['LF'] = duracion_proyecto
        else:
            datos['LF'] = min([actividades[s]['LS'] for s in sucesores[id_act]])
        datos['LS'] = datos['LF'] - datos['dur']
        datos['Holgura'] = datos['LS'] - datos['ES']
        datos['Critica'] = 'SÍ' if datos['Holgura'] == 0 else 'No'

    # PREPARACIÓN GRÁFICA COMÚN
    G = nx.DiGraph()
    for act, datos in actividades.items():
        G.add_node(act, label=f"{act}\n({datos['dur']})")
        for p in datos['pred']:
            G.add_edge(p, act)

    pos = {
        'A': (0, 5),
        'B': (2, 5),
        'C': (4, 5), 'D': (4, 3),
        'E': (6, 6), 'F': (6, 4), 'J': (6, 2),
        'G': (8, 6), 'H': (8, 4),
        'I': (10, 5),
        'K': (12, 5),
        'L': (14, 6), 'M': (14, 4),
        'N': (16, 5),
        'O': (18, 5),
        'P': (20, 5),
        'Q': (22, 5)
    }

    # --- GENERAR DIAGRAMA BASE ---
    plt.figure(figsize=(14, 8))
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrowsize=20, node_size=1000)
    nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='lightblue', edgecolors='gray')
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
    
    plt.title("Diagrama de Red - Estructura del Proyecto", fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("diagrama_base.png")
    print("✅ Imagen generada: diagrama_base.png")
    plt.close() 

    # --- GENERAR RUTA CRÍTICA ---
    plt.figure(figsize=(14, 8))
    
    nx.draw_networkx_edges(G, pos, edge_color='lightgray', arrowsize=20, node_size=1000)
    nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='lightblue', edgecolors='gray')

    # Identificar elementos críticos
    nodos_criticos = [n for n in actividades if actividades[n]['Critica'] == 'SÍ']
    aristas_criticas = []
    for u, v in G.edges():
        if u in nodos_criticos and v in nodos_criticos:
            # Validar continuidad estricta (EF de U == ES de V)
            if actividades[u]['EF'] == actividades[v]['ES']:
                aristas_criticas.append((u, v))

    # Superponer elementos críticos en rojo
    nx.draw_networkx_nodes(G, pos, nodelist=nodos_criticos, node_color='#FF6F61', node_size=1000, edgecolors='red')
    nx.draw_networkx_edges(G, pos, edgelist=aristas_criticas, edge_color='red', width=2.5, arrowsize=25, node_size=1000)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

    plt.title(f"Ruta Crítica (CPM) - Duración: {duracion_proyecto} días", fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("diagrama_critico.png")
    print("✅ Imagen generada: diagrama_critico.png")
    plt.close()

if __name__ == "__main__":
    generar_graficos()
