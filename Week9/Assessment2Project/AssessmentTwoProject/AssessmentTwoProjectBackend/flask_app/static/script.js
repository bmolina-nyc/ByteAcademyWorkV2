window.apikey = null 

// navbar routes 
const navbar = document.getElementById('navbar')
const homeNav = document.getElementById("homeNav")
const tickerNav = document.getElementById("tickerNav")
const depositNav = document.getElementById("depositNav")
const buyNav = document.getElementById("buyNav")
const sellNav = document.getElementById("sellNav")
const tradesNav = document.getElementById("tradesNav")

// all forms
const loginForm = document.getElementById('form-login')
const tickerForm = document.getElementById('stockTicker')
const depositForm = document.getElementById('div-deposit')
const tradeForm = document.getElementById('trades')
const stockForm = document.getElementById('stock')
const sellForm = document.getElementById('stockSell')

const formbutton = document.getElementById('login')
const username_input =document.getElementById('username')
const password_input = document.getElementById('password')


// ticker form items
const inputArea = document.getElementById('tickerEntry')
const pricebutton = document.getElementById('getprice')
const outputArea = document.querySelector('.priceDisplay')

// trade form items
const inputAreaTrades = document.getElementById('tradesTicker')
const tickerbutton = document.getElementById('tradesByTicker')
const tradebutton = document.getElementById('tradesHistory')
const outputAreaTrades = document.querySelector('.tradesDisplay')

//buy stock items
const stockPriceButton = document.getElementById('getStockPrice')
const tickerPurchaseInput = document.getElementById('buy_ticker')
const amountPurchaseInput = document.getElementById("buy_amount")
const outputAreaStocks = document.querySelector(".stocksDisplay")

// sell stock items
const sellStockPriceButton = document.getElementById('sellStockButton')
const sellTickerPurchaseInput = document.getElementById('sell_ticker')
const amountSellInput = document.getElementById("sell_amount")
const outputAreaSellStocks = document.querySelector(".sellStocksDisplay")


