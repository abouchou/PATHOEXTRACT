Installation
============
Télécharger le code source depuis GitHub
----------------------------------------


    1- Cloner l'application via ce `lien <https://github.com/stanlasso/DREPAL-PATHOEXTRACT.git>`_
    2- Ouvrez une invite de commande ou un terminal sur votre système.
    3- Accédez au répertoire dans lequel vous souhaitez cloner le projet.
    4- Clonez le projet à partir de Git en utilisant la commande suivante :

    .. code-block:: bash
    
       git clone https://github.com/stanlasso/DREPAL-PATHOEXTRACT.git

    5- Une fois le clonage terminé, accédez au répertoire DREPAL-PATHOEXTRACT en utilisant la commande suivante :

    .. code-block:: bash
    
       cd DREPAL-PATHOEXTRACT
    
    6- Suivez les instructions dans le fichier README pour la configuration et l'utilisation de DREPAL-PATHOEXTRACT.
    
    .. note::
        
       Notez que pour cloner DREPAL-PATHOEXTRACT à partir de Git, vous avez besoin d'un accès Internet et de privilèges administratifs sur votre système.


Installer les dépendances nécessaires 
-------------------------------------

Installation de Snakemake et des outils de l'environnement de production
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   Avant d'installer Snakemake, nous devons installer Conda. Nous pouvons choisir d'installer Conda à l'emplacement de notre choix. Voici les étapes à suivre :
   
.. rubric:: Conda

    1- Accédez à votre répertoire de choix et téléchargez le script d'installation de Miniconda :

    .. code-block:: bash
    
        wget https://repo.anaconda.com/miniconda/Miniconda3-py37_23.1.0-1-Linux-x86_64.sh

    2- Exécutez le script d'installation de Miniconda :

    .. code-block:: bash
    bash Miniconda3-py37_23.1.0-1-Linux-x86_64.sh

    Suivez les instructions pour installer Conda. N'oubliez pas de fermer et de relancer la console après l'installation.

    3- Pour plus de détails sur l'installation de Conda, vous pouvez consulter ce lien_.

.. rubric:: Snakemake (Minimal installation)

Une fois Conda installé, nous pouvons installer Snakemake. Voici les étapes à suivre :

    1- Toujours dans votre répertoire de choix, installez Mamba :

    .. code-block:: bash
    conda install -n base -c conda-forge mamba

    2- Installez la version minimale de Snakemake avec Mamba :

    .. code-block:: bash
    mamba create -c bioconda -c conda-forge -n snakemake snakemake-minimal

    3- Vérifiez que Snakemake est correctement installé en exécutant les commandes suivantes :

    .. code-block:: bash
       
       conda activate snakemake
       snakemake

    4- Pour plus d'informations sur l'installation de Snakemake, vous pouvez consulter ce lien_.

.. _ce lien: https://conda.io/projects/conda/en/latest/user-guide/install/index.html
.. _ce lien: https://snakemake.readthedocs.io/en/stable/getting_started/installation.html

Installation de PM2 et du serveur Apache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

a - Installation de PM2

Avant d'installer PM2, il faut d'abord installer npm en suivant les étapes suivantes :

    1- Ouvrez un terminal et mettez à jour les paquets existants en exécutant la commande suivante :

    .. code-block:: bash
    sudo apt update

    2- Installez Node.js en utilisant la commande suivante :

    .. code-block:: bash
    sudo apt install nodejs

    3- Vérifiez la version de Node.js et npm pour vous assurer que l'installation a réussi en utilisant les commandes suivantes :

    .. code-block:: bash
    node -v
    npm -v

    4- Si npm n'est pas installé, installez le gestionnaire de paquets npm en utilisant la commande suivante :

    .. code-block:: bash
    sudo apt install npm

    5- Une fois npm installé, vous pouvez installer PM2 en exécutant la commande suivante :

    .. code-block:: bash
    sudo npm install pm2 -g

    Cette commande va installer PM2 globalement sur votre système.

