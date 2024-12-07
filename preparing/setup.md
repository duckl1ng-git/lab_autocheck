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

# Windows 7

[Установить](https://www.microsoft.com/ru-ru/download/details.aspx?id=48137) .NET Framework 4.6

Установить [обновление](https://aka.ms/wmf51download) для PowerShell до версии 5.1 (Win7AndW2K8R2-KB3191566-x64.zip)

Выполнить скрипт как для Windows 10

# Checker

```bash
apt update
apt install git
git clone https://github.com/duckl1ng-git/lab_autocheck.git
cd lab_autocheck
chmod +x install.sh
./install.sh
```

Если по каким-то причинам не доступен `galaxy.ansible.com`, произвести установку модуля `pfsensible.core` вручную.
```bash
cd /root/lab_autocheck/ansible/collections/ansible_collections
wget https://github.com/pfsensible/core/archive/refs/tags/0.6.1.zip
unzip 0.6.1.zip -d pfsensible
rm 0.6.1.zip
mv pfsensible/core-0.6.1 pfsensible/core
```