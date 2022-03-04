# PR307_ATRAV
S9 Advanced Project - ENSEIRB-MATMECA - GR 8

La simulation est effectuée sur une aire d'environ 2-3km². Elle contient environ 500 vehicules dont 24 trams. Le nombre de nœud sur mininet est parametré à 30 pour que cela reste fluide, mais il est largement possible de passer à 100 voir plus si votre machine peut supporter la charge. Pour augmenter le nombre de nœuds au sein de mininet il suffit de modifier le range dans la boucle "for id in range(0, 30)" [ligne 26] du fichier vanet-sumo.py.

Pour faire marcher cette simulation il faut ajouter le fichier "Grande_Map" dans le répertoire "/usr/local/lib/python2.7/dist-packages/mininet_wifi-2.6-py2.7.egg/mn_wifi/sumo/data", puis remplacer le fichier "vanet-sumo.py" de ce répertoire git à la place de celui existant dans votre dossier mininet/examples présent suite à l'installation de mininet_wifi.

Une fois tout cela effectué, pour lancer la simulation il faut se placer dans votre dossier "mininet" et lancer la commande suivante :
sudo python examples/vanet-sumo.py  (!! attention le python sera peut-être à modifier en fonction de votre version de python, ex: python3 ou python2.7)

# English version
The simulation is performed on an area of about 2-3km². It contains about 500 vehicles including 24 tramways. The number of nodes on mininet is set to 30 to keep it smooth (running), but it is possible to increase it to 100 or more if your hardware can handle the load. To increase the number of nodes in mininet you just have to modify the range in the loop "for id in range(0, 30)" [line 26] of the file vanet-sumo.py.

To make this simulation work you have to add the file "Grande_Map" in the directory "/usr/local/lib/python2.7/dist-packages/mininet_wifi-2.6-py2.7.egg/mn_wifi/sumo/data" if you use python2, then replace the file "vanet-sumo.py" in this git directory with the one in your mininet/examples folder which was created after the installation of mininet_wifi If you use python3, put the file "Grande_Map" in the corresponding directory "/usr/local/lib/python3.x/...."

Once all this done, to launch the simulation you have to go in your "mininet" folder and run the following command
sudo python examples/vanet-sumo.py (!! attention the python may have to be modified according to your python version, ex: python3 or python2.7)
