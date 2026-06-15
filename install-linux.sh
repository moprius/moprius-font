#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${XDG_DATA_HOME:-$HOME/.local/share}/fonts/Moprius"
mkdir -p "$DEST"
cp "$ROOT"/fonts/ttf/*.ttf "$DEST"/
cp "$ROOT"/fonts/otf/*.otf "$DEST"/
fc-cache -f
printf 'Installed 12 Moprius fonts in %s
' "$DEST"
