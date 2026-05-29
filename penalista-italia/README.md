# Penalista Italia — Documentazione del Plugin

## Le 4 skill del kit

### `penalista-strategia`
Dato un capo di imputazione o una descrizione del caso, produce un'analisi difensiva strutturata in 10 sezioni: inquadramento del fatto, elementi costitutivi e onere probatorio della pubblica accusa, criticità dell'impianto accusatorio, eccezioni processuali, strategie difensive graduate dal proscioglimento pieno alla minimizzazione della pena, giurisprudenza di riferimento per sezione di Cassazione, angoli CEDU, verifica prescrizione e improcedibilità Cartabia, profilo 231 se coinvolto un ente, piano d'azione concreto, punti di vulnerabilità della difesa.

**Attivazione:** "analizza questa accusa", "come mi difendo da...", "che strategia adottiamo", "c'è spazio per un'eccezione processuale"

---

### `penalista-atti`
Redige tutti i principali atti processuali penali italiani con la struttura e le formule corrette per ogni tipo di atto e grado di giudizio: memoria difensiva ex art. 415-bis c.p.p., memoria ex art. 121 c.p.p., atto di appello (con guida ai motivi e calcolo del termine), ricorso per Cassazione (con mappatura dei motivi ex art. 606), istanza di riesame ex art. 309, istanza di revoca/sostituzione misura cautelare, richiesta di patteggiamento, richiesta di giudizio abbreviato, richiesta di messa alla prova, lista testi e periti.

**Attivazione:** "scrivi la memoria", "prepara l'istanza di riesame", "imposta i motivi di appello", "bozza il ricorso per Cassazione"

---

### `penalista-scadenze`
Calcola qualsiasi termine processuale penale con ragionamento esplicito passo per passo: termini di impugnazione (appello, Cassazione), termini del riesame cautelare, termini di fase della custodia cautelare (con distinzione reati comuni / reati gravi art. 407 co. 2), prescrizione (regime ante/post Bonafede con interruzioni e sospensioni), improcedibilità Cartabia (art. 344-bis c.p.p.), termini dell'udienza di convalida. Applica automaticamente le regole dell'art. 172 c.p.p. (dies a quo, festività, sospensione feriale).

**Attivazione:** "quando scade il termine per", "calcola la prescrizione", "ho ancora tempo per il riesame", "quando scade la custodia cautelare"

---

### `penalista-cautelare`
Gestisce l'intero ciclo difensivo delle misure cautelari personali. Modulo 1: verifica immediata dei termini di fase (PRIORITÀ ASSOLUTA se in scadenza). Modulo 2: analisi sistematica dei presupposti (gravi indizi, esigenze cautelari, proporzionalità). Modulo 3: costruzione dei motivi di riesame ex art. 309. Modulo 4: revoca e sostituzione ex artt. 299-300. Modulo 5: istanza di scarcerazione d'urgenza per scadenza termini. Modulo 6: preparazione udienza di convalida.

**Attivazione:** "il cliente è in custodia cautelare", "dobbiamo chiedere il riesame", "quando scade la custodia", "possiamo chiedere i domiciliari", "il tribunale del riesame non ha deciso"

---

## Knowledge base inclusa

Il plugin include una base di conoscenza procedurale completa:

- **Processo penale italiano** — tutte le fasi dalle indagini alla Cassazione
- **Riti speciali** — giudizio abbreviato, patteggiamento, messa alla prova, direttissimo, immediato
- **Riforma Cartabia (D.Lgs. 150/2022)** — improcedibilità art. 344-bis come strumento difensivo
- **Nullità e inutilizzabilità** — sistematica artt. 177-191 c.p.p.
- **Intercettazioni** — presupposti, captatore informatico, divieti di utilizzo
- **Investigazioni difensive** — artt. 391-bis ss. c.p.p.
- **Giurisprudenza CEDU** — Torreggiani, Scoppola, Viola, Contrada e altri
- **D.Lgs. 231/2001** — responsabilità degli enti, MOG, OdV
- **Prescrizione** — regime Bonafede e pre-Bonafede con calcolo dettagliato
- **Esecuzione penale** — misure alternative, Tribunale di Sorveglianza
- **Tenuità del fatto** — art. 131-bis come riformato dalla Riforma Cartabia

---

## Sistema di memoria a wikilinks

Il kit usa file `.md` collegati da wikilinks `[[]]` per gestire il contesto per fascicolo. Vedere `SISTEMA_MEMORIA.md` nella cartella di lavoro per le regole operative.

---

## Versione e aggiornamenti

Versione attuale: **1.0.0**

Attivare la sincronizzazione automatica da GitHub per ricevere aggiornamenti automatici al rilascio di nuove versioni.

Vedere [CHANGELOG.md](../CHANGELOG.md) per il dettaglio delle modifiche.
