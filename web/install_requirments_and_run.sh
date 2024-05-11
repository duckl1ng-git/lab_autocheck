#!/usr/bin/bash
python3 -m venv .venv
.venv/bin/python -m pip install flask ansi2html
.venv/bin/python app.py