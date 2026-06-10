# Installazione assistita delle skill — istruzioni per Claude

> **Per l'utente:** non devi leggere questo file. Apri Cowork, seleziona la cartella `Penale-Italia` e incolla questo messaggio a Claude:
>
> ```
> Installa le skill del kit Penalista Italia seguendo il file INSTALLAZIONE_ASSISTITA.md; se il file non è nella cartella selezionata, scaricalo da https://raw.githubusercontent.com/Synthos-Logic/penalista-italia/main/INSTALLAZIONE_ASSISTITA.md e segui le sue istruzioni.
> ```
>
> Claude ti presenterà le 8 skill come schede con il pulsante **"Salva skill"**: clicca il pulsante su ciascuna, e l'installazione è fatta. Niente Terminale, niente cartelle nascoste. Il messaggio funziona anche se la tua cartella è di una versione precedente del kit.

---

## Istruzioni per Claude (eseguire alla lettera)

Sei in una sessione Cowork con la cartella `Penale-Italia` selezionata. L'utente è un avvocato, non un tecnico: niente gergo, niente percorsi di file, niente spiegazioni sull'architettura.

### Cosa NON fare (errori noti)

- **NON copiare le cartelle skill in `~/.claude/skills`** — quel percorso vale solo per Claude Code (CLI), l'app desktop non lo legge.
- **NON copiare/duplicare le cartelle skill dentro la cartella di lavoro** — non installa nulla, crea solo confusione.
- **NON dire all'utente di usare il Terminale.**

### Procedura corretta

0-bis. **Controllo versioni precedenti (utenti del progetto pilota).** Guarda le skill e i plugin disponibili nella tua sessione: se vedi il **plugin "Penalista Italia"** (skill con prefisso `penalista-italia:`) o vecchie skill `penalista-*` standalone, avverti l'utente PRIMA di procedere: *"Ha installato una versione precedente del kit. Prima di salvare le nuove skill: Personalizza → Plugin → disinstalli 'Penalista Italia', e in Personalizza → Skills elimini le skill penalista-* esistenti. Poi mi scriva 'fatto' e proseguiamo."* Senza questa pulizia le versioni vecchie continuano a rispondere al posto delle nuove.

0. **Se la cartella selezionata non contiene le 8 skill aggiornate** (perché l'utente ha una versione precedente del kit, o nessun kit): scarica le skill direttamente dal repository. Elenca i file di ogni skill con l'API GitHub (`https://api.github.com/repos/Synthos-Logic/penalista-italia/contents/skills/<nome-skill>`) e scarica ciascun file dal corrispondente URL raw (`https://raw.githubusercontent.com/Synthos-Logic/penalista-italia/main/skills/<nome-skill>/...`), ricostruendo le cartelle in una posizione temporanea. Poi prosegui normalmente dal punto 2. Suggerisci comunque all'utente, a fine installazione, di scaricare il kit completo (ZIP da GitHub) per avere Knowledge Base e documentazione aggiornate.

1. Individua le cartelle skill in `skills/` (sono 8: `penalista-inizia`, `penalista-strategia`, `penalista-atti`, `penalista-scadenze`, `penalista-cautelare`, `penalista-giurisprudenza`, `penalista-esecuzione`, `penalista-verifica`). Verifica che ognuna contenga `SKILL.md`.

2. Per ciascuna cartella, crea un archivio ZIP **con la cartella della skill come radice dell'archivio** (non i file sciolti, non una sottocartella in più) e **rinominalo con estensione `.skill`**. Nota operativa: crea gli archivi in una cartella temporanea (`/tmp`) e poi copiali nella cartella di output — la scrittura diretta di zip nelle cartelle montate può fallire. Esempio:
   ```bash
   cd /tmp && rm -rf skillpack && mkdir skillpack && cd skillpack
   for s in penalista-inizia penalista-strategia penalista-atti penalista-scadenze penalista-cautelare penalista-giurisprudenza penalista-esecuzione penalista-verifica; do
     cp -r "[cartella Penale-Italia]/skills/$s" .
     zip -qr "$s.skill" "$s" -x "*.DS_Store"
   done
   cp *.skill [cartella outputs di lavoro]/
   ```

3. Presenta all'utente gli 8 file `.skill` con lo strumento di presentazione file (le schede mostreranno il pulsante **"Salva skill"**).

4. Di' all'utente, in tono semplice: *"Clicchi 'Salva skill' su ciascuna delle 8 schede qui sopra. Quando ha finito, mi scriva 'fatto' e verifichiamo insieme."*

5. Alla conferma, suggerisci di controllare in **Personalizza → Skills** che le 8 skill risultino attive (interruttore acceso). Se una non compare, ripresenta solo quella.

6. Chiudi proponendo il primo passo operativo: *"Ora scriva 'Iniziamo' e la accompagno ad aprire il suo primo fascicolo."*

### Requisiti tecnici da rispettare nella creazione degli archivi

- Il nome della cartella DEVE coincidere con il campo `name:` del relativo `SKILL.md` (è già così nel kit — non rinominare nulla).
- Radice dell'archivio = cartella della skill (struttura: `penalista-atti.skill → penalista-atti/SKILL.md`).
- Escludere file di sistema (`.DS_Store`, `Thumbs.db`).
- Includere le sottocartelle `references/` dove presenti.
