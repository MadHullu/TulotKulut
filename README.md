### Pääikkuna (PaaIkkuna.py) muuttujat ja selitykset

1. **root**: Tämä on tk.Tk() -objekti, joka luo pääikkunan. Se on tkinter

-ohjelman pääikkuna, jossa kaikki muut käyttöliittymäelementit sijaitsevat.

2. **aloi**: Tämä on tk.Label -objekti, joka luo tekstielementin pääikkunaan. Se näyttää tervetuloviestin käyttäjälle.

3. **tekstilaatikko**: Tämä on tk.Text -objekti, joka luo tekstilaatikon pääikkunaan. Käyttäjä voi kirjoittaa ja muokata tekstiä tässä laatikossa.

4. **tulotmenot_painike**: Tämä on tk.Button -objekti, joka luo painikkeen pääikkunaan. Kun painiketta painetaan, se kutsuu 
tuo_tulotmenot -funktiota, joka tuo ja suorittaa TulotMenot -moduulin.

5. **sulje_painike**: Tämä on tk.Button -objekti, joka luo sulkupainikkeen pääikkunaan. Kun painiketta painetaan, se sulkee pääikkunan ja lopettaa ohjelman.

6. **tuo_tulotmenot**: Tämä funktio tuo TulotMenot -moduulin importlib.import_module -funktiolla ja kutsuu sen main -funktiota.

7. **main**: Tämä funktio luo pääikkunan ja lisää siihen käyttöliittymäelementtejä. Se käynnistää myös 

tkinter -pääsilmukan, joka pitää ikkunan auki ja käsittelee tapahtumia.
