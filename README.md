# Análisis Bioinformático de la Insulina Humana

## Descripción
Trabajo Práctico Final Integrador de la cátedra **Bioinformática 1** (FIUNER). Este proyecto aborda el estudio integral del gen de la insulina humana (*INS*, ID: `AH002844.2`), su precursor proteico preproinsulina (`NP_000198.1`) y la estructura tridimensional de su hexámero estabilizado por iones de Zinc (PDB ID: `1AIY`).

## Estructura del Proyecto
* `data/`: Secuencias nucleotídicas y proteicas en formato FASTA y GenBank.
* `scripts/`: Script en Python para descarga automatizada, cálculo de métricas y búsqueda de motivos mediante expresiones regulares.
* `results/`: Visualizaciones estructurales 3D generadas en UCSF ChimeraX.

## Prerrequisitos
* Sistema operativo GNU/Linux o entorno WSL (Windows Subsystem for Linux).
* **Python 3.x** (utiliza exclusivamente librerías nativas: `urllib`, `re`, `os`).
* Herramientas de línea de comandos: `entrez-direct`, `gawk`, `grep`.
* **UCSF ChimeraX** para la inspección estructural 3D.

## Instrucciones de Ejecución
Desde la raíz del repositorio, otorgar permisos y ejecutar el script principal:

    chmod +x scripts/analisis_insulina.py
    python3 scripts/analisis_insulina.py

## Referencias Bibliográficas
1. Bell, G. I., Pictet, R. L., Rutter, W. J., Cordell, B., Tischer, E., & Goodman, H. M. (1980). Sequence of the human insulin gene. *Nature*, 284(5751), 26-32.
2. Chang, X., Jorgensen, A. M., Bardrum, P., & Led, J. J. (1997). Solution structures of the R6 human insulin hexamer. *Biochemistry*, 36(31), 9409-9422.
3. Owerbach, D., Bell, G. I., Rutter, W. J., & Shows, T. B. (1980). The insulin gene is located on chromosome 11 in humans. *Nature*, 286(5768), 82-84.
