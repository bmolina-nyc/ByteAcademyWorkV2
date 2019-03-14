const button = document.getElementById("getprice")
const ticker = document.getElementById("ticker")
const outputdiv = document.querySelector(".priceDisplay")
const spandisplay = document.querySelector(".priceDisplay .display")

button.addEventListener("click", function(e) {
  e.preventDefault()
  const symbol = encodeURIComponent(ticker.value)
  const promise = fetch(`http://127.0.0.1:5000/price/${symbol}`)
  promise.then(data => {
          return data.json()
        })
        .then(data => {
          if (data.error === 404) {
            console.log('err')
          spandisplay.innerHTML = `
              <b>Not Found</b>
            `
          }
          else {
          console.log(data)
          spandisplay.innerHTML = `
            <b>price = ${data.price}</b>
            `
         }})
         .catch(e => {
          console.log(e);
         });
});
