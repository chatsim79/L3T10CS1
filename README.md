# L3T10 Compulsory Task.

## Description:

This repository contains the files for Level 3 Task 10, as requested 
in the same's compulsory task. The purpose of this task is to bring 
together the concepts taught with Django, Github, Docker and Sphinx
and demonstarte the capacity to utilise them. As always, if 
anything would lose me marks, please fail me and I'll resub with 
corrections.

## Table of Contents:

### 1 - Installation
### 2 - Usage
### 3 - Credits

## 1 - Installation:

This requires docker desktop be installed if not already.

In an appropriate location/folder create a clone of this repository by 
running the following command in VSC or command line (remember to open 
the folder in VSC, or open terminal within the folder). I reccomend 
command line opened in the appropriate folder as it demonstrates the 
app running indepedent of VSC.

#### "git clone https://github.com/chatsim79/L3T10CS1.git"

once the repository is cloned, cd into the L1T23CompTask folder:

"cd L3T10CS1"

"cd L1T23CompTask"

run the following command, providing an approriate app name:

"docker build --tag [app name]"

The Build process will occur automatically.

## 2 - Usage:

Run the following command to execute the code remembering to use the
app name you assigned in the build step:

"docker run --publish 8000:8000 [app name]"

in your browser, enter the following URL:

"127.0.0.1:8000"

Register as a user, and have a look through the site!

## 3 - Credits: 

Me :) Also thanks to John and Njabulo, who always provide excellent
assistance.
