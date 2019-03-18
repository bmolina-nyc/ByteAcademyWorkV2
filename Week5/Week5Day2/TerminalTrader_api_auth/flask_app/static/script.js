window.apikey = null 

const loginform = document.getElementById('form-login')
const stockform = document.getElementById('stock')

const formbutton = document.getElementById('login')
const username_input =document.getElementById('username')
const password_input = document.getElementById('password')

const navbar = document.getElementById('navbar')

// ticker items
const inputArea = document.getElementById('ticker')
const pricebutton = document.getElementById('getprice')
const outputArea = document.querySelector('.priceDisplay')

// trade items
const inputAreaTrades = document.getElementById('tradesTicker')
const tickerbutton = document.getElementById('tradesByTicker')
const tradebutton = document.getElementById('tradesHistory')
const outputAreaTrades = document.querySelector('.tradesDisplay')


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
      loginform.classList.add('hide')
      stockform.classList.remove('hide')
      navbar.classList.remove
      ('hide')
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
  prom = fetch(`http://127.0.0.1:5000/api/${window.apikey}/trades/${inputAreaTrades.value}`)
  prom.then(data => data.json())
  .then(json =>{
    if (Object.entries(json["trades"]).length === 0){
      outputAreaTrades.innerHTML += `<strong>You have no trades at this time for ${inputAreaTrades}</strong>`
      } else {
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

 