b - Installation serveur Apache

    1- Ouvrez un terminal et mettez à jour les paquets existants avec la commande suivante :

    .. code-block:: bash
    sudo apt update

    2- Installez le serveur Apache en utilisant la commande suivante :

    .. code-block:: bash
    sudo apt install apache2

    3- Une fois l'installation terminée, vérifiez si le serveur Apache est en cours d'exécution avec la commande suivante :

    .. code-block:: bash
    sudo systemctl status apache2

    4- Si Apache n'est pas en cours d'exécution, vous pouvez le démarrer en utilisant la commande suivante :

    .. code-block:: bash
    sudo service apache2 start

    5- Si Apache est en cours d'exécution, vous devriez voir un message indiquant que le service est actif et en cours d'exécution.

    6- Si vous avez un pare-feu en cours d'exécution sur votre serveur, vous devez autoriser les connexions entrantes sur le port 80 (HTTP) avec la commande suivante :

    .. code-block:: bash
    sudo ufw allow http

    7- Vous pouvez maintenant accéder à votre serveur Apache en ouvrant un navigateur et en saisissant l'adresse IP de votre serveur (localhost). Par défaut, la page d'accueil d'Apache devrait s'afficher. Vous pouvez également placer votre site web dans le répertoire /var/www/html/ et y accéder via un navigateur en saisissant l'adresse IP de votre serveur.

Installation des composants du backend (Toolskit)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

a- Architecture de l'application

L'application est basée sur une architecture full-stack, composée de deux dossiers distincts : le frontend et le backend. Le dossier frontend contient le build d'Angular, tandis que le dossier toolskit contient le backend codé en Node.js avec Express. Pour assurer le bon fonctionnement des répertoires, il est recommandé de copier le contenu du dossier frontend dans le répertoire www/html du serveur Apache. Pour ce faire, exécutez la commande suivante :

.. code-block:: bash

   DREPAL-PATHOEXTRACT$ sudo cp -r patho /var/www/html/

Ensuite, ouvrez votre navigateur et saisissez l'URL localhost/patho pour accéder à l'application.

Concernant le dossier toolskit, il est important de noter que les dépendances du backend doivent être installées avant de lancer l'application. Pour cela, accédez au répertoire toolskit et exécutez la commande suivante :

.. code-block:: bash
   npm install

Cette commande installe toutes les dépendances nécessaires au bon fonctionnement de l'application. Une fois l'installation terminée, vous pouvez lancer le backend en utilisant la commande suivante dans le répertoire toolskit :

.. code-block:: bash

   pm2 start server.js

b- Arborescence

Dans le dossier "patho", vous trouverez plusieurs fichiers et dossiers essentiels à l'application. Le fichier "index.html" est la page d'accueil de l'application. Les fichiers JavaScript sont situés dans le dossier "assets". Le fichier "styles.99f4b67f677e816d.css" contient les styles de l'application, tandis que le fichier "polyfills.d3e1f472fbd76fc8.js" assure la compatibilité avec les navigateurs.

Le dossier "toolskit" contient le backend de l'application. Le fichier "app.js" définit les routes de l'application et comment chaque route doit être gérée. Le dossier "controllers" contient les fichiers de contrôleurs qui gèrent la logique métier de l'application. Le dossier "data" contient les fichiers de données de l'application, tels que les informations sur les fichiers chargés dans l'application, les paramètres de configuration et les informations sur les utilisateurs. Le dossier "middleware" contient les fichiers de middleware qui interceptent les requêtes HTTP.

Le fichier "package.json" est la configuration npm de l'application. Le dossier "routes" contient les routes pour les pages principales de l'application, ainsi que pour la gestion de Conda, les données des utilisateurs, les paramètres de l'application, les références utilisées dans l'application, les téléchargements de fichiers et les utilisateurs de l'application. Le fichier "server.js" lance le serveur et écoute les connexions entrantes sur le port spécifié dans le code du fichier "server.js".

Pour assurer le bon fonctionnement des répertoires, il est nécessaire de copier le frontend dans le répertoire www/html du serveur Apache. De plus, avant de lancer la commande "pm2 start server.js", assurez-vous d'exécuter la commande "npm install" dans le répertoire "toolskit" pour installer les dépendances nécessaires au backend.

A cool bit of code::

   Some cool Code

.. code-block:: rst

   A bit of **rst** which should be *highlighted* properly.





