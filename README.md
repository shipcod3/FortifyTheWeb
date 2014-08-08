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

medz - Midelito Barao - contributor

Directory structure
-------------------

	[root]
	| - auxiliary
    | - config
    | - data
    | - modules
    |  `- recon
    |  `- discovery
    |  `- exploitation 
    | - unittest
    |  `- modules 
    |      `- recon
    |	   `- crypto
    |  `- auxiliary
    |  `- exploits
    |
    `- ftw.py (core)
    `- bootstrap.py (dependency)
	`- Changelog
	`- ToDo
	`- Readme

Python Dependencies
-------------------
Run bootstrap.py to see all necessary python dependencies in order for FortifyTheWeb to run properly.
	
Coding Standards
-------------------
Maven Convention - http://maven.apache.org/developers/conventions/code.html

Python PEP - http://www.python.org/dev/peps/pep-0008/#code-lay-out

Install
------------------

Python2.7 should be present on the system

1. (Install Option #1) Using git - git clone git@github.com:semprix/FortifyTheWeb.git
2. (Install Option #2) Downloading release - download at https://github.com/semprix/FortifyTheWeb/releases
3. Run bootstrap.py - this will check all python module dependencies
4. Run ftw.py - python ftw.py <yourtarget.com> <yourtargetport>
5. Move the result away from data/<target_folder> to avoid overwriting it.




