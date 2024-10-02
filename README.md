# Créer des sangaku à l'aide d'une découpeuse laser

*Ce projet est un premier essai de publication de projet 'maker', vous pouvez m'adresser vos remarques : fdecomite@gmail.com*
## Définition

Les sangakus sont des problèmes mathématiques (très souvent géométriques) que les fidèles déposaient dans les temples au
japon.

Il y a à ma connaissance deux livres sur le sujet. 

- Le premier en anglais : 

	**Sacred Mathematics: Japanese Temple Geometry** écrit par Fukagawa Hidetoshi et Tony Rothman

	Disponible plus ou moins [légalement en ligne](https://archive.org/details/fukakgawa-hidetoshi-sacred-mathematics-japanese-temple-geometry)
- Le second en français :

	**Sangaku - Le mystère des énigmes géométriques japonaises ** écrite par Gery Huvent, actuellement indisponible.
	
## Le programme

La découpeuse laser accepte des fichier au format SVG. Ce sont des fichiers textes qui décrivent les points, courbes et chemins
composant un dessin. 

Le [programme](./touslessangakus.py) fabrique ces fichiers texte en fonction du dessin à réaliser, en utilisant des fonctions de base (triangle, cercles ...)

Plusieurs sangakus sont définis dans le fichier, et l'exécution du programme les génère tous, dans des fichiers séparés. 


Si programmer, ça vous gonfle, j'ai mis aussi les fichiers SVG tout prêts [ici](./sangakusfinis/)

