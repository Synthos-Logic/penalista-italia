# Penalista Italia — Kit Operativo per Avvocati Penalisti

[![Version](https://img.shields.io/badge/versione-1.2.0-blue)](https://github.com/Synthos-Logic/penalista-italia/releases)
[![License: MIT](https://img.shields.io/badge/licenza-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/piattaforma-Claude%20Cowork-orange)](https://claude.ai)
[![Wiki](https://img.shields.io/badge/📚_Wiki-metodologia-blueviolet)](https://github.com/Synthos-Logic/penalista-italia/wiki)
[![Sviluppato da](https://img.shields.io/badge/sviluppato%20da-Synthos%20Logic-purple)](https://github.com/Synthos-Logic)

**Marketplace per l'installazione del plugin Penalista Italia su Claude Cowork Desktop.**

Il plugin offre un kit operativo completo e specializzato **esclusivamente** per avvocati penalisti italiani: strategia difensiva, redazione atti processuali, calcolo termini, gestione misure cautelari e compliance D.Lgs. 231/2001.

> **Non è uno strumento generico per avvocati.** È progettato per il penalista che lavora quotidianamente su GIP, GUP, dibattimento, impugnazioni, misure cautelari e Cassazione penale.

---

## ⚠️ Prima di iniziare: la metodologia è fondamentale

Il kit non è un motore di ricerca che risponde a domande generiche. È un assistente che **lavora nella struttura che tu costruisci**. Questo significa che la qualità del suo lavoro dipende direttamente da come organizzi i tuoi documenti e fascicoli.

Un fascicolo ben strutturato — con i dati dell'indagato, il capo di imputazione, le scadenze e i link alla giurisprudenza rilevante — permette al kit di rispondere con precisione professionale, ricordare la strategia stabilita nelle sessioni precedenti, e produrre atti coerenti con il lavoro già fatto. Senza questa struttura, ogni sessione riparte da zero.

**Leggere la guida metodologica prima di iniziare non è opzionale — è il passaggio che determina l'efficacia reale del kit.**

📚 **[Guida metodologica completa → Wiki](https://github.com/Synthos-Logic/penalista-italia/wiki)**
🌐 **[Sito documentazione → GitHub Pages](https://synthos-logic.github.io/penalista-italia/)**
📐 **[Guida metodologica interattiva](https://synthos-logic.github.io/penalista-italia/METODOLOGIA.html)**

---

## Installazione rapida

1. In Claude Cowork, clicca **Personalizza** → **Sfoglia plugin** → **Personali** → **+** → **Aggiungi marketplace da GitHub**
2. Inserisci `Synthos-Logic/penalista-italia` e clicca **Sincronizza**
3. Clicca **Installa** sulla scheda *Penalista Italia*
4. Configura i dati dello studio (nome, foro, tribunale di riferimento)

📖 **[Guida all'installazione passo per passo con screenshot](docs/INSTALLAZIONE.md)**

---

## Cosa include il kit

### 6 skill specializzate

| Skill | Descrizione |
|---|---|
| `penalista-strategia` | Analisi difensiva del capo di imputazione: elementi costitutivi, criticità dell'accusa, eccezioni processuali, strategie graduate, giurisprudenza Cassazione e CEDU |
| `penalista-atti` | Redazione di tutti i principali atti processuali penali: memoria difensiva, appello, ricorso Cassazione, riesame, revoca cautelare, patteggiamento, abbreviato, messa alla prova |
| `penalista-scadenze` | Calcolo preciso di ogni termine processuale con ragionamento esplicito: impugnazioni, prescrizione, improcedibilità Cartabia, termini di fase della custodia cautelare |
| `penalista-cautelare` | Workflow completo misure cautelari: analisi presupposti, riesame, revoca/sostituzione, scadenze di fase, istanza di scarcerazione d'urgenza |
| `penalista-giurisprudenza` | Ricerca e organizzazione della giurisprudenza penale per la difesa: mappa sezioni Cassazione, orientamenti per area tematica, contrasti SS.UU., CEDU |
| `penalista-esecuzione` | Diritto penitenziario: misure alternative, liberazione anticipata/condizionale, reclami condizioni detentive, regime 41-bis, calcolo pena residua |

### 10 comandi slash

`/strategia` `/atti` `/scadenze` `/cautelare` `/prescrizione` `/giurisprudenza` `/esecuzione` `/fascicolo` `/versione` `/aiuto`

### Knowledge base procedurale integrata
- Mappa completa del processo penale italiano (indagini → Cassazione)
- Riforma Cartabia (art. 344-bis c.p.p.) come strumento difensivo
- Giurisprudenza CEDU (Torreggiani, Scoppola, Viola, Contrada, De Tommaso)
- D.Lgs. 231/2001 — responsabilità degli enti
- Investigazioni difensive, intercettazioni, nullità processuali, esecuzione penale

### Sistema di memoria a wikilinks
Gestione del contesto per fascicolo con file `.md` collegati tramite `[[wikilinks]]`. Supporto per tutti i formati documentali (PDF, DOCX, HTML). Caricamento selettivo del contesto per ridurre il consumo di token.

---

## Come funziona il sistema documentale

Il kit è progettato per lavorare con **tutti i formati di file** che uno studio penalistico usa quotidianamente:

| Formato | Uso consigliato | Come funziona |
|---|---|---|
| `.md` | Fascicoli, note strategia, giurisprudenza | Il kit legge e collega automaticamente via `[[wikilinks]]` |
| `.pdf` | Ordinanze, sentenze, testi normativi, CNR | Allegare alla conversazione quando serve — il kit analizza il contenuto |
| `.docx` | Atti prodotti, template, bozze | Allegare o usare la skill `docx` per lavorarci direttamente |
| `.html` | Guide, riferimenti, documentazione interna | Allegare o aprire come riferimento nella conversazione |

> Il formato `.md` è preferenziale per i file di lavoro (fascicoli, note, giurisprudenza) perché supporta i wikilinks e il caricamento selettivo del contesto. I documenti ricevuti da terzi (ordinanze, sentenze) vanno salvati nel loro formato originale e allegati quando necessario.

---

## Configurazione

Al momento dell'installazione il plugin chiede:
- **Nome e cognome** dell'avvocato (per le intestazioni degli atti)
- **Foro di iscrizione** (es. Milano)
- **Numero di iscrizione** all'Ordine
- **Tribunale di riferimento** principale
- **Iscrizione all'Albo Cassazionisti** (per i ricorsi per Cassazione)

---

## Comandi principali

```
"Analizza questo capo di imputazione e dimmi come mi difendo"
→ /penalista-italia:strategia

"Scrivi l'istanza di riesame per Rossi"
→ /penalista-italia:atti

"Calcola quando scade il termine per l'appello"
→ /penalista-italia:scadenze

"Il cliente è in custodia dal 10 marzo, quando scade la fase?"
→ /penalista-italia:cautelare

"Cosa dice la Cassazione sulla lieve entità degli stupefacenti?"
→ /penalista-italia:giurisprudenza

"Quando può chiedere l'affidamento in prova?"
→ /penalista-italia:esecuzione
```

---

## Differenza rispetto ad altri strumenti legali

| | Penalista Italia | Strumenti generici |
|---|---|---|
| Specializzazione | Solo diritto penale italiano | Diritto generico |
| Strategia difensiva | Analisi strutturata per capo di imputazione | Non prevista |
| Termini cautelari | Calcolo automatico con alert urgenza | Non previsto |
| Riforma Cartabia | Integrata come strumento difensivo | Assente |
| CEDU | Giurisprudenza specifica per penalisti | Generica |
| Atti processuali | Template per ogni atto con formule corrette | Generici |
| Memoria persistente | Sistema wikilinks tra fascicoli | Assente |
| Formati supportati | MD, PDF, DOCX, HTML | Variabile |

---

## 📚 Documentazione completa

| Documento | Contenuto |
|---|---|
| [Wiki — Home](https://github.com/Synthos-Logic/penalista-italia/wiki) | Indice di tutta la documentazione |
| [Metodologia di Lavoro](https://github.com/Synthos-Logic/penalista-italia/wiki/Metodologia-di-Lavoro) | Come organizzare lo studio digitale |
| [Fonti Giuridiche](https://github.com/Synthos-Logic/penalista-italia/wiki/Fonti-Giuridiche-Ufficiali) | Normattiva, HUDOC, Massimario Cassazione |
| [Mini-Progetti](https://github.com/Synthos-Logic/penalista-italia/wiki/Mini-Progetti) | Template per pratiche ricorrenti |
| [Comandi Slash](https://github.com/Synthos-Logic/penalista-italia/wiki/Comandi-Slash) | Tutti i comandi con esempi |
| [FAQ](https://github.com/Synthos-Logic/penalista-italia/wiki/FAQ) | Domande frequenti |
| [Guida installazione](docs/INSTALLAZIONE.md) | Passo per passo con screenshot |
| [Sito documentazione](https://synthos-logic.github.io/penalista-italia/) | Homepage GitHub Pages |
| [Metodologia HTML](https://synthos-logic.github.io/penalista-italia/METODOLOGIA.html) | Guida interattiva con sidebar navigabile |

---

## Licenza

[MIT](LICENSE) — libero utilizzo, distribuzione e modifica con attribuzione.

---

## Sviluppato da

**Synthos Logic** — [github.com/Synthos-Logic](https://github.com/Synthos-Logic)

*Contributi benvenuti — vedi [CONTRIBUTING.md](CONTRIBUTING.md)*
