# PR307_ATRAV
S9 Advanced Project - ENSEIRB-MATMECA - GR 8

La mise en place de la simulation est normalement terminée, la simulation est effectuée sur une aire d'environ 2-3km². Elle contient environ 500 vehicules dont 24 trams. Le nombre de nœud sur mininet est parametré à 30 pour que cela reste fluide, mais il est largement possible de passer à 100 voir plus si votre machine peut supporter la charge. Pour augmenter le nombre de nœuds au sein de mininet il suffit de modifier le range dans la boucle "for id in range(0, 30)" [ligne 26] du fichier vanet-sumo.py.

Pour faire marcher cette simulation il faut ajouter le fichier "Grande_Map" dans le répertoire "/usr/local/lib/python2.7/dist-packages/mininet_wifi-2.6-py2.7.egg/mn_wifi/sumo/data", puis remplacer le fichier "vanet-sumo.py" de ce répertoire git à la place de celui existant dans votre dossier mininet/examples présent suite à l'installation de mininet_wifi.

Une fois tout cela effectué, pour lancer la simulation il faut se placer dans votre dossier "mininet" et lancer la commande suivante :
sudo python examples/vanet-sumo.py  (!! attention le python sera peut-être à modifier en fonction de votre version de python, ex: python3 ou python2.7)
