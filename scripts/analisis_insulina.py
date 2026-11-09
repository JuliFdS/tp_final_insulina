#!/usr/bin/env python3
# Descripción: Automatización del análisis bioinformático de la insulina (Gen y Proteína)
import urllib.request
import re
import os

if not os.path.exists("data"):
    os.makedirs("data")

# ==============================================================================
# SECCIÓN 1: OBTENCIÓN DE DATOS (Descarga automatizada)
# ==============================================================================
urls = {
    "data/insulina_gen.fasta": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AH002844.2&rettype=fasta&retmode=text",
    "data/insulina_gen.gb": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AH002844.2&rettype=gb&retmode=text",
    "data/insulina_prot.fasta": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=NP_000198.1&rettype=fasta&retmode=text"
}

for archivo, url in urls.items():
    urllib.request.urlretrieve(url, archivo)

def leer_fasta(ruta):
    secuencia = ""
    cantidad = 0
    with open(ruta, "r") as f:
        for linea in f:
            if linea.startswith(">"):
                cantidad += 1
            else:
                secuencia += linea.strip().upper()
    return secuencia, cantidad

# ==============================================================================
# SECCIÓN 2: MÉTRICAS DEL ADN
# ==============================================================================
seq_adn, cant_adn = leer_fasta("data/insulina_gen.fasta")
long_adn = len(seq_adn)
gc_count = seq_adn.count('G') + seq_adn.count('C')
porcentaje_gc = (gc_count / long_adn) * 100

print("=== MÉTRICAS DEL GEN (AH002844.2) ===")
print(f"Cantidad de secuencias: {cant_adn}")
print(f"Longitud: {long_adn} pb")
print(f"Porcentaje GC: {porcentaje_gc:.2f}%\n")

# ==============================================================================
# SECCIÓN 3: MÉTRICAS DE LA PROTEÍNA
# ==============================================================================
seq_prot, cant_prot = leer_fasta("data/insulina_prot.fasta")
long_prot = len(seq_prot)

conteo_aa = {}
for aa in seq_prot:
    conteo_aa[aa] = conteo_aa.get(aa, 0) + 1

print("=== COMPOSICIÓN DE AMINOÁCIDOS (NP_000198.1) ===")
print(f"Cantidad de secuencias: {cant_prot} | Longitud: {long_prot} aa")

for aa, cant in sorted(conteo_aa.items(), key=lambda x: x[1], reverse=True):
    porcentaje_aa = (cant / long_prot) * 100
    print(f"  Aminoácido {aa}: {cant} ({porcentaje_aa:.2f}%)")
print()

# ==============================================================================
# SECCIÓN 4: BÚSQUEDA DE MOTIVOS (REGEX)
# ==============================================================================
poly_a = re.findall(r'AATAAA', seq_adn)
print(f"Señales de poliadenilación (AATAAA): {len(poly_a)}")

orfs = re.findall(r'ATG(?:[ACGT]{3}){10,}(?:TAA|TAG|TGA)', seq_adn)
print(f"Candidatos a ORFs detectados en el gen: {len(orfs)}")

motivo_cys = re.findall(r'CC[A-Z]{3}C[A-Z]{8}C', seq_prot)
print(f"Motivo de cisteínas conservado en proteína: {motivo_cys[0]}")
