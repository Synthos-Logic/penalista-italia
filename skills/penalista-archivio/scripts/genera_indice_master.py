#!/usr/bin/env python3
"""genera_indice_master.py — unisce i *.index.json in un indice master Markdown
grep-friendly a due livelli: STRUTTURALE (concetto->pagina) + CITAZIONALE (Rv->pagina)."""
import sys, os, json, glob, datetime

def main():
    d, out = sys.argv[1], sys.argv[2]
    vols = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(d, "*.index.json")))]
    tot = sum(v["sentenze_rv"] for v in vols
              if not v.get("schede") and not v.get("registro_dedicato"))
    tot_seg = sum(v["sentenze_rv"] for v in vols
                  if v.get("schede") and not v.get("registro_dedicato"))
    tot_ded = sum(v["sentenze_rv"] for v in vols if v.get("registro_dedicato"))
    L = ["# INDICE GIURISPRUDENZA PENALE — Knowledge Base", "",
         f"> Generato il {datetime.date.today().isoformat()} da {len(vols)} fonti. "
         f"Sentenze indicizzate (Rv): {tot}."
         + (f" Pronunce segnalate (senza Rv): {tot_seg}." if tot_seg else "")
         + (f" Archivi con registro dedicato: {tot_ded} pronunce." if tot_ded else ""), ">",
         "> **Protocollo quote-then-claim.** Per citare una massima: cerca qui il numero "
         "**Rv** o la parte → ottieni *file* e *pagina* → apri il .md al marcatore "
         "`<!-- pag. N -->`, leggi e **incolla la massima testuale**. "
         "Per cercare un concetto: usa l'indice strutturale qui sotto oppure "
         "`grep` sul file .md. **Ciò che non è qui NON è nella KB**: in tal caso si dichiara "
         "'non presente in KB', non si cita a memoria.", "",
         "## 1. Indice strutturale (concetto → fonte : pagina)", ""]
    for v in vols:
        if v.get("schede") or v.get("registro_dedicato"): continue
        L += [f"### {v['fonte']} _( {v.get('tipo','documento')} )_  ·  `{v['file_md']}`", ""]
        for liv, et, tit, pag in v["strutturale"]:
            ind = "" if liv == "PARTE" else "  "
            etichetta = f"{et} — {tit}" if tit else et
            L.append(f"{ind}- **{etichetta}** — p.{pag}")
        L.append("")
    L += ["## 2. Registro citazionale (Rv → fonte : pagina → massima)", "",
          "Backbone del grounding: ogni riga è una sentenza realmente presente nelle Rassegne.", ""]
    for v in vols:
        if v.get("schede") or v.get("registro_dedicato"): continue
        L += [f"### {v['fonte']} _( {v.get('tipo','documento')} )_  ·  `{v['file_md']}`", ""]
        for c in sorted(v["citazioni"], key=lambda x: x["rv"]):
            pg = ",".join(f"p.{p}" for p in c["pagine"])
            L.append(f"- `Rv {c['rv']}` ({pg}) — {c['cit']}")
        L.append("")
    seg = [v for v in vols if v.get("schede") and not v.get("registro_dedicato")]
    if seg:
        L += ["## 3. Registro segnalate (numero/anno \u2192 scheda \u2192 massima)", "",
              "Pronunce segnalate dall'Ufficio del Massimario (aggiornamento settimanale via "
              "cassazione-penale-db). Non hanno ancora numero Rv: si citano per numero/anno "
              "con riferimento alla scheda e al PDF ufficiale linkato nella scheda. "
              "Le questioni SU PENDENTI non sono precedenti citabili come autorit\u00e0.", ""]
        for v in seg:
            L += [f"### {v['fonte']} _( {v.get('tipo')} )_  \u00b7  `{v['file_md']}`", ""]
            for c in v["schede"]:
                L.append(f"- `{c['rif']}` \u00b7 {c['etichetta']} \u2192 `{c['file']}` \u2014 {c['massima_incipit']}")
            L.append("")
    ded = [v for v in vols if v.get("registro_dedicato")]
    if ded:
        L += ["## 4. Archivi con registro dedicato", "",
              "Fonti consultabili con registro proprio (troppo ampie per questo indice): "
              "per NUMERO/ANNO cerca nel registro indicato; per NORMA fai grep direttamente "
              "sulle schede della cartella (es. `grep -rl '131-bis' .../CONSULTA/`), "
              "poi apri la scheda e cita la massima testuale.", ""]
        for v in ded:
            L.append(f"- **{v['fonte']}** _( {v.get('tipo')} )_ — {v['sentenze_rv']} pronunce → "
                     f"registro: `{v['registro_dedicato']}` · schede in `{v['file_md']}`")
        L.append("")
    open(out, "w").write("\n".join(L))
    print(f"[OK] indice master: {os.path.getsize(out)//1024} KB | {len(vols)} fonti | {tot} sentenze")

if __name__ == "__main__": main()
