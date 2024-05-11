if ([System.Environment]::OSVersion.Version.Major -eq 10){
    Set-NetConnectionProfile -NetworkCategory Private
}

Set-WSManQuickConfig

if ((get-item WSMan:\localhost\Client\AllowUnencrypted).value -like "false"){
    write-host "[winRM] : set Client AllowUnencrypted to true" -for Yellow
    set-item WSMan:\localhost\Client\AllowUnencrypted -Value $true
}else{
    write-host "[winRM] : Client AllowUnencrypted is true" -for Green
}

if ((get-item WSMan:\localhost\Client\Auth\Basic).value -like "false"){
    write-host "[winRM] : set Client Basic auth to true" -for Yellow
    set-item WSMan:\localhost\Client\Auth\Basic -value $true
}else{
    write-host "[winRM] : Client Basic auth is true" -for Green
}

if ((get-item WSMan:\localhost\Service\AllowUnencrypted).value -like "false"){
    write-host "[winRM] : set Service AllowUnencrypted to true" -for Yellow
    set-item WSMan:\localhost\Service\AllowUnencrypted -Value $true
}else{
    write-host "[winRM] : Service AllowUnencrypted is true" -for Green
}

if ((get-item WSMan:\localhost\Service\Auth\Basic).value -like "false"){
    write-host "[winRM] : set Service Basic auth to true" -for Yellow
    set-item WSMan:\localhost\Service\Auth\Basic -value $true
}else{
    write-host "[winRM] : Client Basic auth is true" -for Green
}

if ((get-item WSMan:\localhost\Client\TrustedHosts).value -notlike "*"){
    write-host "[winRM] : set Client TrustedHosts to *" -for Yellow
    set-item WSMan:\localhost\Client\TrustedHosts -Value *
}else{
    write-host "[winRM] : Client TrustedHosts is *" -for Green
}