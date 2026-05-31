# Progetto: Penale Italia
*Versione 2.1 — 8 maggio 2026*

## Contesto del progetto

Questo è il progetto "Penale Italia" — un ambiente di lavoro completo per la pratica penalistica nell'ordinamento italiano, costruito su Cowork.

Il progetto è composto da quattro macro-aree:

1. **Skills** (`skills/`) — 6 skill specializzate per il penalista italiano
2. **Documentazione** (`documentazione/`) — mappa del kit, guida for dummies, template documentale
3. **Fascicolo simulato** (`FASCICOLO_SIMULATO/`) — caso di studio completo per test e formazione
4. **Knowledge Base** (`KNOWLEDGE_BASE/`) — corpus documentale di fonti giuridiche ufficiali

## Le 6 skill del Kit Penalista

| Skill | Cosa fa | Trigger principali |
|---|---|---|
| `penalista-atti` | Analisi e schedatura atti processuali | informativa, CNR, ordinanza, intercettazioni, perizia |
| `penalista-memorie` | Redazione memorie difensive e note udienza | memoria 415-bis, note udienza, lista testi, conclusioni |
| `penalista-impugnazioni` | Appello, riesame, ricorso Cassazione | appello, riesame, ricorso, opposizione decreto penale |
| `penalista-giurisprudenza` | Ricerca e analisi giurisprudenziale | giurisprudenza, sentenza, Cassazione, Sezioni Unite, CEDU |
| `penalista-pareri` | Pareri pro veritate e consulenze | parere, risk assessment, qualificazione giuridica |
| `penalista-scadenze` | Calcolo termini processuali | prescrizione, termini custodia, scadenze, sospensione feriale |

## Caso simulato: Mario Rossi

Un fascicolo completo per testare tutte le skill. Il caso riguarda Mario Rossi, amministratore unico di Edil Rossi SRL, accusato di:
- **Truffa aggravata** ai danni del Comune di Monterotondo (art. 640 co. 2 n. 1 c.p.) — €420.000
- **Fatture per operazioni inesistenti** (art. 8 D.Lgs. 74/2000) — 7 fatture per €215.000
- **Autoriciclaggio** (art. 648-ter.1 c.p.) — €178.500

Il fascicolo contiene 4 vizi procedurali nascosti che le skill dovrebbero aiutare a individuare.
Dettagli nel file: `FASCICOLO_SIMULATO/2025_ROSSI_Truffa_aggravata/00_SCHEDA_FASCICOLO/LEGGIMI_CASO_SIMULATO.md`

## Regole operative per Claude

Quando lavori su questo progetto:

1. **Mai inventare giurisprudenza.** Ogni sentenza citata a memoria va marcata [VERIFICARE].
2. **Distingui fatto da valutazione.** "L'informativa riferisce che..." ≠ "È accaduto che..."
3. **Segnala sempre la fonte.** Ogni affermazione → atto specifico + pagina.
4. **Ragiona in termini di utilizzabilità processuale.** Informazione vera ma inutilizzabile: distinzione cruciale.
5. **Presunzione di innocenza** nel linguaggio: "indagato/imputato", mai "colpevole".
6. **Termini conservativi.** Nel dubbio, indica la scadenza più breve (più sfavorevole per chi deve rispettarla).
7. **Tutti gli atti prodotti sono BOZZE.** Richiedono sempre revisione del difensore prima del deposito.
8. **Usa la Knowledge Base.** Prima di citare giurisprudenza a memoria, verifica se è presente in `KNOWLEDGE_BASE/`. Le rassegne ufficiali dell'Ufficio del Massimario (2023-2024, penale e civile) sono la fonte primaria da consultare. Leggi sempre `KNOWLEDGE_BASE/00_META/GERARCHIA_FONTI.md` per capire come pesare le fonti.
9. **Rispetta la gerarchia delle fonti.** Sezioni Unite > sezioni semplici Cass. > Corte Costituzionale (ablative) > CEDU > dottrina > giurisprudenza di merito. Dettagli in `KNOWLEDGE_BASE/00_META/GERARCHIA_FONTI.md`.

## Struttura cartelle del progetto

