[![Abrir en Figma](https://img.shields.io/badge/Abrir%20en-Figma-orange)](https://www.figma.com/design/8LVwS06qee6yEe2VGawN0Q/Community-Mobile-App?node-id=0-1&t=pMR1NIXkv8ahIkUF-1)

# 📱 Proyecto Final: Diseño de la App "Community" con UML y OCL

Este proyecto representa la Evidencia de Aprendizaje de la unidad, donde se aplica un conjunto de metodologías de modelado para diseñar la arquitectura completa de una aplicación móvil para la gestión de eventos llamada "Community".

## 📝 Índice

1. [Caso de Estudio](#1-caso-de-estudio-community)
2. [Artefactos del Diseño](#2-artefactos-del-diseño)
   - [Diagramas de Modelado](#diagramas-de-modelado)
   - [Wireframes (Diseño de Interfaz)](#wireframes-diseño-de-interfaz)
   - [Reglas de Consistencia (OCL)](#reglas-de-consistencia-ocl)
3. [Archivos y Herramientas](#3-archivos-y-herramientas)

---

### **1. Caso de Estudio: Community**

El objetivo es diseñar una aplicación móvil para una empresa organizadora de eventos. El sistema debe permitir a los **usuarios** buscar, seleccionar, reservar y pagar por eventos, mientras que los **administradores** deben poder gestionar los catálogos de servicios, lugares, organizadores y generar reportes.

### **2. Artefactos del Diseño**

A continuación, se presentan todos los artefactos visuales generados durante el proceso de análisis y diseño.

#### **Diagramas de Modelado**

| Diagrama                                     | Metodología | Descripción                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------- | :---------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Clases Asociadas**                         |    Booch    | Muestra las 3 clases clave iniciales y su asociación.<br>[![Abrir en Draw.io](https://img.shields.io/badge/Abrir%20en-Draw.io-blue)](https://app.diagrams.net/#Uhttps://raw.githubusercontent.com/scysco/Essentials/tree/main/software-engineering/design-patterns/oriented-object-design/app-community/src/DDOO_U3_EA_FRSM_Booch.drawio)                        |
| ![Booch](./assets/DDOO_U3_EA_FRSM_Booch.jpg) |             |                                                                                                                                                                                                                                                                                                                                                                  |
| **Casos de Uso**                             |    OOSE     | Define las interacciones entre los actores (`Usuario`, `Admin`) y el sistema.<br>[![Abrir en Draw.io](https://img.shields.io/badge/Abrir%20en-Draw.io-blue)](https://app.diagrams.net/#Uhttps://raw.githubusercontent.com/scysco/Essentials/tree/main/software-engineering/design-patterns/oriented-object-design/app-community/src/DDOO_U3_EA_FRSM_OOSE.drawio) |
| ![OOSE](./assets/DDOO_U3_EA_FRSM_OOSE.jpg)   |             |                                                                                                                                                                                                                                                                                                                                                                  |
| **Flujo de Datos**                           |     OMT     | Ilustra cómo fluye la información durante el proceso de reserva.<br>[![Abrir en Draw.io](https://img.shields.io/badge/Abrir%20en-Draw.io-blue)](https://app.diagrams.net/#Uhttps://raw.githubusercontent.com/scysco/Essentials/tree/main/software-engineering/design-patterns/oriented-object-design/app-community/src/DDOO_U3_EA_FRSM_OMT.drawio)               |
| ![OMT](./assets/DDOO_U3_EA_FRSM_OMT.jpg)     |             |                                                                                                                                                                                                                                                                                                                                                                  |
| **Diagrama de Clases Final**                 |     UML     | El modelo estructural completo del sistema, con herencia y composición.<br>[![Abrir en Draw.io](https://img.shields.io/badge/Abrir%20en-Draw.io-blue)](https://app.diagrams.net/#Uhttps://raw.githubusercontent.com/scysco/Essentials/tree/main/software-engineering/design-patterns/oriented-object-design/app-community/src/DDOO_U3_EA_FRSM_UML.drawio)        |
| ![UML](./assets/DDOO_U3_EA_FRSM_UML.jpg)     |             |                                                                                                                                                                                                                                                                                                                                                                  |

#### **Wireframes (Diseño de Interfaz)**

Se diseñó un flujo de usuario de 5 pantallas clave para el proceso de reserva en la aplicación móvil.

|         Búsqueda y Resultados         |          Detalles del Lugar           |         Formulario de Reserva         |
| :-----------------------------------: | :-----------------------------------: | :-----------------------------------: |
| ![Screen 1](./assets/Community-1.png) | ![Screen 2](./assets/Community-2.png) | ![Screen 3](./assets/Community-3.png) |
|               **Pago**                |           **Confirmación**            |
| ![Screen 4](./assets/Community-4.png) | ![Screen 5](./assets/Community-5.png) |

#### **Reglas de Consistencia (OCL)**

Se definieron reglas formales para asegurar la integridad del modelo.

| Regla                                         | Descripción                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Invariante de Clase**                       | Asegura que la capacidad del lugar sea suficiente para los asistentes.<br>[![Abrir en Draw.io](https://img.shields.io/badge/Abrir%20en-Draw.io-blue)](https://app.diagrams.net/#Uhttps://raw.githubusercontent.com/scysco/Essentials/tree/main/software-engineering/design-patterns/oriented-object-design/app-community/src/DDOO_U3_EA_FRSM_OCL_I.drawio)    |
| ![OCL 1](./assets/DDOO_U3_EA_FRSM_OCL_I.jpg)  |                                                                                                                                                                                                                                                                                                                                                               |
| **Consistencia (Caso de Uso -> Clase)**       | Vincula la acción del actor en el Caso de Uso con un método en la Clase.<br>[![Abrir en Draw.io](https://img.shields.io/badge/Abrir%20en-Draw.io-blue)](https://app.diagrams.net/#Uhttps://raw.githubusercontent.com/scysco/Essentials/tree/main/software-engineering/design-patterns/oriented-object-design/app-community/src/DDOO_U3_EA_FRSM_OCL_II.drawio) |
| ![OCL 2](./assets/DDOO_U3_EA_FRSM_OCL_II.jpg) |                                                                                                                                                                                                                                                                                                                                                               |

### **3. Archivos y Herramientas**

- **Archivos Fuente (`.drawio`):** Todos los diagramas de modelado y las gráficas OCL se encuentran en la raíz de esta carpeta para ser editados con [Draw.io](https://app.diagrams.net/).
- **Diseño de UI (Figma):** Los wireframes fueron diseñados en Figma. Puedes ver e interactuar con el prototipo a través de este enlace:
  - [**Abrir Prototipo en Figma**](https://www.figma.com/design/8LVwS06qee6yEe2VGawN0Q/Community-Mobile-App?node-id=0-1&t=pMR1NIXkv8ahIkUF-1)
