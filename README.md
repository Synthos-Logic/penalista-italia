# Kit Penalista Italiano

[![Versione](https://img.shields.io/badge/versione-3.0.0-blue)](https://github.com/Synthos-Logic/penalista-italia/releases)
[![Licenza](https://img.shields.io/badge/licenza-MIT-green)](LICENSE)

Kit operativo per avvocati penalisti italiani su Claude Cowork.

---

## Installazione — 3 passi

### Passo 1 — Scarica il kit

Clicca **Code → Download ZIP**, decomprimi e rinomina la cartella in `Penale-Italia`.

### Passo 2 — Installa le 6 skill

Copia le 6 cartelle da `skills/` nella cartella skill di Claude.

**Su Mac:**

1. Apri il **Finder**
2. Nel menu in alto: **Vai → Vai alla cartella...** (o premi **Cmd+Shift+G**)
3. Incolla: `~/.claude/skills` e premi Invio
4. Se non trova la cartella: vai prima a `~/.claude`, crea la cartella `skills`
5. Copia le 6 cartelle da `Penale-Italia/skills/` dentro `skills`

> La cartella `.claude` è nascosta. Se non la vedi: premi **Cmd+Shift+.** nel Finder. Il metodo "Vai alla cartella" funziona anche senza vedere le cartelle nascoste.

**Su Windows:**

1. Apri **Esplora File**
2. Nella barra indirizzi incolla: `%USERPROFILE%\.claude\skills` e premi Invio
3. Se non esiste: crea `.claude` nella home, poi `skills` dentro
4. Copia le 6 cartelle

**Le 6 cartelle:** `penalista-strategia`, `penalista-atti`, `penalista-scadenze`, `penalista-cautelare`, `penalista-giurisprudenza`, `penalista-esecuzione`

### Passo 3 — Collega il kit a Cowork

Claude Desktop → Cowork → **Seleziona cartella** → seleziona `Penale-Italia` (tutta). Riavvia Claude Desktop.

---

## Configura i dati del tuo studio

Apri `CLAUDE.md` con TextEdit (Mac) o Blocco Note (Windows) e compila:

```
AVVOCATO:          Avv. Mario Rossi
FORO:              Foro di Milano
N. ISCRIZIONE:     12345
TRIBUNALE:         Tribunale di Milano
CASSAZIONISTA:     NO
```

---

## Aggiornamento

1. Scarica il nuovo ZIP (Code → Download ZIP)
2. Sostituisci la cartella `Penale-Italia`
3. Se ci sono nuove skill: copia le nuove cartelle in `~/.claude/skills/`
4. Riavvia Claude Desktop

---

## Cosa include

### 6 Skill operative

| Skill | Funzione |
|---|---|
| `penalista-strategia` | Analisi difensiva del capo di imputazione |
| `penalista-atti` | Redazione atti: memoria 415-bis, appello, riesame, Cassazione |
| `penalista-scadenze` | Termini: prescrizione, custodia cautelare, impugnazioni, Cartabia |
| `penalista-cautelare` | Misure cautelari: analisi, riesame, revoca, scadenze di fase |
| `penalista-giurisprudenza` | Orientamenti Cassazione, contrasti, CEDU |
| `penalista-esecuzione` | Diritto penitenziario: misure alternative, liberazione, 41-bis |

### Knowledge Base
- 13 Schede Reato operative (8 macro-categorie)
- Gerarchia delle fonti giuridiche
- I 9 Massimari Cassazione 2023-2024 vanno aggiunti localmente in `KNOWLEDGE_BASE/02_GIURISPRUDENZA/`

---

## Privacy

I file restano sul tuo computer. Il testo analizzato transita sui server Anthropic.
La **Legge 132/2025 art. 13** impone di informare i clienti dell'uso dell'AI.

[Pagina Privacy completa](https://github.com/Synthos-Logic/penalista-italia/wiki/Privacy) | [Guida installazione dettagliata](documentazione/INSTALLAZIONE.md)