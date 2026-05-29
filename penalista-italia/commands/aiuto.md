---
description: "Mostra il riferimento completo dei comandi, delle skill e degli esempi d'uso del plugin Penalista Italia."
---

Sei invocato tramite `/penalista-italia:aiuto`. Mostra il riferimento completo del kit.

---

## Penalista Italia — Guida Rapida

### Comandi

| Comando | Cosa fa |
|---|---|
| `/penalista-italia:strategia` | Analisi difensiva completa di un capo di imputazione o caso penale |
| `/penalista-italia:atti` | Redige un atto processuale penale (memoria, appello, riesame, patteggiamento...) |
| `/penalista-italia:scadenze` | Calcola qualsiasi termine processuale con ragionamento esplicito |
| `/penalista-italia:cautelare` | Gestisce l'intero ciclo delle misure cautelari personali |
| `/penalista-italia:prescrizione` | Calcola la prescrizione con doppio regime ante/post Bonafede |
| `/penalista-italia:fascicolo` | Crea un nuovo fascicolo nel sistema di memoria wikilinks |
| `/penalista-italia:versione` | Mostra versione installata e stato del sistema |
| `/penalista-italia:aiuto` | Mostra questa guida |

### Skill automatiche

Le skill si attivano anche senza comandi slash — basta descrivere cosa serve:

| Cosa dici | Skill attivata |
|---|---|
| "come mi difendo da questa accusa di corruzione?" | `penalista-strategia` |
| "scrivi l'istanza di riesame per Rossi" | `penalista-atti` + `penalista-cautelare` |
| "quando scade il termine per l'appello?" | `penalista-scadenze` |
| "il cliente è in custodia dal 10 marzo" | `penalista-cautelare` |
| "calcola la prescrizione per truffa del 2018" | `penalista-scadenze` |

### Esempi d'uso

```
/penalista-italia:strategia
Il mio cliente è accusato di corruzione propria art. 318 c.p. — fatto del 2022, fase indagini.
Capo di imputazione: [incolla testo]

/penalista-italia:atti
Scrivi l'istanza di riesame per Mario Rossi, in custodia cautelare dal 20 maggio 2026,
Tribunale di Milano, reato: bancarotta fraudolenta art. 216 L.F.

/penalista-italia:scadenze
Avviso di deposito sentenza d'appello notificato il 15 maggio 2026.
Quando scade il termine per il ricorso in Cassazione?

/penalista-italia:prescrizione
Reato: omessa dichiarazione art. 5 D.Lgs. 74/2000. Fatto: giugno 2018.
Regime ante o post Bonafede? Quando matura la prescrizione?

/penalista-italia:fascicolo
Cliente: Giovanni Bianchi — art. 73 DPR 309/1990 (fatto non lieve)
Procura di Roma, R.G.N.R. 5678/2025 — fase: udienza preliminare fissata per 10/07/2026
```

### Sistema di memoria

Il kit usa file `.md` collegati da `[[wikilinks]]` per gestire il contesto per fascicolo e ridurre il consumo di token. Vedi `SISTEMA_MEMORIA.md` nella tua cartella di lavoro per le regole operative.

### Supporto

Segnalazioni e richieste: [github.com/Synthos-Logic/penalista-italia/issues](https://github.com/Synthos-Logic/penalista-italia/issues)

---

$ARGUMENTS
