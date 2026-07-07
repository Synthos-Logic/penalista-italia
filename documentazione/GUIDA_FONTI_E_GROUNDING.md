# Guida — Le fonti del kit e la garanzia anti-allucinazione
*Per l'avvocato che usa il Kit Penalista Italia. Linguaggio operativo, niente tecnicismi.*

## In una frase
Il kit cita **solo** ciò che è stato caricato e indicizzato come fonte. Se una massima
non è tra le fonti, il sistema **lo dice** ("non presente in KB") invece di inventarla.
Questa è la garanzia: nel dubbio si astiene, non si inventa.

## Perché serve
Un assistente che "ricorda" sentenze a memoria, prima o poi ne inventa una. In ambito
penale è inaccettabile. Per questo il kit non cita dalla memoria: cita da un **indice**
costruito sui documenti reali che tu gli dai. È il protocollo *quote-then-claim* —
"prima trova nel testo, poi afferma" — descritto in
`KNOWLEDGE_BASE/00_META/PROTOCOLLO_GROUNDING.md`.

## Le due zone delle fonti
- **Zona globale** — `KNOWLEDGE_BASE/`: fonti valide per **tutti** i casi
  (massimari, sentenze, dottrina, tue note di studio).
- **Zona fascicolo** — `FASCICOLI/<caso>/`: il materiale del **singolo** caso
  (atti, perizie, ordinanze). Consultabile **solo** dentro quel fascicolo: il materiale
  di un cliente non entra mai nell'analisi di un altro.

Ogni zona ha un **REGISTRO_FONTI.md** che elenca *tutte e sole* le fonti ammesse.
Quello che non è nel registro, per il kit non esiste.

## Come aggiungo una fonte (3 passi)
1. **Metti il file** (PDF) nella cartella della zona giusta:
   una fonte generale → dentro `KNOWLEDGE_BASE/…`; un atto di causa → dentro `FASCICOLI/<tuo caso>/…`.
2. **Dillo all'assistente**, per esempio: *"aggiungi questo PDF alla knowledge base"* /
   *"indicizza i documenti del fascicolo Rossi"*. (Tecnicamente lancia
   `aggiorna_indice.py` sulla cartella della zona.)
3. **Fatto**: l'indice e il registro si aggiornano. Da quel momento la fonte è
   consultabile e citabile, con pagina e testo esatti.

> I documenti **scansionati** (immagini) vanno prima passati per un OCR: il kit se ne
> accorge e te lo segnala, non li indicizza "alla cieca".

## La banca dati delle pronunce segnalate (si aggiorna da sola)

Oltre alle fonti che aggiungi tu, il kit ha una banca dati che **si alimenta da sola**:
le pronunce penali che l'Ufficio del Massimario segnala ogni settimana sul sito della
Corte di Cassazione (le 3-5 di rilievo nomofilattico, comprese le Sezioni Unite e le
questioni rimesse). Una pipeline automatica le trasforma in schede — massima ufficiale,
esito in sintesi, **link al PDF autentico della Corte** — e le pubblica ogni lunedì.

Per averle (o aggiornarle) nella tua Knowledge Base, di' a Claude: **"aggiorna la banca dati"**.
Non serve alcun account: il comando scarica le schede in `02_GIURISPRUDENZA/SEGNALATE/`
e le indicizza. Da quel momento sono citabili come ogni altra fonte del registro, con una
particolarità: non hanno ancora il numero Rv (arriva col massimario annuale), quindi si
citano per numero/anno — e ogni citazione porta con sé il link al PDF ufficiale, che puoi
aprire e verificare con un clic.

Attenzione: la cartella `SEGNALATE/` appartiene alla pipeline — le modifiche manuali
vengono sovrascritte all'aggiornamento successivo. Le tue note vanno nelle altre cartelle.

## Cosa vuol dire "non presente in KB"
Significa che la sentenza/principio che serve non è tra le fonti caricate. Non è un errore:
è il sistema che ti avvisa di **non avere un appiglio documentale**. Da lì puoi (a) caricare
la fonte e re-indicizzare, oppure (b) verificarla tu sulla banca dati ufficiale
(Italgiure / DeJure / Portale del Massimario).

## Consultabile non vuol dire "vale come una Cassazione"
Ogni fonte porta un **tipo**: massimario, sentenza, dottrina, nota-studio, atto-causa.
Il kit cita con l'etichetta giusta ("secondo la nota interna dello studio…" ≠
"Cass., Sez. Un., …") e rispetta la gerarchia delle fonti
(`KNOWLEDGE_BASE/00_META/GERARCHIA_FONTI.md`). Aggiungere una tua nota la rende
*consultabile*, non le dà l'autorità di una Sezioni Unite.

## Promemoria
Tutto ciò che il kit produce è una **bozza di lavoro**. La verifica finale delle
citazioni sulla fonte ufficiale, prima del deposito, resta sempre del difensore.
