# Installazione del Kit Penalista Italia — guida passo passo

*Tempo richiesto: 5 minuti. Non serve alcuna competenza tecnica.*

Due passi: prima il **plugin**, poi la **struttura di lavoro**. In fondo alla pagina trovi una nota che spiega che cosa fa ciascuno.

---

## Passo 1 — Installa il plugin

### 1. Apri Personalizza

In Claude Desktop, clicca l'icona **Personalizza** in basso a sinistra. Si apre la schermata "Personalizza Claude".

![Personalizza Claude](images/installazione/01-personalizza.png)

### 2. Aggiungi il marketplace

Clicca il **+** in alto → **Crea plugin** → **Aggiungi marketplace**.

![Crea plugin → Aggiungi marketplace](images/installazione/02-crea-plugin.png)

Si apre la finestra "Aggiungi marketplace":

![Aggiungi marketplace](images/installazione/03-aggiungi-marketplace-vuoto.png)

Nel campo URL incolla esattamente:

```
Synthos-Logic/penalista-italia
```

e clicca **Sincronizza**.

![URL del marketplace](images/installazione/04-aggiungi-marketplace-url.png)

### 3. Installa il plugin

Nella Directory (Plugin → **Personale**) compare la scheda **Penalista Italia** di Synthos Logic. Clicca il **+** sulla scheda.

![La scheda del plugin](images/installazione/05-directory-plugin.png)

Comparirà la conferma "Penalista italia è installato e pronto all'uso":

![Installato](images/installazione/06-installato.png)

### 4. Controlla la scheda del plugin

Cliccando sul plugin vedi versione, autore e le competenze installate:

![Dettaglio del plugin](images/installazione/07-dettaglio-installato.png)

> La versione mostrata deve corrispondere all'[ultima release](https://github.com/Synthos-Logic/penalista-italia/releases).

### 5. Attiva gli aggiornamenti automatici (consigliato)

Sempre in Plugin → Personale, accanto al nome `penalista-italia` ci sono **tre puntini (···)**. Cliccali e attiva **"Sincronizza automaticamente"**. Da quel momento le nuove versioni delle skill arrivano da sole.

> Se compare una richiesta di autorizzazione GitHub ("Concedi"), è la verifica di accesso al repository: serve un account GitHub gratuito. Se non vuoi crearlo, nessun problema — dallo stesso menu puoi usare **"Verifica aggiornamenti"** quando vuoi, oppure vedi l'[installazione alternativa](../documentazione/INSTALLAZIONE_ALTERNATIVA.md).

### 6. Verifica

Apri una nuova conversazione e scrivi `/penalista-italia:versione`. Deve rispondere con la versione del kit e l'elenco delle 8 skill.

---

## Passo 2 — Installa la struttura di lavoro

### 1. Scarica lo ZIP

Su [github.com/Synthos-Logic/penalista-italia](https://github.com/Synthos-Logic/penalista-italia) clicca **Code → Download ZIP**.

### 2. Decomprimi e rinomina

Decomprimi lo ZIP e rinomina la cartella in `Penale-Italia`. Mettila dove preferisci (es. Documenti).

### 3. Collegala a Cowork

Claude Desktop → **Cowork** → **Seleziona cartella** → scegli `Penale-Italia`.

---

## Fatto — il primo avvio

Ecco come si presenta il kit al lavoro — qui la skill delle misure cautelari raccoglie i dati del fascicolo:

![Il kit al lavoro: fascicolo cautelare](images/esempio-cautelare.png)


Nella conversazione Cowork con la cartella selezionata, scrivi:

```
Iniziamo
```

Il kit si presenta, raccoglie i dati del tuo studio (nome, foro, tribunale — li chiede una volta sola) e apre con te il primo fascicolo su un caso vero. Quindici minuti.

---

> **Che cosa hai appena installato?** Il Passo 1 monta il **motore**: le competenze del kit (le 8 skill). Il Passo 2 monta l'**archivio**: la cartella dove il kit conserva i tuoi fascicoli, le scadenze e i dati del tuo studio. Servono entrambi: il motore senza archivio risponde alle domande, ma non conserva il lavoro sui tuoi casi.

---

## Aggiornare il kit

Quando esce una nuova versione (la trovi tra le [release](https://github.com/Synthos-Logic/penalista-italia/releases)), il plugin si aggiorna così:

### 1. Apri la Directory dei plugin

**Impostazioni** → **Plugin** → clicca **Sfoglia**. Si apre la Directory: vai su **Plugin** → **Personale**.

### 2. Sincronizza il catalogo

Accanto al nome del marketplace `penalista-italia` clicca i **tre puntini (···)** → **"Verifica aggiornamenti"**. Il "Commit sincronizzato" mostrato nel menu deve cambiare: è il segno che il catalogo si è allineato a GitHub.

### 3. Applica e verifica

Riavvia l'app, apri una **conversazione nuova** e scrivi `/penalista-italia:versione`: il comando confronta da solo la versione installata con l'ultima pubblicata su GitHub e ti dice se sei aggiornato.

### Se il kit resta fermo (dice "aggiornato" ma non lo è)

Esiste un problema noto dell'app Claude: la sincronizzazione del marketplace può bloccarsi in silenzio e il client continua a rispondere "aggiornato" restando fermo a una versione vecchia (`/versione` te lo segnala). La procedura di sblocco è garantita e **non tocca i tuoi fascicoli né la Knowledge Base** — rimuove solo il catalogo:

1. **Impostazioni** → **Plugin** → **Sfoglia** → **Plugin** → **Personale**;
2. sul chip `penalista-italia` clicca **···** → **Rimuovi**;
3. clicca il **+** → **Aggiungi marketplace** → incolla `Synthos-Logic/penalista-italia` → **Sincronizza**;
4. reinstalla il plugin (**+** sulla scheda Penalista Italia): arriva l'ultima versione;
5. riavvia l'app, apri una conversazione nuova e verifica con `/penalista-italia:versione`.

---

## Problemi comuni

**"Questo repository non è un marketplace"** — Controlla di aver scritto esattamente `Synthos-Logic/penalista-italia` (con il trattino).

**Claude parla di "6 skill" o risponde con versioni vecchie** — Sul computer ci sono residui di versioni precedenti. Pulizia: **Personalizza → Skills** → elimina le eventuali skill `penalista-*` caricate singolarmente (il plugin le sostituisce tutte). Poi apri una conversazione nuova.

**Ho installato un aggiornamento ma non lo vedo** — Gli aggiornamenti valgono per le conversazioni nuove: chiudi quella aperta e aprine un'altra.

**Il pulsante "Aggiorna" sulla scheda del plugin è grigio** — È normale: prima va sincronizzato il catalogo. Usa i **tre puntini (···)** accanto al nome del marketplace → **"Verifica aggiornamenti"**.

**Il kit dice "aggiornato" ma `/versione` segnala una versione vecchia** — È il blocco silenzioso della sincronizzazione (problema noto dell'app). Segui la procedura di sblocco nella sezione [Aggiornare il kit](#aggiornare-il-kit): rimuovi e ri-aggiungi il marketplace. Fascicoli e Knowledge Base non vengono toccati.

**Non voglio usare GitHub** — [Installazione alternativa senza marketplace](../documentazione/INSTALLAZIONE_ALTERNATIVA.md).

---

*Assistenza: apri una segnalazione su [GitHub](https://github.com/Synthos-Logic/penalista-italia/issues) oppure scrivi a Synthos Logic.*
