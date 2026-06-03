# Penalista Italia -- Kit Operativo per Avvocati Penalisti

[![Versione](https://img.shields.io/badge/versione-3.0.0-blue)](https://github.com/Synthos-Logic/penalista-italia/releases)
[![Licenza](https://img.shields.io/badge/licenza-MIT-green)](LICENSE)
[![Piattaforma](https://img.shields.io/badge/piattaforma-Claude%20Cowork-orange)](https://claude.ai)
[![Wiki](https://img.shields.io/badge/Wiki-metodologia-blueviolet)](https://github.com/Synthos-Logic/penalista-italia/wiki)
[![Sviluppato da](https://img.shields.io/badge/sviluppato%20da-Synthos%20Logic-purple)](https://github.com/Synthos-Logic)

**Kit operativo specializzato esclusivamente per avvocati penalisti italiani.** Strategia difensiva, redazione atti processuali, calcolo termini, gestione misure cautelari, ricerca giurisprudenziale, diritto penitenziario.

> **Calibrato su GIP, GUP, indagini, dibattimento, impugnazioni, misure cautelari e Cassazione penale.** Synthos Logic ha costruito questo kit insieme a professionisti del foro, in un progetto pilota reale con avvocati penalisti in attivita'.

---

## La metodologia fa la differenza

Il kit e' un assistente che **lavora nella struttura che tu costruisci**. Un fascicolo ben organizzato -- con i dati dell'indagato, il capo di imputazione, le scadenze e i link alla giurisprudenza rilevante -- abilita risposte di precisione professionale, memoria della strategia tra sessioni successive, atti coerenti con il lavoro gia' fatto.

Investire dieci minuti nell'organizzazione di un fascicolo restituisce ore di lavoro nel tempo.

Wiki [Guida metodologica completa](https://github.com/Synthos-Logic/penalista-italia/wiki) | Sito [Documentazione](https://synthos-logic.github.io/penalista-italia/) | Guida [Metodologia interattiva](https://synthos-logic.github.io/penalista-italia/METODOLOGIA.html)

---

## Installazione - 3 passi

### Passo 1 - Scarica il kit

Clicca **Code -> Download ZIP** in questa pagina. Decomprimi e rinomina la cartella in `Penale-Italia`.

### Passo 2 - Installa le 6 skill

Il kit include uno script di installazione automatica per entrambe le piattaforme.

**Su Mac** -- apri il Terminale, trascina il file `install.sh` dentro la finestra e premi Invio:
- Lo script crea la cartella `~/.claude/skills` se non esiste
- Copia le 6 skill automaticamente
- Conferma ogni skill installata

**Su Windows** -- doppio clic su `install.bat`:
- La finestra cmd si apre, mostra l'avanzamento e si chiude con il risultato
- Se Windows chiede conferma per eseguire lo script: clicca "Esegui comunque"

> **Preferisci farlo a mano?** I dettagli per Mac e Windows sono nella [guida installazione completa](documentazione/INSTALLAZIONE.md).

### Passo 3 - Collega il kit a Cowork

Claude Desktop -> Cowork -> **Seleziona cartella** -> seleziona la cartella `Penale-Italia` intera. Riavvia Claude Desktop.

---

## Configurazione dati studio

Apri `CLAUDE.md` con TextEdit (Mac) o Blocco Note (Windows) e compila la sezione "Dati dello studio":

```
AVVOCATO:          Avv. Mario Rossi
FORO:              Foro di Milano
N. ISCRIZIONE:     12345
TRIBUNALE:         Tribunale di Milano
CASSAZIONISTA:     NO
```

Da quel momento Claude usa questi dati nelle intestazioni di ogni atto processuale prodotto.

---

## 6 Skill specializzate

| Skill | Cosa fa |
|---|---|
| `penalista-strategia` | Analisi difensiva del capo di imputazione: elementi costitutivi, criticita' dell'accusa, eccezioni processuali, strategie graduate, giurisprudenza Cassazione e CEDU |
| `penalista-atti` | Redazione di tutti i principali atti: memoria 415-bis, appello, ricorso Cassazione, riesame, revoca cautelare, patteggiamento, abbreviato, messa alla prova |
| `penalista-scadenze` | Calcolo preciso di ogni termine processuale: impugnazioni, prescrizione ante/post Bonafede, custodia cautelare, improcedibilita' Cartabia, udienza di convalida |
| `penalista-cautelare` | Workflow completo misure cautelari: analisi presupposti, costruzione motivi riesame, revoca e sostituzione, scadenze di fase, scarcerazione urgente |
| `penalista-giurisprudenza` | Mappatura orientamenti Cassazione, analisi sentenze, individuazione contrasti tra sezioni, giurisprudenza CEDU, integrazione wikilinks |
| `penalista-esecuzione` | Diritto penitenziario: misure alternative, liberazione anticipata e condizionale, permessi premio, reclami condizioni detentive, regime 41-bis |

---

## Il sistema documentale

Il kit lavora con tutti i formati che uno studio penalistico usa ogni giorno:

| Formato | Uso | Come funziona |
|---|---|---|
| `.md` | Fascicoli, note strategia, giurisprudenza interna | Collegamento automatico via wikilinks, caricamento selettivo del contesto |
| `.pdf` | Ordinanze, sentenze, CNR, testi normativi | Allegare alla conversazione -- il kit legge e analizza |
| `.docx` | Atti prodotti, template, bozze | Allegare o usare la skill docx per lavorarci direttamente |
| `.html` | Guide, riferimenti, documentazione interna | Allegare o aprire come riferimento nella conversazione |

> Il formato `.md` e' ottimale per i file di lavoro: supporta i wikilinks, abilita il caricamento selettivo del contesto e riduce il consumo di token.

---

## Perche' Penalista Italia

Un kit costruito da chi conosce il processo penale italiano -- testato sul campo con avvocati in attivita' nel corso di un progetto pilota reale.

- **Specializzazione verticale** -- GIP, GUP, dibattimento, impugnazioni, Cassazione penale, Sorveglianza, D.Lgs. 231. Ogni risposta e' calibrata su questo specifico perimetro.
- **Memoria persistente tra sessioni** -- Il sistema wikilinks collega fascicoli, giurisprudenza e documenti. La strategia concordata in una sessione e' disponibile nella successiva.
- **Fonti deterministiche** -- Normativa ufficiale, HUDOC, Massimario Cassazione. Quando usi i testi come contesto, le risposte sono precise, tracciabili e citabili.
- **Template operativi** -- Pratiche ricorrenti gia' strutturate: gestione cautelare, risposta 415-bis, appello, ricorso Cassazione, esecuzione penale, D.Lgs. 231.
- **Riforma Cartabia come strumento difensivo** -- L'improcedibilita' ex art. 344-bis c.p.p. trattata come leva della difesa, con calcolo integrato nei termini processuali.
- **Aggiornato con la prassi reale** -- La Knowledge Base include schede operative per i reati piu' frequenti negli studi penali italiani, costruite con avvocati in attivita'.

---

## Aggiornamento

1. Scarica il nuovo ZIP (Code -> Download ZIP)
2. Sostituisci la cartella `Penale-Italia`
3. Se il changelog indica nuove skill: copia le nuove cartelle in `~/.claude/skills/`
4. Riavvia Claude Desktop

---

## Privacy e dati

I file fisici rimangono sul computer dello studio. Il testo portato in analisi transita sui server Anthropic esclusivamente per l'elaborazione.
La **Legge 132/2025 art. 13** regola l'obbligo di informativa ai clienti sull'uso di strumenti AI. Il CNF ha pubblicato uno schema di informativa pronto all'uso.

[Pagina Privacy completa -- Wiki](https://github.com/Synthos-Logic/penalista-italia/wiki/Privacy) | [Guida installazione dettagliata](documentazione/INSTALLAZIONE.md)

---

*Sviluppato da [Synthos Logic](https://github.com/Synthos-Logic) -- Intelligenza artificiale applicata alla pratica professionale italiana.*