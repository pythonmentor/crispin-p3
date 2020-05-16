# Commentaires du 16 mai 2020

## Sur le plan de la structure et de la PEP8:
- Pipfile et Pipfile.lock ne doivent pas être dans .gitignore. Ajouter les répertoires `__pycache__/` dans .gitignore. Eliminer to requirements.txt qui n'est pas conforme.
- le répertoire Mcgyver ne prend pas de majuscule et contient un fichier `__init__.py`. Le fichier de lancement du programme sera `__main__.py`.
- les noms de modules ne contiennent si possible pas de underscore.
- Eviter de coder avec une ligne vide entre chaque instruction.
- attention de respecter la PEP 8 dans l'ordre des imports.

## Plateau:
- quelle utilité de plateauvide?
- set_accessible et move_posible inutiles à mon avis.
- si tu mets un getter et un setter sur chaque attribut, autant tout mettre en public dès le départ, non?

## Hero:
- stocker le plateau dans un attribut du héro pour qu'il puisse l'utiliser pour valider les positions lors du déplacement
- la méthode pas_macgyver (nom à modifier, pas de verbe) ne modifie pas la position du héro.
- pour valider les déplacements autorisés, il suffit d'utiliser les routes du plateau.

## Sortie et Guardien:
- je comprends l'utilité à long terme de Gardien, mais pas de sortie. En effet, le gardien est sur la sortie.

## Positionnement des objets:
- pourquoi ne pas faire simplement un tirage au sort sur les routes du plateau avec random.sample est suffisant. Il me semble plus logique que les objets soient disposés sur le plateau et que la méthode de ramassage soit dans Hero (c'est le héro qui collecte les objets)

## mg_console:
- La classe mg_console n'a pas un nom conforme. On n'hérite pas explicitement de object en python 3.
- la méthode `__init__` sert uniquement à l'initialisation. Utiliser une méthode séparée pour la boucle de jeu.
- draw_console peut directement utiliser les routes et les murs de plateau. 
- utiliser x, y ou i, j plutôt que i_1 et i_0 pour les positions. x, y est un standard pour représenter des coordonnées cartésiennes.

## mode_pygame:
- le nom de la classe n'est pas conforme à la PEP8. Pas besoin d'hériter explicitement de object en python 3.
- lancer le jeu via le constructeur n'est pas sémantiquement correct. Appeler explicitement jeu_pygame (un nom tel que demarrer ou mieux, start ou run, conviendrait mieux)
- Charger une seule fois l'image du mur suffit. Pas besoin de le faire dans une boucle.
- Les murs ne bougent pas. Il n'est pas nécessaire de les redessiner à chaque tour de boucle. Préparer un fond avec le labyrinthe au démarrave du jeu.
- Utiliser des classes de type pygame.sprite.Spritr pour représenter les sprites de McGyver, des objets et du gardien. Gérer l'affichage des sprites en bloc via un pygame.sprite.Group.
- si ta méthode est longue (longue == plus d'un demi écran), essaie de factoriser.
