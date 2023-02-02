# Installatie
Om dit project te kunnen runnen moeten er een aantal dingen geïnstallerd zijn. Dit zijn:
Python: https://www.python.org/
IDE / code editor: https://code.visualstudio.com/
Volg de instructies op de desbetreffende sites voor de installatie.

# Let op! Het kan zijn dat er een foutmelding optreed tijdens het uitvoeren van de volgende commando's. Kijk voor de oplossing bij het kopje: Probleemoplossing.
```
pip install virtualenv
virtualenv venv
.\venv\scripts\activate
pip install -r requirements.txt
```


# Probleemoplossing:
1. 
```
Foutcode:
File "Pathname here"\venv\Scripts\Activate.ps1 cannot be loaded. The file "Pathname here"\venv\Scripts\Activate.ps1 is not digitally signed. You cannot run this script on the current system. For more information about running scripts and setting execution policy, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.

Oplossing:
Voer de volgende code uit in de terminal: Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process

Waarschuwing!
Dit zorgt ervoor dat elk script in de IDE zonder controle gerunned kan worden, zolang deze draait. Nadat de IDE afgesloten is wordt deze policy weer naar de standaard teruggezet. Zorg er dus voor dat je, als je klaar bent, de IDE afsluit!
```