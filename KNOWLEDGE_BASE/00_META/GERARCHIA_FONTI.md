# Gerarchia delle Fonti — Regole per l'AI

Questo file definisce come Claude deve pesare le fonti presenti nella Knowledge Base.
**È il documento più importante dell'intera KB: va letto prima di qualsiasi ragionamento giuridico.**

---

## Regola fondamentale

Non tutte le fonti hanno lo stesso valore giuridico. Un orientamento del Tribunale di Roma non vale quanto una sentenza delle Sezioni Unite. L'AI deve sempre indicare la fonte usata e il suo livello gerarchico, e segnalare quando fonti di livello diverso sono in contrasto.

---

## Gerarchia in ordine decrescente di autorità

### LIVELLO 1 — Autorità assoluta (vincolante)

**Sezioni Unite Penali della Cassazione**
- Enunciano principi di diritto vincolanti per tutte le sezioni semplici e per i giudici di merito (art. 618 c.p.p.)
- In caso di contrasto con sezioni semplici, prevalgono sempre
- Rimettere alle Sezioni Unite è l'unica via per discostarsi dal principio enunciato
- Cartella: `02_GIURISPRUDENZA/sezioni_unite_penali/`

**Corte Costituzionale — sentenze ablative** ← *archivio completo in questa KB (tipo `corte-costituzionale`)*
- Una norma penale dichiarata illegittima cessa di esistere nell'ordinamento
- Qualsiasi ragionamento su quella norma (prescrizione, elementi costitutivi, pena) deve tenere conto della declaratoria di illegittimità
- L'AI deve segnalare immediatamente se la norma discussa è stata oggetto di pronuncia della Corte Costituzionale
- Cartella: `02_GIURISPRUDENZA/CONSULTA/` (archivio completo 1956→oggi, registro dedicato `INDICE_CONSULTA.md`)

### LIVELLO 2 — Alta autorità (orientamento dominante)

**Cassazione Penale — sezioni semplici**
- Orientamento tendenzialmente seguito dai giudici di merito
- In presenza di contrasto tra sezioni, indicare entrambi gli orientamenti senza sceglierne uno
- Se l'orientamento è superato da pronuncia successiva, indicare la sentenza più recente
- Cartelle: `02_GIURISPRUDENZA/cassazione_penale/per_reato/` e `per_istituto/`

**Rassegne dell'Ufficio del Massimario della Cassazione** ← *fonti presenti in questa KB*
- Sintesi ufficiale degli orientamenti delle sezioni penali (e civili) per anno
- Già strutturate per tema: ottimali per identificare l'orientamento prevalente
- Non sostituiscono le sentenze originali, ma le rappresentano fedelmente
- Citarle come: "Rassegna Massimario [Penale/Civile] [anno], p. [pagina]"

**Pronunce segnalate dall'Ufficio del Massimario** (tipo `massimario-segnalate`) ← *aggiornamento settimanale in questa KB*
- Massime ufficiali delle pronunce di rilievo nomofilattico, pubblicate dalla Corte stessa (3–5/settimana)
- Se la pronuncia è delle **Sezioni Unite** → pesa come LIVELLO 1
- Non hanno ancora numero Rv: citare per numero/anno + scheda + PDF ufficiale linkato
- Le **questioni SU pendenti** NON sono precedenti: solo segnalazione del contrasto rimesso
- Cartella: `02_GIURISPRUDENZA/SEGNALATE/` · registro: sezione 3 dell'INDICE

**Corte Costituzionale — sentenze interpretative / additive**
- Non abrogano la norma, ma ne fissano l'interpretazione costituzionalmente orientata
- Hanno forza di orientamento vincolante per l'interpretazione

### LIVELLO 3 — Autorità sovranazionale (applicazione diretta)

