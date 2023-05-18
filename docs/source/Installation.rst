Installation
============
Télécharger le code source depuis GitHub
----------------------------------------

L'application DREPAL-PATHOEXTRACT est disponible sur la plateforme Git via le lien suivant : https://github.com/stanlasso/DREPAL-PATHOEXTRACT.git. Vous pouvez y accéder pour télécharger et installer l'application sur votre système. Une fois installée, vous pouvez suivre les prochaines étapes pour la configuration. 


Pour cloner DREPAL-PATHOEXTRACT à partir de Git, suivez les étapes ci-dessous :
1.	Assurez-vous que Git est installé sur votre système. Si ce n'est pas le cas, téléchargez et installez Git à partir du site officiel de Git.
2.	Ouvrez une invite de commande ou un terminal sur votre système.
3.	Accédez au répertoire dans lequel vous souhaitez cloner le projet.
4.	Clonez le projet à partir de Git en utilisant la commande suivante :

git clone https://github.com/stanlasso/DREPAL-PATHOEXTRACT.git
5.	Une fois le clonage terminé, accédez au répertoire DREPAL-PATHOEXTRACT en utilisant la commande suivante : 

cd DREPAL-PATHOEXTRACT
6.	Suivez les instructions dans le fichier README pour la configuration et l'utilisation de DREPAL-PATHOEXTRACT.

Notez que pour cloner DREPAL-PATHOEXTRACT à partir de Git, vous avez besoin d'un accès Internet et de privilèges administratifs sur votre système.

Installer les dépendances nécessaires 
-------------------------------------

Installation de Snakemake et des outils de l'environnement de production
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Avant d'installer Snakemake, nous devons installer Conda. Nous pouvons choisir d'installer Conda à l'emplacement de notre choix. Voici les étapes à suivre :
 		a-Conda 
1.	 Accédez à votre répertoire de choix et téléchargez le script 'installation de Miniconda :
wget https://repo.anaconda.com/miniconda/Miniconda3-py37_23.1.0-1-Linux-x86_64.sh
2.	Exécutez le script d'installation de Miniconda :
bash Miniconda3-py37_23.1.0-1-Linux-x86_64.sh et suivre les instruction
3.	Suivez les instructions pour installer Conda. N'oubliez pas de fermer et de relancer la console après l'installation.
4.	Pour plus de détails sur l'installation de Conda, vous pouvez consulter le lien suivant :
https://conda.io/projects/conda/en/latest/user-guide/install/index.html
b-Snakemake(Minimal installation)
Une fois Conda installé, nous pouvons installer Snakemake. Voici les étapes à suivre :
1.	Toujours dans votre répertoire de choix, installez Mamba :
conda install -n base -c conda-forge mamba
2.	Installez la version minimale de Snakemake avec Mamba :
mamba create -c bioconda -c conda-forge -n snakemake snakemake-minimal
3.	Vérifiez que Snakemake est correctement installé en exécutant les commandes suivantes :
#conda activate snakemake 
#snakemake 
4.	Pour plus d'informations sur l'installation de Snakemake, vous pouvez consulter le lien suivant : https://snakemake.readthedocs.io/en/stable/getting_started/installation.html
Installation de PM2 et du serveur Apache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
a - Installation de PM2 :
Avant d'installer PM2, il faut d'abord installer npm en suivant les étapes suivantes :
1.	Ouvrez un terminal et mettez à jour les paquets existants en exécutant la commande suivante :
sudo apt update
2.	Installez Node.js en utilisant la commande suivante :
sudo apt install nodejs
3.	Vérifiez la version de Node.js et npm pour vous assurer que l'installation a réussi en utilisant les commandes suivantes :
node -v
npm -v
4.	Si npm n'est pas installé, installez le gestionnaire de paquets npm en utilisant la commande suivante :
sudo apt install npm
5.	Une fois npm installé, vous pouvez installer PM2 en exécutant la commande suivante :
sudo npm install pm2 -g
Cette commande va installer PM2 globalement sur votre système.
b - Installation serveur Apache
1.	Ouvrez un terminal et mettez à jour les paquets existants avec la commande suivante :
sudo apt update
2.	Installez le serveur Apache en utilisant la commande suivante :
sudo apt install apache2
3.	Une fois l'installation terminée, vérifiez si le serveur Apache est en cours d'exécution avec la commande suivante :
sudo systemctl status apache2
4.	Si non exétez la commande 
sudo service apache2 start
5.	Si Apache est en cours d'exécution, vous devriez voir un message indiquant que le service est actif et en cours d'exécution.				
6.	Si vous avez un pare-feu en cours d'exécution sur votre serveur, vous devez autoriser les connexions entrantes sur le port 80 (HTTP) avec la commande suivante :
sudo ufw allow http
7.	Vous pouvez maintenant accéder à votre serveur Apache en ouvrant un navigateur et en saisissant l'adresse IP de votre serveur(localhost). Par défaut, la page d'accueil d'Apache devrait s'afficher. Vous pouvez également 			placer votre site web dans le répertoire /var/www/html/ et accéder à celui-ci via un navigateur en saisissant l'adresse IP de votre serveur.
Installation des composants du backend (Toolskit)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

a- Architecture de l'application :

L'application est codée sur une architecture full-stack comprenant deux dossiers distincts : le frontend et le backend. Le dossier frontend contient le build d'Angular, tandis que le dossier toolskit contient le backend codé en 	Node.js avec Express.	Afin de s'assurer que les répertoires fonctionnent correctement, il est recommandé de copier le contenu du dossier frontend dans le répertoire www/html du serveur Apache.
DREPAL-PATHOEXTRACT$ sudo cp -r patho /var/www/html/

Ensuite, il suffit de lancer le navigateur et de saisir l'URL localhost/patho pour accéder à l'application.



