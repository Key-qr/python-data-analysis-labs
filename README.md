# Python Data Analysis Labs

Notebooks, scripts y datasets de mi formación en análisis de datos con Python: desde fundamentos del lenguaje y Pandas hasta limpieza de datos y visualización.

El repo está ordenado por etapas. Cada carpeta es autocontenida: el notebook y el dataset que usa están juntos.

## Contenido

| Carpeta | Qué hay | Datasets | Stack |
|---|---|---|---|
| `01_analisis_datos` | Fundamentos de Pandas: lectura de CSV, `Series`, `DataFrame`, índices, `loc`/`iloc`, vectorización vs. loops (benchmark ~70x). Ejercicios de filtrado, `merge` y agregaciones por grupo. | `titanic.csv`, `sueldo_funcionarios_2019.csv/.xlsx`, `comunidades_descripcion.csv` | pandas, numpy, plotly |
| `02_data_wrangling` | Análisis preliminar (dimensiones, estadísticos, tipos), tratamiento de missing values (borrado e imputación), variables dummy, subsetting, filtros booleanos, muestreo aleatorio con semilla. | `titanic3.csv`, `Customer Churn Model.txt` | pandas |
| `03_visualizacion` | Matplotlib desde cero: líneas, dispersión, barras, histogramas, densidad. Ejercicios con series macroeconómicas (medias y desvíos móviles) e Iris. | `heart_failure_clinical_records_dataset.csv`, `data_macro.csv`, `data_iris.csv` | pandas, matplotlib |
| `04_semma_diamonds` | Dataset base para practicar la fase *Sample* de la metodología SEMMA. | `diamonds.csv` | — |
| `05_semana_01` | Fundamentos de Python: variables, tipos numéricos y cadenas, operadores, listas/tuplas/diccionarios. | — | Python |
| `06_semana_02` | Estructuras de control: `if/elif/else`, `while`, `for`, ejercicios tipo examen. | — | Python |

## Proyecto relacionado

El caso de detección de hurto de energía con PU Learning (Hackathon EQUANS Perú 2026) está en su propio repo: [energy-theft-detection-pu-learning](https://github.com/Key-qr/energy-theft-detection-pu-learning).

## Cómo correrlo

```bash
git clone https://github.com/Key-qr/python-data-analysis-labs.git
cd python-data-analysis-labs
python -m venv .venv
# Windows (Git Bash): source .venv/Scripts/activate
# Linux/macOS:        source .venv/bin/activate
pip install pandas numpy matplotlib plotly openpyxl jupyter
jupyter notebook
```

Los notebooks leen los CSV con rutas relativas, así que hay que abrirlos desde su propia carpeta.

## Autora

Keysi Quiñe Rebaza · Arquitectura de Datos Empresariales, mención Big Data Developer (Cibertec)
GitHub: [Key-qr](https://github.com/Key-qr)

## Licencia

El código está bajo licencia [MIT](LICENSE). Los datasets públicos incluidos (Titanic, Iris, Diamonds, Heart Failure, etc.) mantienen las licencias de sus fuentes originales.
