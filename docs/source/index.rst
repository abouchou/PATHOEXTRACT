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

- Stanislas Egomli ASSOHOUN (1)(2)
- Aristide Berenger AKO (2)
- Abouchou Paul Christian AKO (2)
- Catherine DAUGA (3)
- Jérôme Adou. KABLAN (1)
- Ronan JAMBOU (2)

1: Laboratory of Mechanics and Computer Science (LAMI), Felix Houphouet-Boigny University, Abidjan, Côte d'Ivoire

2: Parasitology and Mycology Unit, Pasteur Institute (IPCI), Abidjan, Côte d'Ivoire

3: Arbovirus and Vector Insects Unit, Pasteur Institute, Paris, France

4: Medical and Health Research Center (CERMES), Niamey, Niger

.. toctree::
   Installation
   DREPAL-PATHOEXTRACT
   Fonctionnalite
