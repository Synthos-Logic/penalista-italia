---
name: penalista-atti
description: >
  Analisi, sintesi e schedatura di atti processuali penali nell'ordinamento italiano.
  Trigger: atti processuali, CNR, informativa, ordinanza cautelare, decreto di sequestro,
  decreto di rinvio a giudizio, avviso 415-bis, avviso di garanzia, richiesta di archiviazione,
  opposizione archiviazione, decreto penale, notifica, elezione di domicilio, nomina difensore,
  verbale udienza, sentenza, analisi fascicolo, discovery, intercettazioni, captazioni,
  brogliaccio, RIT, tabulati, perizia, consulenza tecnica, CT, esame atti, copia atti,
  fascicolo dibattimentale, fascicolo PM, allegati. Attiva anche per: riassumere atti giudiziari,
  estrarre informazioni da documenti processuali, preparare schede sintetiche su fascicoli penali,
  confrontare versioni di atti, timeline dei fatti, analisi intercettazioni telefoniche o ambientali.
---

# penalista-atti — Analisi e schedatura atti processuali penali

## Cosa fa questa skill

Questa skill guida l'analisi strutturata di atti processuali penali italiani. Non si limita a "riassumere": il lavoro del penalista sugli atti richiede lettura critica, individuazione di vizi procedurali, estrazione di elementi utili alla difesa, e costruzione di una narrativa alternativa a quella accusatoria.

Ogni atto va letto con la domanda: "cosa posso usare a favore del mio assistito, e dove l'accusa è debole?"

## Flusso di lavoro

### 1. Acquisizione e inventario

Quando l'utente carica o indica atti processuali:

1. **Identifica la tipologia** di ciascun atto (informativa, ordinanza, decreto, verbale, perizia, intercettazione, ecc.)
2. **Crea un inventario strutturato** con: tipo atto, data, autorità emittente, soggetti coinvolti, numero di pagine/fogli
3. **Verifica la completezza**: segnala se mancano atti che normalmente dovrebbero esserci in quella fase processuale (es. manca l'avviso 415-bis, manca il verbale di una udienza intermedia)

### 2. Analisi per tipologia

#### Informative di reato e CNR
- Fonte della notizia di reato (denuncia, querela, iniziativa PG, stralcio)
- Qualificazione giuridica proposta dalla PG vs quella del PM
- Atti di PG compiuti d'iniziativa (art. 347-357 c.p.p.) — verifica rispetto termini e modalità
- Dichiarazioni raccolte: chi, quando, dove, con quali garanzie, presenza difensore se dovuta
- Attività tecniche: intercettazioni (verifica decreti autorizzativi), perquisizioni (verifica decreto o urgenza), sequestri
- **Profilo critico**: per ogni atto d'indagine, segnala potenziali nullità, inutilizzabilità, o irregolarità

#### Ordinanze cautelari (art. 272 ss. c.p.p.)
- Gravi indizi di colpevolezza: su cosa si fondano, quanto sono solidi
- Esigenze cautelari invocate (art. 274 c.p.p.): pericolo di fuga, inquinamento prove, reiterazione
- Proporzionalità e adeguatezza della misura
- **Profilo critico**: indizi che non raggiungono la gravità, esigenze cautelari non attuali, misura sproporzionata, mancata valutazione di misure meno afflittive

#### Decreti e provvedimenti del GIP/GUP
- Motivazione: adeguatezza, completezza, eventuale motivazione apparente o per relationem
- Rispetto del contraddittorio
- Termini

#### Perizie e consulenze tecniche
- Quesito posto
- Metodologia utilizzata (è scientificamente accreditata? Daubert/Cozzini)
- Conclusioni e margini di incertezza
- **Profilo critico**: vizi metodologici, conclusioni non supportate dai dati, quesito mal posto

#### Intercettazioni e captazioni
- Decreti autorizzativi: motivazione, durata, proroghe
- Brogliaccio: completezza, trascrizione vs riassunto PG
- Contenuto rilevante: passaggi chiave, contesto delle conversazioni
- **Profilo critico**: intercettazioni a strascico, utilizzo in procedimenti diversi senza autorizzazione, violazione art. 270 c.p.p., captatore informatico senza i presupposti

### 3. Output strutturati

Produci i seguenti documenti nella cartella del fascicolo:

#### Scheda sintetica fascicolo
```
SCHEDA FASCICOLO
================
Procedimento: [n. RGNR / RG GIP / RG Trib]
Indagato/Imputato: [nome assistito]
Reati contestati: [artt. c.p. con descrizione sintetica]
Fase processuale: [indagini / udienza preliminare / dibattimento / impugnazione]
PM: [nome]
Giudice: [nome]
Difensore: [nome]

TIMELINE DEI FATTI
- [data]: [evento]
- [data]: [evento]

ELEMENTI A FAVORE
1. [elemento con riferimento all'atto e pagina]

ELEMENTI A SFAVORE
1. [elemento con riferimento all'atto e pagina]

VIZI PROCEDURALI RILEVATI
1. [vizio con norma violata e conseguenza processuale]

ATTIVITÀ DIFENSIVE SUGGERITE
1. [attività con urgenza e termine se presente]
```

#### Timeline cronologica
Ricostruisci una timeline che includa sia i fatti contestati sia gli atti processuali, distinguendoli visivamente.

#### Matrice elementi probatori
Tabella che incrocia: elemento di prova × reato contestato × valutazione (a favore / a sfavore / neutro / inutilizzabile)

### 4. Regole fondamentali

- **Mai inventare riferimenti normativi.** Se non sei certo di un articolo, dillo esplicitamente.
- **Distingui sempre fatto da valutazione.** "L'informativa riferisce che..." è diverso da "È accaduto che..."
- **Segnala sempre la fonte.** Ogni affermazione deve essere riconducibile a un atto specifico con indicazione di pagina.
- **Ragiona in termini di utilizzabilità processuale.** Un'informazione può essere vera ma inutilizzabile: questa distinzione è cruciale per il penalista.
- **Rispetta la presunzione di innocenza** nel linguaggio: "persona sottoposta alle indagini", non "colpevole".
