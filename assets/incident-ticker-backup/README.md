# Incident ticker source backup

This folder contains the canonical animated SVG and the source code needed to regenerate the GIF.

## Contents

- `animated-cyber-incidents-descending.svg` — canonical animated SVG containing all 100 incident records and the descending-year sequence.
- `generate_incident_ticker.py` — Python/Pillow generator that reads the incident titles and the three analytical fields directly from the SVG and rebuilds the animated GIF.
- `incident-ticker.gif` — generated output; create it locally by running the generator.

## Regenerate the GIF

Requirements: Python 3.10+ and Pillow.

```bash
python -m pip install Pillow
python generate_incident_ticker.py
```

The script creates `incident-ticker.gif` in this directory. It displays each incident in sequence with Attack Vector, Impact and Significance, using a dark background, green terminal-style typography, and a bottom progress bar.

## Design / animation settings

- Canvas: 1100 × 540
- Background: `#050c09`
- Green accent: `#58ff91`
- Pale green body text: `#c2ffd5`
- Incident order: descending year
- GIF sequence per incident: Attack Vector → Impact → Significance
- Stage durations: 1.2 s → 1.5 s → 3.9 s
- Loop: infinite

The uploaded GIF reference in the conversation was inspected and contained one frame. This backup therefore preserves the complete animated SVG as the source of truth and includes a reproducible generator for the full animated GIF.