**Corte EDU (Strasburgo)**
- I principi CEDU si applicano direttamente nell'ordinamento italiano quando la norma interna è incompatibile (art. 117 Cost.)
- Particolarmente rilevanti: art. 6 CEDU (equo processo), art. 7 (legalità), art. 8 (vita privata), art. 3 (trattamento inumano)
- Le sentenze contro l'Italia hanno forza vincolante diretta; le sentenze contro altri Stati hanno valore di precedente
- Cartella: `02_GIURISPRUDENZA/cedu/`

**CGUE (Lussemburgo)**
- Rilevante per reati con dimensione eurounitaria (frodi IVA, reati doganali, riciclaggio transnazionale)
- Il diritto UE prevale sul diritto interno in caso di conflitto (primauté)

### LIVELLO 4 — Dottrina

**Commentari e monografie**
- Non creano diritto, ma orientano l'interpretazione e forniscono argomenti difensivi
- In caso di contrasto dottrina/giurisprudenza, prevalenza alla giurisprudenza
- Utili per: costruire argomenti originali, identificare questioni aperte, formulare eccezioni

**Riviste specializzate**
- Aggiornamento su orientamenti recenti e questioni aperte
- Segnalare sempre l'autore e la pubblicazione

### LIVELLO 5 — Giurisprudenza di merito

**Corti d'Appello e Tribunali**
- Descrivono la prassi applicativa locale, non vincolante
- Utili per: valutare l'orientamento del giudice specifico, calibrare la strategia difensiva
- Non citarle come "diritto vigente" ma come "prassi del distretto"

---

## Regole operative per l'AI

### Quando citi una fonte della KB:
1. Indica titolo esatto, anno, e pagina (es: "Rassegna Massimario Penale 2024, p. 47")
2. Indica il livello gerarchico della fonte
3. Se la fonte è una rassegna, segnala che la sentenza originale va verificata su banca dati

### Quando non trovi la fonte nella KB:
1. Indica che la sentenza non è nella KB locale
2. Fornisci il ragionamento giuridico attingendo alla conoscenza generale
3. **Marca ogni sentenza citata a memoria con [VERIFICARE]**
4. Non inventare mai numeri di sentenze

### In caso di contrasto tra fonti:
1. Esponi entrambi gli orientamenti con le rispettive fonti
2. Indica quale è più recente e quale è di livello gerarchico superiore
3. Non scegliere per il difensore: la scelta strategica spetta all'avvocato
4. Segnala se la questione è stata rimessa alle Sezioni Unite

### Successione di leggi penali nel tempo:
- Verifica SEMPRE se la norma applicabile è quella vigente al momento del fatto o quella successiva
- In caso di successione di leggi penali, applica la norma più favorevole (art. 2 c.p.)
- Segnala se il fatto è stato commesso prima o dopo una modifica normativa rilevante

### Presunzione di innocenza nel linguaggio:
- L'indagato/imputato non è "colpevole": usa sempre "indagato", "imputato", "persona sottoposta ad indagini"
- "L'informativa riferisce che..." ≠ "È provato che..."
- Le accuse sono "contestazioni", non "fatti accertati"

---

## Nota sull'uso della Cassazione Civile in contesto penale

Le rassegne della Cassazione Civile presenti in questa KB (Massimari 2023 e 2024) sono rilevanti per:
- **Parte civile nel processo penale**: disciplina del risarcimento del danno ex art. 185 c.p.
- **CEDU e diritti fondamentali**: la Cassazione civile elabora ricca giurisprudenza su art. 6, 7, 8 CEDU applicabile anche in penale
- **Ne bis in idem** (art. 50 Carta di Nizza): trattato nel Vol. I Civile 2024, cap. I
- **Stranieri e diritti**: rilevante per imputati non italiani
- **Procedimenti speciali**: opposizione a decreto ingiuntivo, possessorio — utili in procedimenti penali con risvolti patrimoniali

Citarle come: "Cass. Civ., [sezione], [data], n. [numero]" o "Rassegna Massimario Civile [anno], Vol. [I/II/III], p. [pagina]"
