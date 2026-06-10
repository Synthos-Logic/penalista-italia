# Changelog — Penalista Italia

## [3.1.0] — 2026-06-10

### 🔧 FIX CRITICO — Installazione skill su Cowork (segnalazione tester)

La procedura di installazione della v3.0 era **errata per gli utenti Cowork**: `install.sh`/`install.bat` copiano le skill in `~/.claude/skills`, percorso letto **solo da Claude Code (CLI)** — l'app desktop non lo legge (fonte: documentazione ufficiale Anthropic). Risultato: skill "installate" ma invisibili.

**Nuova procedura ufficiale — installazione assistita:**
1. Seleziona la cartella `Penale-Italia` in Cowork
2. Incolla: *"Leggi il file INSTALLAZIONE_ASSISTITA.md ed esegui l'installazione assistita delle skill"*
3. Claude presenta 8 schede con pulsante **"Salva skill"** — un clic ciascuna

Nuovo file `INSTALLAZIONE_ASSISTITA.md` (istruzioni operative per Claude, incluso l'elenco degli errori da non commettere). Guide installazione riscritte (README, documentazione/INSTALLAZIONE.md, docs/INSTALLAZIONE.md — quest'ultima conteneva ancora la guida del plugin abbandonato). `install.sh`/`install.bat` spostati in `claude-code/` (**solo per utenti Claude Code**, con avviso in testa; su Mac lanciare con `bash claude-code/install.sh` — lo ZIP di GitHub non conserva i permessi di esecuzione).

### 🔄 Aggiornamento assistito con protezione dati

Nuovo file `AGGIORNAMENTO_ASSISTITO.md`: l'aggiornamento del kit non si fa più sostituendo la cartella (avrebbe cancellato `FASCICOLI/` e i dati studio in `CLAUDE.md`!). Nuovo flusso: ZIP trascinato nella cartella → prompt a Claude → aggiornamento selettivo che **non tocca mai fascicoli, dati studio e file personali**, con ripresentazione delle skill aggiornate via pulsante "Salva skill".

### Due nuove skill (il kit passa da 6 a 8)

- **`penalista-inizia`** — onboarding guidato: dal primo "Iniziamo" al primo fascicolo operativo, su un caso vero, senza leggere documentazione. Configura i dati studio, crea la struttura di lavoro, orienta sulla fase processuale, propone il controllo scadenze automatico quotidiano.
- **`penalista-verifica`** — controllo qualita' pre-deposito: verifica indipendente (con subagente, dove disponibile) di ogni citazione giurisprudenziale contro la Knowledge Base, ricalcolo dei termini da zero, coerenza atto-fascicolo, requisiti formali. Report 🟢/🟡/🔴.

**Per chi aggiorna dalla v3.0:** seguire la procedura di aggiornamento assistito (vedi sopra); le 2 skill nuove e le 2 aggiornate verranno presentate con il pulsante "Salva skill".

### Aggiornamento normativo 2025-2026

Nuovo documento `KNOWLEDGE_BASE/00_META/AGGIORNAMENTO_NORMATIVO_2025-2026.md` con il quadro verificato delle novita':
- **GIP collegiale rinviato a fine febbraio 2027** (decreto-legge CdM 4 giugno 2026) — aggiornata `penalista-cautelare`
- **Interrogatorio preventivo** ex art. 291 co. 1-bis c.p.p. (L. 114/2024, in vigore) — integrato in `penalista-cautelare`
- **L. 80/2025 Decreto Sicurezza** (14 nuovi reati, rivolta penitenziaria) — integrata in `penalista-esecuzione`
- **D.lgs. 215-216/2025 e-evidence** (EPOC/EPOC-PR, piena applicazione 18/8/2026) — integrati nella scheda Reati Informatici
- Segnalate le rassegne mensili Massimario 2025 da aggiungere alla KB

### Documentazione per percorsi

`docs/METODOLOGIA.html` ristrutturata intorno al **percorso dell'avvocato** (Giorno 1 → Prima pratica → Routine): la nuova sezione di apertura rende la guida un percorso, non un manuale. La sezione wikilinks chiarisce il principio: **i collegamenti li crea e li mantiene il kit, non l'utente**. Sidebar riorganizzata: "Inizia qui" / "Le pratiche" / "Fonti giuridiche" / "Come funziona il motore".

