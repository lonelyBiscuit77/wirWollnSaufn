# Skifahren und saufen und saufen und skifahren

# Install chrome driver
The script only works with chrome. You MUST use chrome. To install the correct chrome driver version first go to ```chrome://settings/help``` and check your version. 
Then download the correct version from [here](https://developer.chrome.com/docs/chromedriver/downloads) or [here](https://googlechromelabs.github.io/chrome-for-testing/#stable). Install the correct version for your OS (windows or mac), don't worry if the exact versions don't match, just make sure it's as close as possible. 

On mac I used: [this](https://storage.googleapis.com/chrome-for-testing-public/129.0.6668.58/mac-arm64/chromedriver-mac-arm64.zip) (used 24.09.24).

Unzip the zip file and you should see a chrome driver file in some folder, just move this file to the downloads folder. We need to move the chrome driver to system path. First open a new terminal window. For mac the command looks like this (you may get prompted for your password):
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

# Download the script and input your data

Download the script either with ```git clone``` or by clicking on the green ```code``` button up top and downloading the zip file and unzip it. 

Change directory using ```cd``` to go to the folder where you have the script. If it is in your downloads folder, the path probably looks something like this ```/Users/your_usernmae/Downloads/wirWollnSaufn``` Example where the scripts are in the folder ```wirWollnSaufn``` with the path ```/Users/your_usernmae/Downloads/wirWollnSaufn```:
```bash
cd /Users/your_usernmae/Downloads/wirWollnSaufn
``` 
you are now in the folder ```wirWollnSaufn```. This is where we will be running the scripts from. Type ```ls -l``` into the terminal to make sure you see the correct files.

Open the ```inputLogin.json``` file and input your values. 
[comment](Especially for the ```status``` field it is extremely important that you type in the exact text the dropdown menu would show.)
[comment](Don't mess this is up. Check on the hochschulsport page what option applies to you and write it exactly the way they do in the dropdown menu.)
The email and password are the account credentials used for your huchschulsport account. 
Save the file after modifying. 

# Testing
Change the default ```booking_url``` in the ```json``` file to some other booking that is currently open. 
For example: ```https://buchung.hsz.rwth-aachen.de/angebote/Sommersemester/_SUP_-_Stand_Up_Paddle.html```. 
You can now test whether everything works and you login successfully by running the ```davos_withLogin.py``` file. 
You should end up on the page final booking page that shows the button **kostenpflichtig buchen**.
If you don't end up on this page then something went wrong. 
You will **NOT** book the course, as you have to **MANUALLY** click the final conformation button **kostenpflichtig buchen**, so don't worry. 

Run (from the folder ```wirWollnSaufn```):
```bash
python3 davos_withLoign.py
```


# Run:
**IMPORTANT**: If you use the script ```davos_withLogin.py``` it assumes you **already** have a hochschulsport account. If you don't have one, go create one. 


The ```default booking_url``` stored in the json file is for the davos trip in march. Change that to whatever trip you want to take. 
Now you can run (from the folder ```wirWollnSaufn```) the script with:
```bash
python3 davosBook_withLogin.py
```
You can quit the running of the script with ```Ctrl + z```


The site refreshes every couple seconds and automatically detects the correct booking button depending on your age (whether you're above or below 26). If this fails you are still able to manually click the buttons. The rest should fill automatically. 
You will be brought to the final booking page where you have to **MANUALLY** click the final conformation button **kostenpflichtig buchen**. This button is not pressed automatically. 












