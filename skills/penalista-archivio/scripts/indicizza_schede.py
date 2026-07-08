#!/usr/bin/env python3
"""
indicizza_schede.py — Kit Penalista Italia
Indicizza le schede delle PRONUNCE SEGNALATE (repo cassazione-penale-db) presenti in
<zona>/02_GIURISPRUDENZA/SEGNALATE/: genera in <zona>/_INDICE/ un manifest
*.index.json per anno, compatibile con genera_indice_master.py e con il
REGISTRO_FONTI (una riga per collezione/anno — decisione D2 della spec).

Le segnalate NON hanno ancora numero Rv (arriva col massimario annuale): si citano
per numero/anno e compaiono nella sezione "Registro segnalate" dell'INDICE master.

Uso: python3 indicizza_schede.py <dir_zona>     (es. KNOWLEDGE_BASE)
Chiamato automaticamente da aggiorna_indice.py se la cartella SEGNALATE esiste.
"""
import sys, os, re, json, glob

def leggi_frontmatter(path):
    fm = {}
    try:
        righe = open(path, encoding="utf-8").read().split("\n")
    except OSError:
        return fm
    if not righe or righe[0].strip() != "---":
        return fm
    corpo_da = 0
    for i, r in enumerate(righe[1:], 1):
        if r.strip() == "---":
            corpo_da = i + 1
            break
        m = re.match(r"(\w+):\s*(.*)", r)
        if m:
            v = m.group(2).strip().strip('"')
            fm[m.group(1)] = None if v in ("null", "") else v
    # incipit della massima/quesito per il registro (prima riga utile del primo blockquote)
    for r in righe[corpo_da:]:
        if r.startswith("> ") and r[2:].strip():
            fm["_incipit"] = (r[2:].strip()[:140] + ("…" if len(r[2:].strip()) > 140 else ""))
            break
    return fm

SEZ_ROM = {"Prima":"I","Seconda":"II","Terza":"III","Quarta":"IV","Quinta":"V",
           "Sesta":"VI","Settima":"VII","Sezioni Unite":"U"}

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 indicizza_schede.py <dir_zona>"); sys.exit(2)
    zona = os.path.abspath(sys.argv[1])
    seg = os.path.join(zona, "02_GIURISPRUDENZA", "SEGNALATE")
    out = os.path.join(zona, "_INDICE")
    if not os.path.isdir(seg):
        print("[indicizza_schede] nessuna cartella SEGNALATE nella zona: nulla da fare.")
        return
    os.makedirs(out, exist_ok=True)

    per_anno = {}
    for p in sorted(glob.glob(os.path.join(seg, "*", "*.md"))):
        if os.sep + "_QUARANTENA" + os.sep in p:
            continue
        fm = leggi_frontmatter(p)
        if not fm.get("tipo"):
            continue
        anno = fm.get("anno") or os.path.basename(os.path.dirname(p))
        rel = os.path.relpath(p, zona)
        if fm["tipo"] == "questione-su":
            rif = f"QSP R.G. {fm.get('rg')} {(fm.get('stato') or '?').upper()}"
            etich = f"ud. {fm.get('data_udienza') or '?'}" + (f" · {fm['materia']}" if fm.get("materia") else "")
        else:
            sez = SEZ_ROM.get(fm.get("sezione") or "", fm.get("sezione") or "?")
            rif = f"Cass. Sez. {sez} n. {fm.get('numero')}/{fm.get('anno')}"
            etich = f"{fm.get('materia') or 'materia n.i.'} · dep. {fm.get('data_deposito') or '?'}"
            if fm.get("rv"):
                rif += f" (Rv {fm['rv']})"
        per_anno.setdefault(str(anno), []).append(
            {"rif": rif, "etichetta": etich, "file": rel,
             "massima_incipit": fm.get("_incipit", "")})

    # rimuove manifest segnalate di run precedenti (rigenerazione pulita)
    for f in glob.glob(os.path.join(out, "Pronunce_Segnalate_*.index.json")):
        os.remove(f)

    # ---- CONSULTA: una sola fonte-riga per l'intero archivio (registro dedicato)
    cons = os.path.join(zona, "02_GIURISPRUDENZA", "CONSULTA")
    for f in glob.glob(os.path.join(out, "Corte_Costituzionale.index.json")):
        os.remove(f)
    if os.path.isdir(cons):
        n_cons = sum(1 for dp, dn, fn in os.walk(cons) for x in fn
                     if x.endswith(".md") and not x.startswith("INDICE"))
        anni = sorted(d for d in os.listdir(cons) if d.isdigit())
        man = {"fonte": f"Corte costituzionale — archivio completo {anni[0]}–{anni[-1]}" if anni
                        else "Corte costituzionale — archivio",
               "tipo": "corte-costituzionale",
               "file_md": "02_GIURISPRUDENZA/CONSULTA/",
               "pagine_con_testo": "—",
               "sentenze_rv": n_cons,
               "strutturale": [], "citazioni": [],
               "registro_dedicato": "02_GIURISPRUDENZA/CONSULTA/INDICE_CONSULTA.md"}
        json.dump(man, open(os.path.join(out, "Corte_Costituzionale.index.json"), "w",
                            encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"[indicizza_schede] CONSULTA: {n_cons} pronunce -> Corte_Costituzionale.index.json")

    tot = 0
    for anno, schede in sorted(per_anno.items()):
        man = {"fonte": f"Pronunce segnalate Massimario {anno}",
               "tipo": "massimario-segnalate",
               "file_md": f"02_GIURISPRUDENZA/SEGNALATE/{anno}/",
               "pagine_con_testo": "—",
               "sentenze_rv": len(schede),
               "strutturale": [], "citazioni": [],
               "schede": schede}
        dest = os.path.join(out, f"Pronunce_Segnalate_{anno}.index.json")
        json.dump(man, open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        tot += len(schede)
        print(f"[indicizza_schede] {anno}: {len(schede)} schede -> {os.path.basename(dest)}")
    print(f"[indicizza_schede] totale schede indicizzate: {tot}")

if __name__ == "__main__":
    main()
