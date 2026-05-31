# Template Cartella Documentale — Studio Legale Penalista

Questa è la struttura consigliata per organizzare i fascicoli processuali.
Il tuo amico può personalizzarla in base alle esigenze del suo studio.

## Struttura tipo per singolo fascicolo

```
FASCICOLI/
└── [ANNO]_[COGNOME_CLIENTE]_[REATO_SINTETICO]/
    │
    ├── 00_SCHEDA_FASCICOLO/
    │   ├── scheda_sintetica.md          ← generata da penalista-atti
    │   ├── timeline_fatti.md            ← generata da penalista-atti
    │   ├── matrice_prove.xlsx           ← generata da penalista-atti
    │   └── prospetto_scadenze.md        ← generata da penalista-scadenze
    │
    ├── 01_ATTI_ACCUSA/
    │   ├── informativa/
    │   ├── ordinanza_cautelare/
    │   ├── decreto_rinvio_giudizio/
    │   ├── richieste_PM/
    │   └── perizie_accusa/
    │
    ├── 02_ATTI_DIFESA/
    │   ├── memorie/                     ← generati con penalista-memorie
    │   ├── istanze/
    │   ├── impugnazioni/                ← generati con penalista-impugnazioni
    │   ├── liste_testi/                 ← generati con penalista-memorie
    │   └── consulenze_tecniche_difesa/
    │
    ├── 03_PROVVEDIMENTI_GIUDICE/
    │   ├── ordinanze/
    │   ├── sentenze/
    │   └── decreti/
    │
    ├── 04_INTERCETTAZIONI/
    │   ├── decreti_autorizzativi/
    │   ├── brogliacci/
    │   ├── trascrizioni/
    │   └── note_analisi.md              ← generata da penalista-atti
    │
    ├── 05_GIURISPRUDENZA/
    │   ├── sentenze_favorevoli/         ← raccolte con penalista-giurisprudenza
    │   ├── sentenze_sfavorevoli/
    │   └── rassegna_tematica.md         ← generata da penalista-giurisprudenza
    │
    ├── 06_PARERI/
    │   └── parere_pro_veritate.md       ← generato con penalista-pareri
    │
    ├── 07_CORRISPONDENZA/
    │   ├── con_cliente/
    │   ├── con_controparte/
    │   └── con_autorita/
    │
    ├── 08_VERBALI_UDIENZA/
    │   └── [data]_verbale.pdf
    │
    └── 09_NOTE_INTERNE/
        ├── strategia_difensiva.md
        ├── appunti_riunione_cliente.md
        └── todo_fascicolo.md
```

## Come collegare le skill al documentale

Ogni skill del kit è progettata per produrre output che si inseriscono
naturalmente in questa struttura:

| Skill | Output → Cartella |
|---|---|
| penalista-atti | Scheda, timeline, matrice → `00_SCHEDA_FASCICOLO/` |
| penalista-memorie | Memorie, note, liste testi → `02_ATTI_DIFESA/memorie/` e `liste_testi/` |
| penalista-impugnazioni | Appelli, riesami, ricorsi → `02_ATTI_DIFESA/impugnazioni/` |
| penalista-giurisprudenza | Rassegne, schede sentenze → `05_GIURISPRUDENZA/` |
| penalista-pareri | Pareri pro veritate → `06_PARERI/` |
| penalista-scadenze | Prospetto scadenze → `00_SCHEDA_FASCICOLO/` |

## Personalizzazione

Il difensore dovrebbe adattare questa struttura a:

1. **Il suo gestionale.** Se usa un software di gestione studio (es. Cliens, Consolle Avvocato,
   Anthesis, Lextel), la cartella può rispecchiare la struttura del gestionale.

2. **Le sue aree di specializzazione.** Un penalista che fa molto diritto penale d'impresa
   potrebbe aggiungere cartelle specifiche per documentazione societaria, flussi finanziari, ecc.

3. **Il volume di fascicoli.** Per studi con molti fascicoli, aggiungere un livello
   per materia: `FASCICOLI/CAUTELARE/`, `FASCICOLI/DIBATTIMENTO/`, `FASCICOLI/ESECUZIONE/`.

4. **La collaborazione.** Se lo studio ha più avvocati, aggiungere cartelle per note
   del collaboratore e versioning degli atti.
