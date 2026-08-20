# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This project generates an iCal feed for the Ohio State University academic calendar by fetching events from an undocumented REST API at `https://registrar.osu.edu/umbraco/api/calendar/getentries`.

## Commands

### Running the Calendar Builder
```bash
python3 build.py
```
This fetches calendar data and generates `build/academic.ics`.

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Architecture

The project consists of a single Python script (`build.py`) that:
1. Fetches calendar entries from OSU's REST API using the "Academic Calendar" filter
2. Processes entries to extract title and date information
3. Generates an iCal feed using the `ics` library
4. Outputs to `build/academic.ics`

Key functions:
- `get_calendar()`: Fetches data from the OSU API with configurable year range
- `make_calendar()`: Converts API entries into iCal events with proper timezone (America/New_York)

## Deployment

The project uses GitHub Actions (`.github/workflows/build_ical.yml`) to:
- Build the iCal feed weekly (cron: "0 0 * * 0")
- Deploy to GitHub Pages on push to main branch
- The feed is available at: https://vqv.github.io/osu-ical/academic.ics

## Dependencies

- `requests`: API communication
- `ics`: iCal file generation
- `beautifulsoup4`: Listed but not actively used in current implementation