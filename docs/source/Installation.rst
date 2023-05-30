Installation
============

Download the Source Code from GitHub
-----------------------------------

1. Clone the application using this `link <https://github.com/stanlasso/DREPAL-PATHOEXTRACT.git>`_.

2. Open a command prompt or terminal on your system.

3. Navigate to the directory where you want to clone the project.

4. Clone the project from Git using the following command:

   .. code-block:: bash

      git clone https://github.com/stanlasso/DREPAL-PATHOEXTRACT.git

5. Once the cloning is complete, navigate to the DREPAL-PATHOEXTRACT directory using the following command:

   .. code-block:: bash

      cd DREPAL-PATHOEXTRACT

6. Follow the instructions in the README file for the configuration and usage of DREPAL-PATHOEXTRACT.

.. note::

   Please note that to clone DREPAL-PATHOEXTRACT from Git, you need internet access and administrative privileges on your system.
   
Install the Required Dependencies
-------------------------------

Install Snakemake and Production Environment Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   Before installing Snakemake, we need to install Conda. We can choose to install Conda in the location of our choice. Here are the steps to follow:

.. rubric:: Conda

   1. Navigate to your desired directory and download the Miniconda installation script:

      .. code-block:: bash

         wget https://repo.anaconda.com/miniconda/Miniconda3-py37_23.1.0-1-Linux-x86_64.sh

   2. Execute the Miniconda installation script:

      .. code-block:: bash

         bash Miniconda3-py37_23.1.0-1-Linux-x86_64.sh

      Follow the instructions to install Conda. Remember to close and reopen the console after installation.

   3. For more details on Conda installation, you can refer to this link_.

.. rubric:: Snakemake (Minimal installation)

   Once Conda is installed, we can proceed with installing Snakemake. Here are the steps to follow:

   1. Still in your desired directory, install Mamba:

      .. code-block:: bash

         conda install -n base -c conda-forge mamba

   2. Install the minimal version of Snakemake with Mamba:

      .. code-block:: bash

         mamba create -c bioconda -c conda-forge -n snakemake snakemake-minimal

   3. Verify that Snakemake is properly installed by executing the following commands:

      .. code-block:: bash

         conda activate snakemake
         snakemake

   4. For more information on Snakemake installation, you can refer to this `link <https://snakemake.readthedocs.io/en/stable/getting_started/installation.html>`_.

PM2 and Apache Server Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: PM2 Installation


   Before installing PM2, we need to first install npm by following the steps below:

   1. Open a terminal and update the existing packages by running the following command:

      .. code-block:: bash

         sudo apt update

   2. Install Node.js using the following command:

      .. code-block:: bash

         sudo apt install nodejs

   3. Verify the version of Node.js and npm to ensure the installation was successful, using the following commands:

      .. code-block:: bash

         node -v
         npm -v

   4. If npm is not installed, install the npm package manager using the following command:

      .. code-block:: bash

         sudo apt install npm

   5. Once npm is installed, you can install PM2 by executing the following command:

      .. code-block:: bash

         sudo npm install pm2 -g



.. rubric:: Apache Server Installation

   1. Open a terminal and update the existing packages using the following command:

      .. code-block:: bash

         sudo apt update

   2. Install the Apache server using the following command:

      .. code-block:: bash

         sudo apt install apache2

   3. Once the installation is complete, check if the Apache server is running by using the following command:

      .. code-block:: bash

         sudo systemctl status apache2

   4. If Apache is not running, you can start it using the following command:

      .. code-block:: bash

         sudo service apache2 start

   5. If Apache is running, you should see a message indicating that the service is active and running.

   6. If you have a firewall running on your server, you need to allow incoming connections on port 80 (HTTP) using the following command:

      .. code-block:: bash

         sudo ufw allow http

   7. You can now access your Apache server by opening a browser and entering your server's IP address (localhost). By default, the Apache default page should be displayed. You can also place your website files in the /var/www/html/ directory and access it through a browser by entering your server's IP address.
   
   
Backend Components (Toolskit) Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Application Architecture

The application is based on a full-stack architecture, consisting of two distinct folders: the frontend and the backend. The frontend folder contains the Angular build, while the toolskit folder contains the backend coded in Node.js Express. To ensure the proper functioning of the directories, it is recommended to copy the contents of the frontend folder to the www/html directory of the Apache server. To do this, execute the following command:

.. code-block:: bash

   DREPAL-PATHOEXTRACT$ sudo cp -r patho /var/www/html/

Then, open your browser and enter the URL localhost/patho to access the application.

Regarding the toolskit folder, it is important to note that the backend dependencies need to be installed before launching the application. To do this, navigate to the toolskit directory and execute the following command:

.. code-block:: bash

   npm install

This command installs all the dependencies required for the proper functioning of the application. Once the installation is complete, you can start the backend by using the following command in the toolskit directory:

.. code-block:: bash

   pm2 start server.js

.. rubric:: Directory Structure patho

In the "patho" directory, you'll find essential files and folders for the application. The "index.html" file serves as the application's homepage. JavaScript files are located in the "assets" folder. The "styles.99f4b67f677e816d.css" file contains the application's styles, and "polyfills.d3e1f472fbd76fc8.js" ensures browser compatibility.

.. rubric:: Directory Structure toolskit

The "toolskit" directory holds the application's backend. The "app.js" file defines the application's routes and how each route should be handled. The "controllers" directory contains controller files that manage the application's business logic. The "data" directory contains data files such as information about files loaded in the application, configuration parameters, and user information.

The "middleware" directory contains middleware files that intercept HTTP requests. The "package.json" file is the application's npm configuration. The "routes" directory contains routes for the main pages of the application, as well as for Conda management, user data, application settings, references used in the application, file downloads, and application users.



.. note::
   The "server.js" file launches the server and listens for incoming connections on the specified port in its code. It's important to note that to ensure proper directory functionality, you need to copy the frontend to      the www/html directory of the Apache server and access it from the browser using the URL "localhost/patho". Additionally, remember to run "npm install" in the "toolskit" directory before executing the "pm2 start          server.js" command to install the necessary dependencies for the backend.








