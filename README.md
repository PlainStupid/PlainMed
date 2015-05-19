# PlainMed
PlainMed is the ultimate personal medicine diary. 
Users can add their medicine to the webpage and be able to 
read more information about it through Lyfjabókin.is

## Install
To install, user should first install the environment needed to run.
Prerequest is Python 3 (3.4.3 works perfectly)

```
virtualenv
source env/bin/activate
pip install -r requirements.txt
```

Now you have two posibilities. You can run either scripts but not both.
  * ``python install_lyfjabok.py`` to install scraped data from Lyfjabókin.is.
    But this website is kind of broken because after page 18 the site doesn't
    display more medicine.
  * ``python install_lyfjaver.py`` to install scraped data from Lyfjaver.is.
    This scrape can't always make sure the links work to Lyfjabókin.is.

## Run
Now here comes the hardest part.

Run following command
```
python run.py
```

Thats it!


Got to http://127.0.0.1:8080 and enjoy
