---

# 🎓 UniTutor - Sistema de Gestión de Tutorías

[![Descargar UniTutor](https://img.shields.io/badge/Download-UniTutor_ZIP-blue?style=for-the-badge&logo=github)](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/scysco/essentials/tree/main/programming/oop-java/unitutor)

UniTutor es una aplicación de escritorio desarrollada en Java diseñada para facilitar la programación y el seguimiento de tutorías académicas. Este proyecto se centra en la implementación de interfaces gráficas de usuario (GUI) robustas y una arquitectura de gestión de eventos desacoplada.

Este proyecto forma parte de la asignatura **Programación Orientada a Objetos II**.


## 🚀 Características

* **Interfaz Personalizada:** Uso de componentes Swing con diseños redondeados y bordes personalizados (`BotonRedondeado`, `RoundedBorder`).
* **Gestión de Eventos:** Arquitectura basada en Listeners específicos para cada acción, mejorando la modularidad y el mantenimiento.
* **Interactividad:** * Soporte para arrastre de ventana personalizada (`ListenerMoverVentana`).
* Formularios dinámicos para agendar nuevas tutorías.
* Validación de interacciones mediante eventos de ratón y teclado.



## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Java 17+
* **Librería GUI:** Swing & AWT
* **Gestor de Dependencias:** Gradle
* **Arquitectura:** Programación Orientada a Eventos (Event-Driven Programming)

## 📁 Estructura del Proyecto

```text
unitutor/
├── app/
│   ├── src/
│   │   ├── main/java/com/scysco/unitutor/
│   │   │   ├── App.java              # Punto de entrada
│   │   │   ├── componentes/          # Componentes visuales personalizados
│   │   │   ├── eventos/              # Lógica de manejo de eventos (Listeners)
│   │   │   └── gui/                  # Definición de ventanas y paneles
│   │   └── test/                     # Pruebas unitarias
│   └── build.gradle                  # Configuración de Gradle
└── gradlew                           # Script de ejecución

```

## ⚙️ Instrucciones de Ejecución

Al ser un proyecto gestionado con Gradle, puedes ejecutarlo fácilmente desde la terminal:

1. **Clonar el repositorio y navegar a la carpeta:**
```bash
cd programming/oop-java/unitutor

```


2. **Compilar y ejecutar la aplicación:**
```bash
./gradlew run

```


3. **Limpiar archivos de compilación (opcional):**
```bash
./gradlew clean

```



---

## 👨‍💻 Autor

**Jesús Sanchez** - _scysco_

---
