@echo off
REM Launches the Jekyll dev server for local testing.
REM Uses port 4001 because port 4000 is often held by a PuTTY SSH tunnel on this machine.
cd /d "%~dp0"
bundle exec jekyll serve --host 127.0.0.1 --port 4001 --livereload
pause
