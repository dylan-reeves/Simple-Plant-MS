# Simple-Plant-MS
Simple Plant Maintenance System

Introduction
Simple Plant Maintenance System is a CMMS(Computerised maintenance management system) designed to fill a gap in the market that I came across when investigating possible solutions to manage the maintenance of various departments equipment at an industrial site I worked at. All the solutions I was able to find off the shelf were either over complicated and over priced or free but severely lacking in capability. So I decided to create an open-source solution. I envisage the target users of this application to be any organization with equipment which they would like to formalize and record the preventative maintenance of. I will go into more detail of the workings of the application below. Please note as at 16/11/2015 this is still a work in progress and I will be continuously updating both the readme and the wiki. One final note this will be by first open-source project on GitHub so please feel free to correct me at any time, any input is very much appreciated.

System Overview
The system will be designed such that the users will be able to configure sites or plants and departments as a way to split up the work. The users will then be able to create the various pieces of equipment on the system. Each piece of equipment will belong to a site and a department. The users will then be able to configure various maintenance jobs. Now we get to the action section, the users will then be able to assign the various maintenance jobs to pieces of equipment, when this assignment is made a service interval will be defined which will be how often the maintenance should take place. The system will then enable technical teams to print out job cards for the scheduled maintenance which they can fill out as the maintenance is completed and captured by the system. Managers will then be able to run reports on pieces of equipment and print out the captured job cards after the fact.

Technologies
I will be developing the application using Django 1.8, other libraries I will make use of are Twitter Bootstrap 3.5 and JQuery. They will all be included in the project as well as the requirements file for the virtualenv. I will also look at bundling the application in a docker file which I will link to.

Installation
I will include installation instructions in the wiki page. I will try and get around to creating instructions for bot NGINX and Apache2.
