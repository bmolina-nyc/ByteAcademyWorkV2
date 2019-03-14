"use strict";   // Gabby: is this still a thing?

const searchTicker = document.querySelector('.search-ticker');
const tickerPrice = document.querySelector('.ticker-price');

function findMatch(e) {
  e.preventDefault();
  const ticker = (this.querySelector('[name=tickersearch]')).value;
  prom = fetch(`https://api.iextrading.com/1.0/stock/${ticker}/quote`);
  prom.then(blob => blob.json())
      .then(data => {showPrice(data)})
      .catch(err => {console.log(err)});
}

function showPrice (data) {
  console.log(price);
  let difference = price.week52High - price.week52Low

  const 
  const list = document.createElement('<ul>');
  list.classList.

  const close = document.createElement('<li>');
  close.appendChild(document.createTextNode(`The closing price of ${data.companyName} is: ${data.price.close}`));
  list.appendChild(close)

  const sector = document.createElement('<li>');
  sector.appendChild(document.createTextNode(`The primary industry is ${price.sector}`));
  list.appendChild(sector);

  const high = document.createElement('<li>');
  high.appendChild(document.createTextNode(`The 52-week high is ${price.week52High}`));
  list.appendChild(high);

  const low = document.createElement('<li>');
  low.appendChild(document.createTextNode(`The 52-week low is ${price.week52Low}`));
  list.appendChild(low);
  
  const difference = document.createElement('<li>');
  difference.appendChild(document.createTextNode(`Which is a difference of ${difference}`));
  list.appendChild(difference);

  tickerPrice.
}
