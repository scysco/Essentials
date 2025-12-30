# 📊 Diagrama de Proceso de Negocio: ComidaYa

![Notation](https://img.shields.io/badge/Notation-BPMN%202.0-blue)
![Tool](https://img.shields.io/badge/Tool-draw.io-orange)

Este repositorio contiene el modelado de procesos de negocio para el flujo de **"Entrega de Pedidos a Domicilio"** de la plataforma ficticia "ComidaYa". El trabajo fue desarrollado como la Evidencia de Aprendizaje de la Unidad 2 para la asignatura de **Modelado de Negocios**.

El objetivo es presentar un análisis completo del proceso en distintos niveles de abstracción, utilizando el estándar **BPMN 2.0** para garantizar la claridad, precisión y una base sólida para la futura optimización del flujo de trabajo.

---

## 🌍 Vista Estratégica (Macro-Modelamiento)

Este diagrama de colaboración de alto nivel muestra a los participantes clave del ecosistema (`Cliente`, `Plataforma`, `Restaurante`, `Repartidor`) como "cajas negras", centrándose exclusivamente en la secuencia de interacciones o "mensajes" principales entre ellos.

![Diagrama de Colaboración Macro](pools.jpg)

---

## 🔬 Vista Operacional Completa (Micro-Modelamiento)

El siguiente diagrama muestra el flujo de trabajo operacional completo ("as-is"), detallando cada tarea, decisión y evento dentro de cada participante. Dado el tamaño del modelo, a continuación se presentan vistas ampliadas de cada fase principal del proceso.

![Vista Previa del Diagrama Completo](DMDN_U2_EA_FRSM.jpg)

---

## 🔎 Vistas Detalladas por Fase

#### 1. Toma y Confirmación de Pedido
*Interacción inicial entre el Cliente y la Plataforma, desde la búsqueda hasta que el pedido es formalmente aceptado.*
![Fase 1: Pedido del Cliente](1.jpg)

#### 2. Preparación en Restaurante
*Flujo que se activa cuando la Plataforma notifica al Restaurante, y termina cuando el pedido está listo para ser recogido.*
![Fase 2: Preparación en Restaurante](2.jpg)

#### 3. Asignación y Recogida del Pedido
*Proceso de la Plataforma para asignar un repartidor y la subsecuente coordinación entre el Repartidor y el Restaurante para la recogida física del pedido.*
![Fase 3: Asignación y Recogida](3.jpg)

#### 4. Ejecución de la Entrega
*Flujo que abarca el viaje del Repartidor, las notificaciones de seguimiento a la Plataforma y las interacciones opcionales del Cliente (rastreo y comunicación).*
![Fase 4: Ejecución de la Entrega](4.jpg)

#### 5. Cierre y Retroalimentación
*Fase final que incluye la entrega al cliente, la notificación de finalización y el proceso opcional de calificación y propina.*
![Fase 5: Cierre y Feedback](5.jpg)

---

## 📂 Cómo Abrir y Editar el Archivo Fuente

El diagrama completo se encuentra en el archivo: `DMDN_U2_EA_FRSM.drawio`.

Para visualizar y editar el diagrama, puedes utilizar uno de los siguientes métodos:

#### 🌐 **Método 1: Editor Web (Recomendado)**
1.  **Descarga** el archivo `DMDN_U2_EA_FRSM.drawio`.
2.  Abre la página oficial del editor: **[app.diagrams.net](https://app.diagrams.net/)**.
3.  **Arrastra y suelta** el archivo descargado sobre la ventana del editor.

#### 🖥️ **Método 2: Aplicación de Escritorio**
1.  Asegúrate de tener instalada la aplicación de escritorio de **draw.io**.
2.  **Descarga** el archivo `DMDN_U2_EA_FRSM.drawio`.
3.  Abre el archivo con la aplicación.

---

## 🛠️ Herramientas Utilizadas

* **Lenguaje de Modelado:** BPMN 2.0
* **Software de Diagramación:** draw.io (diagrams.net)

---

## 👨‍💻 Autor

* Francisco Jesús Sánchez Manuel