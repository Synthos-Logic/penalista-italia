#!/usr/bin/env python3
"""genera_indice_master.py — unisce i *.index.json in un indice master Markdown
grep-friendly a due livelli: STRUTTURALE (concetto->pagina) + CITAZIONALE (Rv->pagina)."""
import sys, os, json, glob, datetime

def main():
    d, out = sys.argv[1], sys.argv[2]
    vols = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(d, "*.index.json")))]
    tot = sum(v["sentenze_rv"] for v in vols)
    L = ["# INDICE GIURISPRUDENZA PENALE — Knowledge Base", "",
         f"> Generato il {datetime.date.today().isoformat()} da {len(vols)} fonti. "
         f"Sentenze indicizzate (Rv): {tot}.", ">",
         "> **Protocollo quote-then-claim.** Per citare una massima: cerca qui il numero "
         "**Rv** o la parte → ottieni *file* e *pagina* → apri il .md al marcatore "
         "`<!-- pag. N -->`, leggi e **incolla la massima testuale**. "
         "Per cercare un concetto: usa l'indice strutturale qui sotto oppure "
         "`grep` sul file .md. **Ciò che non è qui NON è nella KB**: in tal caso si dichiara "
         "'non presente in KB', non si cita a memoria.", "",
         "## 1. Indice strutturale (concetto → fonte : pagina)", ""]
    for v in vols:
        L += [f"### {v['fonte']} _( {v.get('tipo','documento')} )_  ·  `{v['file_md']}`", ""]
        for liv, et, tit, pag in v["strutturale"]:
            ind = "" if liv == "PARTE" else "  "
            etichetta = f"{et} — {tit}" if tit else et
            L.append(f"{ind}- **{etichetta}** — p.{pag}")
        L.append("")
    L += ["## 2. Registro citazionale (Rv → fonte : pagina → massima)", "",
          "Backbone del grounding: ogni riga è una sentenza realmente presente nelle Rassegne.", ""]
    for v in vols:
        L += [f"### {v['fonte']} _( {v.get('tipo','documento')} )_  ·  `{v['file_md']}`", ""]
        for c in sorted(v["citazioni"], key=lambda x: x["rv"]):
            pg = ",".join(f"p.{p}" for p in c["pagine"])
            L.append(f"- `Rv {c['rv']}` ({pg}) — {c['cit']}")
        L.append("")
    open(out, "w").write("\n".join(L))
    print(f"[OK] indice master: {os.path.getsize(out)//1024} KB | {len(vols)} fonti | {tot} sentenze")

if __name__ == "__main__": main()
