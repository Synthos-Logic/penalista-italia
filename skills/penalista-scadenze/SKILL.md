---
name: penalista-scadenze
description: >
  Calcolo e gestione dei termini processuali penali nell'ordinamento italiano.
  Trigger: termine processuale, scadenza, decadenza, prescrizione, termini custodia
  cautelare, termini indagini, termine impugnazione, sospensione feriale, termini
  a difesa, proroga indagini, durata massima indagini, termini fase, scadenza misura
  cautelare, efficacia misura cautelare, termini deposito, calcolo prescrizione,
  dies a quo, dies ad quem, termini perentori, termini ordinatori, calendario
  processuale, agenda udienze, promemoria scadenze.
  Attiva anche per: calcolare quando scade un termine, verificare la prescrizione
  di un reato, controllare i termini di custodia cautelare, pianificare le scadenze
  di un fascicolo, calcolare il termine per impugnare.
---

# penalista-scadenze — Termini processuali penali

## Cosa fa questa skill

Assiste nel calcolo e nella gestione dei termini processuali penali. Nel penale, sbagliare un termine significa perdere un'impugnazione, far scarcerare un indagato (o il contrario: lasciarlo dentro quando potrebbe uscire), far prescrivere un reato. I termini sono vita professionale per il penalista.

## Avvertenza critica

Il calcolo dei termini processuali ha conseguenze irreversibili. Claude fornisce un **supporto al calcolo**, ma il difensore **deve sempre verificare personalmente**. Fattori che Claude potrebbe non conoscere o calcolare correttamente: sospensioni specifiche, rinvii con termini a difesa, modifiche normative recenti, prassi locali.

## Principali categorie di termini

### 1. Termini di impugnazione (art. 585 c.p.p.)

| Provvedimento | Termine | Decorrenza |
|---|---|---|
| Sentenza con motivazione contestuale | 15 gg | Dalla lettura |
| Sentenza con motivazione differita (30 gg) | 30 gg | Dalla notifica avviso deposito |
| Sentenza con motivazione differita (90 gg) | 45 gg | Dalla notifica avviso deposito |
| Ordinanza (appello cautelare) | 20 gg | Dalla comunicazione/notifica |
| Riesame | 10 gg | Dall'esecuzione/notifica ordinanza |
| Opposizione decreto penale | 15 gg | Dalla notifica |

**Regole di calcolo:**
- Si contano i giorni liberi (non si conta il giorno iniziale)
- Se il termine scade in giorno festivo, è prorogato al primo giorno non festivo successivo
- **Sospensione feriale**: dal 1° al 31 agosto (salvo eccezioni: procedimenti cautelari, custodia cautelare, procedimenti con detenuti se rinuncia alla sospensione)

### 2. Termini di custodia cautelare (art. 303-308 c.p.p.)

Struttura a fasi. I termini variano per gravità del reato. Schema semplificato:

| Fase | Reati minori (art. 278: pena max < 6 anni) | Reati gravi (pena max ≥ 20 anni) | Reati gravissimi (ergastolo) |
|---|---|---|---|
| Indagini | 3 mesi (proroga a 6) | 6 mesi (proroga a 1 anno) | 1 anno (proroga a 2) |
| Udienza preliminare | 3 mesi (proroga a 6) | 6 mesi (proroga a 9) | 1 anno |
| Dibattimento primo grado | 6 mesi | 1 anno | 1 anno e 6 mesi |
| Appello | 9 mesi | 1 anno | 1 anno e 6 mesi |
| Cassazione | 6 mesi | 9 mesi | 1 anno |

**Termine complessivo massimo**: somma di tutte le fasi, con tetto massimo assoluto.

**ATTENZIONE**: questo schema è semplificato. Le regole reali sono più complesse (art. 303-308 c.p.p.) e ci sono cause di sospensione (art. 304 c.p.p.) che interrompono il decorso. Verificare sempre sul testo di legge aggiornato.

### 3. Prescrizione (artt. 157-161 c.p.)

**Formula base** (post riforma 2005, Legge n. 251/2005, con successive modifiche):
- Tempo di prescrizione = pena massima edittale, comunque non inferiore a 6 anni (delitti) o 4 anni (contravvenzioni)
- Con atti interruttivi: aumento di 1/4 del tempo base
- Cause di sospensione: elencate nell'art. 159 c.p. (es. autorizzazione a procedere, rogatorie, sospensione del processo)

