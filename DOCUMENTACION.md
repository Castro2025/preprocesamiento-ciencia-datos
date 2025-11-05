Documentación del Proyecto
Preprocesamiento de Ciencia de Datos
### 1. Introducción

En este proyecto quise poner en práctica lo que aprendí sobre Git y GitHub, sobre todo para entender mejor cómo manejar versiones y trabajar en grupo dentro de un proyecto de Ciencia de Datos.

Además, me enfoqué en hacer un proceso completo de preprocesamiento de datos usando Pandas en Python. Durante el trabajo eliminé datos repetidos, traté valores nulos, ajusté variables numéricas y convertí las categóricas para dejar el conjunto de datos listo para analizar o usar en algún modelo.

La idea principal fue mejorar mis habilidades tanto en el manejo de versiones como en la limpieza y preparación de datos, que son pasos súper importantes en cualquier proyecto de ciencia de datos.

### 2. Configuración del entorno de trabajo

Para desarrollar el proyecto usé Visual Studio Code, con la integración de Git y Python 3.10.

El repositorio remoto lo creé en GitHub con el nombre:
 Castro2025/preprocesamiento-ciencia-datos

Estructura del proyecto:
📁 preprocesamiento-ciencia-datos
┣ 📁 data
┣ 📁 scripts
┣ 📁 .github
┃ ┗ 📁 workflows
┣ 📄 .gitignore
┣ 📄 README.md
┣ 📄 DOCUMENTACION.md


---

### 3. Comandos Git utilizados  

| Comando | Descripción |
|----------|--------------|
| `git init` | Inicializa un repositorio local. |
| `git add .` | Agrega los archivos al área de preparación. |
| `git commit -m "mensaje"` | Guarda los cambios en el repositorio local. |
| `git remote add origin <url>` | Conecta el repositorio local con el remoto. |
| `git push origin main` | Envía los cambios al repositorio remoto. |
| `git checkout -b feature-preprocesamiento` | Crea una nueva rama de trabajo. |
| `git push origin feature-preprocesamiento` | Sube la rama secundaria al remoto. |
| `git merge` | Fusiona ramas en Git (se realizó mediante Pull Request). |

Cada comando fue ejecutado siguiendo las buenas prácticas de control de versiones, manteniendo la trazabilidad de los cambios realizados.

---

### 4. Desarrollo e implementación del preprocesamiento  

En la rama `feature-preprocesamiento` se desarrolló el archivo **`scripts/preprocesamiento.py`**, que incluye las siguientes funciones principales:

- **`limpiar_datos(df)`**: elimina duplicados y rellena valores nulos numéricos con la media.  
- **`normalizar_datos(df, columnas)`**: aplica normalización Min-Max a columnas numéricas.  
- **`codificar_categoricas(df, columnas)`**: convierte variables categóricas en valores numéricos utilizando *LabelEncoder*.  

El script procesa un archivo de ejemplo (`data/ejemplo.csv`) y genera un nuevo archivo limpio y transformado (`data/ejemplo_preprocesado.csv`).  

Ejecución esperada del programa:
Shape original: (6, 6)
Después de eliminar duplicados: (5, 6)

Datos preprocesados (primeras filas):
id nombre edad genero ciudad ingresos
0 1 0 0.0 0 1 0.0
...
Guardado en: data/ejemplo_preprocesado.csv

---

### 5. Automatización con GitHub Actions  

Se creó un flujo de trabajo (`.github/workflows/python-check.yml`) para automatizar la ejecución del script de preprocesamiento cada vez que se realiza un *push* o un *pull request* hacia la rama principal.  

El workflow instala las dependencias necesarias (`pandas`, `scikit-learn`) y ejecuta el script principal para verificar su correcto funcionamiento.  
Esto garantiza que el código sea probado automáticamente antes de integrarse a la rama principal, aplicando buenas prácticas de **Integración Continua (CI)**.

---

### 6. Pull Request y Fusión de Ramas  

Una vez desarrollada la funcionalidad en la rama `feature-preprocesamiento`, se procedió a crear un **Pull Request (PR)** en GitHub para su revisión y fusión con la rama `main`.  

Pasos realizados:
1. Creación de la rama secundaria con `git checkout -b feature-preprocesamiento`.
2. Desarrollo del script en `scripts/preprocesamiento.py`.
3. Ejecución de `git add`, `git commit` y `git push origin feature-preprocesamiento`.
4. Creación del **Pull Request** desde GitHub.
5. Simulación de revisión y aprobación.
6. Fusión (merge) de la rama secundaria con la principal.
7. Eliminación de la rama `feature-preprocesamiento`.

---

### 7. Resultados obtenidos  

Después de ejecutar el script, se generó correctamente el archivo data/ejemplo_preprocesado.csv, donde quedaron guardados los datos ya limpios y transformados.
Este resultado me confirmó que las técnicas de preprocesamiento con Pandas funcionaron bien y que el flujo de trabajo usando Git y GitHub fue totalmente efectivo.

---

### 8. Conclusiones  

Con este proyecto pude entender de forma práctica cómo funciona todo el proceso de control de versiones con Git y GitHub, además de ver lo útil que es aplicar métodos de trabajo colaborativo y automatización dentro de un proyecto de Ciencia de Datos.

También reforcé mis conocimientos sobre limpieza, normalización y codificación de datos, que son pasos clave antes de cualquier análisis o modelo. En resumen, fue una buena experiencia para conectar la parte técnica con la práctica real del manejo de datos.

---

### 9. Referencias bibliográficas  

- Chacon, S., & Straub, B. (2014). *Pro Git.* Apress.  
- McKinney, W. (2018). *Python for Data Analysis.* O’Reilly Media.  
- GitHub Docs. (2024). *About pull requests.* https://docs.github.com  
- Pandas Documentation. (2024). *User Guide.* https://pandas.pydata.org/docs/  

---


### 10. Enlace al repositorio final  
 [https://github.com/Castro2025/preprocesamiento-ciencia-datos](https://github.com/Castro2025/preprocesamiento-ciencia-datos)
