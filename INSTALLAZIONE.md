# Installazione Skills — Progetto Penale Italia

## Passaggio manuale necessario

Le skill di Cowork vivono in una cartella specifica del tuo computer che non è scrivibile
dall'interno di una sessione Cowork. Devi copiare le 6 cartelle **a mano** — ci vuole un minuto.

## Istruzioni

### 1. Trova la cartella sorgente

Le 6 skill si trovano dentro la cartella del progetto Penale Italia che hai scaricato:

```
Penale-Italia/skills/
├── penalista-atti/
├── penalista-memorie/
├── penalista-impugnazioni/
├── penalista-giurisprudenza/
├── penalista-pareri/
└── penalista-scadenze/
```

### 2. Trova la cartella destinazione

**Su Mac:**
1. Apri Finder
2. Premi `Cmd + Shift + G`
3. Incolla: `~/.claude/skills`
4. Premi Invio

**Su Windows:**
1. Apri Esplora File
2. Nella barra indirizzi, incolla: `%USERPROFILE%\.claude\skills`
3. Premi Invio

> Se la cartella `skills` non esiste, creala dentro `.claude`.
> Su Mac, premi `Cmd + Shift + .` nel Finder per vedere le cartelle nascoste.

### 3. Copia

Seleziona le 6 cartelle (`penalista-atti`, `penalista-memorie`, ecc.) e copiale
nella cartella `~/.claude/skills/`.

Il risultato deve essere:

```
~/.claude/skills/
├── penalista-atti/
│   └── SKILL.md
├── penalista-memorie/
│   └── SKILL.md
├── penalista-impugnazioni/
│   └── SKILL.md
├── penalista-giurisprudenza/
│   └── SKILL.md
├── penalista-pareri/
│   └── SKILL.md
├── penalista-scadenze/
│   └── SKILL.md
└── ... (altre skill che avevi già, come 231-expert, ecc.)
```

### 4. Verifica

1. Chiudi Claude Desktop (completamente, non solo la finestra)
2. Riaprilo
3. Vai in modalità Cowork
4. Scrivi: "Elencami le skill disponibili"
5. Dovresti vedere le 6 skill penalista nella lista

### 5. Collegare la cartella del progetto

Per lavorare sui file del progetto (fascicolo simulato, documenti, ecc.):
1. In Cowork, clicca "Seleziona cartella"
2. Naviga alla cartella `Penale-Italia` sul tuo computer
3. Selezionala

Da quel momento Claude può leggere e scrivere direttamente nei fascicoli.

## Aggiornamento skill

Se ricevi versioni aggiornate delle skill, semplicemente sostituisci i file SKILL.md
nelle rispettive cartelle. Non serve reinstallare nulla.

## Disinstallazione

Per rimuovere una skill, cancella la sua cartella da `~/.claude/skills/`.
