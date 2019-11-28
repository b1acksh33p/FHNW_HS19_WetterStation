## <span style="color:green">**Wetterstation - Anleitung für Aufbau und Inbetriebnahme**

## Hardware
### *Hardwarevoraussetzungen:*

- Waveshare Display 10.1 inch HDM LCDD (B) (with case)
- Raspberry Pi 4 Computer
- SD Karte für OS und Daten (16GB)

### *Zusammenbau Hardware*

Um den Monitor und den Raspberry Pi zusammenzubauen nutzten Sie bitte folgenden Link und folgen Sie der Bildanleitung:

***[Bauanleitung](https://www.waveshare.com/w/upload/4/4a/10.1inch-HDMI-LCD-B-with-Holder-assemble.jpg)***

## Software

### *Softwarevoraussetzungen:*

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

Füge das repository hinzu (**Hinweis: bitte "stretch" mit der eigenen Version ersetzen wenn nötig!**)   
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


Für das erste Laden der Daten kann das Skript '




Laden der Daten ist mit crontab erstellt. script lädt automatisch am start

bildschirm sleep mode:
Open your lightdm configuration:

sudo nano /etc/lightdm/lightdm.conf
Anywhere below the [SeatDefaults] header, add:

xserver-command=X -s 0 -dpms
This will set your blanking timeout to 0 and turn off your display power management signaling.

