# Penalista Italia — Kit Operativo per Avvocati Penalisti

[![Version](https://img.shields.io/badge/versione-1.0.0-blue)](https://github.com/Synthos-Logic/penalista-italia/releases)
[![License: MIT](https://img.shields.io/badge/licenza-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/piattaforma-Claude%20Cowork-orange)](https://claude.ai)
[![Sviluppato da](https://img.shields.io/badge/sviluppato%20da-Synthos%20Logic-purple)](https://github.com/Synthos-Logic)

**Marketplace per l'installazione del plugin Penalista Italia su Claude Cowork Desktop.**

Il plugin offre un kit operativo completo e specializzato **esclusivamente** per avvocati penalisti italiani: strategia difensiva, redazione atti processuali, calcolo termini, gestione misure cautelari e compliance D.Lgs. 231/2001.

> **Non è uno strumento generico per avvocati.** È progettato per il penalista che lavora quotidianamente su GIP, GUP, dibattimento, impugnazioni, misure cautelari e Cassazione penale.

---

## Installazione rapida

1. In Claude Cowork, clicca **Personalizza** → **Sfoglia plugin** → **Personali** → **+** → **Aggiungi marketplace da GitHub**
2. Inserisci `Synthos-Logic/penalista-italia` e clicca **Sincronizza**
3. Clicca **Installa** sulla scheda *Penalista Italia*
4. Configura i dati dello studio (nome, foro, tribunale di riferimento)

📖 **[Guida all'installazione passo per passo con screenshot](docs/INSTALLAZIONE.md)**

---

## Cosa include il kit

### 4 skill specializzate

| Skill | Descrizione |
|---|---|
| `penalista-strategia` | Analisi difensiva del capo di imputazione: elementi costitutivi, criticità dell'accusa, eccezioni processuali, strategie graduate, giurisprudenza Cassazione e CEDU |
| `penalista-atti` | Redazione di tutti i principali atti processuali penali: memoria difensiva, appello, ricorso Cassazione, riesame, revoca cautelare, patteggiamento, abbreviato, messa alla prova |
| `penalista-scadenze` | Calcolo preciso di ogni termine processuale con ragionamento esplicito: impugnazioni, prescrizione, improcedibilità Cartabia, termini di fase della custodia cautelare |
| `penalista-cautelare` | Workflow completo misure cautelari: analisi presupposti, riesame, revoca/sostituzione, scadenze di fase, istanza di scarcerazione d'urgenza |

### Knowledge base procedurale integrata
- Mappa completa del processo penale italiano (indagini → Cassazione)
- Riforma Cartabia (art. 344-bis c.p.p.) come strumento difensivo
- Giurisprudenza CEDU rilevante (Torreggiani, Scoppola, Viola, Contrada)
- D.Lgs. 231/2001 — responsabilità degli enti
- Investigazioni difensive, intercettazioni, nullità processuali

### Sistema di memoria a wikilinks
Gestione del contesto per fascicolo con file `.md` collegati tramite `[[wikilinks]]`. Caricamento selettivo del contesto per ridurre il consumo di token.

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

Dopo l'installazione, usare le skill in modo naturale:

```
"Analizza questo capo di imputazione e dimmi come mi difendo"
→ attiva penalista-strategia

"Scrivi l'istanza di riesame per Rossi"
→ attiva penalista-atti

"Calcola quando scade il termine per l'appello"
→ attiva penalista-scadenze

"Il cliente è in custodia dal 10 marzo, quando scade la fase?"
→ attiva penalista-cautelare
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

---

## Licenza

[MIT](LICENSE) — libero utilizzo, distribuzione e modifica con attribuzione.

---

## Sviluppato da

**Synthos Logic** — [github.com/Synthos-Logic](https://github.com/Synthos-Logic)

*Contributi benvenuti — vedi [CONTRIBUTING.md](CONTRIBUTING.md)*
