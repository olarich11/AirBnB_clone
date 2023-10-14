AIRBnB CLONE - THE Console

Airbnb Description
------------------

This is a console program that allow users to manage object of 
different classes such as Users, State, City,
Reviews, and Place.

Command Line interpreter
------------------------

The command line interpreter serves a interface where the users can
interact with the application. The command line interpreter is built 
with CMD modules.

Table of Content
----------------

* Project Overview
* Getting Started
	* Prerequisites
	* installation
* Usage
* Command Interpreter
	* Available Commands
		* create
		* show
		* destroy
		* all
		* update
* Examples


PROJECT OVERVIEW:

This AirBnB Clone Project is designed to simulate the functionality
of AirBNB, allowing users to manage and manipulate data using the 
command line interface. users can create an instance of different
classes, display thier information update attributes and more

GETTING STARTED

Prerequisites
-------------

To run this project, you need to install the following
software:

* Python (>=3.4)

Installation
------------

1. git clone https://github.com/olarich11/AirBnB_clone.git
2. cd AirBnB clone
3. python console.py


Command Interpreter:
Users can interate with the app with availables commands

Available Commands

1. create

This Create a new instance of a specified class and save it into
a file storage(Json), and print the ID

Example:

(hbnb) Create BaseModel

2. Show

This print the string representation of an instance based on the
class name and ID

Example

(hbnb) show BaseModel 1232453423

3. destory:
Delete an instance of a class based on the Class name and ID provided

Example

(hbnb) destory BaseModel 32434243

4. all

This print the string representation of a class based on the class name or
you can print all string representaition of instance stored in file storage
without add the class name

Example
(hbnb) all BaseModel
(hbnb) all B

5. update

This update an instance of a class using class name, ID by adding or
updating an attribute of that class
(hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"


General Examples
----------------

(hbnb) create BaseModel
(hbnb) show BaseModel 1234-1234-1234
(hbnb) destroy BaseModel 1234-1234-1234
(hbnb) all BaseModel
(hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"
