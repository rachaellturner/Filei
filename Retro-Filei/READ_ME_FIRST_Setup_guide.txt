Retro Filei set up guide:

*The user is assumed to be using Linux Ubuntu*
*OSX and Windows operating systems may encounter unexpected errors*

The following should be installed:
r-base
Python 3
pip3

**You may encounter missing system requirements when trying to install R and python packages. These are unpredictable. The ones we encountered are listed here.**

setuptools 
(pip3 install setuptools)
gfortran 
(sudo apt-get install gfortran)
g++ 
(sudo apt-get install g++)
python3-dev 
(sudo apt-get install python3-dev)
wheel 
(pip3 install wheel)
readline 
(sudo apt-get install libreadline6 libreadline6-dev)

Libraries:
sudo apt-get install <library>

libxml2-dev 
libmysqlclient-dev 
libcurl4-openssl-dev 
libssl-dev 
libc6-dev 
libpq-dev
libxslt1-dev
libldap2-dev
libsasl2-dev
libffi-dev
libpcre++-dev
liblapack-dev 
libperl-dev 


Enter the Retro-Filei directory

$ cd Retro-Filei

Install the required R packages using install_R_packages.R

$ Rscript install_R_packages.R

Install the Python3 requirements 

$ pip3 install -r requirements.txt

Enter the /src directory

$ cd src

Set up the sqlite3 database via manage.py (this should be in the /src directory)

$ python3 manage.py makemigrations
$ python3 manage.py migrate

Install packages for rpy2

$ python3 manage.py runscript install_rpy2_packages

***Activate urls.py and views.py***

In retotransposons/views.py, remove the ''' from the start and end of the script to uncomment everything.

In group_project/urls.py:

*Remove the ''' symbols to uncomment the 'imports' section.

*Remove the closing bracket from urlpatterns=[] so it goes to urlpatterns = [

*Remove the ''' symbols from the start and end to uncomment contents of the urlpatterns list. Make sure the closing ] is in place.

These parts are commented out so that the database can be rebuilt without conflict.



Populate the database with the included sample csvs (containing 25% of the actual dataset se used). 

**Note: These scripts will produce a float type error upon completion. The cause for this remains unknown. It may be due to the last lines of the csv being empty. This only seems to happen in the manage.py shell.**

$ python3 manage.py runscript populate_database_LINE1
$ python3 manage.py runscript populate_database_HERV

This will take some time!

Once the populate_database.py script is finished, the website (should) be ready to go.

Start the local server:

$ python3 manage.py runserver

Open your favourite web browser and go to 127.0.0.1:8000/home

The Retro-Filei website should be running.







