from utils import powershell


def update_dns() -> None:
    powershell.execute_commands([
        r'netsh interface ipv4 set dnsservers Wi-Fi static 8.8.8.8 primary',
        r'netsh interface ipv4 set dnsservers Wi-Fi static 1.1.1.1 primary',
        r'netsh interface ipv4 set dnsservers Ethernet static 8.8.8.8 primary',
        r'netsh interface ipv4 set dnsservers Ethernet static 1.1.1.1 primary',
        r'netsh interface ipv6 set dnsservers Wi-Fi static 8.8.8.8 primary',
        r'netsh interface ipv6 set dnsservers Wi-Fi static 1.1.1.1 primary',
        r'netsh interface ipv6 set dnsservers Ethernet static 8.8.8.8 primary',
        r'netsh interface ipv6 set dnsservers Ethernet static 1.1.1.1 primary'    
    ])

def disable_services() -> None:
    powershell.execute_commands([
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider /v LocalPriority /t REG_DWORD /d 4 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider /v HostsPriority /t REG_DWORD /d 5 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider /v DnsPriority /t REG_DWORD /d 6 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider /v NetbtPriority /t REG_DWORD /d 7 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\QoS /v Do not use NLA /t REG_SZ /d 1 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters /v Size /t REG_DWORD /d 3 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters /v MaxUserPort /t REG_DWORD /d 65534 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters /v TcpTimedWaitDelay /t REG_DWORD /d 30 /f',
        r'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters /v DefaultTTL /t REG_DWORD /d 64 /f'
    ])

def disable_throttling() -> None:
    powershell.execute_commands([
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\"Windows NT"\CurrentVersion\Multimedia\SystemProfile /v NetworkThrottlingIndex /t REG_DWORD /d 4294967295 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Psched /v TimerResolution /t REG_DWORD /d 0 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Psched /v NonBestEffortLimit /t REG_DWORD /d 0 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\"Internet Explorer"\Main\FeatureControl\FEATURE_MAXCONNECTIONSPERSERVER /v explorer.exe /t REG_DWORD /d 10 /f',
        r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\"Internet Explorer"\Main\FeatureControl\FEATURE_MAXCONNECTIONSPER1_0SERVER /v explorer.exe /t REG_DWORD /d 10 /f'
    ])

def configure_adapter() -> None:
    powershell.execute_commands([
        r'Set-NetTCPSetting -SettingName internet -AutoTuningLevelLocal normal',
        r'Set-NetTCPSetting -SettingName internet -ScalingHeuristics disabled',
        r'netsh int tcp set supplemental internet congestionprovider=CUBIC',
        r'Set-NetOffloadGlobalSetting -ReceiveSegmentCoalescing disabled',
        r'Set-NetOffloadGlobalSetting -ReceiveSideScaling enabled',
        r'Disable-NetAdapterLso -Name *',
        r'Enable-NetAdapterChecksumOffload -Name *',
        r'Set-NetTCPSetting -SettingName internet -EcnCapability disabled',
        r'Set-NetOffloadGlobalSetting -Chimney disabled',
        r'Set-NetTCPSetting -SettingName internet -Timestamps disabled',
        r'Set-NetTCPSetting -SettingName internet -MaxSynRetransmissions 2',
        r'Set-NetTCPSetting -SettingName internet -NonSackRttResiliency disabled',
        r'Set-NetTCPSetting -SettingName internet -InitialRto 2000',
        r'Set-NetTCPSetting -SettingName internet -MinRto 300',
        r'netsh interface ipv4 set subinterface Ethernet mtu=1500 store=persistent',
        r'netsh interface ipv6 set subinterface Ethernet mtu=1500 store=persistent',
        r'netsh interface ipv4 set subinterface Wi-Fi mtu=1500 store=persistent',
        r'netsh interface ipv6 set subinterface Wi-Fi mtu=1500 store=persistent'
    ])