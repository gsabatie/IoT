# IoT II

Ce projet s'inscrit dans le cadre du module IoT II, proposé aux étudiants de 5e année à Epitech.

## Auteurs

* Sylvain GIROD
* Loic ECHEVET
* Guillaume SABATIE

## Présentation du projet

Il s'agit d'une application sur Raspberry Pi 3 qui surveille l'environnement d'une pièce (luminosité, température, humidité).

L'utilisateur défini à quel moment il considère que la pièce n'est pas suffisament éclairée, si la température est trop/pas assez élevée, et si le taux d'humidité est trop élevée.

Le Raspberry contrôle en permanence l'état de la pièce, et lorsqu'un des seuils est dépassée, il allume une LED pour avertir l'utilisateur.

Celà est rendu possible grâce à l'utilisation d'un raspberry, un brocker MQTT, et un node red.

Le brocker MQTT va permettre au Raspberry et au node red de communiquer, le raspberry envoie les valeurs au node red, le node red vérifie si les seuils sont dépassés, et renvoie au raspberry s'il faut allumer les LED ou non.

## Présentation technique

Le projet de room monitoring prend place grace à une board de prototypage [Raspberry Pi 3](https://www.amazon.fr/Raspberry-Pi-Carte-M%C3%A8re-Model/dp/B01CD5VC92).

Ce choix est fait car la board prêtée pendant le séminaire a laché suite à une erreur de branchements, et que nous n'en avions pas d'autres sous la main.

Ce projet aurait pu prendre place sur une petite board sans soucis, et c'est prévu pour la suite du projet.

Afin de simplifier les branchements, nous avons pris une breadboard standard, ainsi qu'une [carte d'extension RPi GPIO](https://www.amazon.fr/gp/product/B01N562X2P/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1).

Pour le montage électronique, il est fait sur une plaque de prototypage achetée à un revendeur chinois via l'application Wish.

La captation de la température et de la luminosité se fait via un [capteur de température et d'humidité](https://www.amazon.fr/gp/product/B06XF4TNT9/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1).

Nous avons fait ce choix car le capteur est à un prix raisonnable, ce qui nous a permis d'en prendre plusieurs, mais aussi car il existe une librairie python qui permet de simplifier la lecture

Pour la luminosité, nous avons d'abord choisi un [capteur de luminosité compatible avec la lecture digitale du RPi](https://www.amazon.fr/gp/product/B01LX0K01H/ref=oh_aui_detailpage_o04_s00?ie=UTF8&psc=1), mais suite à des erreurs, nous avons du nous rabattre sur un capteur standard avec un condensateur.

Au delà de ce matériel, nous avons utilisé quelques résistances, leds, et cables, que nous avons acheté via Wish, par mesure d'économie.

Au delà du montage, il y a une partie purement software :

Le script est fait en Python 2.7. Le langage a été utilisé car il permet de faire beaucoup en très peu de lignes de code, ce qui nous a permis de prendre plus de temps pour la partie hardware.

Le script permet de lire les deux capteurs, et va `publish` les infos en question sur un channel MQTT par type d'infos.

Le broker MQTT se trouve sur un ordinateur à part, afin d'éviter de surcharger le RPi, qui doit déjà lire en boucle.

Sur celui-ci, les channels utilisés pour remonter la data sont :
* IoT/light
* IoT/humidity
* IoT/temperature

Nous écoutons ensuite ces channels sur un node-red, lui aussi installé sur un ordinateur à part, pour les mêmes raisons.

En l'état, le node-red lit les trois channels ci-dessus, et, en fonction du `payload`, publie `1` ou `0` sur un nouveau channel en fonction de paramètres définis arbitrairement dans node-red.

Les channels utilisés pour savoir si les valeurs sont dépassées sont :
* IoT/redLed
* IoT/whiteLed
* IoT/greenLed

Ces noms sont en fonction de la led qu'ils vont allumer, lorsque le RPi va lire les données depuis les trois channels ci-dessus. Tout simplement, s'il lit `1`, la led s'allume. Sinon, elle reste éteinte.

## Sécurisation de la solution

Etant donné que le projet est en version alpha, nous avons choisi de ne pas mettre l'accent surla sécurité du broker MQTT.

Pour assurer une sécurité, nous le faisons au niveau du réseau en lui-même, en installant notre solution dans un réseau isolé de toute activité humaine.

Ceci permet de sécuriser les informations, sans pour autant devoir chiffrer les trames réseau, car celui-ci n'est tout simplement pas accessible par un humain.

## Difficultés rencontrées

La première difficulté a été de choisir le matériel à utiliser.

Amazon est un super site de e-commerce, mais en ce qui concerne les composants electroniques, il manque de précision. Un Raspberry pi ne gérant pas la lecture analogique, nous avons du faire attention aux composants choisis, afin d'éviter d'acheter des convertisseurs à gérer nous même.


Ensuite, notre niveau général en électronique a été un frein au projet. Nous avons du prendre des composants bien documentés car nous n'avons pas les savoirs nécessaires pour faire un montage sans tutoriel.

Nous avons par exemple fait l'erreur de commander un capteur de lumière avec convertisseur analogique - numérique, idéal pour RPi, mais sans documentation facilement trouvable.

Voici l'objet en question : [capteur](https://www.amazon.fr/gp/product/B01LX0K01H/ref=oh_aui_detailpage_o04_s00?ie=UTF8&psc=1)

Au final, nous en avons commandé plusieurs exemplaires, tous grillés à cause de branchement incorrects.

Cette dernière phrase amène l'avant dernier problème, le côté financier.

De base, nous voulions réaliser un projet beaucoup plus ambitieux, mais les composants les plus petits ont un prix non négligeable, surtout avec un budget d'étudiants. Nous avons fait en sorte de pouvoir faire avec un coût minimum.