# /penalista-italia:configura — Setup dati dello studio

Questo comando configura il kit con i dati del tuo studio.
Viene eseguito una sola volta all'installazione (o quando vuoi aggiornare i tuoi dati).

## Istruzioni per Claude

Quando l'avvocato usa questo comando:

1. Saluta brevemente e spiega che raccoglierai i dati necessari per compilare le intestazioni degli atti.

2. Chiedi **tutti i dati in un'unica domanda**, in modo che l'avvocato possa rispondere in un colpo solo:

---

**Messaggio da mostrare all'avvocato:**

Perfetto, configuro il kit con i dati del tuo studio. Rispondi pure in forma libera — estraggo io i valori.

Ho bisogno di:
- **Nome completo** (es. Avv. Mario Rossi)
- **Foro di iscrizione** (es. Foro di Milano)
- **Numero iscrizione all'Albo** (es. 12345)
- **Tribunale dove lavori principalmente** (es. Tribunale di Milano)
- **Sei iscritto all'Albo Speciale dei Cassazionisti?** (Sì / No)
- **Nome dello studio** *(facoltativo)*
- **Indirizzo** *(facoltativo)*
- **Email** *(facoltativa)*
- **PEC** *(facoltativa)*

---

3. Dopo che l'avvocato risponde, **estrai i dati** dalla risposta libera e mostra un riepilogo di conferma in questo formato:

```
Ho configurato il kit con questi dati:

AVVOCATO:          Avv. [nome]
FORO:              Foro di [città]
N. ISCRIZIONE:     [numero]
TRIBUNALE:         Tribunale di [città]
CASSAZIONISTA:     [SI / NO]
STUDIO:            [nome studio o —]
INDIRIZZO:         [indirizzo o —]
EMAIL:             [email o —]
PEC:               [pec o —]

È tutto corretto? (Rispondi SÌ per salvare, oppure dimmi cosa cambiare)
```

4. Se l'avvocato conferma con SÌ (o varianti: sì, ok, corretto, perfetto...):

   - Salva i dati nel file `CLAUDE.md` della cartella del plugin con questo contenuto:

```markdown
# Dati dello Studio — Penalista Italia

## Dati configurati

AVVOCATO:          [valore]
FORO:              [valore]
N. ISCRIZIONE:     [valore]
TRIBUNALE:         [valore]
CASSAZIONISTA:     [valore]
STUDIO:            [valore]
INDIRIZZO:         [valore]
EMAIL:             [valore]
PEC:               [valore]

---
*Configurato il: [data]*
*Per aggiornare i dati, usa il comando /penalista-italia:configura*
```

5. Conferma con un messaggio finale, ad esempio:

```
✓ Configurazione salvata. Ora tutti gli atti che genero useranno automaticamente 
i tuoi dati. Puoi iniziare con /penalista-italia:strategia o /penalista-italia:atti.
```

## Note tecniche

- Se `CLAUDE.md` esiste già con dati compilati, mostra i dati attuali e chiedi se l'avvocato vuole aggiornarli.
- Non richiedere i dati facoltativi se l'avvocato non li ha forniti — lascia `—` nel file.
- Il tono deve essere professionale ma diretto — l'avvocato è impegnato.
