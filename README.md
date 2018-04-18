# ebcparser

This projects scrapes EBC RSS feeds for current currency exchange rates and provides them via REST Api

## 1. Installation
Enter following bash commands
```
sudo apt-get install git python3
git clone https://github.com/kelsohmm/ebcparser.git
cd ebcparser
pip install -r requirements.txt
python3 manage.py migrate
```

## 2. Usage
Scripts scrapes feeds provided in *feeds.py* file, feel free to change them

To populate database with latest currency exchange rates use:
> python3 manage.py scrape_feeds

To run server use:
> python3 manage.py runserver

To run tests use:
> python3 manage.py test

Api provides currency exchange rate at:
> serveraddress:serverport/$base_currency/$target_currency
