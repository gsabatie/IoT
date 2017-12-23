# IoT II

Ce projet s'inscrit dans le cadre du module IoT II, proposé aux étudiants de 5e année à Epitech.

## Auteurs

* Sylvain GIROD
* Loic ECHEVET
* Guillaume SABATIER

## Présentation du projet

Il s'agit d'une application sur Raspberry Pi 3 qui surveille l'environnement d'une pièce (luminosité, température, humidité).

L'utilisateur définit les seuils à partir desquels il considère que la pièce est trop ou pas assez éclairée, chaude, ou humide

Le Raspberry contrôle en permanence l'état de la pièce, et lorsqu'un des seuils est dépassée, il allume une LED pour avertir l'utilisateur.

Cela est rendu possible grâce à l'utilisation d'un raspberry, un brocker MQTT, et un node red.

Le brocker MQTT va permettre au Raspberry et au node red de communiquer. Le raspberry envoie les valeurs au node red, le node red vérifie si les seuils sont dépassés, et renvoie au raspberry s'il faut allumer les LED ou non.

## Cahier des charges et présentation technique

## Difficultées rencontrées