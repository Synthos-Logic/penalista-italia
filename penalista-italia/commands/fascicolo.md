---
description: "Crea un nuovo fascicolo nel sistema di memoria wikilinks dello studio. Genera il file .md con frontmatter strutturato, sezioni standard e wikilinks, aggiorna INDEX.md e SCADENZIARIO.md. Usa quando si apre un nuovo procedimento o si vuole iniziare a tracciare digitalmente un caso esistente."
---

Sei invocato tramite `/penalista-italia:fascicolo`. Crea un nuovo fascicolo nel sistema di memoria [[SISTEMA_MEMORIA]].

Se l'utente ha fornito i dati del caso negli argomenti, usali. Altrimenti chiedi in un'unica domanda: nome e cognome del cliente, numero R.G.N.R. (se noto), reato contestato con articolo, autorità procedente, fase attuale, eventuali scadenze già note.

Crea il file fascicolo con naming convention `cognome-anno-reato.md` nella cartella `penalista-atti/` usando il formato standard:

```markdown
---
cliente: [Nome Cognome]
rgnr: [numero]
reato: [articolo e rubrica]
fase: [fase attuale]
giudice: [se noto]
pm: [se noto]
stato: [descrizione breve]
prossima_scadenza: [YYYY-MM-DD se nota]
---

# Fascicolo [Cognome] — [Reato] [Anno]

## Fatti essenziali
[da completare]

## Capi di imputazione
[da completare]

## Strategia difensiva
[da definire — usare /strategia per l'analisi completa]

## Eccezioni processuali rilevate
[da verificare]

## Scadenze del fascicolo
[da completare]

## Documenti prodotti
[vuoto — aggiornare man mano]

## Note e aggiornamenti
*[data apertura]*: fascicolo aperto.
```

Aggiorna `INDEX.md` aggiungendo il fascicolo alla lista dei fascicoli attivi. Se ci sono scadenze note, aggiungerle a [[SCADENZIARIO]].

$ARGUMENTS
