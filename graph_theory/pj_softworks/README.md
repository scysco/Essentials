# 🏢 Proyecto: Red de Optimización SoftWorks (MST)

Este proyecto aplica la **Teoría de Grafos** para resolver problemas de modelado organizacional y optimización de redes en la empresa "SoftWorks S.A.", basado en el caso de estudio de la Actividad 2 (Matemáticas Discretas).

## 🎯 Objetivo

El objetivo es utilizar Python y la librería `NetworkX` para modelar dos escenarios distintos dentro de la empresa:

1.  **Estructura Organizacional (Grafo Dirigido):** Visualizar la jerarquía de la empresa, desde la Dirección General hasta los asistentes de cada área, modelando las relaciones de supervisión como un grafo dirigido.
2.  **Infraestructura de Red (Árbol de Expansión Mínima):** Diseñar una red de fibra óptica que interconecte los 6 servidores principales de la empresa (Dirección, Desarrollo, Finanzas, etc.) con el **mínimo costo total**.

## 🧩 Conceptos Clave

- **Grafos Dirigidos (DiGraph):** Utilizados para el organigrama, donde las aristas tienen una dirección (quién supervisa a quién).
- **Grafos Ponderados:** La red de servidores tiene costos asociados a cada conexión (en miles de pesos).
- **Árbol de Expansión Mínima (MST):** Se aplican algoritmos como **Kruskal** (o Prim) para encontrar el subconjunto de conexiones que enlaza todos los nodos con el menor peso total posible, evitando ciclos.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Librerías:**
  - `networkx`: Para la creación de grafos y cálculo del MST.
  - `matplotlib`: Para la visualización y generación de las imágenes.

## 📂 Estructura del Proyecto

- `graph_softworks.py`: Script principal que define los nodos, aristas y pesos, y genera los gráficos.
- `1_organigrama.png`: Visualización generada de la jerarquía de la empresa.
- `2_grafo_completo.png`: Red de servidores con todas las posibles conexiones y sus costos.
- `3_resultado_prim.png` / `4_resultado_kruskal.png`: Visualización de la red óptima (MST) resultante tras aplicar los algoritmos.

## ⚙️ Instrucciones de Ejecución

1.  Asegúrate de tener instaladas las dependencias:
    ```bash
    pip install networkx matplotlib
    ```
2.  Ejecuta el script principal:
    ```bash
    python graph_softworks.py
    ```
3.  El script generará las imágenes `.png` en el mismo directorio, mostrando tanto el organigrama como la solución óptima de cableado.
