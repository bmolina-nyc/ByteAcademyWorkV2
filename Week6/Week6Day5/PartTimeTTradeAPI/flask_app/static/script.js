window.apikey = null
let deposit = document.getElementById('deposit')
let amount = document.getElementById('amount')
let apikey = document.getElementById('apikey')
let userbox = document.getElementById('username')
let passbox = document.getElementById('password')
let divlogin = document.getElementById('divlogin')
let divdeposit = document.getElementById('divdeposit')

function login_click() {
  let password = passbox.value
  let username = userbox.value
  let prom = fetch('/api/getkey', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json, text/plain, */*'
    },
    body: JSON.stringify({'username': username, 'password': password})
  });
  console.log(prom)
  prom.then(data => data.json()).then(json => {
    console.log(json)
    if (json.api_key === undefined) {
      passbox.value=""
      return null
    }
    // login successful
    window.apikey = json.api_key
    apikey.value = json.api_key
    console.log('hide')
    divlogin.classList.add('hide')
    divdeposit.classList.remove('hide')
    return json.api_key
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
      console.log(json)
      output.innerHTML = json.balance
    });
};
