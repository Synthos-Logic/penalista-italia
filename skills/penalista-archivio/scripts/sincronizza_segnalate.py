#!/usr/bin/env python3
"""
sincronizza_segnalate.py — Kit Penalista Italia (v3.6.0)
Scarica/aggiorna la BANCA DATI GIURISPRUDENZIALE del kit (repo pubblico
Synthos-Logic/cassazione-penale-db — nessun account GitHub richiesto):

  - SEGNALATE/  -> KNOWLEDGE_BASE/02_GIURISPRUDENZA/SEGNALATE/
                   (pronunce segnalate dal Massimario + Radar del merito)
  - CONSULTA/   -> KNOWLEDGE_BASE/02_GIURISPRUDENZA/CONSULTA/
                   (Corte costituzionale: di default gli ULTIMI 10 ANNI;
                   con --tutto l'archivio completo dal 1956, ~160 MB)

e rilancia l'indicizzazione della zona.

Dalla v3.6.0 l'archivio della Consulta è FILTRATO di default agli ultimi
10 anni (feedback operativo: 22.000+ pronunce dal 1956 sono rumore per il
lavoro quotidiano). Il repo remoto resta completo: --tutto scarica tutto,
--da-anno N sceglie una soglia diversa. Le pronunce storiche fondamentali
restano comunque raggiungibili dalla scheda ufficiale della Corte.

Per efficienza usa una CACHE git locale (<zona>/.banca_dati_cache): il primo
sync scarica solo la finestra scelta (sparse checkout), i successivi solo i
delta. Le cartelle SEGNALATE e CONSULTA sono di proprietà della pipeline:
le modifiche locali vengono sovrascritte.

Uso: python3 sincronizza_segnalate.py <dir_zona> [--tutto] [--da-anno N] [--solo-segnalate]
"""
import argparse, datetime, os, shutil, subprocess, sys

REPO_URL = "https://github.com/Synthos-Logic/cassazione-penale-db.git"
ANNI_FINESTRA = 10  # default richiesto dall'uso di studio: ultimi 10 anni


def run(cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def conta_schede(radice):
    return sum(1 for dp, dn, fn in os.walk(radice) for f in fn
               if f.endswith(".md") and not f.startswith(("INDICE", "RASSEGNE", "LOG_", "RADAR_")))


def imposta_sparse(cache, da_anno, tutto):
    """Limita il working tree della cache alla finestra scelta (e, sui cloni
    parziali, il download). Non bloccante: su git molto vecchi si prosegue
    e fa fede il filtro in fase di copia."""
    if tutto:
        r = run(["git", "-C", cache, "sparse-checkout", "disable"])
        return r.returncode == 0
    anno_max = datetime.date.today().year
    dirs = ["SEGNALATE"] + [f"CONSULTA/{a}" for a in range(da_anno, anno_max + 1)]
    # init --cone PRIMA del set: su git meno recenti (es. 2.34) '--cone' passato
    # a 'set' viene scambiato per un percorso; il cone mode serve anche a
    # includere i file radice (README, CONSULTA/INDICE_CONSULTA.md, ...)
    run(["git", "-C", cache, "sparse-checkout", "init", "--cone"])
    r = run(["git", "-C", cache, "sparse-checkout", "set"] + dirs)
    if r.returncode != 0:
        print(f"[sync] nota: sparse checkout non disponibile ({r.stderr.strip()[:120]}) — "
              "si scarica tutto e si filtra in copia.")
        return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zona")
    ap.add_argument("--tutto", action="store_true",
                    help="archivio Consulta completo dal 1956 (~160 MB) invece degli ultimi 10 anni")
    ap.add_argument("--da-anno", type=int, default=None,
                    help=f"soglia personalizzata (default: anno corrente - {ANNI_FINESTRA})")
    ap.add_argument("--solo-segnalate", action="store_true",
                    help="non copiare l'archivio della Corte costituzionale")
    a = ap.parse_args()
    zona = os.path.abspath(a.zona)
    cache = os.path.join(zona, ".banca_dati_cache")
    here = os.path.dirname(os.path.abspath(__file__))
    da_anno = a.da_anno or (datetime.date.today().year - ANNI_FINESTRA)
    if a.tutto:
        da_anno = 0

    # ---- cache git: clone la prima volta, pull (solo delta) le successive
    nuovo_clone = not os.path.isdir(os.path.join(cache, ".git"))
    if nuovo_clone:
        dim = "~160 MB" if a.tutto else "qualche decina di MB"
        print(f"[sync] primo scaricamento della banca dati (una tantum, {dim})...")
        cmd = ["git", "clone", "--depth", "1", REPO_URL, cache]
        if not a.tutto:
            # clone parziale: i contenuti fuori finestra non vengono proprio scaricati
            cmd = ["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse", REPO_URL, cache]
        r = run(cmd)
        if r.returncode != 0 and not a.tutto:
            # server/git senza clone parziale: si ripiega sul clone pieno
            r = run(["git", "clone", "--depth", "1", REPO_URL, cache])
    else:
        print("[sync] aggiorno la cache locale (solo differenze)...")
        r = run(["git", "-C", cache, "pull", "--ff-only", "origin", "main"])
    if r.returncode != 0:
        print("[sync][ERRORE] scaricamento fallito. Verifica la connessione, oppure scarica lo ZIP da\n"
              f"  {REPO_URL[:-4]} (Code -> Download ZIP) e copia SEGNALATE/ e CONSULTA/ in\n"
              f"  {os.path.join(zona, '02_GIURISPRUDENZA')}\nDettaglio: {r.stderr.strip()[:300]}")
        sys.exit(1)
    imposta_sparse(cache, da_anno, a.tutto)

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

        def fuori_finestra(dirpath, nomi):
            # filtro anche in copia (vale pure se lo sparse checkout non c'è)
            if nome != "CONSULTA" or os.path.abspath(dirpath) != os.path.abspath(src):
                return []
            return [n for n in nomi if n.isdigit() and int(n) < da_anno]

        shutil.copytree(src, dest, ignore=fuori_finestra)

        finestra = ""
        if nome == "CONSULTA" and not a.tutto:
            finestra = f" (dal {da_anno}; per l'archivio completo dal 1956: --tutto)"
            indice = os.path.join(dest, "INDICE_CONSULTA.md")
            if os.path.isfile(indice):
                t = open(indice, encoding="utf-8").read()
                avviso = (f"> ⚠️ **Copia locale filtrata: pronunce dal {da_anno} in poi.** L'indice qui sotto\n"
                          f"> elenca l'intero archivio remoto (dal 1956): le schede anteriori al {da_anno}\n"
                          "> non sono presenti in locale. Per averle: sincronizza con `--tutto`.\n\n")
                open(indice, "w", encoding="utf-8").write(t.replace("# INDICE", avviso + "# INDICE", 1)
                                                          if t.startswith("# INDICE") else avviso + t)
        print(f"[sync] {nome} aggiornata: {conta_schede(dest)} schede in {dest}{finestra}")

    # ---- reindicizzazione della zona
    print("[sync] reindicizzazione della zona ...")
    subprocess.run([sys.executable, os.path.join(here, "aggiorna_indice.py"), zona], check=False)
    print("[sync] FATTO. Segnalate e Consulta sono citabili via INDICE/REGISTRO della zona.")


if __name__ == "__main__":
    main()
