# Guida all'Installazione — Penalista Italia

Questa guida accompagna passo per passo nell'installazione del plugin **Penalista Italia** su Claude Cowork Desktop.

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

Per permettere a Claude di compilare correttamente le intestazioni di ogni atto (nome, foro, tribunale), devi inserire i tuoi dati in un file di configurazione.

**Come trovare il file:**

Dopo l'installazione del plugin, il file si trova nella cartella di Claude Cowork sul tuo computer:

- **Mac:** `~/.claude/plugins/penalista-italia/CLAUDE.md`
  *(apri Finder → Vai alla cartella... → incolla il percorso)*
- **Windows:** `%USERPROFILE%\.claude\plugins\penalista-italia\CLAUDE.md`

Apri il file con qualsiasi editor di testo (TextEdit su Mac, Blocco Note su Windows) e compila i campi:

```
AVVOCATO:          Avv. Mario Rossi
FORO:              Foro di Milano
N. ISCRIZIONE:     12345
TRIBUNALE:         Tribunale Ordinario di Milano
CASSAZIONISTA:     NO
```

Salva il file. Da quel momento Claude userà questi dati in tutte le intestazioni degli atti.

> **Nota:** questo file è locale sul tuo computer — non viene mai pubblicato online.

---

## Passo 7 — Attiva sincronizzazione automatica

Per ricevere aggiornamenti del plugin senza doverlo reinstallare manualmente:

**Personalizza** → **Sfoglia plugin** → **Personale** → clicca **…** accanto a *penalista-italia* → attiva **Sincronizza automaticamente**

Da quel momento, ogni aggiornamento pubblicato su GitHub viene scaricato automaticamente da Cowork.

---

## Passo 8 — Verifica

Apri una nuova conversazione e scrivi `/penalista-italia:aiuto` — vedrai la guida completa con tutti i comandi disponibili.

---

## Utilizzo rapido

| Comando | Funzione |
|---|---|
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
| I dati non compaiono negli atti | Completa la configurazione ⚙️ con nome, foro e tribunale |

---

## Supporto

[github.com/Synthos-Logic/penalista-italia/issues](https://github.com/Synthos-Logic/penalista-italia/issues)

[← Torna al README](../README.md)
