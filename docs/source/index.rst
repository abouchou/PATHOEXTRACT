DREPAL-PATHOEXTRACT
===================

DREPAL-PATHOEXTRACT is an integrated Snakemake pipeline that enables:

- Quality control
- Digital filtering (double digital subtraction) to retain only the portion of interest of a pathogen carried by NGS (Illumina) sequencing data from clinical samples
- De novo assembly / consensus generation of the extracted pathogen portion.

Depending on the available hardware resources, DREPAL-PATHOEXTRACT supports multiple paired-end NGS (Illumina) sequencing data in a single run. Optimized for Linux (Ubuntu) usage, DREPAL-PATHOEXTRACT provides a simple and interactive graphical interface that facilitates its utilization by many scientists lacking adequate bioinformatics expertise.

The key features of DREPAL-PATHOEXTRACT are explained below:

- NGS platform support: Illumina, 454/Roche, and Ion Torrent.
- Analysis of sequencing data from paired-end FASTQ files with Sanger quality encoding.
- Simultaneous analysis of multiple patients/samples in a single run.

Contributors:

- Stanislas Egomli Assohoun: Laboratory of Mechanics and Computer Science (LAMI), Université Félix Houphouët Boigny, Abidjan, Côte d'Ivoire
- Aristide Berenger Ako: Unit of Parasitology Mycology, Institut Pasteur (IPCI), Abidjan, Côte d'Ivoire
- Abouchou Paul Christian Ako: Unit of Parasitology Mycology, Institut Pasteur (IPCI), Abidjan, Côte d'Ivoire
- Catherine Dauga: Arbovirus and Vector Insects Unit, Institut Pasteur, Paris, France
- Jérôme Adou Kablan: Laboratory of Mechanics and Computer Science (LAMI), Université Félix Houphouët Boigny, Abidjan, Côte d'Ivoire
- Ronan Jambou: Unit of Parasitology Mycology, Institut Pasteur (IPCI), Abidjan, Côte d'Ivoire
- Centre de Recherche Médicale et Sanitaire (CERMES), Niamey, Niger



.. toctree::
   Installation
   DREPAL-PATHOEXTRACT
   Fonctionnalite
