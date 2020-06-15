<#
.SYNOPSIS
Creates the test files for the FillIntheGaps project

.NOTES
Sometimes, PowerShell is just easier...
#>
[CmdletBinding(SupportsShouldProcess)]
param(
    [switch] $Clean,
    [string] $Folder = '.\FillInTheGapsTestFiles'
)

$Prefix = 'spam'
$FilenameTemplate = "$Prefix-0{0}.txt"

if ($Clean) {
    if (Test-Path $Folder) {
        Write-Verbose -Message "Cleaning $folder"
        Remove-Item $folder -Recurse -force
        Write-Verbose -Message "Cleaned $folder"
    }
    else {
        Write-Verbose -Message "Found $folder was removed"
    }
}
else {
    if (Test-Path $Folder) {
        Write-Verbose -Message "Found $folder in place"
    }
    else {
        $null = mkdir $folder
        Write-Verbose -Message "Created $folder "
    }

    1..3 | ForEach-Object { Get-Random -Minimum 1 -maximum 9 } | 
    ForEach-Object { Set-Content -value 'foo' -path (Join-Path -Path $Folder -ChildPath ($FilenameTemplate -f $_ )) }
    
}

