# Django_project
A Django Project that parses xml file as input and stores into a dictionary also in the form of table.

Technologies used
----------
- Python backend
- Django web framework
- XML as input
- Pyhon3
- HTML/CSS
- Bootstrap

Installation
-----------
1.For this project to work you need Django installed first, you need to get Django first (you will also need Python3 installed).

`pip install Django `

2.Clone this repo to your machine and change to root directory of project.

` cd Django_project/ `

3.To run this project 

` python3 manage.py runserver `

{*Migrations warning can be removed by running --> ` python3 manage.py migrate `

4.If everything runs fine the project should be started at <b>http://127.0.0.1:8000/</b>


Basic Usage And Xml Parsing
----------------------------
Input file is taken as box2.xml i.e that contains data regarding vulnerabilities etc in a xml format,
we are extracting specific information such as <b>name of vulnerability, severity, confidence, url path</b>

Path of box2.xml -->  <b> cd /Django_project/xmlparser/templates/xmlparser/data</b>

We are using xml.etree for parsing XML file the parser file is present at,

Path of parser.py --> <b> cd /Django_project/xmlparser/templates/xmlparser/</b>


Parsing of Xml file in commandline
----------------------------------
Change path to <b>/Django_project/xmlparser/templates/xmlparser/</b> and run parser2.py

` python3 parser2.py `



