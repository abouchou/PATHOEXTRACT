DREPAL-PATHOEXTRACT
===================

DREPAL-PATHOEXTRACT est un pipeline Snakemake intégré qui permet :
    - le contrôle qualité;
    - le filtrage digitale (double soustraction digitale) pour ne retenir que la part d'un pathogene d'interêt porté par des données de sequençage NGS (Illumina) issues d'échantantillons clinique 
    - et d'assemblage de novo / de génération consensus de la portion du pathogène extrait.
Selon les ressources materielles disponibles, DREPAL-PATHOEXTRACT prend en charge plusieurs données de séquençage NGS (Illumina) de type paired-end en une seule exécution. Optimisée pour une utilisation sous Linux (Ubuntu), DREPAL-PATHOEXTRACT fournit une interface graphique simple et interactive qui facilite son utilisation par de nombreux scientifiques ne disposant d'expertise bioinformatique adequate.

Les caractéristiques essentielles de DREPAL-PATHOEXTRACT sont expliquées ci-dessous :

    - Prise en charge des plates-formes NGS : Illumina, 454/Roche et Ion Torrent.
    
    - Analyse des données de séquençage à partir defichiers FASTQ de type paired-end avec un encodage de qualité Sanger.

    - Analyse simultanée de plusieurs patients/échantillons en une seule exécution.
    
.. toctree::

   Installation
   DREPAL-PATHOEXTRACT
   Fonctionnalite Générale
   Analyse_bio-informatique
   
