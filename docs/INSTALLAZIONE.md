# Guida all'Installazione — Penalista Italia

Questa guida ti accompagna passo per passo nell'installazione del plugin **Penalista Italia** su Claude Cowork Desktop.

---

## Prerequisiti

- [Claude Cowork Desktop](https://claude.ai) installato e aggiornato all'ultima versione
- Account Claude attivo (Piano Pro o superiore)
- Connessione internet attiva

---

## Passo 1 — Apri Personalizza

In Claude Cowork, clicca su **Personalizza** nella barra laterale sinistra.

---

## Passo 2 — Accedi ai Plugin Personali

Nella sezione **Plugin personali**, clicca sul pulsante **+** e seleziona **Aggiungi marketplace da GitHub**.

---

## Passo 3 — Inserisci il Repository

Nel campo che appare, digita esattamente:

```
Synthos-Logic/penalista-italia
```

Clicca **Sincronizza**.

---

## Passo 4 — Installa il Plugin

Dopo la sincronizzazione, comparirà la scheda **Penalista Italia**. Clicca su **Installa**.

---

## Passo 5 — Configura i Dati dello Studio

Clicca sull'icona della **ruota dentata ⚙️** accanto al plugin installato. Compila i campi:

| Campo | Descrizione | Esempio |
|---|---|---|
| Nome e cognome | Il tuo nome completo per le intestazioni degli atti | Mario Rossi |
| Foro di iscrizione | Il tuo Ordine di appartenenza | Milano |
| Numero iscrizione | Numero all'Albo degli Avvocati | 12345 |
| Tribunale principale | Il tribunale dove lavori più frequentemente | Tribunale di Milano |
| Cassazionista | Sei iscritto all'Albo Speciale? | SI / NO |

---

## Passo 6 — Seleziona la Cartella di Lavoro

Al primo avvio, Cowork ti chiederà di selezionare una cartella sul tuo computer per i file dello studio. Scegli la cartella dove vuoi archiviare i fascicoli digitali.

La struttura verrà creata automaticamente:
```
📁 [cartella scelta]/
├── 📁 penalista-atti/
├── 📁 penalista-giurisprudenza/
├── 📁 penalista-impugnazioni/
├── 📁 penalista-memorie/
├── 📁 penalista-pareri/
└── 📁 penalista-scadenze/
    └── SCADENZIARIO.md
```

---

## Passo 7 — Attiva la Sincronizzazione Automatica

Per ricevere gli aggiornamenti automaticamente: **Personalizza** → **Sfoglia plugin** → **Personali** → clicca sui tre puntini (**…**) accanto a *penalista-italia* → attiva **Sincronizza automaticamente**.

---

## Passo 8 — Verifica l'Installazione

Apri una nuova conversazione e scrivi:

```
Analizza questo capo di imputazione: [incolla il testo]
```

Se il plugin è installato correttamente, vedrai l'analisi difensiva strutturata in 10 sezioni.

---

## Utilizzo delle skill

Le skill si attivano automaticamente in base al contesto. Non è necessario usare comandi speciali.

**Esempi di utilizzo:**

```
"Come mi difendo da questa accusa di corruzione?"
→ si attiva penalista-strategia — analisi difensiva completa

"Scrivi l'istanza di riesame per il sig. Bianchi, in custodia dal 15 marzo"
→ si attivano penalista-cautelare + penalista-atti

"Quando scade la prescrizione per una truffa commessa il 3 maggio 2019?"
→ si attiva penalista-scadenze — calcolo con ragionamento completo

"Prepara i motivi di appello avverso la sentenza del Tribunale di Roma"
→ si attiva penalista-atti — guida alla redazione dell'atto di appello
```

---

## Sistema di memoria — Gestione fascicoli

Il kit usa un sistema di file `.md` collegati da **wikilinks** `[[]]` per mantenere il contesto tra sessioni e ridurre il consumo di token.

**Come iniziare un fascicolo:**

1. Nella cartella `penalista-atti/`, crea un file `cognome-anno-reato.md`
2. Usa il formato standard indicato nel file `SISTEMA_MEMORIA.md`
3. Ogni sessione, indica il fascicolo attivo — il kit caricherà solo il contesto necessario

---

## Problemi comuni

| Problema | Soluzione |
|---|---|
| "Sync failed" | Verifica di aver digitato esattamente `Synthos-Logic/penalista-italia` |
| Le skill non si attivano | Verifica che il plugin sia attivo (toggle blu nella pagina del plugin) |
| I dati dello studio non compaiono negli atti | Verifica di aver compilato tutti i campi nella configurazione (⚙️) |
| Il SCADENZIARIO non si aggiorna | Aprire il file `penalista-scadenze/SCADENZIARIO.md` e chiedere al kit di aggiornarlo |

---

## Supporto

Per segnalazioni e richieste: [github.com/Synthos-Logic/penalista-italia/issues](https://github.com/Synthos-Logic/penalista-italia/issues)

---

[← Torna al README](../README.md)
