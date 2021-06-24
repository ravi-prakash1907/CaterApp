# UPDATES WILL BE INITIALLY DONE AND TESTED HERE BEFORE RELEASING THE STABLE VERSION

---  

## **CaterApp - v1.1**  

<p align="center">
  <a href="#-installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-usage">Usage</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-contributing">Contributing</a>
</p>  

![icon banner](./assets/logo.jpg)

<!-- _A Quick & Secured Data Sharing Application!_ --> 

![Python minimum version](https://img.shields.io/badge/Python-3.2%2B-brightgreen)
[![cater minimum version](https://img.shields.io/badge/cater-0.1%2B-blue)](https://github.com/ravi-prakash1907/cater)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Website](https://img.shields.io/badge/website-up-lightgreen)](https://ravi-prakash1907.github.io/CaterApp)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/73MP0R4L)
[![current version](https://img.shields.io/badge/version-v1.1-blue)](https://github.com/ravi-prakash1907/CaterApp/releases)

## ✉️ Description
CaterApp is a cross platform, remotely data sharing tool created for sharing files in a quick and secured manner. It is aimed to integrate this tool with several more features including providing a User Interface.\
The _version 1.1_ of the CaterApp currently works with **command line interface** i.e. **CLI**.

### 💥 What's so exciting ?  
CaterApp comes with a range of fantastic features for you:  
1. Share **any** type of file, including large videos and compressed documents.  
2. You can choose as much files as you want.  
3. Keeps you updated with the file, i.e. being shared in real time.  
4. Also, it displays the size of files (in bytes).  
5. Automatically detects sender's IP.  
6. Compresses multiple files before sending, if asked to do that.  
6. Tells the **speed** at which the data got delivered and a lot more...

## 📌 Installation  
This is a `python` application that relies on its [**cater**](https://ravi-prakash1907.github.io/cater/) module.  

### ❓ Requirements  
1. A device with any operating system having bash / zsh terminal or python shell(preferred Linux)  
2. Python 3.2 or higher version  
3. pip (latest recommended)  

### ➡ Steps to Install
Installation can be done through CLI in just a few of the simple steps:  

1. Either clone this repository or simply download the CaterApp-v1.1 here \([tar](https://github.com/ravi-prakash1907/CaterApp/archive/refs/tags/v1.1.tar.gz), [zip](https://github.com/ravi-prakash1907/CaterApp/archive/refs/tags/v1.1.zip)\)  
2. Extract the compressed file (if you have cloned/downloaded) and navigate into **CaterApp** directory  
3. Execute the `installer.sh` to install the application through following terminal command:  
```sh
$ ./installer.sh
```
### Alternate Method 
If you love the terminal than following method is indeed for you:  
```sh
$ wget https://github.com/ravi-prakash1907/CaterApp/archive/refs/tags/v1.1.zip
$ unzip v1.1.zip
$ cd CaterApp-1.1
$ sh ./installer.sh
```  

After successful installation, you should see something like this:  
![installing screenshot](./assets/installation.png)  

## 🤔 Usage  
Once you have installed the application on your system, you can simply access CaterApp tool with a single command as follows: 
```sh
$ cater-app
```
As an alternative, you can also follow the following:  
```sh
$ cd ~/CaterApp/caterapp
$ python cater.py
```
#### Remember
1. Keep the file(s) in current working directory, that you want to sahre.  
2. All your received files will appear in **received/** directory at the current location. 
3. Both - the sender and reciever must be at the same network.  
4. To know your current location before sharing / receiving the files, run:  
```sh
$ pwd
```  

To use the app **without installation**, please refer to [this link](./caterapp/).

## 🤝 Contributing  
If you wish to contribute in this project, you can always **fork** this repo and generate a pull request with new changes. You may also raise issues, if any.  

🌟 Happy sharing!!! 🌟

---  
_Developed by [ravi](http://ravi-prakash1907.gitlab.io/) with ❤️ in 🐍_
