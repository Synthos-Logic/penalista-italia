# PROTOCOLLO DI GROUNDING — quote-then-claim
*Fonte unica di verità per l'ancoraggio documentale. Citato da CLAUDE.md e dalle skill.*

## Principio
**Ancora o astieniti.** Si afferma un contenuto documentale (in primis una massima o un
principio giurisprudenziale) **solo** se lo si è letto in una fonte indicizzata. In assenza,
si dichiara "non presente in KB": non si cita a memoria, non si ricostruisce un numero.

## Le due zone consultabili
1. **GLOBALE** — `KNOWLEDGE_BASE/_INDICE/` (INDICE.md + REGISTRO_FONTI.md): fonti valide in
   ogni fascicolo (massimari, sentenze, dottrina, note dello studio).
2. **FASCICOLO** — `FASCICOLI/<caso>/_INDICE/`: materiale di causa, consultabile **solo**
   dentro quel fascicolo. Non usare il materiale di un fascicolo per un altro.

Il **REGISTRO_FONTI.md** di ciascuna zona elenca *tutte e sole* le fonti ammesse.
**Ciò che non è nel registro/indice NON è nella KB.**

## Procedura vincolante (per ogni citazione che dovrebbe essere in KB)
1. **Cerca nell'indice.** Concetto → indice strutturale di `INDICE.md` o `grep` sul `.md`.
   Sentenza → `grep` del numero **Rv** o della parte nel registro citazionale di `INDICE.md`.
   Quando si lavora su un caso, cerca sia nella zona GLOBALE sia nel `_INDICE` del fascicolo.
2. **Apri e leggi.** Vai al file `.md` indicato, al marcatore `<!-- pag. N -->`.
3. **Incolla la massima testuale**, con riferimento `(fonte, p. N)`. Si afferma solo il letto.
4. **Se non c'è → astieniti.** Scrivi "non presente in KB"; eventualmente segnala dove
   l'avvocato può verificarla (Italgiure/DeJure/Portale del Massimario). Mai inventare.

## Tipo-fonte e gerarchia (consultabile ≠ stessa autorità)
Ogni fonte porta un **tipo** (massimario | sentenza | dottrina | nota-studio | atto-causa).
Cita con l'etichetta corretta ("secondo la nota interna dello studio…" ≠ "Cass. SU n. …")
e pesa secondo `GERARCHIA_FONTI.md`. Una nota di studio non vale come una Sezioni Unite.

## Aggiungere una fonte (per l'avvocato)
1. Metti il PDF nella zona giusta: globale → in `KNOWLEDGE_BASE/…`; di causa → in `FASCICOLI/<caso>/…`.
2. Lancia: `python3 skills/penalista-archivio/scripts/aggiorna_indice.py <dir_zona>`.
3. L'indice e il registro si rigenerano: da quel momento la fonte è consultabile e citabile.
   (PDF scansionati: prima OCR — lo strumento si ferma e lo segnala.)

## Limite
Tutto il materiale è di lavoro: la verifica finale sulla fonte ufficiale resta del difensore.
