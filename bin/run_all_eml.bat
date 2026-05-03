@echo off
echo Processing all .eml files...

for %%F in (*.eml) do (
    echo ----------------------------------------
    echo Processing: %%F
    python parse_eml.py "%%F"
)

echo Done!
pause
