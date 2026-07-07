#!/usr/bin/env python3
"""
sincronizza_segnalate.py — Kit Penalista Italia
Scarica/aggiorna la banca dati delle PRONUNCE SEGNALATE della Cassazione penale
(repo pubblico Synthos-Logic/cassazione-penale-db — nessun account GitHub richiesto)
dentro <zona>/02_GIURISPRUDENZA/SEGNALATE/ e rilancia l'indicizzazione della zona.

ATTENZIONE: la cartella SEGNALATE è di proprietà della pipeline — le modifiche
locali alle schede vengono sovrascritte. Le note personali vanno altrove in KB.

Uso: python3 sincronizza_segnalate.py <dir_zona>     (es. KNOWLEDGE_BASE)
"""
import sys, os, shutil, subprocess, tempfile

REPO_URL = "https://github.com/Synthos-Logic/cassazione-penale-db.git"

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 sincronizza_segnalate.py <dir_zona>"); sys.exit(2)
    zona = os.path.abspath(sys.argv[1])
    dest = os.path.join(zona, "02_GIURISPRUDENZA", "SEGNALATE")
    here = os.path.dirname(os.path.abspath(__file__))

    tmp = tempfile.mkdtemp(prefix="cpdb_")
    print(f"[sync] clone {REPO_URL} ...")
    r = subprocess.run(["git", "clone", "--depth", "1", REPO_URL, tmp],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("[sync][ERRORE] clone fallito. Verifica la connessione o scarica lo ZIP da\n"
              f"  {REPO_URL[:-4]} (Code -> Download ZIP) e copia la cartella SEGNALATE in\n"
              f"  {dest}\nDettaglio: {r.stderr.strip()[:300]}")
        sys.exit(1)

    src = os.path.join(tmp, "SEGNALATE")
    if not os.path.isdir(src):
        print("[sync][ERRORE] il repo scaricato non contiene SEGNALATE/: struttura cambiata?")
        sys.exit(1)

    if os.path.isdir(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
    n = sum(1 for dp, dn, fn in os.walk(dest) for f in fn
            if f.endswith(".md") and f not in ("INDICE.md", "RASSEGNE.md", "LOG_ERRORI.md"))
    print(f"[sync] SEGNALATE aggiornata: {n} schede in {dest}")
    shutil.rmtree(tmp, ignore_errors=True)

    print("[sync] reindicizzazione della zona ...")
    subprocess.run([sys.executable, os.path.join(here, "aggiorna_indice.py"), zona], check=False)
    print("[sync] FATTO. Le segnalate sono ora citabili via INDICE/REGISTRO della zona.")

if __name__ == "__main__":
    main()
