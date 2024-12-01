#!/usr/bin/bash
apt update
apt install ansible sshpass python3-venv curl -y
cd ansible
ansible-galaxy collection install pfsensible.core -p ./collections
cd ../web
python3 -m venv .venv
.venv/bin/python -m pip install flask ansi2html
cp ../lab_checker.service /etc/systemd/system/
systemctl daemon-reload
systemctl start lab_checker.service
systemctl enable lab_checker.service
echo "IP: \4{ens3}" >> /etc/issue
echo "" >> /etc/issue