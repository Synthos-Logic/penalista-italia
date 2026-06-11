# Aggiornamento assistito del kit — istruzioni per Claude

> **Per l'utente:** quando esce una nuova versione del kit, NON sostituire la cartella `Penale-Italia` a mano — dentro ci sono i tuoi fascicoli e i dati del tuo studio. Fai così:
>
> 1. Scarica il nuovo ZIP da GitHub (**Code → Download ZIP**)
> 2. Trascina il file ZIP scaricato (senza decomprimerlo) **dentro la cartella `Penale-Italia`**
> 3. In Cowork, incolla questo messaggio a Claude:
>
> ```
> Ho scaricato l'aggiornamento del kit Penalista Italia: eseguilo seguendo AGGIORNAMENTO_ASSISTITO.md; se il file non è nella cartella selezionata, scaricalo da https://raw.githubusercontent.com/Synthos-Logic/penalista-italia/main/AGGIORNAMENTO_ASSISTITO.md e segui le sue istruzioni.
> ```
>
> Claude aggiorna tutto **senza toccare i tuoi fascicoli e i dati del tuo studio**, ti dice cosa è cambiato e, se ci sono skill nuove o aggiornate, te le presenta da installare con un clic.

---

## Istruzioni per Claude (eseguire alla lettera)

### Regola assoluta — COSA NON TOCCARE MAI

- **`FASCICOLI/`** — contiene i fascicoli reali dello studio. Non sovrascrivere, non eliminare, non rinominare nulla al suo interno.
- **La sezione "Dati dello studio" di `CLAUDE.md`** — contiene i dati compilati dall'avvocato.
- **File creati dall'utente** ovunque si trovino (note giurisprudenziali proprie, PDF in `penalista-fonti/`, documenti personali nella Knowledge Base): l'aggiornamento **aggiunge e sostituisce i file del kit, non elimina mai ciò che non riconosce**.

### Procedura

1. **Trova lo ZIP** nella cartella di lavoro (nome tipico: `penalista-italia-main.zip`). Se non c'è, chiedi all'utente di trascinarlo nella cartella `Penale-Italia` e fermati.

2. **Decomprimi in una cartella temporanea** (`/tmp`), non nella cartella di lavoro.

3. **Confronta le versioni**: leggi il `CHANGELOG.md` nuovo e quello attuale. Riassumi all'utente in 3-5 righe cosa cambia, in linguaggio piano. Se le versioni coincidono, dillo e fermati.

4. **Aggiorna i file del kit**, copiando dal nuovo al vecchio:
   - `skills/` (tutte le cartelle)
   - `KNOWLEDGE_BASE/` (solo i file presenti nel nuovo kit — non eliminare i file aggiunti dall'utente)
   - `documentazione/`, `docs/`, `claude-code/`
   - `README.md`, `CHANGELOG.md`, `INSTALLAZIONE_ASSISTITA.md`, `AGGIORNAMENTO_ASSISTITO.md`, `FASCICOLO_SIMULATO/`
   - **`CLAUDE.md`: caso speciale** — se è cambiato nel nuovo kit, applica il nuovo testo MA ricopia dentro la sezione "Dati dello studio" i valori già compilati dall'avvocato. Verifica il risultato prima di salvare.

5. **Elimina lo ZIP** dalla cartella di lavoro (chiedi conferma prima).

6. **Skill nuove o aggiornate**: controlla come sono installate le skill in questa sessione. Se l'utente ha il **plugin** (skill con prefisso `penalista-italia:`), le skill si aggiornano da sole: ricordagli solo di usare ··· → "Verifica aggiornamenti" sul marketplace (Personalizza → Plugin) o di attivare "Sincronizza automaticamente", e di aprire una conversazione nuova. Solo se l'utente usa le skill standalone (senza plugin): identifica dal CHANGELOG quali skill sono nuove o modificate, crea i pacchetti `.skill` (procedura in `INSTALLAZIONE_ASSISTITA.md`) e presentali con il pulsante "Salva skill", avvertendo di eliminare prima le versioni vecchie da Personalizza → Skills.

7. **Verifica finale**: conferma all'utente versione installata (dal CHANGELOG), skill aggiornate, e che fascicoli e dati studio sono intatti — dillo esplicitamente: *"I suoi fascicoli e i dati dello studio non sono stati toccati."*

### Se qualcosa va storto

Non improvvisare rimedi distruttivi. Se un passaggio fallisce, spiega cosa è successo e cosa NON è stato toccato. La regola del kit vale anche qui: nel dubbio, la scelta più conservativa.
