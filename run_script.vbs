Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "D:\Practice\Python\Vocabulary\run_script.bat" & Chr(34), 0
Set WinScriptHost = Nothing
