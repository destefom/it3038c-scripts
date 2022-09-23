$IP = getIP
$USER = Get-LocalUser
$Host = Get-Host
$HOST = get-host
$Date = Get-Date
Write-Host("This machine's IP is $IP, User is $USER, Hostname is $Host, Today's date is $Date")
$Body = Write-Host
Send-MailMessage -To "reedws-win" -From "oliviadestefano20@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $Body -SmtpServer smtp.gmail.com -port 587 -UseSsl -Credential (Get-Credential)