**ATTENZIONE - Riforma Cartabia (D.Lgs. 150/2022):**
Per i reati commessi dopo il 1° gennaio 2020, la prescrizione si ferma con la sentenza di primo grado. Dopo il primo grado si applica l'**improcedibilità per superamento dei termini** di durata massima del giudizio di impugnazione (art. 344-bis c.p.p.):
- Appello: 2 anni (3 per reati gravi)
- Cassazione: 1 anno (1 anno e 6 mesi per reati gravi)
- Prorogabili dal giudice per complessità

**Regime transitorio**: i reati commessi prima del 1° gennaio 2020 seguono il vecchio regime. Attenzione alla sovrapposizione dei regimi.

### 4. Termini delle indagini preliminari (art. 405-407 c.p.p.)

| Tipologia | Durata ordinaria | Proroga massima |
|---|---|---|
| Reati ordinari | 6 mesi | fino a 18 mesi |
| Reati gravi (art. 407, co. 2) | 1 anno | fino a 2 anni |

Il dies a quo è la data di iscrizione nel registro notizie di reato. Problema pratico frequente: la retrodatazione dell'iscrizione (Cass., Sez. Un., Catanzaro).

### 5. Altri termini ricorrenti

- **Avviso 415-bis**: termine a difesa di **20 giorni** per presentare memorie, documenti, chiedere di essere interrogato
- **Lista testi art. 468**: almeno **7 giorni liberi** prima dell'udienza dibattimentale
- **Costituzione parte civile**: fino all'apertura del dibattimento (ma con termine per notifica all'imputato)
- **Richiesta di giudizio abbreviato**: prima delle conclusioni dell'udienza preliminare
- **Richiesta di patteggiamento**: fino alle conclusioni dell'udienza preliminare (o fino alla dichiarazione di apertura del dibattimento)
- **Oblazione**: prima dell'apertura del dibattimento

## Flusso operativo

### Quando l'utente chiede un calcolo di termine

1. **Raccogli i dati necessari**:
   - Tipo di provvedimento / atto
   - Data del provvedimento o dell'evento da cui decorre il termine
   - Se il soggetto è detenuto o libero
   - Se ci sono state sospensioni feriali o altre sospensioni
   - Rito (ordinario, abbreviato, ecc.)

2. **Calcola** mostrando ogni passaggio:
   ```
   CALCOLO TERMINE
   ================
   Tipo: [es. termine per appello]
   Dies a quo: [data] — [motivo: lettura/notifica/esecuzione]
   Termine base: [n. giorni]
   Sospensione feriale: [SI/NO — dal ... al ...]
   Giorni festivi finali: [se il termine cade di festivo]

   SCADENZA CALCOLATA: [data]

   ⚠️ VERIFICARE: [eventuali fattori di incertezza]
   ```

3. **Segnala il livello di affidabilità**:
   - ALTA: termini semplici, senza variabili incerte
   - MEDIA: termini con possibili sospensioni o complessità
   - BASSA: termini che dipendono da fattori che l'utente dovrebbe verificare

### Quando l'utente chiede di gestire le scadenze di un fascicolo

Produci un **prospetto scadenze** con tutte le date rilevanti:

```
PROSPETTO SCADENZE — Proc. n. [...]
==========================================

SCADENZE IMMINENTI (prossimi 30 giorni)
⚡ [data] — [termine] — URGENTE
📋 [data] — [termine]

SCADENZE A MEDIO TERMINE (30-90 giorni)
📋 [data] — [termine]

SCADENZE A LUNGO TERMINE / DA MONITORARE
📋 [data stimata] — Prescrizione
📋 [data stimata] — Termini custodia cautelare fase [...]

NOTE
- [eventuali incertezze o date da verificare]
```

## Regole fondamentali

- **Mai dare per certo un calcolo complesso.** Segnala sempre i fattori di incertezza.
- **Conservativo**: nel dubbio, indica la scadenza più breve (più sfavorevole per chi deve rispettarla).
- **Sospensione feriale**: ricorda sempre di verificare se si applica o no al caso specifico.
- **Regime transitorio**: attenzione alle norme intertemporali, specialmente per prescrizione e improcedibilità.
- **Aggiornamento normativo**: segnala se il termine potrebbe essere stato modificato da riforme recenti che Claude non conosce.
