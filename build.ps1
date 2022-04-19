pyinstaller --noconfirm --clean -D -F -i ./src/Assets/ICON.ico -n "WinOptimizer" ./src/main.py

Remove-Item -R -Force ".\build"
Remove-Item -R -Force ".\src\__pycache__"
Remove-Item -Force "WinOptimizer.spec"
Remove-Item -R -Force ".\bin\"

Rename-Item ".\dist" ".\bin" 

Set-Location ".\bin"

Get-FileHash -A SHA256 ".\WinOptimizer.exe" | Format-List >> SHA256
Get-Content SHA256

explorer.exe .
Set-Location ..