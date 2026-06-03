# Guida all'Installazione — Kit Penalista Italiano v3.0

---

## Prima di iniziare — Chat, Cowork o un progetto per cliente?

| Situazione | Cosa usare |
|---|---|
| Domanda rapida su una norma | Chat normale |
| Lavorare con documenti di causa | Cowork con la cartella del kit |
| Gestire più fascicoli nel tempo | **Un unico progetto Cowork per tutto lo studio** |

---

## Prerequisiti

- Claude Desktop con Cowork installato e aggiornato
- Account Claude Pro o superiore

---

## Passo 1 — Scarica il kit

Vai su [github.com/Synthos-Logic/penalista-italia](https://github.com/Synthos-Logic/penalista-italia) e clicca **Code → Download ZIP**. Decomprimi e rinomina la cartella in `Penale-Italia`.

---

## Passo 2 — Installa le 6 skill

Copia le 6 cartelle da `skills/` nella cartella skill di Claude:

**Mac:**
1. Finder → menu Vai → Vai alla cartella → incolla `~/.claude/skills`
2. Se non esiste, crea la cartella `skills` dentro `.claude`
3. Copia le 6 cartelle: `penalista-strategia`, `penalista-atti`, `penalista-scadenze`, `penalista-cautelare`, `penalista-giurisprudenza`, `penalista-esecuzione`

> La cartella `.claude` è nascosta. Premi `Cmd+Shift+.` nel Finder per vederla.

**Windows:**
1. Esplora File → barra indirizzi → `%USERPROFILE%\.claude\skills`
2. Copia le 6 cartelle

---

## Passo 3 — Collega il kit a Cowork

Apri Claude Desktop → Cowork → **"Seleziona cartella"** → seleziona `Penale-Italia` (tutta). Riavvia Claude Desktop.

> Seleziona la cartella intera, non solo `FASCICOLI/`. Claude ha bisogno anche della Knowledge Base e del CLAUDE.md.

---

## Passo 4 — Configura i dati del tuo studio

Apri `CLAUDE.md` nella cartella `Penale-Italia` con TextEdit (Mac) o Blocco Note (Windows). Compila:

```
AVVOCATO:          Avv. Mario Rossi
FORO:              Foro di Milano
N. ISCRIZIONE:     12345
TRIBUNALE:         Tribunale di Milano
CASSAZIONISTA:     NO
```

Salva. Claude usa questi dati nelle intestazioni degli atti.

---

## Passo 5 — Verifica

Scrivi in Cowork:

> "Ho un fascicolo per truffa aggravata. Calcola il termine per la memoria 415-bis notificata il 1 giugno 2026."

Claude deve rispondere con una data precisa (21 giugno 2026) e il calcolo dettagliato. Se risponde in modo generico, verifica i passi 2 e 3 e riavvia Claude Desktop.

---

## Aggiornamento

1. Scarica il nuovo ZIP (Code → Download ZIP)
2. Sostituisci la cartella `Penale-Italia`
3. Se il changelog indica nuove skill: copia le nuove cartelle in `~/.claude/skills/`
4. Riavvia Claude Desktop

---

## 🔒 Privacy

I file restano sul tuo computer. Il testo analizzato transita sui server Anthropic.
**Legge 132/2025 art. 13**: informare i clienti prima di usare strumenti AI.

[Pagina Privacy completa](https://github.com/Synthos-Logic/penalista-italia/wiki/Privacy)

---

## Problemi comuni

| Problema | Soluzione |
|---|---|
| Skill non attive | Verifica che le cartelle siano in `~/.claude/skills/` con `SKILL.md` dentro. Riavvia. |
| Claude non vede i documenti | Seleziona tutta la cartella `Penale-Italia`, non una sottocartella |
| Claude non usa il tuo nome | Apri `CLAUDE.md` e compila "Dati dello studio" |
| Cartella `.claude` non esiste (Mac) | Apri Terminale: `mkdir -p ~/.claude/skills` |