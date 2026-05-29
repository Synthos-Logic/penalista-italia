---
description: "Calcola la prescrizione di un reato penale italiano con ragionamento dettagliato. Gestisce automaticamente il doppio regime: ante-Bonafede (fatti prima del 1° gennaio 2020) e post-Bonafede (fatti dal 1° gennaio 2020 in poi), con calcolo di interruzioni, sospensioni e confronto con l'improcedibilità Cartabia (art. 344-bis c.p.p.) se applicabile."
---

Sei invocato tramite `/penalista-italia:prescrizione`. Attiva la skill `penalista-scadenze` — sezione Prescrizione.

Se l'utente ha fornito il reato e la data del fatto negli argomenti, procedi direttamente. Altrimenti chiedi: reato contestato (con norma se nota), data del fatto, fase processuale attuale, eventuali interruzioni già note (interrogatorio, decreto penale, sentenza).

Presenta il calcolo in questo formato:
1. Regime applicabile (ante/post Bonafede) e motivazione
2. Termine base con riferimento al massimo edittale
3. Interruzioni e sospensioni rilevanti con date
4. Data di maturazione stimata
5. Se il procedimento è in fase di impugnazione: confronto con improcedibilità art. 344-bis
6. Valutazione strategica: la prescrizione è uno strumento difensivo percorribile?

Se la prescrizione è già maturata o prossima (< 3 mesi): **SEGNALARE COME PRIORITÀ ASSOLUTA**.

$ARGUMENTS
