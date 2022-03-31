# ETM Project 

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
 
