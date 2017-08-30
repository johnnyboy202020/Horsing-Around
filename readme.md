# Horsing Around
*Scraps data from the official web site of the horse races run in Turkey in order to forecast the race results.*

Official Web site of Turkish Jokey Organization:[Turkish](http://www.tjk.org/)|[English](http://www.tjk.org/EN/YarisSever/YarisSever/Index)

Abbreviations:
* ML: Machine Learning
* DL: Deep Learning
* BS: BeautifulSoup

## Brief Summary
Each day there are races in at least two cities and in those cities there are at least six races run for each city. The way to win the grand prize is to correctly guess the winners of the designated six race, this is called "Pick 6" in horse races. [more info](https://en.wikipedia.org/wiki/Pick_6_(horse_racing)). The goal of Horsing Around is to scrap the fixture and statics of each horse in order to leverage machine learning and deep learning algorithms. 

### Technical Summary
The entire project planned around Python and [Django](https://www.djangoproject.com). Suggested interpreter is [Anaconda](https://www.anaconda.com) 3.5 since it comes with ML and DL frameworks. Please be mindful of Django being only supported for version 3.5. For scrappers [BS](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) will be used. For future [Celery](http://www.celeryproject.org/) is going to be used in order to create workers that will scrap the statics automatically.


## Road Map
* Write tests for scrappers
* Develop the scrappers
* Start forecasting with regression and create HTML pages for display
* Create a worker to scrap races automatically in order to save them to database 


## Eager to help?
Everybody is welcome for contribution. THe ultimate reason for open-sourcing is to exceed the potential of this project and get the maximum accuracy, this cannot be done alone. Even small advices and suggestions are appreciated.