# Kit Penalista Italiano

[![Versione](https://img.shields.io/badge/versione-3.0.0-blue)](https://github.com/Synthos-Logic/penalista-italia/releases)
[![Licenza](https://img.shields.io/badge/licenza-MIT-green)](LICENSE)
[![Piattaforma](https://img.shields.io/badge/piattaforma-Claude%20Cowork-orange)](https://claude.ai)

Kit operativo completo per avvocati penalisti italiani su Claude Cowork.

---

## Installazione â 3 passi

### 1. Scarica il kit
Clicca **Code â Download ZIP** in questa pagina. Decomprimi e rinomina la cartella in `Penale-Italia`.

### 2. Installa le 6 skill
Copia le 6 cartelle da `skills/` nella cartella di Claude:

**Mac:** Finder â Vai â Vai alla cartella â incolla `~/.claude/skills` â copia le 6 cartelle.

**Windows:** Esplora File â barra indirizzi â `%USERPROFILE%\.claude\skills` â copia le 6 cartelle.

Cartelle da copiare: `penalista-atti`, `penalista-cautelare`, `penalista-esecuzione`, `penalista-giurisprudenza`, `penalista-scadenze`, `penalista-strategia`.

> **Mac:** la cartella `.claude` Ã¨ nascosta â premi `Cmd+Shift+.` per vederla. Se la cartella `skills` non esiste, creala dentro `.claude`.

### 3. Collega il kit a Cowork
Apri Claude Desktop â Cowork â **"Seleziona cartella"** â seleziona la cartella `Penale-Italia` (tutta). Riavvia Claude Desktop.

---

## Configura i dati del tuo studio
Apri `CLAUDE.md` e compila la sezione "Dati dello studio" con nome, foro, tribunale, numero iscrizione. Salva. Claude userÃ  questi dati nelle intestazioni degli atti.

---

## Aggiornamento
1. Scarica il nuovo ZIP (Code â Download ZIP)
2. Sostituisci la cartella `Penale-Italia`
3. Se ci sono nuove skill: copia le nuove cartelle in `~/.claude/skills/`
4. Riavvia Claude Desktop

---

## Come organizzarsi
Un unico progetto Cowork per tutto lo studio. Una cartella per ogni fascicolo dentro `FASCICOLI/`. Non creare un progetto per ogni cliente.

---

## Cosa include

### 6 Skill operative
| Skill | Funzione |
|---|---|
| `penalista-atti` | Analisi e schedatura di atti processuali (informative, ordinanze, intercettazioni, perizie) |
| `penalista-memorie` | Redazione memorie difensive 415-bis, note udienza, lista testi, conclusioni scritte |
| `penalista-impugnazioni` | Appello, riesame (art. 309), ricorso Cassazione, opposizione a decreto penale |
| `penalista-giurisprudenza` | Ricerca orientamenti Cassazione, contrasti tra sezioni, CEDU |
| `penalista-pareri` | Pareri pro veritate, risk assessment penale, qualificazione giuridica |
| `penalista-scadenze` | Calcolo termini (prescrizione, custodia cautelare, impugnazioni, Cartabia) |

### Knowledge Base
- 13 Schede Reato operative (8 macro-categorie)
- Gerarchia delle fonti giuridiche
- I 9 volumi Massimari Cassazione 2023-2024 vanno aggiunti localmente in `KNOWLEDGE_BASE/02_GIURISPRUDENZA/`

### Fascicolo simulato
Caso Mario Rossi: truffa aggravata + reati tributari + autoriciclaggio.

---

## Privacy
I file restano sul tuo computer. Il testo analizzato transita sui server Anthropic.
La **Legge 132/2025 art. 13** impone di informare i clienti dell'uso dell'AI.

[Pagina Privacy completa](https://github.com/Synthos-Logic/penalista-italia/wiki/Privacy) | [Guida installazione dettagliata](documentazione/INSTALLAZIONE.md)