General Features
================

Pathoextract provides a set of features as described in the figure below:

.. image:: ../pictures/gen.png
   :alt: General Features
   
Load Host/Pathogen Reference Files
----------------------------------

.. image:: ../pictures/-21504.png

To import a reference genome file, you can start by clicking the "Select files" button, which allows you to choose the file(s) you want to import. The application supports files with extensions such as ".fasta", ".fa", and ".fna".

It is important to note that if you change your mind or select the wrong file, the "Close" button allows you to cancel the file selection. This way, you can ensure that you import the appropriate reference genome files for your analyses.

Once the files are selected, you can click the "Upload" button to load the files into the application. You will be informed about the progress of the upload, and once it's completed, you will see a confirmation of success.

A set of buttons is provided to perform actions on the reference genome files, such as indexing and deletion.


.. rubric:: The Index button

Indexing reference genome files is a necessary step for digital subtractions operations.

To index a reference genome, you need to load it into the application through the import. Then, select it and click the "Index" button. You will be informed about the progress of indexing and receive a confirmation of success.

Please note that indexing may take time depending on the size of the indexed reference genome and the power of your computer. Once indexing is completed, you will be able to use the file in the post-sequencing processing of the application for faster and more efficient analysis.


.. rubric:: The Check button

The "Check" button allows you to check if the selected reference genome has already been indexed in the application. This feature prevents reindexing a file that is already present. A green color code indicates that the selected genome has already been indexed, while a red color code indicates that it hasn't been indexed.


Load and Visualize Quality of Clinical Samples/Isolates
------------------------------------------------------

.. image:: ../pictures/-21533.png

The "Manage Samples" session allows you to load clinical sample files (*Fastq*, *Fq*, in *Fastq.gz* or *Fq.gz*) and visualize their quality using the FastQC and MultiQC software options. By default, the downloaded samples are intended for the "Files to All Step" option, where the loaded files will be available for all analyses. Other loading options are available:

- **Files to Run Double Filtering** should only contain *Fq.gz* files for performing double subtraction.
- **Files to Generate De Novo** should only contain *Fastq* files for de novo generation.

This organization enables efficient file management and prevents processing errors.

Quality Control: Artifact Removal
---------------------------------

.. image:: ../pictures/-21612.png

The "Quality Control" session adjusts the quality of patient samples, preparing them for further post-sequencing analyses.


Extract Target Pathogen
-----------------------

.. image:: ../pictures/-21642.png

The "Double Digital Filtering" session extracts the portion of reads corresponding to a target pathogen of interest carried by patient samples (human host).


Quality Control and Double Digital Subtraction Pipeline
------------------------------------------------------

.. image:: ../pictures/-21707.png

The Pipeline section of our application combines two essential steps: Quality Control and Double Digital Subtraction.


Assemble and Generate Consensus Files
-------------------------------------

The "Assemble and Generate Consensus Files" section consists of three essential phases:

.. rubric:: 1. Split Reference Pathogen Genome
.. image:: ../pictures/-171555.png

This step involves breaking down the genome of the target pathogen into fragments corresponding to each chromosome. This prepares the data for generating the consensus file.

.. rubric:: 2. Assembly
.. image:: ../pictures/-171610.png

In this step, sequence fragments are aligned and combined to reconstruct the complete sequence of the genome. It is important to consider the ploidy of the pathogen for accurate assembly.

.. rubric:: 3. Consensus Generation
.. image:: ../pictures/-171625.png

Once the assembly is complete, consensus files are generated. They represent the most probable sequence for each position of the genome, taking into account variations and errors present in the sequence fragments.

These three steps provide a complete and reliable representation of the target pathogen's genome, facilitating further analysis and scientific discoveries.

Other Features
--------------

.. rubric:: The Filter field

The "Filter" field in our application is a very useful search tool that allows you to search for reference genome files based on various criteria, such as file name, file extension, modification date, or even file size.
For example, if you are looking for a specific file, you can simply enter part of its name or extension in the "Filter" field, and the application will display all files matching your search.
Similarly, if you need to sort files based on their size or modification date, you can simply use the "Filter" field and specify these criteria in the search.
In summary, the "Filter" field in our application is a flexible and powerful search tool that enables users to quickly and easily find the reference genome files they need for their work.

.. rubric:: The Delete button

The "Delete" button is an important feature of our application that allows you to delete the selected files in the directory list. To use this feature, you can first select the files you want to delete by checking the checkboxes next to the file names in the list.
Once you have selected the files to delete, you can click the "Delete" button to initiate the deletion process. This step is important as file deletion is permanent, and deleted files cannot be recovered.
The files will be removed from the directory list and from the application. This feature can be very useful for removing obsolete or unnecessary files, freeing up disk space for new files to import.

.. rubric:: The Status button

The "Status" button allows us to know whether a process has been successful or not. This button displays three different colors to indicate the state of the process: red, yellow, and green.
The red color indicates that the process did not run successfully, often due to a system error. For example, this could be due to a file that is not properly formatted or cannot be found. If you encounter a red error, it is recommended to download the associated log file to see the error details and determine the cause of the problem.
The yellow color indicates that the process ran successfully but not 100%. This may indicate that you are reprocessing the same files or that some files were ignored. It is also advisable to check the associated logs for more information about the processed files.
Finally, the green color indicates that the process ran successfully at 100% and all operations were completed successfully. There is no need to check the associated logs in this case.
The "Status" button is an easy way to check the status of processes and see if everything went well. It is important to note that the associated logs provide detailed information to help troubleshoot errors and issues.

.. rubric:: The Download Log button

The "Download Log" button is a very useful feature of our application. It allows you to view all the operations that have been performed during the various processes of the application. By clicking this button, a text file will be downloaded directly from the browser.
The log file contains all the information related to the operations performed in the application, including errors and warnings. It can be very helpful in diagnosing problems and errors that may occur during data processing processes.
It is important to note that log files are typically large. Therefore, it is recommended to take appropriate security measures to store and manage these files.
