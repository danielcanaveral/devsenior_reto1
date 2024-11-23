Proyecto de Investigación Científica en Python
Descripción General
Este proyecto es una simulación de un proyecto de investigación científica desarrollado en Python. Permite gestionar datos experimentales, analizarlos y generar informes de manera interactiva. Fue diseñado como parte del curso Python de Cero a Senior: La Ruta Maestra del Código, para aplicar conceptos básicos y avanzados de programación en un contexto práctico y estructurado.

Características Principales
Gestión de Experimentos:

Agregar experimentos con atributos como:
Nombre.
Fecha de realización (formato DD/MM/AAAA).
Tipo de experimento (Química, Biología, Física).
Resultados numéricos.
Visualizar una lista de experimentos registrados.
Análisis de Resultados:

Cálculo de estadísticas básicas: promedio, valor máximo y mínimo.
Comparación entre experimentos para identificar el mejor o peor desempeño.
Generación de Informes:

Creación de un informe resumen que incluye los datos de los experimentos, análisis estadísticos y conclusiones.
Exportación del informe a un archivo de texto (.txt).
Interacción con el Usuario:

Menú interactivo para realizar todas las operaciones disponibles.
Validaciones para asegurar entradas correctas y manejo de errores.
Requisitos Previos
Python 3.9 o superior.
Biblioteca estándar de Python.
Instalación y Ejecución
Clona el repositorio desde GitHub:
bash
Copiar código
git clone <URL-del-repositorio>
Navega al directorio del proyecto:
bash
Copiar código
cd proyecto-investigacion-cientifica
Ejecuta el script principal:
bash
Copiar código
python main.py
Uso
Al iniciar el programa, se presenta un menú con opciones para:

Agregar nuevos experimentos.
Ver la lista de experimentos.
Realizar análisis estadísticos.
Generar un informe.
Salir del programa.
Sigue las instrucciones en pantalla para interactuar con las diferentes funcionalidades.

Estructura del Código
main.py: Archivo principal que inicia la aplicación y presenta el menú.
experimentos.py: Contiene la lógica para gestionar los experimentos.
analisis.py: Funciones para realizar cálculos estadísticos.
informe.py: Genera el informe resumen y lo exporta.
utils.py: Utilidades para validaciones y manejo de errores.
Colaboración y Control de Versiones
Cada funcionalidad se desarrolló en una rama independiente y se integró en la rama principal tras una revisión mutua del código.
Se utilizaron commits frecuentes con mensajes descriptivos, siguiendo estas convenciones:
feat: para nuevas funcionalidades.
fix: para correcciones de errores.
refactor: para mejoras de código existentes.
Presentación
Un video de demostración explica las características del proyecto, incluyendo:

Introducción al objetivo y desafíos abordados.
Ejecución del programa con ejemplos de cada funcionalidad.
Implementaciones destacadas, como validaciones y manejo de errores.
Contribuidores
Daniel Fernando Cañaveral Marin
Mauricio Laguna Santa
Licencia
Este proyecto es de uso académico y está protegido bajo las normas del curso Python de Cero a Senior: La Ruta Maestra del Código.
