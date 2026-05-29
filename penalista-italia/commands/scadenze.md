---
description: "Calcola qualsiasi termine processuale penale con ragionamento esplicito passo per passo: termini di impugnazione (appello, Cassazione), riesame cautelare, termini di fase della custodia cautelare, prescrizione (ante/post Bonafede), improcedibilità Cartabia art. 344-bis c.p.p., udienza di convalida. Applica automaticamente art. 172 c.p.p. e sospensione feriale."
---

Sei invocato tramite `/penalista-italia:scadenze`. Attiva la skill `penalista-scadenze` e calcola il termine richiesto.

Se l'utente ha fornito il tipo di termine e la data di riferimento negli argomenti, procedi direttamente al calcolo. Altrimenti chiedi solo le informazioni strettamente necessarie per quel calcolo specifico.

Mostra sempre il ragionamento completo: norma applicata → dies a quo → eventuali sospensioni → dies ad quem → livello di urgenza.

Se il termine è CRITICO (già scaduto o entro 48 ore), segnalarlo immediatamente in evidenza e indicare l'azione urgente da intraprendere.

Aggiorna [[SCADENZIARIO]] con il termine calcolato.

$ARGUMENTS
