## <span style="color:green">**Wetterstation - Anleitung für Aufbau und Inbetriebnahme**

## Hardware
### Hardwarevoraussetzungen:

- Waveshare Display 10.1 inch HDM LCDD (B) (with case)
- Raspberry Pi 4 Computer
- SD Karte für OS und Daten (8GB)

### Zusammenbau Hardware

Um den Monitor und den Raspberry Pi zusammenzubauen nutzten Sie bitte folgenden Link und folgen Sie der Bildanleitung:

***[Bauanleitung](https://www.waveshare.com/w/upload/4/4a/10.1inch-HDMI-LCD-B-with-Holder-assemble.jpg)***

## Software

### Softwarevoraussetzungen:

 Library  | Version | Link
:---------|:---------:| ------
fhnw-ds-hs2019-weatherstation-api | v 0.21 | [GitHub](https://github.com/markif/WeatherStation_HS2019)

### System Update:

Nachdem Start des raspberry Pi Terminal öffnen und Betriebssystem auf den neusten Stand bringen:

`sudo apt-get update`   
`sudo apt-get upgrade`


### Tick (Telegraf, InfluxDB, Chronograf, Kapacitor) Stack Installation:


Vor dem Start der Installtion zuerst die Version auf dem raspberry Pi überprüfen. Im Terminal folgenden Befehl im Termianl eingeben:

`car /etc/os-release`

Folgender Output sollte zu sehen sein:

![Output](https://i.imgur.com/RwTwNOg.png)

Uns interessiert die Verision und der Name der Version. Hier wäre es "9" und "stretch"

Im nächsten Schritt werden die GPG Schlüssel hinzugefügt   
`curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -`   

Füge das repository hinzu   
**Hinweis: bitte "stretch" mit der eigenen Version ersetzen wenn nötig!**   
`echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.lis`

Zum Schluss noch einmal alle Komponenten auf den neusten Stand bringen   
`sudo apt-get update`

Jetzt kann der ganze Stack installiert werden   
`sudo apt-get install telegraf influxdb chronograf kapacitor`

## Initiales Laden der Daten

Die Influx Datenbank ist im Moment noch leer und kann über die fhnw-ds-hs2019-weatherstation-api befüllt werden.   
Im ersten Schritt werden die historischen Daten geladen. Dazu Terminal öffnen und folgende Befehle eingeben:   
   
`mkdir data && cd data`  
`wget https://raw.githubusercontent.com/markif/WeatherStation_HS2019/master/data/messwerte_mythenquai_2007-2018.csv`  
`wget https://raw.githubusercontent.com/markif/WeatherStation_HS2019/master/data/`  `messwerte_tiefenbrunnen_2007-2018.csv`  
`wget https://raw.githubusercontent.com/markif/WeatherStation_HS2019/master/data/messwerte_mythenquai_2019.csv`  
`wget https://raw.githubusercontent.com/markif/WeatherStation_HS2019/master/data/messwerte_tiefenbrunnen_2019.csv`  
`cd..` 

Wetter API installieren    
`sudo pip3 install fhnw_ds_hs2019_weatherstation_api`


Für das erste Laden der Daten kann folgendes Skript ausgeführt werden     
`init_load_weather_data.py`   
Das Skript lädt alle Daten bis zum jetzigen Zeitpunkt.

## Wiederkehrendes Laden der Daten

Um sicherzustellen, dass alle Daten automatisch geladen werden, auch nach Neustart des System wird ein Skript zur Verfügung gestellt welches automatisch ausgeführt werden sollte durch raspberry Pi   

Folgende Schritte sind dazu nötig:

1. Runterladen des skripts `load_current_weather_data.py`
2. Directory des Skripts merken wo das Skript liegt
3. Terminal öffnen und `crontab -e` eingeben
4. Auf die letzte Zeile scrollen und `@reboot /"path to skript"/load_current_weather_data.py` hinzufügen
5. `Ctrl + x` drücken und Änderungen abspeichern

## Sleep Modus deaktivieren
Standardmässig wird bei raspberry Pi modellen und Debian Distributionen der "Sleep Modus" nach längerer Inaktivität auf dem Gerät aktiviert. Da es sich beim Wettermonitor um eine Lösung handelt die permanent sichtbar sein muss, sollte der "Sleep Modus" deaktiviert werden. Dazu wie folgt vorgehen:

1. lightdm-Konfiguration im Terminal öffnen `sudo nano /etc/lightdm/lightdm.conf`
2. In der conf Datei den [Seat:*] Header suchen
3. Zuunterst folgende Zeile hinzufügen: `xserver-command=X -s 0 -dpms`

Damit sollte sich der Bildschirm nicht mehr automatisch verdunkeln bzw. in den "Sleep Modus" wechseln

## Zusätzliche Daten in die Datenbank senden
Falls es sich in Zukunft ergeben würde dass weitere Daten in die Datenbank eingespeist werden, würde dieser Abschnitt dazu dienen. Dabei werden folgende 3 Schritte dokumentiert:   

***Instantiation --> Datenbank erstellen --> Daten an Datenbank senden***

Standardoperationen sind im Skiprt `new_data_influxdb.py` und dort kommentiert


Weiterführende Informationen und Erklärungen welche nicht im Skript enthalten sind können in der API Dokumentation unter diesem Link gefunden werden:    

**[Python API Dokumentation](https://influxdb-python.readthedocs.io/en/latest/api-documentation.html)**

## Benutzeroberfläche (Chronograf)
Um die geladenen Daten zu bearbeiten bzw. in eine grafische Form zu bringen wird nun der Browser gestartet und folgende URL aufgerufen:   

`localhost:8888`   

Die eingelesenen Daten können im Menüpunkt "Explore" angeschaut werden und die Queries für die Charts und Grafiken auch. 

Wie Queries geschrieben werden würde den Rahmen dieses Files sprengen, aus diesem Grund wird auf die Dokumentation von InfluxDB gewiesen. Link siehe unten

**[Influx SQL Dokumentation](https://docs.influxdata.com/influxdb/v1.7/query_language/database_management/)**

Um die Queries im Nachgang in eine ansprechende Visualisierung zu bringen, wird im nächsten Schritt am oberen Rand "Visualization" ausgewählt. Dort können dann die ausgewählten Daten aus dem Query in eine ansprechende grafische Formatierung gebracht werden.   
Wenn der Query und die Visualisierung den Ansprüchen genügt, dann kann das Resulat in ein Dashboard gesendet werden über den Bedienknopf "Send to Dashboard"

Weiterführende Informationen bezüglich Visualisierungen können auf der InfluxDB Dokumentation gefunden werden

**[Chronograf Dokumentation](https://docs.influxdata.com/chronograf/v1.7/)**