```
Penale-Italia/
├── CLAUDE.md                          ← questo file (istruzioni progetto) v2.0
├── INSTALLAZIONE.md                   ← guida per installare le skill
├── skills/                            ← le 6 skill (da copiare in ~/.claude/skills/)
│   ├── penalista-atti/SKILL.md
│   ├── penalista-memorie/SKILL.md
│   ├── penalista-impugnazioni/SKILL.md
│   ├── penalista-giurisprudenza/SKILL.md
│   ├── penalista-pareri/SKILL.md
│   └── penalista-scadenze/SKILL.md
├── documentazione/
│   ├── MAPPA_KIT.html                 ← mappa visuale v2.0 + guida for dummies
│   ├── documentale-template/
│   │   └── STRUTTURA_FASCICOLO.md     ← template struttura cartelle
│   └── output_demo/                   ← demo output generati dalle skill
├── FASCICOLI/                         ← fascicoli reali dello studio (da popolare)
├── FASCICOLO_SIMULATO/
│   └── 2025_ROSSI_Truffa_aggravata/   ← caso completo di test
│       ├── 00_SCHEDA_FASCICOLO/
│       ├── 01_ATTI_ACCUSA/
│       ├── 02_ATTI_DIFESA/
│       ├── 03_PROVVEDIMENTI_GIUDICE/
│       ├── 04_INTERCETTAZIONI/
│       └── 05_GIURISPRUDENZA/
└── KNOWLEDGE_BASE/                    ← ★ NUOVO v2.0 — corpus fonti ufficiali
    ├── 00_META/
    │   ├── GERARCHIA_FONTI.md         ← regole per pesare le fonti (LEGGERE PRIMA)
    │   └── REGISTRO_DOCUMENTI.md      ← indice completo di tutto il corpus
    ├── 01_NORMATIVA/
    │   ├── codici/
    │   │   ├── codice_penale/
    │   │   ├── codice_procedura_penale/
    │   │   └── normativa_speciale/
    │   │       ├── dlgs_74_2000_reati_tributari/
    │   │       ├── dlgs_231_2001_enti/
    │   │       └── dlgs_159_2011_antimafia/
    │   └── aggiornamenti/
    ├── 02_GIURISPRUDENZA/
    │   ├── sezioni_unite_penali/      ← PRIORITÀ MASSIMA
    │   ├── cassazione_penale/
    │   │   ├── per_reato/             (truffa, reati tributari, autoriciclaggio...)
    │   │   ├── per_istituto/          (cautelari, intercettazioni, prescrizione...)
    │   │   └── rassegne_massimario/   ★ 2023 Vol.I+II · 2024 Vol.Unico [9 PDF]
    │   ├── cassazione_civile/
    │   │   ├── rassegne_annuali/      ★ 2023 Vol.I+II+III · 2024 Vol.I+II+III [6 PDF]
    │   │   └── temi_rilevanti_penale/
    │   ├── corte_costituzionale/
    │   ├── cedu/
    │   └── merito/
    ├── 03_DOTTRINA/
    ├── 04_PRASSI_STUDIO/              ← fascicoli reali dello studio (da popolare)
    ├── 05_AGGIORNAMENTO/
    └── 06_SCHEDE_REATO/               ← ★ NUOVO v2.1 — schede operative per reato
        ├── 00_README.md               ← istruzioni e template standard
        ├── A_REATI_PATRIMONIO/        (Truffa, Furto, Rapina, Estorsione, Appropriazione, Riciclaggio)
        ├── B_REATI_PERSONA/           (Maltrattamenti, Stalking, Omicidio/Lesioni stradali)
        ├── C_REATI_TRIBUTARI/         (D.Lgs. 74/2000 — artt. 2, 4, 5, 8, 11...)
        ├── D_REATI_PA/                (Corruzione, Peculato, Concussione, Turbata libertà incanti)
        ├── E_REATI_SOCIETARI_FALLIMENTARI/ (Bancarotta, False comunicazioni sociali)
        ├── F_REATI_INFORMATICI/       (Accesso abusivo, Frode informatica, Revenge porn)
        ├── G_STUPEFACENTI/            (D.P.R. 309/1990 — artt. 73, 74)
        └── H_CRIMINALITA_ORGANIZZATA/ (Associazione per delinquere, 416-bis)
```

## Cronologia del progetto

- **Sessione 1** (8 aprile 2026): Creazione kit base 6 skill, guida for dummies, template documentale, caso simulato Mario Rossi con fascicolo completo (7 documenti).
- **Sessione 2** (8 maggio 2026): Avvio test con avvocato pilota. Aggiunta Knowledge Base con corpus ufficiale Corte di Cassazione — Ufficio del Massimario: 9 volumi (Massimario Penale 2023-2024 + Massimario Civile 2023-2024). Creazione GERARCHIA_FONTI.md e REGISTRO_DOCUMENTI.md. Analisi quadro normativo AI Act + Legge 132/2025 + privacy GDPR/Anthropic per product strategy. Creazione 06_SCHEDE_REATO/ con 10 schede operative sui reati più diffusi negli studi penali italiani (8 macro-categorie). Aggiornamento MAPPA_KIT v2.1 e CLAUDE.md v2.1.

## Prossimi sviluppi possibili

- Simulazione completa: redazione difesa (memoria 415-bis, riesame, parere) sul caso Rossi
- Aggiunta Massimario Penale e Civile per anni 2021-2022 (completare la serie storica)
- Aggiunta normativa: testi coordinati c.p., c.p.p., D.Lgs. 74/2000, D.Lgs. 231/2001
- Aggiunta giurisprudenza Sezioni Unite su temi chiave dello studio
- Aggiunta sentenze CEDU vs Italia più rilevanti
- Nuove skill: indagini difensive, esecuzione penale, patrocinio a spese dello Stato
- Integrazione con skill 231-expert per casi di responsabilità dell'ente
- Skill `penalista-kb` dedicata alla ricerca nel corpus KB locale
- Plugin dedicato "Penalista Italiano" per distribuzione commerciale
