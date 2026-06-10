# Penalista Italia -- Kit Operativo per Avvocati Penalisti

[![Versione](https://img.shields.io/badge/versione-3.1.2-blue)](https://github.com/Synthos-Logic/penalista-italia/releases)
[![Licenza](https://img.shields.io/badge/licenza-MIT-green)](LICENSE)
[![Piattaforma](https://img.shields.io/badge/piattaforma-Claude%20Cowork-orange)](https://claude.ai)
[![Wiki](https://img.shields.io/badge/Wiki-metodologia-blueviolet)](https://github.com/Synthos-Logic/penalista-italia/wiki)
[![Sviluppato da](https://img.shields.io/badge/sviluppato%20da-Synthos%20Logic-purple)](https://github.com/Synthos-Logic)

**Kit operativo specializzato esclusivamente per avvocati penalisti italiani.** Strategia difensiva, redazione atti processuali, calcolo termini, gestione misure cautelari, ricerca giurisprudenziale, diritto penitenziario.

> **Calibrato su GIP, GUP, indagini, dibattimento, impugnazioni, misure cautelari e Cassazione penale.** Synthos Logic ha costruito questo kit insieme a professionisti del foro, in un progetto pilota reale con avvocati penalisti in attivita'.

---

## La metodologia fa la differenza

Il kit e' un assistente che **lavora in una struttura organizzata — e la struttura la costruisce lui**. Fascicoli, indici, scadenziario e collegamenti tra documenti: li crea e li mantiene il kit a ogni operazione. Un fascicolo ben organizzato -- con i dati dell'indagato, il capo di imputazione, le scadenze e la giurisprudenza rilevante -- abilita risposte di precisione professionale, memoria della strategia tra sessioni successive, atti coerenti con il lavoro gia' fatto. Per partire basta scrivere **"Iniziamo"**: la skill di onboarding accompagna il primo avvio passo per passo.

Investire dieci minuti nell'organizzazione di un fascicolo restituisce ore di lavoro nel tempo.

Wiki [Guida metodologica completa](https://github.com/Synthos-Logic/penalista-italia/wiki) | Sito [Documentazione](https://synthos-logic.github.io/penalista-italia/) | Guida [Metodologia interattiva](https://synthos-logic.github.io/penalista-italia/METODOLOGIA.html)

---

## Installazione - 3 passi

### Passo 1 - Scarica il kit

Clicca **Code -> Download ZIP** in questa pagina. Decomprimi e rinomina la cartella in `Penale-Italia`.

### Passo 2 - Collega il kit a Cowork

Claude Desktop -> Cowork -> **Seleziona cartella** -> seleziona la cartella `Penale-Italia` intera.

### Passo 3 - Installa le 8 skill (installazione assistita)

Con la cartella selezionata, incolla questo messaggio a Claude:

```
Installa le skill del kit Penalista Italia seguendo il file INSTALLAZIONE_ASSISTITA.md; se il file non è nella cartella selezionata, scaricalo da https://raw.githubusercontent.com/Synthos-Logic/penalista-italia/main/INSTALLAZIONE_ASSISTITA.md e segui le sue istruzioni.
```

Claude presenta **8 schede con il pulsante "Salva skill"**: un clic per ciascuna e l'installazione e' fatta. Niente Terminale, niente cartelle nascoste. Verifica finale in **Personalizza -> Skills**.

> **Importante:** nell'app desktop le skill si installano SOLO cosi' (o caricando gli ZIP a mano da Personalizza -> Skills). Il percorso `~/.claude/skills` e gli script `install.sh`/`install.bat` valgono **solo per chi usa Claude Code da terminale**. Dettagli e metodo manuale nella [guida installazione completa](documentazione/INSTALLAZIONE.md).

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

## 8 Skill specializzate

| Skill | Cosa fa |
|---|---|
| `penalista-inizia` 🆕 | Onboarding guidato: dal primo "Iniziamo" al primo fascicolo operativo in 15 minuti, su un caso vero. Configura i dati studio e accompagna l'avvocato senza richiedere lettura di documentazione |
| `penalista-strategia` | Analisi difensiva del capo di imputazione: elementi costitutivi, criticita' dell'accusa, eccezioni processuali, strategie graduate, giurisprudenza Cassazione e CEDU |
| `penalista-atti` | Redazione di tutti i principali atti: memoria 415-bis, appello, ricorso Cassazione, riesame, revoca cautelare, patteggiamento, abbreviato, messa alla prova |
| `penalista-scadenze` | Calcolo preciso di ogni termine processuale: impugnazioni, prescrizione ante/post Bonafede, custodia cautelare, improcedibilita' Cartabia, udienza di convalida |
| `penalista-cautelare` | Workflow completo misure cautelari: analisi presupposti, costruzione motivi riesame, revoca e sostituzione, scadenze di fase, scarcerazione urgente |
| `penalista-giurisprudenza` | Mappatura orientamenti Cassazione, analisi sentenze, individuazione contrasti tra sezioni, giurisprudenza CEDU, integrazione wikilinks |
| `penalista-esecuzione` | Diritto penitenziario: misure alternative, liberazione anticipata e condizionale, permessi premio, reclami condizioni detentive, regime 41-bis |
| `penalista-verifica` 🆕 | Controllo qualita' pre-deposito: verifica indipendente di ogni citazione giurisprudenziale contro la Knowledge Base, ricalcolo dei termini, coerenza atto-fascicolo. Report con esito 🟢/🟡/🔴 |

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

> ⚠️ **Non sostituire mai la cartella `Penale-Italia` a mano:** dentro ci sono i tuoi fascicoli e i dati del tuo studio.

1. Scarica il nuovo ZIP (Code -> Download ZIP)
2. Trascina il file ZIP (senza decomprimerlo) dentro la cartella `Penale-Italia`
3. Incolla a Claude: *"Ho scaricato l'aggiornamento del kit Penalista Italia: eseguilo seguendo AGGIORNAMENTO_ASSISTITO.md; se il file non è nella cartella selezionata, scaricalo da https://raw.githubusercontent.com/Synthos-Logic/penalista-italia/main/AGGIORNAMENTO_ASSISTITO.md e segui le sue istruzioni."*

Claude aggiorna i file del kit **preservando fascicoli e dati studio**, ti riassume le novita' e ti presenta le skill aggiornate da reinstallare con un clic.

---

## Privacy e dati

I file fisici rimangono sul computer dello studio. Il testo portato in analisi transita sui server Anthropic esclusivamente per l'elaborazione.
La **Legge 132/2025 art. 13** regola l'obbligo di informativa ai clienti sull'uso di strumenti AI. Il CNF ha pubblicato uno schema di informativa pronto all'uso.

[Pagina Privacy completa -- Wiki](https://github.com/Synthos-Logic/penalista-italia/wiki/Privacy) | [Guida installazione dettagliata](documentazione/INSTALLAZIONE.md)

---

*Sviluppato da [Synthos Logic](https://github.com/Synthos-Logic) -- Intelligenza artificiale applicata alla pratica professionale italiana.*