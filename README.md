# Kit Penalista Italiano

[![Versione](https://img.shields.io/badge/versione-3.0.0-blue)](https://github.com/Synthos-Logic/penalista-italia/releases)
[![Licenza](https://img.shields.io/badge/licenza-MIT-green)](LICENSE)
[![Piattaforma](https://img.shields.io/badge/piattaforma-Claude%20Cowork-orange)](https://claude.ai)

Kit operativo completo per avvocati penalisti italiani su Claude Cowork.

---

## Installazione Ã¢ÂÂ 3 passi

### 1. Scarica il kit
Clicca **Code Ã¢ÂÂ Download ZIP** in questa pagina. Decomprimi e rinomina la cartella in `Penale-Italia`.

### 2. Installa le 6 skill
Copia le 6 cartelle da `skills/` nella cartella di Claude:

**Mac:** Finder Ã¢ÂÂ Vai Ã¢ÂÂ Vai alla cartella Ã¢ÂÂ incolla `~/.claude/skills` Ã¢ÂÂ copia le 6 cartelle.

**Windows:** Esplora File Ã¢ÂÂ barra indirizzi Ã¢ÂÂ `%USERPROFILE%\.claude\skills` Ã¢ÂÂ copia le 6 cartelle.

Cartelle da copiare: `penalista-atti`, `penalista-cautelare`, `penalista-esecuzione`, `penalista-giurisprudenza`, `penalista-scadenze`, `penalista-strategia`.

> **Mac:** la cartella `.claude` ÃÂ¨ nascosta Ã¢ÂÂ premi `Cmd+Shift+.` per vederla. Se la cartella `skills` non esiste, creala dentro `.claude`.

### 3. Collega il kit a Cowork
Apri Claude Desktop Ã¢ÂÂ Cowork Ã¢ÂÂ **"Seleziona cartella"** Ã¢ÂÂ seleziona la cartella `Penale-Italia` (tutta). Riavvia Claude Desktop.

---

## Configura i dati del tuo studio
Apri `CLAUDE.md` e compila la sezione "Dati dello studio" con nome, foro, tribunale, numero iscrizione. Salva. Claude userÃÂ  questi dati nelle intestazioni degli atti.

---

## Aggiornamento
1. Scarica il nuovo ZIP (Code Ã¢ÂÂ Download ZIP)
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
| `penalista-strategia` | Analisi difensiva del capo di imputazione: elementi costitutivi, criticità, eccezioni, giurisprudenza |
| `penalista-atti` | Redazione atti processuali: memoria 415-bis, appello, riesame, ricorso Cassazione |
| `penalista-scadenze` | Calcolo termini: prescrizione (ante/post Bonafede), custodia cautelare, impugnazioni, Cartabia |
| `penalista-cautelare` | Misure cautelari: analisi presupposti, riesame, revoca/sostituzione, scadenze di fase |
| `penalista-giurisprudenza` | Ricerca orientamenti Cassazione, contrasti tra sezioni, CEDU |
| `penalista-esecuzione` | Diritto penitenziario: misure alternative, liberazione anticipata/condizionale, 41-bis |

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