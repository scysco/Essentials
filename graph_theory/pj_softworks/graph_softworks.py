import networkx as nx
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN GENERAL PARA GUARDAR IMÁGENES ---
def guardar_imagen(titulo, nombre_archivo):
    plt.title(titulo, fontsize=12, fontweight='bold', pad=12)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(nombre_archivo, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"✅ Generado con éxito: {nombre_archivo}")

# ==========================================
# ORGANIGRAMA
# ==========================================
def generar_organigrama():
    G = nx.DiGraph() # Grafo Dirigido (Con flechas)

    # Definición exacta según Caso de Estudio U3 A2
    # Nivel 1
    G.add_edge("DG", "DES")
    G.add_edge("DG", "ADM")
    # Nivel 2 (Rama Desarrollo)
    G.add_edge("DES", "FE")
    G.add_edge("DES", "BE")
    # Nivel 2 (Rama Admin)
    G.add_edge("ADM", "FIN")
    # Nivel 3 (Rama Front-end)
    G.add_edge("FE", "UI")
    G.add_edge("FE", "QA")
    # Nivel 3 (Rama Back-end)
    G.add_edge("BE", "API")
    G.add_edge("BE", "DB")

    # Posición Manual
    pos = {
        'DG': (0, 10),
        'DES': (-4, 7), 'ADM': (4, 7),
        'FE': (-6, 4), 'BE': (-2, 4), 'FIN': (4, 4),
        'UI': (-7, 1), 'QA': (-5, 1), 'API': (-3, 1), 'DB': (-1, 1)
    }

    plt.figure(figsize=(10, 7))

    # Dibujar nodos
    #nx.draw_networkx_nodes(G, pos, node_size=2200, node_color='#87CEEB', edgecolors='black')

    # Dibujar etiquetas
    #nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

    # Dibujar aristas CON FLECHAS visibles (no me funciono) TODO
    #nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=20, edge_color='gray', width=2)
    
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=9, font_weight='bold', arrows=True, arrowsize=20)

    guardar_imagen("Estructura Jerárquica SoftWorks S.A.", "1_organigrama.png")

# ==========================================
# RED DE SERVIDORES
# ==========================================
def generar_redes_servidores():
    G = nx.Graph() # Grafo NO Dirigido (Fibra óptica va y viene)

    # Nodos (Servidores)
    servidores = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']
    G.add_nodes_from(servidores)

    # Aristas con Costos
    conexiones = [
        ('S1', 'S2', 4), ('S1', 'S3', 6),
        ('S2', 'S3', 5), ('S2', 'S4', 7),
        ('S3', 'S4', 8), ('S3', 'S5', 3),
        ('S4', 'S5', 2), ('S4', 'S6', 9),
        ('S5', 'S6', 1)
    ]
    G.add_weighted_edges_from(conexiones)

    # Posición Geométrica Simétrica
    pos = {
        'S1': (0, 5),   # DG (Arriba)
        'S2': (-4, 2),  # DES
        'S3': (4, 2),   # FE
        'S4': (-4, -2), # BE
        'S5': (4, -2),  # UI
        'S6': (0, -5)   # FIN (Abajo)
    }

    # Calcular MST (Algoritmo Kruskal interno)
    mst = nx.minimum_spanning_tree(G, algorithm='kruskal', weight='weight')
    costo_total = mst.size(weight='weight')

    # Función para dibujar variantes
    def dibujar_variante(titulo, archivo, mostrar_mst=False):
        plt.figure(figsize=(8, 8))

        # Estilo base
        estilo = 'dashed' if mostrar_mst else 'solid'
        color_linea = 'lightgray' if mostrar_mst else 'gray'

        # Dibujar todas las conexiones
        nx.draw_networkx_edges(G, pos, edge_color=color_linea, style=estilo, width=1.5)

        # Si es resultado, resaltar la ruta óptima
        if mostrar_mst:
            nx.draw_networkx_edges(mst, pos, edge_color='#44546A', width=4, label='Árbol Generador Mínimo')

        # Dibujar nodos
        nx.draw_networkx_nodes(G, pos, node_size=1300, node_color='#FFA500', edgecolors='black')
        nx.draw_networkx_labels(G, pos, font_weight='bold', font_size=11)

        # Dibujar costos (pesos)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12, font_color='blue')

        guardar_imagen(titulo, archivo)

    # Generar las imágenes
    # Grafo Completo
    dibujar_variante("Red de Conexiones con Costos", "2_grafo_completo.png", mostrar_mst=False)

    # Resultado Prim
    dibujar_variante(f"Resultado Algoritmo de Prim (Costo: {costo_total})", "3_resultado_prim.png", mostrar_mst=True)

    # Resultado Kruskal
    dibujar_variante(f"Resultado Algoritmo de Kruskal (Costo: {costo_total})", "4_resultado_kruskal.png", mostrar_mst=True)

if __name__ == "__main__":
    print("--- Iniciando generación de gráficos ---")
    generar_organigrama()
    generar_redes_servidores()
    print("--- Proceso finalizado correctamente ---")
