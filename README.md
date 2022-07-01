# ETM Project 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

## Overview
lo scopo del progettto,  è quello di investigare il consumo energetico di varie cryptovalute, mettendo a confronto diversi algoritmi di consenso. Per questo, dopo aver raccolto numerosi dati da svariati papers pubblicati, nella seconda parte del progetto è stato creato un sondaggio, le cui risposte sono state analizzate attraverso uno script in Python, mediante l'utilizzo di alcune famose librerie come:
- Pandas
- Matplotlib
- Seaborn

## Usage

Assicurati anzitutto di avere installato tutte le librerie necessarie, altrimenti puoi installarle con il seguente comando:
``` bash
pip install -r  requirements.txt
```
Lo script ha come parametro necessario "criteria" che va specificato da riga di comando:
``` bash
python .\ETMProject.py earnings 
```
E' possibile salvare tutti i grafici in una volta sola nella cartella plots (senza visualizzarli) con il parametro "save-all":
``` bash
python .\ETMProject.py save-all
```
> per visualizzare tutti i possibili parametri puoi usare il comando di help:
``` bash
python .\ETMProject.py -h
```

### Parametri Opzionali

E' possibile avere un output con più informazioni passando come flag "-v o "--verbose":
``` bash
python .\ETMProject.py earnings -v
```
E' possibile stampare una tabella riepilogativa passando come flag "-t" o "--table":
``` bash
python .\ETMProject.py earnings -t
```
E' possibile salvare i grafici nella cartella plot passando come flag "-s" o "--save":
 ``` bash
python .\ETMProject.py earnings -s
```
