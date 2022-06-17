# Spotifree

## Il s'agit d'un projet de fin de formation proposant un equivalent de Spotify.

Consignes:

- Un utilisateur spotifree a une application spotifree.
- Au lancement de l'application , on demande a l'utilisateur de renseigner un nom d'user et un mdp associé.
- Il peut creer un compte ou se logguer.

Déroulé:

L'utilisateurs avec se connecter sur le site https://www.spotifree.fr/ 
et interagir ensuite avec l’application.

Une fois que l’utilisateur est connecté, il accède à son espace personnel (la redirection vers l'espace personnel n'a pas encore été testé - le user pour l'instant est redirigé une fois connecté vers la page de recherde de musique).

De son espace personnel, l'utilisateur aura 3 choix:
  - chercher de la musique
  - voir ses playlists
  - Spotifriends

Chercher de la musique:
    - Il pourra réaliser des recherches de musique par Artiste, Album et Titre.
    - Il pourra ainsi réaliser des téléchargements et les rajouter à des playlists (partie non encore dévéloppée)
   ==> pour l'instant, on ne peut que faire des recherches et les résultats trouvés s'affichent. Les données sont bien incrémentées dans la BDD

Voir ses playlists:
    - le user peut voir la liste de ses playlists;
    - il peut ajouter ou supprimer des playlists;
    - il peut écouter les musiques d'une playslist;
  ==> à ce stade du projet, cette partie n'a pas encore été devéloppée. Seule la page html existe

Spotifriends:
    - le user voit la liste de ses amis (qui sont aussi des users de spotifree);
    - il peut ajouter ou supprimer des amis;
    - il peut envoyer des messages à ses amis et partager ses playlists.
   ==> à ce stade du projet, cette partie n'a pas encore été devéloppée. Seule la page html existe


## Technos utilisé

Flask Framework web pour le templating des pages.
Python pour la partie scripting

module utilisé
pysftp pour établir la connection avec le sftp

Hébergement des fichier
sFTP
Proftpd
SSH


INSTALLATION :

(Installer les modules python correspondant si besoin: flup, flask, uwsgi)
Dans le dossier site_spotifree de dossier github Spotifree:
1. Dezipper l'archive spotifree.tar.gz au chemin /var/www/.
2. Copier le fichier de configuration spotifree_config au chemin
   /etc/nginx/site_available puis créer son lien symbolique sur
   /etc/nginx/site_enabled
3. dans le fichier global de nginx.conf changer le user http par son propre
   utilisateur (qui devra lancer le script et qui aura les droits)
4. Lancer le socket fastcgi puis nginx

Dans le dossier github Spotifree:
5. Lancer le script acceuil.fcgi (./acceuil.fcgi nimporte ou)
(sinon, refaire un lien pour le fichier acceuil.fcgi dans /var/www/Spotifree/cgi-bin/)




Membres du projet: Justine Bigotte, Thuy Tran DARRITCHON, Felix MARLIO, Monica SASSI, Marine TOURNOIS, Justin UONG
