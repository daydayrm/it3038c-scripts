function getIP{
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}
$IP = getIP
Write-Host("This machine's IP is $IP")



function getUser{
    (Get-LocalUser -Name "Administrator")
}
$UserName = getUser
Write-host("User is $UserName")



function GetHostName{
    ([System.Net.Dns]::GetHostName())
}
$HostName = GetHostName
Write-host("Host is $HostName")



function Version{
    ($PSVersionTable.PSVersion.ToString())
}
$VersionNumber = Version
Write-host("Powershell Version $VersionNumber")



function TodaysDate{
    (Get-Date).ToString('dddd, MMMM d yyyy')
}
$Date = TodaysDate
Write-host("Today's date is $Date")


Send-MailMessage -To "dayrm@mail.uc.edu" -From "ryandaym@gmail.com" -Subject "IT3038C Windows SysInf" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)





