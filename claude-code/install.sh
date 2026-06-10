#!/bin/bash
# ============================================================
# ⚠️  SOLO PER UTENTI CLAUDE CODE (CLI). L'app desktop Claude/Cowork NON legge ~/.claude/skills:
# per Cowork usare l'installazione assistita (vedi INSTALLAZIONE_ASSISTITA.md nella radice del kit).
# Penalista Italia - Installazione skill su Mac
# Trascina questo file nel Terminale e premi Invio
# ============================================================

SKILLS_DIR="$HOME/.claude/skills"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo ""
echo "  Kit Penalista Italia - Installazione skill"
echo "  ============================================"
echo ""

# Crea la cartella skills se non esiste
if [ ! -d "$SKILLS_DIR" ]; then
    mkdir -p "$SKILLS_DIR"
    echo "  Cartella ~/.claude/skills creata."
else
    echo "  Cartella ~/.claude/skills trovata."
fi
echo ""

SKILLS=("penalista-strategia" "penalista-atti" "penalista-scadenze" "penalista-cautelare" "penalista-giurisprudenza" "penalista-esecuzione" "penalista-inizia" "penalista-verifica")

OK=0; ERR=0
for skill in "${SKILLS[@]}"; do
    src="$SCRIPT_DIR/skills/$skill"
    if [ -d "$src" ]; then
        cp -r "$src" "$SKILLS_DIR/"
        echo "  ok  $skill"
        ((OK++))
    else
        echo "  ERRORE: $skill non trovata"
        ((ERR++))
    fi
done

echo ""
if [ $ERR -eq 0 ]; then
    echo "  Fatto! $OK skill installate."
    echo "  Riavvia Claude Desktop per attivarle."
else
    echo "  Completato con $ERR errori."
    echo "  Verifica che la cartella skills/ sia presente in Penale-Italia/."
fi
echo ""