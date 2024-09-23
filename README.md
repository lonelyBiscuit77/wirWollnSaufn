# Skifahren und saufen und saufen und skifahren

# Install chrome driver
The script only works with chrome. You MUST use chrome. To install the correct chrome driver version first go to ```chrome://settings/help``` and check your version. 
Then download the correct version from [here](https://developer.chrome.com/docs/chromedriver/downloads) or [here](https://googlechromelabs.github.io/chrome-for-testing/#stable). Install the correct version for your OS (windows or mac), don't worry if the exact versions don't match, just make sure it's as close as possible. 

Unzip the zip file and you should see a chrome driver file in some folder, just move this file to the downloads folder. We need to move the chrome driver to system path. For mac the command looks like this (you may get prompted for your password):
```bash
sudo mv ~/Downloads/chromedriver /usr/local/bin/
```
# Create conda environment
Now [install conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) if you don't already have conda. 

Then create the environment we will be working in:
```bash
conda create -n davos
```
then enter the environment:
```bash
conda activate davos
```

In the env install selenium:
```bash
pip install selenium
```

Change directory using ```cd``` to go to the folder where you have the script. Example where the scripts are in the folder ```wirWollnSaufn``` with the path ```/Volumes/T7/HSS_buchung/own/wirWollnSaufn```:
```bash
cd /Volumes/T7/HSS_buchung/own/wirWollnSaufn
``` 
you are now in the folder ```wirWollnSaufn```.

Open the ```inputLogin.json``` file and input your values. Especially for the ```status``` field it is extremely important that you type in the exact text the dropdown menu would show. Don't mess this is up. Save the file after modifying. 

**IMPORTANT**: If you use the script ```davos_withLogin.py``` it assumes you **already** have a hochschulsport account. If you don't have one, go create one. 


# Run:
The ```default booking_url``` stored in the json file is for the davos trip in march. Change that to whatever trip you want to take. 
Now you can run (from the folder ```wirWollnSaufn```) the script with:
```bash
python3 davosBook_withLogin.py
```

The site refreshes every couple seconds and automatically detects the correct booking button depending on your age (whether you're above or below 26). If this fail you can are still able to manually click the buttons. The rest should fill automatically. 
You will be brought to the final booking page where you have to **MANUALLY** click the final conformation button **kostenpflichtig buchen**. This button is not pressed automatically. 


# Testing
Change the ```default booking_url``` to ```https://buchung.hsz.rwth-aachen.de/angebote/Sommersemester/_SUP_-_Stand_Up_Paddle.html```. 
You can now test whether everything works with the ```testSUP_withLogin.py``` file. This tests whether you are able to login successfully. You will **NOT** book the course so don't worry. 

Run (from the folder ```wirWollnSaufn```):
```bash
python3 testSUP_withLoign.py
```









