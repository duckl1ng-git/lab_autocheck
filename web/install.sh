#!/usr/bin/bash
python3 -m venv .venv
.venv/bin/python -m pip install flask ansi2html
cp lab_checker.service /etc/systemd/system/
systemctl daemon-reload
systemctl start lab_checker.service
systemctl enable lab_checker.service