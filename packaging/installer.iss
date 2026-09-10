#define MyAppName "PCC YouTube Video Downloader"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Pakistan Code Center"
#define MyAppExeName "PCC YouTube Video Downloader.exe"

[Setup]
AppId={{C1A8C5D2-1D72-4E6A-A1D9-4E5D4A9B7C10}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\PCC YouTube Video Downloader
DefaultGroupName={#MyAppName}
OutputDir=..\release
OutputBaseFilename=PCC-YouTube-Video-Downloader-Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64

[Files]
Source: "..\dist\PCC YouTube Video Downloader\*"; DestDir: "{app}"; Flags: recursesubdirs ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch {#MyAppName}"; Flags: nowait postinstall skipifsilent
