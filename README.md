# Kit Penalista Italiano

**v2.1 — Maggio 2026**

Ambiente di lavoro completo per la pratica penalistica italiana su [Claude Cowork](https://claude.ai).
6 skill specializzate · Knowledge Base giurisprudenziale · 13 Schede Reato operative · Fascicolo simulato

---

## Cosa include

### 6 Skill Cowork
Istruzioni operative che trasformano Claude in un assistente penalista specializzato:

| Skill | Funzione |
|---|---|
| `penalista-atti` | Analisi e schedatura di informative, ordinanze, intercettazioni, perizie |
| `penalista-memorie` | Redazione memorie 415-bis, note udienza, lista testi, conclusioni |
| `penalista-impugnazioni` | Appello, riesame (art. 309), ricorso Cassazione, opposizione decreto penale |
| `penalista-giurisprudenza` | Ricerca orientamenti, analisi sentenze, mappatura contrasti tra sezioni |
| `penalista-pareri` | Pareri pro veritate, risk assessment penale, qualificazione giuridica |
| `penalista-scadenze` | Calcolo termini: prescrizione, custodia cautelare, impugnazioni, sospensione feriale |

### Knowledge Base
- **9 volumi Massimari Cassazione** (Ufficio del Massimario, 2023-2024): Sezioni Penali + Sezioni Civili
- **13 Schede Reato** su 8 macro-categorie: Patrimonio, Persona, Tributari, PA, Societari, Informatici, Stupefacenti, Criminalità organizzata
- **Gerarchia delle fonti** — regole per pesare SU vs. sezioni semplici vs. CEDU vs. merito
- **Registro documenti** — indice completo del corpus

### Fascicolo Simulato
Caso completo per test e formazione: Mario Rossi, amministratore unico, imputato di truffa aggravata (art. 640 co. 2 n. 1 c.p.), emissione fatture false (art. 8 D.Lgs. 74/2000) e autoriciclaggio (art. 648-ter.1 c.p.). Contiene 4 vizi procedurali nascosti.

---

## Requisiti

- **Claude Desktop** con modalità **Cowork** attiva
- Account Claude **Pro** o **Team**
- Mac o Windows

---

## Installazione rapida

> Guida completa con screenshot: apri `documentazione/MAPPA_KIT.html` nel browser.

**1. Scarica il kit**

Clicca il bottone verde **"Code → Download ZIP"** in questa pagina, decomprimi e rinomina la cartella in `Penale-Italia`.

**2. Installa le 6 skill**

Copia le 6 cartelle da `skills/` nella cartella skill di Claude sul tuo computer:

```
# Mac
~/.claude/skills/

# Windows
%USERPROFILE%\.claude\skills\
```

Su Mac, la cartella `.claude` è nascosta: premi `Cmd + Shift + G` nel Finder e incolla `~/.claude/skills`.

**3. Collega il kit a Cowork**

Apri Claude Desktop → Cowork → **"Seleziona cartella"** → seleziona la cartella **`Penale-Italia`** intera (non solo la sottocartella FASCICOLI).

**4. Verifica**

Scrivi nella chat: *"Ho un fascicolo per truffa aggravata. Calcola il termine per depositare memoria 415-bis dalla notifica del 15 maggio 2026."* — Se Claude risponde con data precisa e calcolo strutturato, tutto funziona.

---

## Come aggiornare alla nuova versione

Quando viene rilasciato un aggiornamento:

1. Scarica il nuovo ZIP da questa pagina
2. Sostituisci la cartella `Penale-Italia` sul tuo computer con quella nuova
3. Se nel [CHANGELOG.md](CHANGELOG.md) è indicato *"Aggiornamento skill necessario: Sì"*, sostituisci anche i file in `~/.claude/skills/`
4. Riavvia Claude Desktop

> Le Schede Reato, la Knowledge Base e le istruzioni operative (CLAUDE.md) si aggiornano automaticamente con il punto 2. Le skill in `~/.claude/skills/` si aggiornano solo quando espressamente indicato.

---

## Struttura del repository

```
Penale-Italia/
├── README.md                    ← questo file
├── CHANGELOG.md                 ← storico versioni
├── INSTALLAZIONE.md             ← guida installazione testuale
├── CLAUDE.md                    ← istruzioni operative per Claude
├── skills/                      ← 6 skill (da copiare in ~/.claude/skills/)
│   ├── penalista-atti/SKILL.md
│   ├── penalista-memorie/SKILL.md
│   ├── penalista-impugnazioni/SKILL.md
│   ├── penalista-giurisprudenza/SKILL.md
│   ├── penalista-pareri/SKILL.md
│   └── penalista-scadenze/SKILL.md
├── documentazione/
│   ├── MAPPA_KIT.html           ← guida visuale + installazione (apri nel browser)
│   ├── documentale-template/    ← template struttura fascicolo
│   └── output_demo/             ← esempi di output generati dalle skill
├── FASCICOLI/                   ← i tuoi fascicoli reali (vuota — da popolare)
├── FASCICOLO_SIMULATO/          ← caso Mario Rossi per test
└── KNOWLEDGE_BASE/              ← corpus documentale
    ├── 00_META/                 ← gerarchia fonti + registro documenti
    ├── 01_NORMATIVA/            ← codici e normativa speciale
    ├── 02_GIURISPRUDENZA/       ← massimari Cassazione 2023-2024
    ├── 03_DOTTRINA/
    ├── 04_PRASSI_STUDIO/        ← fascicoli reali anonimizzati (da popolare)
    ├── 05_AGGIORNAMENTO/
    └── 06_SCHEDE_REATO/         ← 13 schede operative per reato
```

---

## Note operative importanti

- **Tutti gli atti prodotti sono BOZZE** — richiedono revisione dell'avvocato prima del deposito.
- **La giurisprudenza marcata [VERIFICARE]** — va controllata su banca dati (De Jure, Italgiure) prima di citarla in un atto.
- **I fascicoli reali** vanno nella cartella `FASCICOLI/` — non vengono tracciati da Git (vedi `.gitignore`).
- **La cartella `04_PRASSI_STUDIO/`** è destinata ai fascicoli reali anonimizzati dello studio — non viene tracciata da Git.

---

## Versioni

| Versione | Data | Novità principali |
|---|---|---|
| v2.1 | Maggio 2026 | 13 Schede Reato operative, fix guida installazione |
| v2.0 | Maggio 2026 | Knowledge Base con 9 Massimari Cassazione |
| v1.0 | Aprile 2026 | Prima release: 6 skill + fascicolo simulato |

Vedi [CHANGELOG.md](CHANGELOG.md) per il dettaglio completo.

---

## I Massimari della Corte di Cassazione

I 9 PDF presenti in `KNOWLEDGE_BASE/02_GIURISPRUDENZA/` sono pubblicazioni ufficiali dell'**Ufficio del Massimario e del Ruolo** della Corte Suprema di Cassazione, liberamente disponibili sul sito istituzionale della Corte. Sono inclusi nel kit per facilitarne l'accesso in sessione Cowork.
