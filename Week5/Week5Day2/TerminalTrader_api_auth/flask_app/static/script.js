const button = document.getElementById('getprice')
const outputArea = document.querySelector('.display')
const inputArea = document.getElementById('ticker')

button.addEventListener('click', function(e) {
  e.preventDefault()
  
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
})

