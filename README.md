## ThinkBridge_intern

This is a python program which returns the output in words for the input currency value

# Prerequisite 
1. **Python3**
   Make sure you have Python3 installed on your machine.
The Python download requires about 25 Mb of disk space; keep it on your machine, in case you need to re-install Python. When installed, Python requires about an additional 90 Mb of disk space.

        download from https://www.python.org/downloads/      
and install it.

 **Python IDLE** (Integrated Development and Learning Environment) is an integrated development environment (IDE) for Python. The Python installer for Windows contains the IDLE module by default.

IDLE is not available by default in Python distributions for Linux. It needs to be installed using the respective package managers. For example, in case of Ubuntu:

$ sudo apt-get install idle

2. **Django Framework**
   Django is a Python-based free and open-source web framework that follows the model-template-view architectural pattern.
  Install django using following command:
  
          $ python -m pip install Django
  
  
 For running this program craete the directories in IDE as shown below:
 
   ![](djangoproject/Images/hierarchy.jpg)
  
 Compile the given codes
 1. urls.py
 2. views.py
 
Run the server using below cmd from parent converterproject directory : 
        $python manage.py runserver

Open the browser and go to url : 
 - http://localhost:8000/    opening the local host on local machine. This will show the 'homepage' web page as shown below
 
   ![](djangoproject/Images/homepage.jpg)
      
     
 - http://localhost:8000/about/  This will show the 'About' web page as shown below
 
   ![](djangoproject/Images/About.jpg)






### For this program to execute give the input as any cuurency of 6 digit upto 2 decimal precision and it will show the currency in words
example:

enter amount

235648.65

RS two lakh thirty five thousand six hundred fourty eigth
  65 /100
