---
name: penalista-giurisprudenza
description: >
  Ricerca, analisi e sistematizzazione della giurisprudenza penale italiana.
  Trigger: giurisprudenza, sentenza, massima, principio di diritto, Cassazione,
  Sezioni Unite, Corte Costituzionale, CEDU, Corte EDU, orientamento giurisprudenziale,
  contrasto giurisprudenziale, diritto vivente, precedente, overruling, nomofilachia,
  massimario, CED, ricerca giurisprudenziale, analisi sentenza, commento sentenza,
  nota a sentenza, rassegna giurisprudenziale, evoluzione giurisprudenziale,
  questione rimessa alle Sezioni Unite, ordinanza di rimessione.
  Attiva anche per: trovare precedenti su un tema penale, analizzare l'evoluzione
  interpretativa di una norma penale, preparare rassegne giurisprudenziali,
  confrontare orientamenti contrastanti della Cassazione.
---

# penalista-giurisprudenza — Ricerca e analisi giurisprudenziale penale

## Cosa fa questa skill

Guida la ricerca, l'analisi e la sistematizzazione della giurisprudenza penale italiana. Il penalista vive di giurisprudenza: la stessa norma può significare cose radicalmente diverse a seconda di come la Cassazione la interpreta in quel momento. Conoscere lo stato dell'arte giurisprudenziale non è un lusso accademico, è la base per ogni atto difensivo.

## Limiti importanti — leggere con attenzione

**Claude non ha accesso a banche dati giurisprudenziali** (Italgiure, DeJure, Pluris, OneKey, ecc.). Questo significa che:

- Non può cercare sentenze specifiche per numero o data con certezza di accuratezza
- Non può garantire che una sentenza citata esista realmente con quei riferimenti
- Non può verificare se un orientamento è stato superato da pronunce recenti

**Cosa può fare Claude:**
- Indicare gli **orientamenti giurisprudenziali consolidati** sui grandi temi del diritto penale (sostanziale e processuale) sulla base della propria conoscenza
- Fornire **framework di ricerca**: quali parole chiave usare, in quali sezioni cercare, come impostare la query
- **Analizzare sentenze** che l'utente carica o incolla
- **Sistematizzare** la giurisprudenza raccolta dall'utente
- **Segnalare contrasti noti** tra sezioni della Cassazione

**Regola d'oro**: ogni riferimento giurisprudenziale prodotto da Claude deve essere **verificato dal difensore** sulla banca dati. Claude segnalerà sempre questa necessità con il tag [VERIFICARE].

## Flusso di lavoro

### 1. Ricerca orientata (quando l'utente cerca giurisprudenza su un tema)

**Fase A — Inquadramento**
1. Chiedi il **tema specifico** (non "furto" ma "furto in abitazione con desistenza volontaria dopo l'introduzione nell'abitazione")
2. Chiedi lo **scopo**: serve per una memoria? Un appello? Un ricorso in Cassazione? Un parere?
3. Chiedi se ci sono **sentenze di riferimento** che l'utente già conosce

**Fase B — Mappa degli orientamenti**
Produci una mappa strutturata:

```
TEMA: [descrizione precisa]

NORMA/E DI RIFERIMENTO: art. [...] c.p./c.p.p.

ORIENTAMENTO PREVALENTE (o CONSOLIDATO)
- Principio: [formulazione sintetica]
- Sezione/i di riferimento: [es. "Sez. II", "Sez. Un."]
- Sentenze note: [VERIFICARE: Cass., Sez. ..., n. ..., anno]
- Ratio: [perché la giurisprudenza si è orientata così]

ORIENTAMENTO MINORITARIO / CONTRARIO (se esiste)
- Principio: [formulazione sintetica]
- Sezione/i: [...]
- Sentenze note: [VERIFICARE]
- Ratio: [...]

EVENTUALI INTERVENTI DELLE SEZIONI UNITE
- [Se pertinente, con indicazione della questione rimessa e della soluzione]

EVOLUZIONE RECENTE
- [Se ci sono segnali di cambiamento o questioni pendenti]

SUGGERIMENTI DI RICERCA
- Parole chiave per banca dati: [...]
- Sezioni da filtrare: [...]
- Periodo temporale consigliato: [...]
```

**Fase C — Selezione strategica**
In base allo scopo dell'utente, suggerisci quale orientamento invocare e come presentarlo nell'atto difensivo. Se l'orientamento favorevole è minoritario, suggerisci come argomentare per il suo accoglimento.

### 2. Analisi di sentenza specifica (quando l'utente carica una sentenza)

Produci una scheda strutturata:

```
SCHEDA SENTENZA
===============
Autorità: [Cass. Pen., Sez. ... / Corte App. ... / Trib. ...]
Numero: [...]
Data: [udienza / deposito]
Presidente: [se indicato]
Relatore/Estensore: [se indicato]

FATTO PROCESSUALE
[Iter del procedimento fino alla sentenza analizzata]

FATTO MATERIALE
[I fatti come ricostruiti dalla sentenza]

QUESTIONE/I DI DIRITTO
1. [Prima questione]
2. [Seconda questione]

PRINCIPIO/I DI DIRITTO
1. [Formulazione precisa del principio affermato]

MOTIVAZIONE — PASSAGGI CHIAVE
[Citazione dei passaggi argomentativi centrali con indicazione paragrafo/pagina]

PRECEDENTI CITATI DALLA SENTENZA
[Elenco delle sentenze richiamate in motivazione]

VALUTAZIONE DIFENSIVA
- Utilizzabilità a favore: [in che contesto questa sentenza aiuta la difesa]
- Rischi: [possibili distinguishing o limiti nell'invocabilità]
- Orientamento confermato o innovativo?
```

### 3. Rassegna giurisprudenziale (quando serve una panoramica completa)

Per rassegne organiche su un istituto o una fattispecie:

1. **Ricostruzione storica**: evoluzione dell'interpretazione nel tempo
2. **Stato attuale**: orientamento prevalente con eventuali contrasti
3. **Questioni aperte**: profili non ancora risolti o rimessi alle Sezioni Unite
4. **Proiezione**: verso dove sembra andare la giurisprudenza

Formato: documento discorsivo con note a piè di pagina per i riferimenti [VERIFICARE].

## Fonti e gerarchie

Per il penalista italiano, la gerarchia delle fonti giurisprudenziali è:

1. **Corte Costituzionale** — sentenze di illegittimità, sentenze interpretative, moniti al legislatore
2. **Cassazione, Sezioni Unite** — risolvono contrasti tra sezioni, massima autorità nomofilattica
3. **Cassazione, Sezioni semplici** — orientamenti delle singole sezioni (I-VII penale)
4. **Corte EDU** — vincolante per interpretazione conforme (artt. 6, 7, 8 CEDU in primis)
5. **Corte di Giustizia UE** — per materie di competenza UE (es. mandato d'arresto europeo, ne bis in idem)
6. **Giurisprudenza di merito** — utile ma non vincolante

## Regole fondamentali

- **[VERIFICARE] è obbligatorio** su ogni sentenza citata a memoria. Sempre.
- **Non confondere massima e motivazione.** La massima è un estratto redazionale, la motivazione è la vera portata della sentenza.
- **Attenzione all'obiter dictum**: non tutto ciò che la Cassazione scrive in motivazione è "principio di diritto". Distingui ratio decidendi da obiter.
- **Contestualizza.** Una sentenza del 2005 su un reato la cui fattispecie è stata modificata nel 2015 va maneggiata con cura.
