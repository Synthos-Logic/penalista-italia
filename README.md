# Penalista Italia -- Kit Operativo per Avvocati Penalisti

[![Versione](https://img.shields.io/badge/versione-3.2.0-blue)](https://github.com/Synthos-Logic/penalista-italia/releases)
[![Licenza](https://img.shields.io/badge/licenza-MIT-green)](LICENSE)
[![Piattaforma](https://img.shields.io/badge/piattaforma-Claude%20Cowork-orange)](https://claude.ai)
[![Wiki](https://img.shields.io/badge/Wiki-metodologia-blueviolet)](https://github.com/Synthos-Logic/penalista-italia/wiki)
[![Sviluppato da](https://img.shields.io/badge/sviluppato%20da-Synthos%20Logic-purple)](https://github.com/Synthos-Logic)

**Kit operativo specializzato esclusivamente per avvocati penalisti italiani.** Strategia difensiva, redazione atti processuali, calcolo termini, gestione misure cautelari, ricerca giurisprudenziale, diritto penitenziario.

> **Calibrato su GIP, GUP, indagini, dibattimento, impugnazioni, misure cautelari e Cassazione penale.** Synthos Logic ha costruito questo kit insieme a professionisti del foro, in un progetto pilota reale con avvocati penalisti in attivita'.

---

## La metodologia fa la differenza

Il kit e' un assistente che **lavora in una struttura organizzata -- e la struttura la costruisce lui**. Quando apri un fascicolo, il kit lo organizza, lo indicizza e lo collega da solo: tu non devi imparare nulla di tecnico. Il risultato e' una **memoria di studio**: la strategia concordata oggi e' disponibile domani, gli atti citano il lavoro gia' fatto, le scadenze restano sotto controllo. Per partire basta scrivere **"Iniziamo"**: la skill di onboarding accompagna il primo avvio passo per passo.

Investire dieci minuti nell'organizzazione di un fascicolo restituisce ore di lavoro nel tempo.

Wiki [Guida metodologica completa](https://github.com/Synthos-Logic/penalista-italia/wiki) | Sito [Documentazione](https://synthos-logic.github.io/penalista-italia/) | Guida [Metodologia interattiva](https://synthos-logic.github.io/penalista-italia/METODOLOGIA.html)

---

## Installazione -- 3 passi

### Passo 1 -- Installa il plugin (le 8 skill, in un colpo solo)

In Claude Desktop:

1. Apri **Personalizza** (icona in basso a sinistra) -> sezione **Plugin** -> scheda **Personale**
2. Clicca **+** -> **Aggiungi marketplace** e incolla: `Synthos-Logic/penalista-italia`
3. Clicca **Sincronizza**, poi **installa** la scheda "Penalista Italia"

Fatto: le 8 skill sono attive. **Gli aggiornamenti arrivano da soli** (vedi sotto).

### Passo 2 -- Scarica la cartella di lavoro

Clicca **Code -> Download ZIP** in questa pagina. Decomprimi, rinomina la cartella in `Penale-Italia` e collegala: Claude Desktop -> Cowork -> **Seleziona cartella** -> `Penale-Italia`.

Dentro ci sono la Knowledge Base (massimari e schede reato), la cartella `FASCICOLI/` per i tuoi casi e il file `CLAUDE.md` con i dati del tuo studio.

### Passo 3 -- Scrivi "Iniziamo"

Il kit si presenta, ti chiede i dati dello studio (nome, foro, tribunale) e apre con te il primo fascicolo. Quindici minuti, su un caso vero.

> Guida con immagini passo-passo: [Installazione dettagliata](docs/INSTALLAZIONE.md) · Senza GitHub/marketplace? [Installazione alternativa](documentazione/INSTALLAZIONE_ALTERNATIVA.md)

---

## Aggiornamenti

**Le skill si aggiornano da sole con il plugin.** Per attivare gli aggiornamenti automatici (una volta sola): Personalizza -> Plugin -> Personale -> clicca i **tre puntini** accanto a `penalista-italia` -> attiva **"Sincronizza automaticamente"**. In alternativa, dallo stesso menu, **"Verifica aggiornamenti"** quando vuoi. Dopo un aggiornamento, apri una conversazione nuova.

**La cartella di lavoro** (Knowledge Base, guide) si aggiorna piu' raramente: quando il changelog lo segnala, scarica il nuovo ZIP, trascinalo **dentro** la cartella `Penale-Italia` senza decomprimerlo e incolla a Claude:

```
Ho scaricato l'aggiornamento del kit Penalista Italia: eseguilo seguendo AGGIORNAMENTO_ASSISTITO.md; se il file non è nella cartella selezionata, scaricalo da https://raw.githubusercontent.com/Synthos-Logic/penalista-italia/main/AGGIORNAMENTO_ASSISTITO.md e segui le sue istruzioni.
```

> ⚠️ **Non sostituire mai la cartella `Penale-Italia` a mano:** dentro ci sono i tuoi fascicoli e i dati del tuo studio. L'aggiornamento assistito non li tocca mai.

---

## Configurazione dati studio

La skill di onboarding la fa con te al primo "Iniziamo". Se preferisci farlo a mano: apri `CLAUDE.md` con TextEdit (Mac) o Blocco Note (Windows) e compila la sezione "Dati dello studio". Da quel momento Claude usa questi dati nelle intestazioni di ogni atto processuale prodotto.

---

## 8 Skill specializzate

| Skill | Cosa fa |
|---|---|
| `penalista-inizia` | Onboarding guidato: dal primo "Iniziamo" al primo fascicolo operativo in 15 minuti, su un caso vero |
| `penalista-strategia` | Analisi difensiva del capo di imputazione: elementi costitutivi, criticita' dell'accusa, eccezioni processuali, strategie graduate, giurisprudenza Cassazione e CEDU |
| `penalista-atti` | Redazione di tutti i principali atti: memoria 415-bis, appello, ricorso Cassazione, riesame, revoca cautelare, patteggiamento, abbreviato, messa alla prova |
| `penalista-scadenze` | Calcolo preciso di ogni termine processuale: impugnazioni, prescrizione ante/post Bonafede, custodia cautelare, improcedibilita' Cartabia, udienza di convalida |
| `penalista-cautelare` | Workflow completo misure cautelari: analisi presupposti, costruzione motivi riesame, revoca e sostituzione, scadenze di fase, scarcerazione urgente |
| `penalista-giurisprudenza` | Mappatura orientamenti Cassazione, analisi sentenze, individuazione contrasti tra sezioni, giurisprudenza CEDU |
| `penalista-esecuzione` | Diritto penitenziario: misure alternative, liberazione anticipata e condizionale, permessi premio, reclami condizioni detentive, regime 41-bis |
| `penalista-verifica` | Controllo qualita' pre-deposito: verifica indipendente di ogni citazione giurisprudenziale contro la Knowledge Base, ricalcolo dei termini, coerenza atto-fascicolo. Report con esito 🟢/🟡/🔴 |

Comandi rapidi: `/penalista-italia:aiuto` (guida) · `/penalista-italia:versione` (versione installata)

---

## Il sistema documentale

Il kit lavora con tutti i formati che uno studio penalistico usa ogni giorno:

| Formato | Uso |
|---|---|
| `.md` | Fascicoli, note strategia, giurisprudenza interna -- il formato di lavoro del kit: leggero e collegabile |
| `.pdf` | Ordinanze, sentenze, CNR, testi normativi -- allega alla conversazione, il kit legge e analizza |
| `.docx` | Atti prodotti, template, bozze |
| `.html` | Guide, riferimenti, documentazione interna |

---

## Perche' Penalista Italia

Un kit costruito da chi conosce il processo penale italiano -- testato sul campo con avvocati in attivita' nel corso di un progetto pilota reale.

- **Specializzazione verticale** -- GIP, GUP, dibattimento, impugnazioni, Cassazione penale, Sorveglianza, D.Lgs. 231. Ogni risposta e' calibrata su questo specifico perimetro.
- **Memoria di studio tra sessioni** -- Il kit collega da solo fascicoli, giurisprudenza e documenti: la strategia concordata in una sessione e' disponibile nella successiva, senza che tu debba fare nulla.
- **Fonti deterministiche** -- Normativa ufficiale, HUDOC, Massimario Cassazione. Quando usi i testi come contesto, le risposte sono precise, tracciabili e citabili.
- **Template operativi** -- Pratiche ricorrenti gia' strutturate: gestione cautelare, risposta 415-bis, appello, ricorso Cassazione, esecuzione penale, D.Lgs. 231.
- **Riforma Cartabia come strumento difensivo** -- L'improcedibilita' ex art. 344-bis c.p.p. trattata come leva della difesa, con calcolo integrato nei termini processuali.
- **Aggiornato con la prassi reale** -- Knowledge Base con schede operative per i reati piu' frequenti negli studi penali italiani, e aggiornamenti che arrivano da soli tramite il plugin.

---

## Privacy e dati

I file fisici rimangono sul computer dello studio. Il testo portato in analisi transita sui server Anthropic esclusivamente per l'elaborazione.
La **Legge 132/2025 art. 13** regola l'obbligo di informativa ai clienti sull'uso di strumenti AI. Il CNF ha pubblicato uno schema di informativa pronto all'uso.

[Pagina Privacy completa -- Wiki](https://github.com/Synthos-Logic/penalista-italia/wiki/Privacy) | [Guida installazione dettagliata](docs/INSTALLAZIONE.md)

---

*Sviluppato da [Synthos Logic](https://github.com/Synthos-Logic) -- Intelligenza artificiale applicata alla pratica professionale italiana.*
