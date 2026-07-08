#!/usr/bin/env python3
"""
sincronizza_segnalate.py — Kit Penalista Italia (v3.5.0)
Scarica/aggiorna la BANCA DATI GIURISPRUDENZIALE del kit (repo pubblico
Synthos-Logic/cassazione-penale-db — nessun account GitHub richiesto):

  - SEGNALATE/  -> KNOWLEDGE_BASE/02_GIURISPRUDENZA/SEGNALATE/
                   (pronunce segnalate dal Massimario + Radar del merito)
  - CONSULTA/   -> KNOWLEDGE_BASE/02_GIURISPRUDENZA/CONSULTA/
                   (archivio completo Corte costituzionale dal 1956, ~160 MB)

e rilancia l'indicizzazione della zona.

Per efficienza usa una CACHE git locale (<zona>/.banca_dati_cache): il primo sync
scarica tutto, i successivi solo i delta. Le cartelle SEGNALATE e CONSULTA sono
di proprietà della pipeline: le modifiche locali vengono sovrascritte.

Uso: python3 sincronizza_segnalate.py <dir_zona> [--solo-segnalate]
"""
import argparse, os, shutil, subprocess, sys

REPO_URL = "https://github.com/Synthos-Logic/cassazione-penale-db.git"

def run(cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)

def conta_schede(radice):
    return sum(1 for dp, dn, fn in os.walk(radice) for f in fn
               if f.endswith(".md") and not f.startswith(("INDICE", "RASSEGNE", "LOG_", "RADAR_")))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zona")
    ap.add_argument("--solo-segnalate", action="store_true",
                    help="non copiare l'archivio della Corte costituzionale (risparmia ~160 MB)")
    a = ap.parse_args()
    zona = os.path.abspath(a.zona)
    cache = os.path.join(zona, ".banca_dati_cache")
    here = os.path.dirname(os.path.abspath(__file__))

    # ---- cache git: clone la prima volta, pull (solo delta) le successive
    if os.path.isdir(os.path.join(cache, ".git")):
        print("[sync] aggiorno la cache locale (solo differenze)...")
        r = run(["git", "-C", cache, "pull", "--ff-only", "origin", "main"])
    else:
        print("[sync] primo scaricamento della banca dati (una tantum, ~160 MB)...")
        r = run(["git", "clone", "--depth", "1", REPO_URL, cache])
    if r.returncode != 0:
        print("[sync][ERRORE] scaricamento fallito. Verifica la connessione, oppure scarica lo ZIP da\n"
              f"  {REPO_URL[:-4]} (Code -> Download ZIP) e copia SEGNALATE/ e CONSULTA/ in\n"
              f"  {os.path.join(zona, '02_GIURISPRUDENZA')}\nDettaglio: {r.stderr.strip()[:300]}")
        sys.exit(1)

    # ---- copia nelle zone di destinazione
    da_copiare = ["SEGNALATE"] + ([] if a.solo_segnalate else ["CONSULTA"])
    for nome in da_copiare:
        src = os.path.join(cache, nome)
        if not os.path.isdir(src):
            print(f"[sync][ERRORE] il repo scaricato non contiene {nome}/: struttura cambiata?")
            sys.exit(1)
        dest = os.path.join(zona, "02_GIURISPRUDENZA", nome)
        if os.path.isdir(dest):
            shutil.rmtree(dest)
        shutil.copytree(src, dest)
        print(f"[sync] {nome} aggiornata: {conta_schede(dest)} schede in {dest}")

    # ---- reindicizzazione della zona
    print("[sync] reindicizzazione della zona ...")
    subprocess.run([sys.executable, os.path.join(here, "aggiorna_indice.py"), zona], check=False)
    print("[sync] FATTO. Segnalate e Consulta sono citabili via INDICE/REGISTRO della zona.")

if __name__ == "__main__":
    main()
