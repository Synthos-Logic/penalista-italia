# Changelog — Kit Penalista Italiano

Tutte le modifiche significative vengono documentate qui.
Formato: [Versione] — Data — Aggiornamento skill necessario: Sì / No

---

## [v2.1] — Maggio 2026
**Aggiornamento skill necessario: No**

### Aggiunto
- `KNOWLEDGE_BASE/06_SCHEDE_REATO/` — 13 schede operative per i reati più diffusi negli studi penali italiani
  - `A_REATI_PATRIMONIO/` — Truffa (art. 640), Furto/Rapina/Estorsione (artt. 624-629), Appropriazione indebita (art. 646), Riciclaggio/Autoriciclaggio (artt. 648-bis, 648-ter.1)
  - `B_REATI_PERSONA/` — Maltrattamenti/Stalking (artt. 572, 612-bis), Omicidio e Lesioni stradali (artt. 589-bis, 590-bis)
  - `C_REATI_TRIBUTARI/` — D.Lgs. 74/2000 completo (artt. 2, 3, 4, 5, 8, 10-bis, 10-ter, 10-quater, 11)
  - `D_REATI_PA/` — Corruzione/Peculato/Concussione (artt. 314, 317, 318, 319, 319-ter, 321, 353)
  - `E_REATI_SOCIETARI_FALLIMENTARI/` — Bancarotta fraudolenta (artt. 216-217 L.F. / 322-323 CCII), False comunicazioni sociali (artt. 2621-2622 c.c.)
  - `F_REATI_INFORMATICI/` — Accesso abusivo, Frode informatica, Revenge porn (artt. 615-ter, 640-ter, 612-ter)
  - `G_STUPEFACENTI/` — D.P.R. 309/1990 artt. 73, 74, 75
  - `H_CRIMINALITA_ORGANIZZATA/` — Associazione per delinquere, Associazione mafiosa (artt. 416, 416-bis)
- `KNOWLEDGE_BASE/06_SCHEDE_REATO/00_README.md` — guida all'uso e template standard per nuove schede
- `README.md` — documentazione GitHub con guida installazione rapida
- `CHANGELOG.md` — questo file
- `.gitignore` — esclusione fascicoli reali e dati sensibili

### Modificato
- `documentazione/MAPPA_KIT.html` → v2.1: nuova sezione "Schede Reato" con mappa delle 8 macro-categorie e tabella dettagliata di cosa inserire in ogni sezione
- `documentazione/MAPPA_KIT.html` — **fix guida installazione**: Passo 2 (fascicoli dentro kit, non cartella separata), Passo 4 (collegare intera cartella Penale-Italia, non solo FASCICOLI), Passo 7 (istruzioni esplicite per trovare ~/.claude/skills/)
- `CLAUDE.md` → v2.1: aggiornata struttura cartelle con `06_SCHEDE_REATO/`
- `KNOWLEDGE_BASE/00_META/REGISTRO_DOCUMENTI.md` → v2.1: aggiunto indice schede reato
- Struttura kit pulita: rimosso duplicato `MAPPA_KIT.html` dalla root

---

## [v2.0] — Maggio 2026
**Aggiornamento skill necessario: No**

### Aggiunto
- `KNOWLEDGE_BASE/` — corpus documentale ufficiale con 9 volumi:
  - Massimario Penale 2024 (volume unico)
  - Massimario Penale 2023 (Vol. I — 252 pp. e Vol. II — 176 pp.)
  - Massimario Civile 2024 (Vol. I, II, III)
  - Massimario Civile 2023 (Vol. I — 320 pp., Vol. II — 268 pp., Vol. III — 288 pp.)
- `KNOWLEDGE_BASE/00_META/GERARCHIA_FONTI.md` — regole per Claude su come pesare le fonti (SU > sezioni semplici > Corte Cost. > CEDU > dottrina > merito)
- `KNOWLEDGE_BASE/00_META/REGISTRO_DOCUMENTI.md` — indice completo del corpus
- `FASCICOLI/` — cartella per i fascicoli reali dello studio

### Modificato
- `CLAUDE.md` → v2.0: aggiunte regole operative 8 (usa KB) e 9 (rispetta gerarchia fonti); aggiornata struttura cartelle
- `documentazione/MAPPA_KIT.html` → v2.0: nuova sezione Knowledge Base con visualizzazione gerarchia fonti e istruzioni per aggiungere documenti

---

## [v1.0] — Aprile 2026
**Prima release**

### Aggiunto
- 6 skill Cowork: `penalista-atti`, `penalista-memorie`, `penalista-impugnazioni`, `penalista-giurisprudenza`, `penalista-pareri`, `penalista-scadenze`
- Fascicolo simulato completo: Mario Rossi (truffa aggravata + reati tributari D.Lgs. 74/2000 + autoriciclaggio) con 4 vizi procedurali nascosti
- Template documentale: `documentazione/documentale-template/STRUTTURA_FASCICOLO.md`
- Demo output: `documentazione/output_demo/`
- `INSTALLAZIONE.md` — guida installazione testuale
- `MAPPA_KIT.html` v1.0 — mappa visuale + guida for dummies
- `CLAUDE.md` v1.0 — istruzioni operative base

---

## Come leggere questo file

Ogni release indica:
- **Aggiornamento skill necessario: Sì** → devi sostituire i file in `~/.claude/skills/` oltre alla cartella `Penale-Italia/`
- **Aggiornamento skill necessario: No** → basta sostituire la cartella `Penale-Italia/`; le skill installate restano valide
