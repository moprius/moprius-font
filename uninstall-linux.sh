#!/usr/bin/env bash
set -euo pipefail
DEST="${XDG_DATA_HOME:-$HOME/.local/share}/fonts/Moprius"
rm -rf "$DEST"
fc-cache -f
printf 'Removed Moprius fonts from %s
' "$DEST"
