**CaterApp - v1.1** (beta)
==========================

.. raw:: html

   <p align="center">
     

Installation    \|    Usage    \|    Contributing

.. raw:: html

   </p>  

.. figure:: ./assets/logo.jpg
   :alt: icon banner

   icon banner

.. raw:: html

   <!-- _A Quick & Secured Data Sharing Application!_ --> 

|Python minimum version| |cater minimum version| |License: MIT|
|Website| |Twitter| |current version|

✉️ Description
--------------

| CaterApp is a cross platform, remotely data sharing tool created for
sharing files in a quick and secured manner. It is aimed to integrate
this tool with several more features including providing a User
Interface.
| The *version 1.1* of the CaterApp currently works with **command line
interface** i.e. **CLI**.

💥 What's so exciting ?
~~~~~~~~~~~~~~~~~~~~~~

| CaterApp comes with a range of fantastic features for you:
| 1. Share **any** type of file, including large videos and compressed
documents.
| 2. You can choose as much files as you want.
| 3. Keeps you updated with the file, i.e. being shared in real time.
| 4. Also, it displays the size of files (in bytes).
| 5. Automatically detects sender's IP.
| 6. Tells the **speed** at which the data got delivered and a lot
more...

📌 Installation
--------------

This is a ``python`` application that relies on its
`**cater** <https://ravi-prakash1907.github.io/cater/>`__ module.

❓ Requirements
~~~~~~~~~~~~~~

1. A device with any operating system having bash / zsh terminal or
   python shell(preferred Linux)
2. Python 3.2 or higher version
3. pip (latest recommended)

➡ Steps to Install
~~~~~~~~~~~~~~~~~~

Installation can be done through CLI in just a few of the simple steps:

1. Either clone this repository or simply download the CaterApp-v1.1
   here
   (`tar <https://github.com/ravi-prakash1907/CaterApp/archive/refs/tags/v1.1-beta.tar.gz>`__,
   `zip <https://github.com/ravi-prakash1907/CaterApp/archive/refs/tags/v1.1-beta.zip>`__)
2. Extract the compressed file (if you have cloned/downloaded) and
   navigate into **CaterApp** directory
3. Execute the ``installer.sh`` to install the application through
   following terminal command:

   .. code:: sh

       $ ./installer.sh

| After successful installation, you should see something like this:
| |installing screenshot|

🤔 Usage
-------

Once you have installed the application on your system, you can simply
access CaterApp tool with a single command as follows:

.. code:: sh

    $ cater-app

As an alternative, you can also follow the following:

.. code:: sh

    $ cd ~/CaterApp/caterapp
    $ python cater.py

Remember
^^^^^^^^

1. Keep the file(s) in current working directory, that you want to
   sahre.
2. All your received files will appear in **received/** directory at the
   current location.
3. To know your current location before sharing / receiving the files,
   run:

   .. code:: sh

       $ pwd

To use the app **without installation**, please refer to `this
link <./caterapp/>`__.

🤝 Contributing
--------------

If you wish to contribute in this project, you can always **fork** this
repo and generate a pull request with new changes. You may also raise
issues, if any.

🌟 Happy sharing!!! 🌟

--------------

*Developed by `ravi <http://ravi-prakash1907.gitlab.io/>`__ with ❤️ in
🐍*

.. |Python minimum version| image:: https://img.shields.io/badge/Python-3.2%2B-brightgreen
.. |cater minimum version| image:: https://img.shields.io/badge/cater-0.1%2B-blue
   :target: https://github.com/ravi-prakash1907/cater
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: ./LICENSE
.. |Website| image:: https://img.shields.io/badge/website-up-lightgreen
   :target: https://ravi-prakash1907.github.io/CaterApp
.. |Twitter| image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social
   :target: https://twitter.com/73MP0R4L
.. |current version| image:: https://img.shields.io/badge/version-v1.1%20beta-blue
   :target: https://github.com/ravi-prakash1907/CaterApp/releases
.. |installing screenshot| image:: ./assets/installation.png
