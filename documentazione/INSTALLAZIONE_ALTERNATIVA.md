# Installazione alternativa — senza marketplace

*Questa è la via di riserva. Il metodo consigliato (più semplice e con aggiornamenti automatici) è il plugin: [guida principale](../docs/INSTALLAZIONE.md).*

Usala solo se non puoi o non vuoi usare il marketplace GitHub.

> ⚠️ **Una via o l'altra, mai entrambe.** Se installi le skill con questo metodo, NON installare anche il plugin (e viceversa): avresti due copie delle stesse skill e risposte imprevedibili.

## Installazione

1. Scarica lo ZIP del kit (**Code → Download ZIP** su GitHub), decomprimi, rinomina la cartella in `Penale-Italia`.
2. Claude Desktop → Cowork → **Seleziona cartella** → `Penale-Italia`.
3. Incolla questo messaggio a Claude:

```
Installa le skill del kit Penalista Italia seguendo il file INSTALLAZIONE_ASSISTITA.md; se il file non è nella cartella selezionata, scaricalo da https://raw.githubusercontent.com/Synthos-Logic/penalista-italia/main/INSTALLAZIONE_ASSISTITA.md e segui le sue istruzioni.
```

4. Claude ti presenta 8 schede con il pulsante **"Salva skill"**: un clic su ciascuna. Verifica in **Personalizza → Skills**.
5. Scrivi **"Iniziamo"**.

## Aggiornamento

Con questo metodo gli aggiornamenti NON sono automatici. Quando esce una nuova versione: scarica il nuovo ZIP, trascinalo dentro la cartella `Penale-Italia` senza decomprimerlo e incolla a Claude il messaggio di aggiornamento che trovi nel [README](../README.md#aggiornamenti). Claude aggiorna tutto preservando fascicoli e dati studio, e ti ripresenta le skill cambiate.

## Solo per chi usa Claude Code (terminale)

Gli script `claude-code/install.sh` (Mac: `bash claude-code/install.sh`) e `claude-code/install.bat` (Windows) copiano le skill in `~/.claude/skills`. Questo percorso vale **solo** per Claude Code da terminale — l'app desktop non lo legge.
