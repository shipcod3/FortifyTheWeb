FortifyTheWeb (FTW)
=====================

Description
----------------
Fortify The Web - Web Application Security Testing Framework, the framework will be built under Python language, the framework will automate some of the manual assessment methods which will save the tester extra time performing those checks. The framework is a non-interactive, one-liner tool that will give results to stdout or written in a file.

Contributors
----------------

semprix / gecko - Dax Labrador - core dev

shipcod3 - Jay Turla - contributor

httphacker - Nathan LaFollete - contributor

napz - Harris Soleminio - contributor

Directory structure
-------------------

	[root]
	| - auxiliary 
    | - modules
    |  `- recon
    |  `- discovery
    |  `- exploitation 
    | - unittest
    |  `- sockets             
    |  `- strings
    |
    `- ftw.py (core)
    `- bootstrap.py (dependency)
	`- Changelog
	`- ToDo
	`- Readme

Python Dependencies
-------------------
ping - pure python ping implementation using raw sockets (download link : https://pypi.python.org/pypi/ping/0.1)

termcolor - ANSII Color formatting for output in terminal (download link : https://pypi.python.org/pypi/termcolor/1.1.0)

BeautifulSoup4 - sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree. (download link : https://pypi.python.org/pypi/beautifulsoup4/4.3.2)

requests - Requests is an Apache2 Licensed HTTP library, written in Python. (download link : https://pypi.python.org/pypi/requests)
	
Coding Standards
-------------------
Maven Convention - http://maven.apache.org/developers/conventions/code.html

Python PEP - http://www.python.org/dev/peps/pep-0008/#code-lay-out




