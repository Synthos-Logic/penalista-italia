# Dati dello Studio — Penalista Italia

Questo file contiene le informazioni personalizzate del tuo studio.
**Leggilo ogni volta che generi un atto processuale** per usare i dati corretti nelle intestazioni.

---

## ⚙️ CONFIGURA QUI I DATI DEL TUO STUDIO

```
AVVOCATO:          [Inserisci: es. Avv. Marco Bianchi]
FORO:              [Inserisci: es. Foro di Roma]
N. ISCRIZIONE:     [Inserisci: es. 12345]
TRIBUNALE:         [Inserisci: es. Tribunale Ordinario di Roma]
CASSAZIONISTA:     [Inserisci: SI oppure NO]
STUDIO:            [Inserisci: nome dello studio, facoltativo]
INDIRIZZO:         [Inserisci: indirizzo studio, facoltativo]
EMAIL:             [Inserisci: email studio, facoltativo]
PEC:               [Inserisci: PEC, facoltativa]
```

---

## Istruzioni per la configurazione

1. Apri questo file (`penalista-italia/CLAUDE.md`) con qualsiasi editor di testo
2. Sostituisci ogni `[Inserisci: ...]` con i tuoi dati reali
3. Salva il file
4. Da quel momento Claude userà queste informazioni in tutti gli atti

**Esempio compilato:**
```
AVVOCATO:          Avv. Marco Bianchi
FORO:              Foro di Roma
N. ISCRIZIONE:     12345
TRIBUNALE:         Tribunale Ordinario di Roma
CASSAZIONISTA:     NO
STUDIO:            Studio Legale Bianchi
INDIRIZZO:         Via del Corso 100, 00186 Roma
EMAIL:             studio@avvbianchi.it
PEC:               m.bianchi@ordineavvocati.roma.it
```

---

## Come Claude usa questi dati

Quando redigi atti con `/penalista-italia:atti` o con la skill `penalista-atti`, Claude legge automaticamente i dati qui sopra e:
- Compila l'intestazione dell'atto con nome, foro e numero iscrizione
- Indica il tribunale corretto nelle conclusioni
- Firma gli atti con la formula corretta in base all'iscrizione (cassazionista o no)

---

## Note operative

- Questo file è **locale** — non viene mai pushato su GitHub (è nella struttura del plugin installato sul tuo computer)
- Se reinstalli il plugin, dovrai ricompilare i dati
- Puoi avere profili diversi per diversi studi o collaboratori: duplica il file e rinominalo
