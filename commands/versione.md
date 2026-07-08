---
description: Mostra la versione installata del Kit Penalista Italiano e verifica se su GitHub esiste una versione piu recente
---
La versione installata di questo plugin e la **3.5.1** (luglio 2026), con 9 skill: strategia, atti, scadenze, cautelare, giurisprudenza, esecuzione, archivio, inizia, verifica.

Esegui questi passi nell'ordine:

1. **Comunica la versione installata** (3.5.1) all'utente.

2. **Verifica la versione pubblicata su GitHub**: scarica `https://raw.githubusercontent.com/Synthos-Logic/penalista-italia/main/.claude-plugin/plugin.json` (con web fetch oppure `curl -s` da shell) e leggi il campo `version`.
   - Se il fetch fallisce (offline, restrizioni di rete): dillo esplicitamente e salta al punto 4. Non dedurre nulla sulla versione remota.

3. **Confronta le versioni** (confronto semantico: 3.10.0 > 3.9.0):
   - **Uguali** → conferma: "Sei aggiornato all'ultima versione."
   - **Remota piu recente** → AVVISA con chiarezza: il kit installato e rimasto indietro. Spiega che esiste un problema noto dell'app Claude per cui la sincronizzazione automatica del marketplace puo bloccarsi in silenzio (il client dice "aggiornato" anche quando non lo e), e fornisci la **procedura di sblocco garantita**:
     1. Impostazioni → Plugin → sezione marketplace (Directory → Plugin → Personale);
     2. sul chip del marketplace `penalista-italia` clicca **···** → **Rimuovi** (rimuove solo il catalogo: fascicoli e Knowledge Base nella cartella dello studio NON vengono toccati);
     3. clicca **+** e ri-aggiungi il marketplace con l'URL `Synthos-Logic/penalista-italia`;
     4. reinstalla il plugin Penalista Italia: arrivera l'ultima versione;
     5. riavvia l'app e apri una conversazione nuova.
     Suggerisci anche di consultare il CHANGELOG (`https://github.com/Synthos-Logic/penalista-italia/blob/main/CHANGELOG.md`) per sapere cosa e cambiato.

4. **Verifica le skill attive**: controlla quali skill `penalista-*` risultano effettivamente disponibili in questa sessione e segnala eventuali differenze rispetto all'elenco delle 9.
