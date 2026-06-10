# Guida all'Installazione — Kit Penalista Italiano v3.1.1

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
- In **Impostazioni → Capacità**: "Esecuzione di codice e creazione di file" attivo (le skill lo richiedono)

---

## Passo 1 — Scarica il kit

Vai su [github.com/Synthos-Logic/penalista-italia](https://github.com/Synthos-Logic/penalista-italia) e clicca **Code → Download ZIP**. Decomprimi e rinomina la cartella in `Penale-Italia`.

---

## Passo 2 — Collega il kit a Cowork

Apri Claude Desktop → Cowork → **"Seleziona cartella"** → seleziona `Penale-Italia` (tutta).

> Seleziona la cartella intera, non solo `FASCICOLI/`. Claude ha bisogno anche della Knowledge Base e del CLAUDE.md.

---

## Passo 3 — Installa le 8 skill

### Metodo consigliato — installazione assistita (nessun file da toccare)

Con la cartella `Penale-Italia` selezionata in Cowork, incolla questo messaggio a Claude:

```
Installa le skill del kit Penalista Italia seguendo il file INSTALLAZIONE_ASSISTITA.md; se il file non è nella cartella selezionata, scaricalo da https://raw.githubusercontent.com/Synthos-Logic/penalista-italia/main/INSTALLAZIONE_ASSISTITA.md e segui le sue istruzioni.
```

Claude ti presenterà **8 schede con il pulsante "Salva skill"**: clicca il pulsante su ciascuna. Fine. Poi verifica in **Personalizza → Skills** che le 8 skill risultino attive (interruttore acceso).

### Metodo manuale (alternativa)

1. Nella cartella `Penale-Italia/skills/` trovi 8 cartelle: `penalista-inizia`, `penalista-strategia`, `penalista-atti`, `penalista-scadenze`, `penalista-cautelare`, `penalista-giurisprudenza`, `penalista-esecuzione`, `penalista-verifica`
2. Comprimi ogni cartella in uno ZIP (Mac: tasto destro → **Comprimi**; Windows: tasto destro → **Invia a → Cartella compressa**)
3. In Claude: **Personalizza → Skills → "+" → Carica una skill** → seleziona lo ZIP
4. Ripeti per tutte e 8 le skill, poi verifica che siano attive

### ⚠️ Cosa NON fare

- **Non copiare le cartelle in `~/.claude/skills`** se usi l'app desktop/Cowork: quel percorso vale **solo per Claude Code (lo strumento da terminale per sviluppatori)**. L'app desktop non lo legge — le skill risulterebbero "installate" ma invisibili.
- **Non chiedere a Claude di "installare le skill" senza il file INSTALLAZIONE_ASSISTITA.md**: senza istruzioni, Claude può solo copiare le cartelle nel posto sbagliato.

> **Usi Claude Code (CLI)?** Allora sì: gli script sono nella cartella `claude-code/`. Su Mac apri il Terminale nella cartella del kit e lancia `bash claude-code/install.sh` (NON eseguirlo con doppio clic o trascinamento: lo ZIP di GitHub non conserva i permessi di esecuzione e otterresti "permission denied"). Su Windows: doppio clic su `claude-code\install.bat`. Gli script copiano le 8 skill in `~/.claude/skills`, che Claude Code legge regolarmente.

---

## Passo 4 — Configura i dati del tuo studio

Due strade equivalenti:

- **La più semplice:** scrivi a Claude **"Iniziamo"** — la skill di onboarding ti chiede i dati (nome, foro, tribunale) e compila tutto lei.
- **Manuale:** apri `CLAUDE.md` nella cartella `Penale-Italia` con TextEdit (Mac) o Blocco Note (Windows) e compila la sezione "Dati dello studio". Salva.

Claude usa questi dati nelle intestazioni degli atti.

---

## Passo 5 — Verifica

Scrivi in Cowork:

> "Ho un fascicolo per truffa aggravata. Calcola il termine per la memoria 415-bis notificata il 1 giugno 2026."

Claude deve rispondere con una data precisa (21 giugno 2026) e il calcolo dettagliato. Se risponde in modo generico, verifica in **Personalizza → Skills** che `penalista-scadenze` sia attiva.

---

## Aggiornamento

> ⚠️ **Non sostituire mai la cartella `Penale-Italia` a mano:** dentro ci sono i tuoi fascicoli (`FASCICOLI/`) e i dati del tuo studio (`CLAUDE.md`). Sostituendola li perderesti.

1. Scarica il nuovo ZIP (**Code → Download ZIP**)
2. Trascina il file ZIP (senza decomprimerlo) **dentro la cartella `Penale-Italia`**
3. Incolla a Claude: *"Ho scaricato l'aggiornamento del kit Penalista Italia: eseguilo seguendo AGGIORNAMENTO_ASSISTITO.md; se il file non è nella cartella selezionata, scaricalo da https://raw.githubusercontent.com/Synthos-Logic/penalista-italia/main/AGGIORNAMENTO_ASSISTITO.md e segui le sue istruzioni."*

Claude confronta le versioni, ti riassume le novità, aggiorna i file del kit **senza toccare fascicoli e dati studio**, e ti presenta le skill nuove o aggiornate da reinstallare con un clic ("Salva skill"). Se una skill risulta già esistente: **Personalizza → Skills** → elimina la versione vecchia → clicca di nuovo "Salva skill".

---

## 🔒 Privacy

I file restano sul tuo computer. Il testo analizzato transita sui server Anthropic.
**Legge 132/2025 art. 13**: informare i clienti prima di usare strumenti AI.

[Pagina Privacy completa](https://github.com/Synthos-Logic/penalista-italia/wiki/Privacy)

---

## Problemi comuni

| Problema | Soluzione |
|---|---|
| Le skill non compaiono | Apri **Personalizza → Skills**: se non ci sono, ripeti il Passo 3. Se sono spente, attiva l'interruttore |
| La sezione Skills non è visibile | **Impostazioni → Capacità** → attiva "Esecuzione di codice e creazione di file" |
|  Ho usato gli script claude-code/ ma le skill non ci sono in Claude | Normale: quel metodo vale solo per Claude Code. Usa il Passo 3 (installazione assistita) |
| Claude ha "installato" da solo ma non funziona nulla | Ha copiato le cartelle nel posto sbagliato. Elimina le copie e usa il Passo 3 |
| Errore al caricamento dello ZIP | Lo ZIP deve contenere la cartella della skill come radice (non i file sciolti) e il nome cartella deve coincidere con la skill |
| Claude non vede i documenti | Seleziona tutta la cartella `Penale-Italia`, non una sottocartella |
| Claude non usa il tuo nome | Scrivi "Iniziamo" oppure compila `CLAUDE.md` a mano |
