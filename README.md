# Dataset

Notebooks, scripts y datasets de mi formación en análisis de datos con Python: desde fundamentos del lenguaje y Pandas hasta limpieza de datos, visualización y un caso real de machine learning semi-supervisado (PU Learning) para detección de hurto de energía.

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
| `07_deteccion_hurto_equans` | Proyecto de hackathon (ver abajo). | Datos privados, no incluidos | pandas, scikit-learn, LightGBM, seaborn |

## Proyecto destacado: detección de hurto de energía con PU Learning

`07_deteccion_hurto_equans/Deteccion_Hurto_PU_Learning_EQUANS.ipynb`

Desarrollado para el Hackathon EQUANS Perú 2026 (Reducción y Control de Pérdidas de Energía). El objetivo era priorizar qué suministros de un alimentador crítico inspeccionar por posible hurto (manipulación de medidor o conexión clandestina).

El problema no es una clasificación binaria normal: el histórico solo tiene fraudes confirmados (positivos) y el alimentador está completamente sin etiquetar. No existen negativos reales.

Pipeline:

1. **Feature engineering**: consumo normalizado a kWh/día (hay cuentas facturadas cada 60-90 días) y 10 variables de comportamiento de consumo.
2. **Clustering**: K-Means (K=3) sobre el histórico para encontrar sub-perfiles de fraude y distancias de cada cuenta a esos prototipos.
3. **PU Bagging**: ensamble de 20 clasificadores LightGBM, cada uno entrenado con los positivos + una muestra distinta del universo sin etiquetar; se promedian las probabilidades.
4. **Modelo de recupero**: `HistGradientBoostingRegressor` que estima los kWh recuperables por cuenta.
5. **Doble score**: probabilidad de fraude x recupero esperado, valorizado en PEN/USD con ROI y curva de retorno acumulado.
6. **Entregable**: Top 31 cuentas priorizadas, con perfil por zona, subestación y tipo de conexión para planificar rutas de inspección.

Los archivos de datos (`DATA_HISTORICO_CNR.xlsx`, `DATA_ALIMENTADOR.xlsx`) fueron provistos por la organización del hackathon y no se publican.

## Cómo correrlo

```bash
git clone https://github.com/Key-qr/Dataset.git
cd Dataset
python -m venv .venv
# Windows (Git Bash): source .venv/Scripts/activate
# Linux/macOS:        source .venv/bin/activate
pip install pandas numpy matplotlib seaborn plotly scikit-learn lightgbm openpyxl jupyter
jupyter notebook
```

Los notebooks leen los CSV con rutas relativas, así que hay que abrirlos desde su propia carpeta.

## Autora

Keysi Quiñe Rebaza · Arquitectura de Datos Empresariales, mención Big Data Developer (Cibertec)
GitHub: [Key-qr](https://github.com/Key-qr)
