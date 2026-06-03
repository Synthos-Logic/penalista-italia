@echo off
rem ============================================================
rem Penalista Italia - Installazione skill su Windows
rem Doppio clic su questo file per avviarlo
rem ============================================================

setlocal EnableDelayedExpansion

set "SKILLS_DIR=%USERPROFILE%\.claude\skills"
set "SCRIPT_DIR=%~dp0"

echo.
echo   Kit Penalista Italia - Installazione skill
echo   ============================================
echo.

rem Crea la cartella skills se non esiste
if not exist "%SKILLS_DIR%" (
    mkdir "%SKILLS_DIR%"
    echo   Cartella .claude\skills creata.
) else (
    echo   Cartella .claude\skills trovata.
)
echo.

set OK=0
set ERR=0

for %%s in (penalista-strategia penalista-atti penalista-scadenze penalista-cautelare penalista-giurisprudenza penalista-esecuzione) do (
    set "SRC=%SCRIPT_DIR%skills\%%s"
    if exist "!SRC!\" (
        xcopy /E /I /Y "!SRC!" "%SKILLS_DIR%\%%s\" > nul
        echo   ok  %%s
        set /a OK+=1
    ) else (
        echo   ERRORE: %%s non trovata
        set /a ERR+=1
    )
)

echo.
if %ERR% EQU 0 (
    echo   Fatto! %OK% skill installate.
    echo   Riavvia Claude Desktop per attivarle.
) else (
    echo   Completato con %ERR% errori.
    echo   Verifica che la cartella skills\ sia presente in Penale-Italia\.
)
echo.
pause