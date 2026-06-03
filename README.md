# Penalista Italia -- Kit Operativo per Avvocati Penalisti

[![Versione](https://img.shields.io/badge/versione-3.0.0-blue)](https://github.com/Synthos-Logic/penalista-italia/releases)
[![Licenza](https://img.shields.io/badge/licenza-MIT-green)](LICENSE)
[![Piattaforma](https://img.shields.io/badge/piattaforma-Claude%20Cowork-orange)](https://claude.ai)
[![Wiki](https://img.shields.io/badge/Wiki-metodologia-blueviolet)](https://github.com/Synthos-Logic/penalista-italia/wiki)
[![Sviluppato da](https://img.shields.io/badge/sviluppato%20da-Synthos%20Logic-purple)](https://github.com/Synthos-Logic)

**Kit operativo per avvocati penalisti italiani su Claude Cowork. Specializzato esclusivamente sul diritto penale italiano.**

> **Non e' uno strumento generico per avvocati.** E' progettato per il penalista che lavora quotidianamente su GIP, GUP, dibattimento, impugnazioni, misure cautelari e Cassazione penale. Non risponde su diritto civile, amministrativo o societario.

---

## Prima di iniziare: la metodologia e' fondamentale

Il kit non e' un motore di ricerca che risponde a domande generiche. E' un assistente che **lavora nella struttura che tu costruisci**.

Un fascicolo ben strutturato -- con i dati dell'indagato, il capo di imputazione, le scadenze e i link alla giurisprudenza rilevante -- permette al kit di rispondere con precisione professionale, ricordare la strategia stabilita nelle sessioni precedenti, e produrre atti coerenti con il lavoro gia' fatto. Senza questa struttura, ogni sessione riparte da zero.

**Leggere la guida metodologica prima di iniziare non e' opzionale -- e' il passaggio che determina l'efficacia reale del kit.**

Wiki [Guida metodologica completa](https://github.com/Synthos-Logic/penalista-italia/wiki)
Sito [Sito documentazione](https://synthos-logic.github.io/penalista-italia/)
Guida [Metodologia interattiva](https://synthos-logic.github.io/penalista-italia/METODOLOGIA.html)

---

## Installazione - 3 passi

### Passo 1 - Scarica il kit

Clicca **Code -> Download ZIP**, decomprimi e rinomina la cartella in `Penale-Italia`.

### Passo 2 - Installa le 6 skill

Copia le 6 cartelle da `skills/` nella cartella skill di Claude.

**Su Mac:** Finder -> menu Vai -> Vai alla cartella (o **Cmd+Shift+G**) -> incolla `~/.claude/skills`
**Su Windows:** Esplora File -> barra indirizzi -> `%USERPROFILE%\.claude\skills`

> La cartella `.claude` e' nascosta. Su Mac usa "Vai alla cartella" (funziona anche senza vedere i file nascosti). Se non esiste, crea prima `.claude` e poi `skills` dentro.

**Le 6 cartelle:** `penalista-strategia`, `penalista-atti`, `penalista-scadenze`, `penalista-cautelare`, `penalista-giurisprudenza`, `penalista-esecuzione`

### Passo 3 - Collega il kit a Cowork

Claude Desktop -> Cowork -> **Seleziona cartella** -> seleziona la cartella `Penale-Italia` intera. Riavvia Claude Desktop.

---

## Configurazione

Apri il file `CLAUDE.md` con TextEdit (Mac) o Blocco Note (Windows) e compila la sezione "Dati dello studio":

```
AVVOCATO:          Avv. Mario Rossi
FORO:              Foro di Milano
N. ISCRIZIONE:     12345
TRIBUNALE:         Tribunale di Milano
CASSAZIONISTA:     NO
```

Da quel momento Claude usa questi dati in tutte le intestazioni degli atti.

---

## 6 Skill specializzate

| Skill | Descrizione |
|---|---|
| `penalista-strategia` | Analisi difensiva del capo di imputazione: elementi costitutivi, criticita' dell'accusa, eccezioni processuali, strategie graduate, giurisprudenza Cassazione e CEDU |
| `penalista-atti` | Redazione di tutti i principali atti processuali penali: memoria 415-bis, appello, ricorso Cassazione, riesame, revoca cautelare, patteggiamento, abbreviato |
| `penalista-scadenze` | Calcolo preciso di ogni termine processuale: impugnazioni, prescrizione, custodia cautelare, improcedibilita' Cartabia, udienza di convalida |
| `penalista-cautelare` | Workflow completo misure cautelari: analisi presupposti, riesame, revoca/sostituzione, scadenze di fase, scarcerazione urgente |
| `penalista-giurisprudenza` | Mappatura orientamenti Cassazione, analisi sentenze, contrasti tra sezioni, giurisprudenza CEDU, integrazione wikilinks |
| `penalista-esecuzione` | Diritto penitenziario: misure alternative, liberazione anticipata/condizionale, permessi, reclami, regime 41-bis, calcolo pena residua |

---

## Come funziona il sistema documentale

Il kit lavora con **tutti i formati** di uno studio penalistico:

| Formato | Uso consigliato | Come funziona |
|---|---|---|
| `.md` | Fascicoli, note strategia, giurisprudenza | Il kit legge e collega automaticamente via wikilinks |
| `.pdf` | Ordinanze, sentenze, testi normativi, CNR | Allegare alla conversazione -- il kit analizza il contenuto |
| `.docx` | Atti prodotti, template, bozze | Allegare o usare la skill docx per lavorarci |
| `.html` | Guide, riferimenti, documentazione | Allegare o aprire come riferimento nella conversazione |

> Il formato `.md` e' preferenziale per i file di lavoro perche' supporta i wikilinks e il caricamento selettivo del contesto.

---

## Perche' Penalista Italia

**Non uno strumento generico. Specializzato esclusivamente sul penale italiano.**

- **Tutti i formati** -- Lavora con MD, PDF, DOCX e HTML. I documenti dello studio sono supportati cos' come arrivano.
- **Memoria persistente** -- Il sistema wikilinks collega fascicoli, giurisprudenza e documenti. Il kit ricorda il contesto tra sessioni senza ricaricare tutto.
- **Fonti deterministiche** -- Normativa, HUDOC, Massimario Cassazione. Quando usi i testi ufficiali come contesto, le risposte sono precise e citabili.
- **Mini-progetti** -- Template per le pratiche ricorrenti: gestione cautelare, risposta 415-bis, appello, Cassazione, esecuzione penale, D.Lgs. 231.
- **Riforma Cartabia integrata** -- L'improcedibilita' ex art. 344-bis c.p.p. e' uno strumento difensivo, non solo un termine da monitorare.
- **Solo diritto penale italiano** -- GIP, GUP, indagini, dibattimento, Cassazione penale, Sorveglianza, 231. Non risponde su diritto civile o amministrativo.

---

## Aggiornamento

1. Scarica il nuovo ZIP (Code -> Download ZIP)
2. Sostituisci la cartella `Penale-Italia`
3. Se ci sono nuove skill: copia le nuove cartelle in `~/.claude/skills/`
4. Riavvia Claude Desktop

---

## Privacy

I file fisici restano sul tuo computer. Il testo che chiedi di analizzare transita sui server di Anthropic per l'elaborazione.
La **Legge 132/2025 art. 13** impone di informare i clienti dell'uso dell'AI. Il CNF ha pubblicato uno schema di informativa.

[Pagina Privacy completa](https://github.com/Synthos-Logic/penalista-italia/wiki/Privacy) | [Guida installazione dettagliata](documentazione/INSTALLAZIONE.md)