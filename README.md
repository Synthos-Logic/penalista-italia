# Kit Penalista Italiano

[![Versione](https://img.shields.io/badge/versione-3.0.0-blue)](https://github.com/Synthos-Logic/penalista-italia/releases)
[![Licenza](https://img.shields.io/badge/licenza-MIT-green)](LICENSE)
[![Piattaforma](https://img.shields.io/badge/piattaforma-Claude%20Cowork-orange)](https://claude.ai)

Kit operativo completo per avvocati penalisti italiani su Claude Cowork.

---

## Installazione — 3 passi

### Passo 1 — Scarica il kit

Clicca il bottone verde **"Code"** in questa pagina, poi **"Download ZIP"**. Decomprimi il file e rinomina la cartella estratta in `Penale-Italia`. Mettila dove vuoi (es. Documenti).

### Passo 2 — Installa le 6 skill

Devi copiare 6 cartelle in un punto specifico del tuo computer.

**Su Mac:**

1. Apri il **Finder**
2. Nel menu in alto clicca **Vai** poi **Vai alla cartella...** (o usa la scorciatoia **Cmd+Shift+G**)
3. Nella finestra che appare, incolla esattamente: `~/.claude/skills` e premi Invio
4. Se compare un errore "cartella non trovata": prima incolla `~/.claude` e crea una nuova cartella chiamata `skills` dentro di essa, poi torna al punto 3

> **Non vedi la cartella .claude nel Finder?** Premi **Cmd+Shift+.** (punto) per mostrare i file nascosti. Oppure usa il metodo con Vai alla cartella — funziona anche senza vedere le cartelle nascoste.

5. Copia le 6 cartelle da `Penale-Italia/skills/` nella cartella `skills` appena aperta

**Su Windows:**

1. Apri **Esplora File**
2. Clicca nella barra degli indirizzi in alto e incolla: `%USERPROFILE%\.claude\skills` poi premi Invio
3. Se non esiste, crea prima la cartella `.claude` dentro la home, poi `skills` dentro `.claude`
4. Copia le 6 cartelle da `Penale-Italia\skills\` nella cartella `skills` appena aperta

**Le 6 cartelle da copiare:**
`penalista-strategia`, `penalista-atti`, `penalista-scadenze`, `penalista-cautelare`, `penalista-giurisprudenza`, `penalista-esecuzione`

Ogni cartella contiene un solo file: `SKILL.md`. Non rinominarlo.

### Passo 3 — Collega il kit a Cowork

1. Apri **Claude Desktop**
2. Seleziona la modalità **Cowork**
3. Clicca **"Seleziona cartella"** (nella barra sotto la chat)
4. Naviga e seleziona la cartella **`Penale-Italia`** — tutta, non solo una sottocartella
5. **Riavvia Claude Desktop** per caricare le skill

---

## Configura i dati del tuo studio

Apri il file `CLAUDE.md` nella cartella `Penale-Italia` con TextEdit (Mac) o Blocco Note (Windows) e compila la sezione "Dati dello studio":

```
AVVOCATO:          Avv. Mario Rossi
FORO:              Foro di Milano
N. ISCRIZIONE:     12345
TRIBUNALE:         Tribunale di Milano
CASSAZIONISTA:     NO
```

Salva. Claude usa questi dati nelle intestazioni degli atti.

---

## Aggiornamento

Quando esce una nuova versione:
1. Scarica il nuovo ZIP (Code → Download ZIP)
2. Sostituisci la cartella `Penale-Italia` sul tuo computer
3. Se il changelog indica nuove skill: copia le nuove cartelle in `~/.claude/skills/`
4. Riavvia Claude Desktop

---

## Come organizzarsi

Un unico progetto Cowork per tutto lo studio. Crea una sottocartella per ogni fascicolo dentro `FASCICOLI/`:

```
FASCICOLI/
├── 2026_ROSSI_Truffa_aggravata/
├── 2026_BIANCHI_Bancarotta/
└── ...
```

Non creare un progetto Cowork separato per ogni cliente — perderesti il contesto tra i casi.

---

## Cosa include il kit

### 6 Skill operative

| Skill | Funzione |
|---|---|
| `penalista-strategia` | Analisi difensiva del capo di imputazione: elementi costitutivi, criticità accusa, eccezioni, giurisprudenza |
| `penalista-atti` | Redazione atti processuali: memoria 415-bis, appello, riesame, ricorso Cassazione |
| `penalista-scadenze` | Calcolo termini: prescrizione (ante/post Bonafede), custodia cautelare, impugnazioni, Cartabia |
| `penalista-cautelare` | Misure cautelari: analisi presupposti, riesame, revoca/sostituzione, scadenze di fase |
| `penalista-giurisprudenza` | Ricerca orientamenti Cassazione, contrasti tra sezioni, CEDU |
| `penalista-esecuzione` | Diritto penitenziario: misure alternative, liberazione anticipata/condizionale, 41-bis |

### Knowledge Base
- 13 Schede Reato operative (8 macro-categorie)
- Gerarchia delle fonti giuridiche
- I 9 volumi Massimari Cassazione 2023-2024 si aggiungono localmente in `KNOWLEDGE_BASE/02_GIURISPRUDENZA/`

### Fascicolo simulato
Caso Mario Rossi: truffa aggravata + reati tributari + autoriciclaggio.

---

## Privacy

I file fisici restano sul tuo computer. Il testo che chiedi a Claude di analizzare transita sui server di Anthropic.
La **Legge 132/2025 art. 13** impone di informare i clienti dell'uso dell'AI. Il CNF ha pubblicato uno schema di informativa.

[Pagina Privacy completa](https://github.com/Synthos-Logic/penalista-italia/wiki/Privacy) | [Guida installazione dettagliata](documentazione/INSTALLAZIONE.md)