# Hummingbird
Final Project for CSE-30332 (Programming Paradigms - Fall 2019) at the University of Notre Dame.  
Group Members:
- Ascolese, Emma     (emmaascolese)
- Cocco, Chad         (ccocco)
- Keene, Stephanie   (skeene)
- Quinn, John        (johnedquinn)

## Project Goals
The goal of this project was to create a simulation of a stock trading platform.

## Framework

### Server
The server was initialized using CherryPy to handle client requests and return formatted data about real-time stocks. This server used RapidAPI's YahooFinance API to handle real-time data.

### Client
The client used Bootstrap, Javascript, jQuery, and Charts.js to create the website.

## To Run
In order to run the server, enter the `server` directory and run `python3 main.py`. Before starting the client, make sure to wait several seconds (approx. 10-20 seconds), as the server is grabbing data from several outside sources on the initial startup. After waiting, the site can be viewed from `http://student04.cse.nd.edu/jquinn13/cse-30332-fa19-final-project/client/`.

## Screenshots
### Home Page
![Alt text](./client/images/home_page.png?raw=true "Home Page")
### Account Page
![Alt text](./client/images/account_page.png?raw=true "Account Page")
### Search Results
![Alt text](./client/images/search.png?raw=true "Search Results")
### Purchase Modal
![Alt text](./client/images/purchase.png?raw=true "Purchase Modal")