import networkx as nx
import matplotlib.pyplot as plt

def generar_graficos():
    print("--- GENERANDO GRÁFICOS FRSM (V2) ---")

    sensores = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']
    conexiones = [
        ('S1', 'S2'), ('S1', 'S3'), 
        ('S2', 'S3'), 
        ('S3', 'S4'), ('S3', 'S5'), 
        ('S4', 'S5')
    ]
    
    G_sen = nx.Graph()
    G_sen.add_nodes_from(sensores)
    G_sen.add_edges_from(conexiones)
    
    pos_s = {
        'S1': (0, 1), 'S2': (0, -1),
        'S3': (2, 0),
        'S4': (4, 1), 'S5': (4, -1),
        'S6': (6, 0)
    }

    plt.figure(figsize=(10, 6))
    
    conectados = ['S1', 'S2', 'S3', 'S4', 'S5']
    aislados = ['S6']
    
    nx.draw_networkx_edges(G_sen, pos_s, width=2, edge_color='gray')
    nx.draw_networkx_nodes(G_sen, pos_s, nodelist=conectados, node_size=1500, node_color='#1F3864', edgecolors='black')
    nx.draw_networkx_nodes(G_sen, pos_s, nodelist=aislados, node_size=1500, node_color='#FF4B4B', edgecolors='black', linewidths=3)
    
    labels_s = {
        'S1': 'S1\n(Sala)', 'S2': 'S2\n(Sala)', 'S3': 'S3\n(Comedor)',
        'S4': 'S4\n(Cocina)', 'S5': 'S5\n(Pasillo)', 'S6': 'S6\n(Garaje)'
    }
    nx.draw_networkx_labels(G_sen, pos_s, labels=labels_s, font_size=7, font_weight='bold', font_color='white')
    
    plt.title("Grafo de Adyacencia de Sensores", fontsize=14)
    plt.axis('off')
    plt.savefig("grafo_sensores.png")
    print("✅ Gráfico generado: grafo_sensores.png")
    plt.close()

    # ==========================================================
    # CONFIGURACIÓN DEL PROYECTO CPM
    # ==========================================================
    actividades = ['A', 'B', 'C', 'D', 'E', 'F']
    # Dependencias completas
    dependencias = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('C', 'D'),
        ('C', 'E'),
        ('D', 'F'), ('E', 'F')
    ]
    
    G_proy = nx.DiGraph()
    G_proy.add_nodes_from(actividades)
    G_proy.add_edges_from(dependencias)
    
    pos_p = {
        'A': (0, 1),
        'B': (2, 2), 'C': (2, 0),
        'D': (4, 2), 'E': (4, 0),
        'F': (6, 1)
    }
    
    duraciones = {'A': 4, 'B': 6, 'C': 3, 'D': 5, 'E': 4, 'F': 3}
    labels_p = {n: f"{n}\n({duraciones[n]}d)" for n in actividades}

    # GRAFO BASE
    plt.figure(figsize=(10, 6))
    
    nx.draw_networkx_edges(G_proy, pos_p, edge_color='gray', arrowsize=20, width=1.5, node_size=1200)
    nx.draw_networkx_nodes(G_proy, pos_p, node_size=1200, node_color='#B4C6E7', edgecolors='gray')
    nx.draw_networkx_labels(G_proy, pos_p, labels=labels_p, font_size=10, font_weight='bold')
    
    plt.title("Diagrama de Red del Proyecto", fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("grafo_proyecto_base.png")
    print("✅ Gráfico generado: grafo_proyecto_base.png")
    plt.close()

    # GRAFO RUTA CRÍTICA 
    plt.figure(figsize=(10, 6))
    
    # Ruta Crítica
    ruta_critica_edges = [('A', 'B'), ('B', 'D'), ('D', 'F')]
    ruta_critica_nodes = ['A', 'B', 'D', 'F']
    
    nx.draw_networkx_edges(G_proy, pos_p, edge_color='lightgray', arrowsize=20, width=1.5, node_size=1200)
    nx.draw_networkx_nodes(G_proy, pos_p, node_size=1200, node_color='#B4C6E7', edgecolors='gray')
    
    # Superponer Ruta Crítica
    nx.draw_networkx_edges(G_proy, pos_p, edgelist=ruta_critica_edges, edge_color='#FF4B4B', arrowsize=25, width=3, node_size=1200)
    nx.draw_networkx_nodes(G_proy, pos_p, nodelist=ruta_critica_nodes, node_size=1200, node_color='#FF6F61', edgecolors='red', linewidths=2)
    
    nx.draw_networkx_labels(G_proy, pos_p, labels=labels_p, font_size=10, font_weight='bold')
    
    plt.title("Ruta Crítica Identificada (Duración: 18 días)", fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("grafo_proyecto_critico.png")
    print("✅ Gráfico generado: grafo_proyecto_critico.png")
    plt.close()

if __name__ == "__main__":
    generar_graficos()
