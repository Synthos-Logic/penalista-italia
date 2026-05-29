# Changelog — Penalista Italia

Tutte le modifiche rilevanti al plugin sono documentate in questo file.
Formato basato su [Keep a Changelog](https://keepachangelog.com/it/1.0.0/).

---

## [1.1.0] — 2026-05-29

### Aggiunto
- 8 slash commands: `/strategia`, `/atti`, `/scadenze`, `/cautelare`, `/prescrizione`, `/fascicolo`, `/versione`, `/aiuto`
- Comando `/prescrizione` con calcolo guidato doppio regime ante/post Bonafede
- Comando `/fascicolo` per creazione automatica fascicolo nel sistema di memoria wikilinks
- Comando `/aiuto` con riferimento completo e esempi d'uso pratici

---

## [1.0.0] — 2026-05-29

### Prima release pubblica

#### Aggiunto
- Skill `penalista-strategia`: analisi difensiva strutturata in 10 sezioni per capo di imputazione o CNR
- Skill `penalista-atti`: redazione di tutti i principali atti processuali penali con formule corrette
- Skill `penalista-scadenze`: calcolo preciso di ogni termine processuale con ragionamento esplicito
- Skill `penalista-cautelare`: workflow completo per misure cautelari personali (riesame, revoca, termini di fase, scarcerazione d'urgenza)
- Knowledge base procedurale: processo penale italiano completo, Riforma Cartabia, CEDU, D.Lgs. 231/2001
- Sistema di memoria a wikilinks per gestione del contesto per fascicolo
- Configurazione personalizzabile: nome avvocato, foro, tribunale, iscrizione Cassazionisti

#### Copertura procedurale
- Indagini preliminari → udienza preliminare → dibattimento → impugnazioni → Cassazione
- Riti speciali: abbreviato, patteggiamento, messa alla prova, direttissimo, immediato
- Misure cautelari personali e reali
- Nullità e inutilizzabilità processuali (artt. 177–191 c.p.p.)
- Intercettazioni e captatore informatico
- Investigazioni difensive (artt. 391-bis ss. c.p.p.)
- Improcedibilità ex art. 344-bis c.p.p. (Riforma Cartabia)
- Esecuzione penale e misure alternative alla detenzione
- Tenuità del fatto ex art. 131-bis c.p. (post Riforma Cartabia)

---

## Roadmap

### [1.2.0] — prossima release
- Integrazione ricerca giurisprudenziale Cassazione penale
- Skill `penalista-esecuzione` per diritto penitenziario e Tribunale di Sorveglianza
- Screenshot guida installazione