// login
function login_click(e){
  formbutton.addEventListener('click', (e) => e.preventDefault())
  let username = username_input.value
  let password = password_input.value 
  let prom = fetch('http://127.0.0.1:5000/api/getkey', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json, text/plain, */*'
    },
    body: JSON.stringify({'username': username, 'password': password })
  });
  prom.then(response => response.json())
      .then(json => {
        console.log(json)
      if (json.api_key === undefined){
        password_input.value=""
        return null
      }
      window.apikey = json.api_key
      apikey.value = json.api_key
      loginForm.classList.add('hide')
      tickerForm.classList.remove('hide')
      navbar.classList.remove('hide')
  })

}

pricebutton.addEventListener('click', (e) => e.preventDefault())
function price_click(e){
  prom = fetch(`http://127.0.0.1:5000/api/price/${inputArea.value}`)
  prom.then(data => data.json())
      .then(json => { 
        if (json.error){
          outputArea.innerHTML = `<strong>Symbol not found</strong>`
        }else{
          outputArea.innerHTML = `The price of <strong>${json.symbol}</strong> is <strong>${json.price}</strong>`
        }
      }
    )
}


tickerbutton.addEventListener('click',(e)=> e.preventDefault())
function ticker_click(){
  outputAreaTrades.innerHTML = ""

  if (inputAreaTrades.value === ""){
    outputAreaTrades.innerHTML += `<strong>Please enter a value to look up</strong>`
    return null 
  } 

  prom = fetch(`http://127.0.0.1:5000/api/${window.apikey}/trades/${inputAreaTrades.value}`)
  prom.then(data => data.json())
  .then(json =>{ 
    if (Object.entries(json["trades"]).length === 0){
      outputAreaTrades.innerHTML += `<strong>You have no trades at this time for ${inputAreaTrades.value}</strong>`
      } 
    else {
        Object.keys(json["trades"]).forEach(key => {
          let trade = json["trades"][key]
          outputAreaTrades.innerHTML +=  `<ol><strong>TICKER: ${trade["ticker"]} || PRICE: ${trade["price"]} || VOLUME: ${trade["volume"]}</strong></ol>`
        }
      )
    }
  })
}
  

tradebutton.addEventListener('click',(e)=> e.preventDefault())
function trades_click(e){
  inputAreaTrades.value = ""
  outputAreaTrades.innerHTML = ""
  prom = fetch(`http://127.0.0.1:5000/api/${window.apikey}/alltrades`)
  prom.then(data => data.json())
    .then(json => {
      if (Object.entries(json["trades"]).length === 0){
        outputAreaTrades.innerHTML += `<strong>You have no trades at this time</strong>`
      } else {
        Object.keys(json["trades"]).forEach(key => {
          let trade = json["trades"][key]
          outputAreaTrades.innerHTML +=  `<ol><strong>TICKER: ${trade["ticker"]} || PRICE: ${trade["price"]} || VOLUME: ${trade["volume"]}</strong></ol>`
        }) 
      }
    })
}

function deposit_click() {
  let dep_prom = fetch(`/api/${window.apikey}/deposit`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'amount': parseFloat(amount.value)})
  })
  dep_prom.then(response => response.json())
    .then(json=>{
      const dollars = json.balance.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
      output.innerHTML = `<b>Your account balance is now $${dollars}</b>`
    });
};
 

// navbar functions
homeNav.addEventListener('click',(e)=> e.preventDefault())
tickerNav.addEventListener('click',(e)=> e.preventDefault())
depositNav.addEventListener('click',(e)=> e.preventDefault())
buyNav.addEventListener('click',(e)=> e.preventDefault())
sellNav.addEventListener('click',(e)=> e.preventDefault())
tradesNav.addEventListener('click',(e)=> e.preventDefault())

function showHome(){
  loginForm.classList.remove('hide')
  tickerForm.classList.add('hide')
  depositForm.classList.add('hide')
  tradeForm.classList.add('hide')
  stockForm.classList.add('hide')
}
function showTicker(){
  loginForm.classList.add('hide')
  tickerForm.classList.remove('hide')
  depositForm.classList.add('hide')
  tradeForm.classList.add('hide')
  stockForm.classList.add('hide')
  sellForm.classList.add('hide')
}
function showDeposit(){
  loginForm.classList.add('hide')
  tickerForm.classList.add('hide')
  depositForm.classList.remove('hide')
  tradeForm.classList.add('hide') 
  stockForm.classList.add('hide')
  sellForm.classList.add('hide')
}
function showBuy(){
  loginForm.classList.add('hide')
  tickerForm.classList.add('hide')
  depositForm.classList.add('hide')
  tradeForm.classList.add('hide') 
  stockForm.classList.remove('hide')
  sellForm.classList.add('hide')
}
function showSell(){
  loginForm.classList.add('hide')
  tickerForm.classList.add('hide')
  depositForm.classList.add('hide')
  tradeForm.classList.add('hide') 
  stockForm.classList.add('hide')
  sellForm.classList.remove('hide')
}
function showTrades(){
  loginForm.classList.add('hide')
  tickerForm.classList.add('hide')
  depositForm.classList.add('hide')
  tradeForm.classList.remove('hide') 
  stockForm.classList.add('hide')
  sellForm.classList.add('hide')
}

stockPriceButton.addEventListener('click', (e)=> e.preventDefault())
function buyStockClick(){
  let tickerValue = tickerPurchaseInput.value 
  let purchaseAmount = amountPurchaseInput.value

  if (tickerValue === "" || purchaseAmount === ""){
    outputAreaStocks.innerHTML += "<h2><b>Please enter a value for both fields</b></h2>" 
    return null
  }

  prom = fetch(`http://127.0.0.1:5000/api/${window.apikey}/buy/${tickerValue}/${purchaseAmount}`,{
         method: 'POST',
         headers: {
           'Content-Type': 'application/json'
         },
         body: JSON.stringify({"ticker":tickerValue, "amount":purchaseAmount})
         })
         prom.then(response => response.json() )
             .then(data => { 
              let balance = dollars = data.balance.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
              outputAreaStocks.innerHTML = `<h2>${data.username}: your new balance is  $${balance}</h2>` })
}

sellStockPriceButton.addEventListener('click', (e) => e.preventDefault())
function sellStockClick(){
  let stockToSell = sellTickerPurchaseInput.value
  let amountToSell = amountSellInput.value

  let prom = fetch(`http://127.0.0.1:5000/api/${window.apikey}/sell/${stockToSell}/${amountToSell}`,{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({"ticker":stockToSell, "amount": amountToSell})
    })
    prom.then(response => response.json())
    .then(data =>{
      let balance = dollars = data.balance.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
      outputAreaSellStocks.innerHTML = `<h2>${data.username}: your new balance is  $${balance}</h2>` 
    })
}