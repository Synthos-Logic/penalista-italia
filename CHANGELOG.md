# Changelog — Penalista Italia

## [2.2.1] — 2026-05-31

### Fix critico
- `penalista-italia/.claude-plugin/plugin.json`: versione aggiornata da 1.2.0 a 2.2.0 — questo era il file che Cowork legge per determinare la versione installata; senza questo fix il plugin appariva sempre alla versione precedente anche dopo reinstallazione
- `docs/INSTALLAZIONE.md` Passo 6: ripristinata la configurazione via pulsante ⚙️ Personalizza (la UI nativa esiste e funziona — il `userConfig` con i 5 campi era già presente nel plugin.json)

---


## [2.2.0] — 2026-05-31

### Aggiunto
- Comando `/penalista-italia:configura` — setup guidato conversazionale dei dati studio (nome, foro, iscrizione, tribunale, cassazionista); Claude raccoglie i dati via chat e salva tutto automaticamente, senza che luutente debba trovare o modificare file nascosti

### Migliorato
- `docs/INSTALLAZIONE.md` Passo 6: sostituito il percorso a file nascosto con un singolo comando `/configura`
- Aggiunto `/configura` come primo comando nella tabella di utilizzo rapido
- Aggiornato Problemi comuni: rimosso riferimento a icona ⚙️ inesistente

---



## [2.1.0] — 2026-05-31

### Aggiunto
- `knowledge-base/06_SCHEDE_REATO/` — 13 schede operative per i reati più diffusi: Truffa, Furto/Rapina/Estorsione, Appropriazione indebita, Riciclaggio/Autoriciclaggio, Maltrattamenti/Stalking, Omicidio/Lesioni stradali, Reati tributari D.Lgs. 74/2000, Corruzione/Peculato/Concussione, Bancarotta fraudolenta, False comunicazioni sociali, Reati informatici, Stupefacenti, Criminalità organizzata
- `knowledge-base/00_META/GERARCHIA_FONTI.md` — regole per pesare le fonti giuridiche
- `knowledge-base/00_META/REGISTRO_DOCUMENTI.md` — indice completo del corpus

### Nessuna modifica alle skill esistenti
---



## [1.2.0] — 2026-05-29

### Aggiunto
- Skill `penalista-giurisprudenza`: ricerca e organizzazione della giurisprudenza penale per la difesa — mappa delle sezioni Cassazione, principali orientamenti per area, contrasti giurisprudenziali utili per la rimessione alle SS.UU., giurisprudenza CEDU, integrazione wikilinks
- Skill `penalista-esecuzione`: diritto penitenziario e esecuzione penale — misure alternative (affidamento, domiciliari, semilibertà), liberazione anticipata e condizionale, permessi, reclami sulle condizioni di detenzione, regime 41-bis, calcolo pena residua e requisiti
- Comandi `/penalista-italia:giurisprudenza` e `/penalista-italia:esecuzione`
- Cartella `docs/images/installazione/` predisposta per gli screenshot della guida

---

## [1.1.0] — 2026-05-29
- 8 slash commands: `/strategia`, `/atti`, `/scadenze`, `/cautelare`, `/prescrizione`, `/fascicolo`, `/versione`, `/aiuto`

## [1.0.0] — 2026-05-29
- Prima release pubblica con 4 skill core
