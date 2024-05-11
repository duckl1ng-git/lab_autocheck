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

Установить [обновление](https://aka.ms/wmf51download) для PowerShell до версии 5.1

Выполнить скрипт как для Windows 10

# Checker

```bash
apt update
apt install -y git ansible sshpass python3-flask
git clone https://github.com/duckl1ng-git/lab_autocheck.git
ansible-galaxy collection install pfsensible.core -p ./collections
```

??? ansible-galaxy collection install microsoft.ad -p ./collections ???