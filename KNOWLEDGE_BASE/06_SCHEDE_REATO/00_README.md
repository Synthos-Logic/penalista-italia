# Schede Reato — Guida all'uso
*Versione 1.0 — Maggio 2026*

Questo folder è il **cuore operativo della Knowledge Base per lo studio**.
Le Schede Reato sono documenti di consultazione rapida che Claude usa come punto di ingresso per ogni caso. Non sono fonti autoritative — sono aggregatori della conoscenza dello studio su ogni singolo reato.

---

## Cos'è una Scheda Reato

Una scheda è un file `.md` che raccoglie, in formato strutturato, tutto ciò che lo studio sa su un determinato reato:
- la norma e i suoi elementi costitutivi
- i termini di prescrizione e cautelari
- la giurisprudenza rilevante (con link alle fonti in KB)
- le strategie difensive che lo studio ha già utilizzato
- gli aggiornamenti normativi recenti

**La scheda non sostituisce le fonti** (che restano in `01_NORMATIVA/` e `02_GIURISPRUDENZA/`): le sintetizza e le rende accessibili in un unico punto.

---

## Struttura delle cartelle

| Cartella | Macro-categoria | Reati principali |
|---|---|---|
| `A_REATI_PATRIMONIO/` | Reati contro il patrimonio | Truffa, Furto, Rapina, Estorsione, Appropriazione indebita, Ricettazione, Riciclaggio, Autoriciclaggio |
| `B_REATI_PERSONA/` | Reati contro la persona | Lesioni, Omicidio colposo, Omicidio/Lesioni stradali, Maltrattamenti, Stalking, Violenza sessuale |
| `C_REATI_TRIBUTARI/` | Reati tributari (D.Lgs. 74/2000) | Dichiarazione fraudolenta (artt. 2-3), Dichiarazione infedele (art. 4), Omessa dichiarazione (art. 5), Emissione fatture false (art. 8), Sottrazione fraudolenta (art. 11) |
| `D_REATI_PA/` | Reati contro la PA | Corruzione (artt. 318-321), Peculato (art. 314), Concussione (art. 317), Turbata libertà degli incanti (art. 353) |
| `E_REATI_SOCIETARI_FALLIMENTARI/` | Reati societari e fallimentari | False comunicazioni sociali (artt. 2621-2622 c.c.), Bancarotta fraudolenta/semplice (artt. 216-217 L.F./CCII) |
| `F_REATI_INFORMATICI/` | Reati informatici | Accesso abusivo (art. 615-ter), Frode informatica (art. 640-ter), Danneggiamento informatico |
| `G_STUPEFACENTI/` | Reati in materia di stupefacenti | Detenzione/spaccio (art. 73 DPR 309/1990), Associazione per traffico (art. 74) |
| `H_CRIMINALITA_ORGANIZZATA/` | Criminalità organizzata | Associazione per delinquere (art. 416), Associazione mafiosa (art. 416-bis) |

---

## Template standard — cosa mettere in ogni scheda

Ogni scheda segue questa struttura. I campi marcati `[DA COMPILARE]` sono quelli che lo studio deve popolare con la propria esperienza.

```
# [NOME REATO] — Scheda Operativa

## 1. Identificazione
- Norma: art. X c.p. / art. X D.Lgs. Y/AAAA
- Categoria: delitto / contravvenzione
- Procedibilità: d'ufficio / querela (indicare termini)
- Bene giuridico protetto: ...

## 2. Elementi costitutivi
### Condotta
### Evento
### Nesso causale
### Elemento soggettivo (dolo/colpa/preterintenzione)

## 3. Circostanze
### Aggravanti specifiche (con effetti su pena e prescrizione)
### Attenuanti specifiche
### Circostanza attenuante speciale (se prevista)

## 4. Pena
- Base: reclusione ... / multa ...
- Con aggravanti: ...
- Pena accessoria: ...

## 5. Prescrizione
- Termine base: ... anni (ex art. 157 c.p.)
- Con aggravanti: ... anni
- Sospensione feriale: sì (dal 1° agosto al 15 settembre)
- Note post-riforma Cartabia (D.Lgs. 150/2022): ...

## 6. Misure cautelari
- Custodia cautelare in carcere: ammessa? (pena max > 5 anni)
- Misure interdittive: quali
- Sequestro preventivo: oggetto tipico

## 7. Questioni difensive ricorrenti
[DA COMPILARE — argomenti difensivi che lo studio ha già utilizzato con successo]

## 8. Giurisprudenza chiave
[Link a fonti in KB o note con [VERIFICARE] se da memoria]
- SU — tema: ...
- Cass. sezione — tema: ...
- Rassegna Massimario Penale [anno], p. [xx]

## 9. Normativa di riferimento in KB
[Link ai file presenti in 01_NORMATIVA/]

## 10. Prassi dello studio
[DA COMPILARE — casi gestiti, argomenti rodati, giudici del distretto]

## 11. Aggiornamenti recenti
[DA COMPILARE — modifiche normative, sentenze rilevanti post-2024]
```

---

## Come alimentare le schede nel tempo

Dopo ogni fascicolo chiuso, l'avvocato (o il praticante) aggiorna la scheda del reato pertinente con:

1. **Sezione 7 — Questioni difensive**: aggiungere l'argomento usato e il risultato ottenuto (es: "eccezione di nullità ex art. 178 lett. c c.p.p. per omessa discovery — accolta da GUP Milano, ud. [data]")
2. **Sezione 10 — Prassi dello studio**: aggiungere il riferimento al fascicolo in `04_PRASSI_STUDIO/` con una riga descrittiva
3. **Sezione 11 — Aggiornamenti**: segnalare qualsiasi novità normativa o giurisprudenziale emersa nel caso

Con il tempo, le schede diventano il **patrimonio conoscitivo** dello studio — la parte che nessun database esterno può replicare.

---

## Nota per Claude

Quando ricevi un incarico su un reato presente in questa cartella:
1. Leggi prima la scheda corrispondente
2. Verifica se esistono fonti collegate in `02_GIURISPRUDENZA/cassazione_penale/per_reato/`
3. Consulta le Rassegne Massimario per gli orientamenti recenti
4. Integra con la sezione "Prassi dello studio" per calibrare la strategia difensiva sul distretto
