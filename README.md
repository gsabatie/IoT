# IoT II

Ce projet s'inscrit dans le cadre du module IoT II, proposé aux étudiants de 5e année à Epitech.

## Auteurs

* Sylvain GIROD
* Loic ECHEVET
* Guillaume SABATIER

## Présentation du projet

Il s'agit d'une application sur Raspberry Pi 3 qui surveille l'environnement d'une pièce (luminosité, température, humidité).

L'utilisateur défini à quel moment il considère que la pièce n'est pas suffisament éclairée, si la température est trop/pas assez élevée, et si le taux d'humidité est trop élevée.

Le Raspberry contrôle en permanence l'état de la pièce, et lorsqu'un des seuils est dépassée, il allume une LED pour avertir l'utilisateur.

Celà est rendu possible grâce à l'utilisation d'un raspberry, un brocker MQTT, et un node red.

Le brocker MQTT va permettre au Raspberry et au node red de communiquer, le raspberry envoie les valeurs au node red, le node red vérifie si les seuils sont dépassés, et renvoie au raspberry s'il faut allumer les LED ou non.

## Cahier des charges et présentation technique

[carte d'extension RPi GPIO](https://www.amazon.fr/gp/product/B01N562X2P/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1)
[capteur de température et d'humidité](https://www.amazon.fr/gp/product/B06XF4TNT9/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)

## Difficultés rencontrées

La première difficulté a été de choisir le matériel à utiliser.

Amazon est un super site de e-commerce, mais en ce qui concerne les composants electroniques, il manque de précision. Un Raspberry pi ne gérant pas la lecture analogique, nous avons du faire attention aux composants choisis, afin d'éviter d'acheter des convertisseurs à gérer nous même.


Ensuite, notre niveau général en électronique a été un frein au projet. Nous avons du prendre des composants bien documentés car nous n'avons pas les savoirs nécessaires pour faire un montage sans tutoriel.

Nous avons par exemple fait l'erreur de commander un capteur de lumière avec convertisseur analogique - numérique, idéal pour RPi, mais sans documentation facilement trouvable.

Voici l'objet en question : [capteur](https://www.amazon.fr/gp/product/B01LX0K01H/ref=oh_aui_detailpage_o04_s00?ie=UTF8&psc=1)

Au final, nous en avons commandé plusieurs exemplaires, tous grillés à cause de branchement incorrects.