`CLAUDE.md` aggiornato con la regola vincolante sui wikilinks automatici e il riferimento all'aggiornamento normativo.

---

## [3.0.0] — 2026-06-03

### Cambio architettura — Skill Kit

Il kit non si distribuisce più come plugin Cowork marketplace ma come **Skill Kit manuale**.

**Nuovo flusso installazione:**
1. Scarica ZIP da GitHub (Code → Download ZIP)
2. Copia `skills/` in `~/.claude/skills/`
3. Monta la cartella `Penale-Italia` in Cowork

**Motivo:** il meccanismo di aggiornamento del plugin Cowork non funziona per utenti esistenti. Con il Skill Kit, gli aggiornamenti si ottengono scaricando il nuovo ZIP.

### Struttura repo
- `skills/` — 6 skill a root level (prima in `penalista-italia/skills/`)
- `KNOWLEDGE_BASE/` — schede reato e meta a root level
- `FASCICOLI/` — cartella vuota per i fascicoli reali
- `CLAUDE.md` — configurazione dati studio

### Rimosso
- Plugin Cowork marketplace (`.claude-plugin/`, `penalista-italia/` subfolder)

---

# Changelog â Penalista Italia

## [2.2.1] â 2026-05-31

### Fix critico
- `penalista-italia/.claude-plugin/plugin.json`: versione aggiornata da 1.2.0 a 2.2.0 â questo era il file che Cowork legge per determinare la versione installata; senza questo fix il plugin appariva sempre alla versione precedente anche dopo reinstallazione
- `docs/INSTALLAZIONE.md` Passo 6: ripristinata la configurazione via pulsante âï¸ Personalizza (la UI nativa esiste e funziona â il `userConfig` con i 5 campi era giÃ  presente nel plugin.json)

---


## [2.2.0] â 2026-05-31

### Aggiunto
- Comando `/penalista-italia:configura` â setup guidato conversazionale dei dati studio (nome, foro, iscrizione, tribunale, cassazionista); Claude raccoglie i dati via chat e salva tutto automaticamente, senza che luutente debba trovare o modificare file nascosti

### Migliorato
- `docs/INSTALLAZIONE.md` Passo 6: sostituito il percorso a file nascosto con un singolo comando `/configura`
- Aggiunto `/configura` come primo comando nella tabella di utilizzo rapido
- Aggiornato Problemi comuni: rimosso riferimento a icona âï¸ inesistente

---



## [2.1.0] â 2026-05-31

### Aggiunto
- `knowledge-base/06_SCHEDE_REATO/` â 13 schede operative per i reati piÃ¹ diffusi: Truffa, Furto/Rapina/Estorsione, Appropriazione indebita, Riciclaggio/Autoriciclaggio, Maltrattamenti/Stalking, Omicidio/Lesioni stradali, Reati tributari D.Lgs. 74/2000, Corruzione/Peculato/Concussione, Bancarotta fraudolenta, False comunicazioni sociali, Reati informatici, Stupefacenti, CriminalitÃ  organizzata
- `knowledge-base/00_META/GERARCHIA_FONTI.md` â regole per pesare le fonti giuridiche
- `knowledge-base/00_META/REGISTRO_DOCUMENTI.md` â indice completo del corpus

### Nessuna modifica alle skill esistenti
---



## [1.2.0] â 2026-05-29

### Aggiunto
- Skill `penalista-giurisprudenza`: ricerca e organizzazione della giurisprudenza penale per la difesa â mappa delle sezioni Cassazione, principali orientamenti per area, contrasti giurisprudenziali utili per la rimessione alle SS.UU., giurisprudenza CEDU, integrazione wikilinks
- Skill `penalista-esecuzione`: diritto penitenziario e esecuzione penale â misure alternative (affidamento, domiciliari, semilibertÃ ), liberazione anticipata e condizionale, permessi, reclami sulle condizioni di detenzione, regime 41-bis, calcolo pena residua e requisiti
- Comandi `/penalista-italia:giurisprudenza` e `/penalista-italia:esecuzione`
- Cartella `docs/images/installazione/` predisposta per gli screenshot della guida

---

## [1.1.0] â 2026-05-29
- 8 slash commands: `/strategia`, `/atti`, `/scadenze`, `/cautelare`, `/prescrizione`, `/fascicolo`, `/versione`, `/aiuto`

## [1.0.0] â 2026-05-29
- Prima release pubblica con 4 skill core
