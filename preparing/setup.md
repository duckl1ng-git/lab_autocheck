# Windows 10 / Windows server 2012R2

Скачать [скрипт](https://raw.githubusercontent.com/duckl1ng-git/lab_autocheck/main/preparing/winrm_basic.ps1)

Разрешить выполнение скриптов:
```PowerShell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Force
```

Выполнить скрипт:
```PowerShell
.\winrm_basic.ps1
```

> Для Windows Server возможно не нужно выполнять скрипт, т.к. winrm уже включен. Проверить!

# Windows 7

[Установить](https://www.microsoft.com/ru-ru/download/details.aspx?id=48137) .NET Framework 4.6

Установить [обновление](https://aka.ms/wmf51download) для PowerShell до версии 5.1 (Win7AndW2K8R2-KB3191566-x64.zip)

Выполнить скрипт как для Windows 10

# Checker

```bash
apt update
apt install -y git ansible sshpass python3-venv
git clone https://github.com/duckl1ng-git/lab_autocheck.git
cd lab_autocheck/ansible
ansible-galaxy collection install pfsensible.core -p ./collections
cd ../web
chmod +x install.sh
./install.sh
```

??? ansible-galaxy collection install microsoft.ad -p ./collections ???