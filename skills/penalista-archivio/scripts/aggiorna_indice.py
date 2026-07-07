#!/usr/bin/env python3
"""
aggiorna_indice.py — Kit Penalista Italia
Aggiorna l'indice di UNA ZONA documentale. Scansiona i PDF della zona, converte
solo quelli nuovi/modificati, rigenera l'INDICE master e il REGISTRO_FONTI.

Zone:
  - GLOBALE  : KNOWLEDGE_BASE           (fonti consultabili in ogni fascicolo)
  - FASCICOLO: FASCICOLI/<caso>         (materiale di causa, scoped a quel caso)

L'output va sempre in <zona>/_INDICE/. Stesso strumento, due posti: questo dà lo
scoping per costruzione (l'indice globale e quello del fascicolo restano separati).

Uso:  python3 aggiorna_indice.py <dir_zona>
"""
import sys, os, re, json, glob, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
CONV = os.path.join(HERE, "converti_indicizza.py")
MAST = os.path.join(HERE, "genera_indice_master.py")

def titolo_da_nome(p):
    b = os.path.splitext(os.path.basename(p))[0]
    return re.sub(r'[_\-]+', ' ', b).strip()

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 aggiorna_indice.py <dir_zona>"); sys.exit(2)
    zona = os.path.abspath(sys.argv[1])
    out = os.path.join(zona, "_INDICE")
    os.makedirs(out, exist_ok=True)
    pdfs = [p for p in glob.glob(os.path.join(zona, "**", "*.pdf"), recursive=True)
            if "/_INDICE/" not in p]
    print(f"Zona: {zona}\nPDF trovati: {len(pdfs)}")
    nuovi = 0; saltati = 0; scansioni = 0
    for pdf in sorted(pdfs):
        base = os.path.splitext(os.path.basename(pdf))[0]
        idx = os.path.join(out, base + ".index.json")
        if os.path.exists(idx) and os.path.getmtime(idx) >= os.path.getmtime(pdf):
            saltati += 1; continue
        r = subprocess.run([sys.executable, CONV, pdf, out, "--titolo", titolo_da_nome(pdf)],
                           capture_output=True, text=True)
        sys.stdout.write("  " + (r.stdout or r.stderr))
        if r.returncode == 3: scansioni += 1
        elif r.returncode == 0: nuovi += 1
    # indicizza le pronunce segnalate (cassazione-penale-db) se presenti nella zona
    SCH = os.path.join(HERE, "indicizza_schede.py")
    if os.path.isdir(os.path.join(zona, "02_GIURISPRUDENZA", "SEGNALATE")):
        r = subprocess.run([sys.executable, SCH, zona], capture_output=True, text=True)
        sys.stdout.write(r.stdout or r.stderr)
    # rigenera master
    subprocess.run([sys.executable, MAST, out, os.path.join(out, "INDICE.md")], check=False)
    # registro fonti (manifest)
    vols = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(out, "*.index.json")))]
    R = ["# REGISTRO FONTI — zona indicizzata", "",
         f"> Aggiornato il {datetime.date.today().isoformat()}. "
         f"Queste sono **tutte e sole** le fonti consultabili in questa zona. "
         f"Ciò che non è elencato qui NON è nella KB.", "",
         "| Fonte | Tipo | Pagine | Sentenze (Rv/schede) | File |", "|---|---|---|---|---|"]
    for v in vols:
        R.append(f"| {v['fonte']} | {v.get('tipo','documento')} | "
                 f"{v.get('pagine_con_testo','?')} | {v['sentenze_rv']} | `{v['file_md']}` |")
    open(os.path.join(out, "REGISTRO_FONTI.md"), "w").write("\n".join(R))
    print(f"\n[FATTO] nuovi: {nuovi} | gia' indicizzati (saltati): {saltati} | "
          f"scansioni da OCR: {scansioni} | fonti totali in zona: {len(vols)}")
    print(f"        indice:  {os.path.join(out,'INDICE.md')}")
    print(f"        registro:{os.path.join(out,'REGISTRO_FONTI.md')}")

if __name__ == "__main__": main()
