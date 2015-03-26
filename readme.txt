Read Me file for The Walking Undead.

This readme assumes you have python 2.7 or above installed. if not, be downlaod and install from the offical python website at http://www.python.org/download/

If pip is not installed, please visit the offical python package website at https://pypi.python.org/pypi/setuptools/1.1.6 and download setuptools. Once downloaded and extracted navigate to the directory you extracted to via the command line, and enter "sudo python ez_setup.py". If running windows, do not enter the sudo command at the start. Once setup is installed, via the command line enter "sudo easy_install pip". Aain, windows users do not need to preface the command with Sudo. once Pip is installed, move onto the next step.

Navigate the the folder where TWU has been downloaded to, and via command line enter the command "pip install -r requirements.txt" This will install all the needed packages for the app.

Following this, it is recommended to set up a virtual enviroment for the app. Enter the command "mkvirtualenv twu", followed by "workon twu" to create and enter a new virtual enviroment for the app. 

Once everything is installed, navigate to the "The_walking_undead_project" folder, and enter command "python manage.py migrate" This will initalise the database. Then enter the command "python populate_twu.py" to add the test users to the database. If you experience errors whilst completing this step, please delete the migrations folder within at twu/the_walking_undead_project/twu, and then run the two commands again

The username for the test user is "test", and the password is also "test"