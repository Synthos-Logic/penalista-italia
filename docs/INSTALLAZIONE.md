# Guida all'Installazione — Penalista Italia

Questa guida accompagna passo per passo nell'installazione del plugin **Penalista Italia** su Claude Cowork Desktop.

---

## Prima di iniziare — Chat, Cowork o un progetto per cliente?

Se hai appena scoperto Claude, potresti chiederti come organizzarti. Ecco la risposta diretta:

| Situazione | Cosa usare |
|---|---|
| Domanda rapida su un termine o una norma | **Chat normale** — nessun progetto necessario |
| Lavorare su documenti di causa (informative, ordinanze, perizie) | **Cowork** — con la cartella dello studio collegata |
| Gestire più fascicoli nel tempo | **Un unico progetto Cowork per tutto lo studio** |

**La scelta consigliata per chi usa questo plugin seriamente: un unico progetto Cowork per lo studio.**

Dentro quel progetto crei una cartella per ogni fascicolo (es. `2026_ROSSI_Truffa/`, `2026_BIANCHI_Bancarotta/`). Claude distingue i casi grazie alla struttura delle cartelle e al sistema `/fascicolo` — non hai bisogno di aprire un progetto diverso per ogni cliente.

> **Non creare un progetto Cowork separato per ogni cliente.** Perderesti il contesto cross-case e dovresti reinstallare il plugin ogni volta. È l'errore più comune dei nuovi utenti.

I comandi slash (`/strategia`, `/atti`, `/scadenze`...) funzionano in qualsiasi contesto — anche in una chat normale, anche senza documenti allegati. Collegare la cartella dello studio serve solo quando vuoi che Claude legga i PDF dei tuoi fascicoli.

---

## Prerequisiti

- [Claude Cowork Desktop](https://claude.ai) installato e aggiornato all'ultima versione
- Account Claude attivo (Piano Pro o superiore)
- Connessione internet attiva

---

## Passo 1 — Apri Personalizza

In Claude Cowork, clicca su **Personalizza** nella barra laterale sinistra.

![Passo 1 — Personalizza Claude](images/installazione/01-personalizza.png)

---

## Passo 2 — Aggiungi marketplace

Clicca sul pulsante **+** accanto a "Plugin personali", poi seleziona **Crea plugin** → **Aggiungi marketplace**.

![Passo 2 — Aggiungi marketplace](images/installazione/02-crea-plugin.png)

---

## Passo 3 — Inserisci il repository

Nel campo URL digita esattamente:

```
Synthos-Logic/penalista-italia
```

oppure l'URL completo `https://github.com/Synthos-Logic/penalista-italia`, poi clicca **Sincronizza**.

![Passo 3a — Dialog vuoto](images/installazione/03-aggiungi-marketplace-vuoto.png)

![Passo 3b — URL inserito](images/installazione/04-aggiungi-marketplace-url.png)

---

## Passo 4 — Installa il plugin

Dopo la sincronizzazione appare la scheda **Penalista Italia** di Synthos Logic. Clicca sul **+** per installarlo.

![Passo 4 — Installa](images/installazione/05-directory-plugin.png)

---

## Passo 5 — Conferma installazione

Vedrai la notifica **"Penalista Italia è installato e pronto all'uso"** insieme alle skill disponibili.

![Passo 5 — Installato](images/installazione/06-installato.png)

---

## Passo 6 — Configura i dati del tuo studio

Apri una nuova conversazione in Cowork e scrivi:

```
/penalista-italia:configura
```

Claude ti farà alcune domande (nome, foro, tribunale, numero iscrizione) e salverà tutto automaticamente. Nessun file da trovare, nessuna cartella nascosta.

![Passo 6 — Configura](images/installazione/07-dettaglio-installato.png)

---

## Passo 7 — Attiva sincronizzazione automatica

Per ricevere aggiornamenti del plugin senza doverlo reinstallare manualmente:

Quando è disponibile un aggiornamento, comparirà il pulsante **Aggiorna** nella scheda del plugin:

**Personalizza** → **Plugin personali** → clicca su **Penalista Italia** → clicca **Aggiorna**

L'aggiornamento scarica l'ultima versione del plugin con tutti i nuovi comandi e skill.

> Se non vedi ancora il pulsante "Aggiorna" dopo un nuovo rilascio, chiudi e riapri Claude Desktop — Cowork controlla gli aggiornamenti all'avvio.

---

## Passo 8 — Verifica

Apri una nuova conversazione e scrivi `/penalista-italia:aiuto` — vedrai la guida completa con tutti i comandi disponibili.

---

## Utilizzo rapido

| Comando | Funzione |
|---|---|
| `/penalista-italia:configura` | **Prima cosa da fare** — configura nome, foro, tribunale |
| `/penalista-italia:strategia` | Analisi difensiva di un capo di imputazione |
| `/penalista-italia:atti` | Redazione di atti processuali penali |
| `/penalista-italia:scadenze` | Calcolo termini processuali |
| `/penalista-italia:cautelare` | Gestione misure cautelari |
| `/penalista-italia:prescrizione` | Calcolo prescrizione |
| `/penalista-italia:fascicolo` | Crea fascicolo nel sistema memoria |
| `/penalista-italia:aiuto` | Guida completa |

---

## Problemi comuni

| Problema | Soluzione |
|---|---|
| "Sync failed" | Verifica di aver inserito esattamente `Synthos-Logic/penalista-italia` |
| Le skill non si attivano | Verifica che il plugin sia attivo (toggle blu) |
| I dati non compaiono negli atti | Esegui `/penalista-italia:configura` per impostare nome, foro e tribunale |
| Non vedo i nuovi comandi dopo un aggiornamento | Vai in Personalizza → Plugin personali → Penalista Italia → clicca **Aggiorna** |
| Il pulsante Aggiorna non compare | Chiudi e riapri Claude Desktop — controlla gli aggiornamenti all'avvio |

---

## 🔒 Privacy e sicurezza dei dati

> Prima di usare il kit con dati reali di clienti, leggi la pagina dedicata.

**In sintesi:**
- I file fisici restano sul tuo computer — non vengono caricati su nessun server
- Il testo dei documenti che chiedi a Claude di analizzare transita sui server di Anthropic per l'elaborazione (è il meccanismo necessario per far funzionare l'AI)
- La **Legge 132/2025 art. 13** (in vigore dal 10 ottobre 2025) impone di informare il cliente prima di usare strumenti AI nell'ambito del mandato
- Il CNF ha pubblicato uno schema di informativa da consegnare ai clienti

📖 **[Pagina completa Privacy → Wiki](https://github.com/Synthos-Logic/penalista-italia/wiki/Privacy)**


## Supporto

[github.com/Synthos-Logic/penalista-italia/issues](https://github.com/Synthos-Logic/penalista-italia/issues)

[← Torna al README](../README.md)
