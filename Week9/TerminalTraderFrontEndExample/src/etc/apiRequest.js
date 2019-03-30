
function apiRequest(endpoint, method="get", data=null) {
  const baseUrl = 'http://127.0.0.1:5000';

  if (method === "get") {
    return fetch(baseUrl + endpoint, {
      method: "get",
      mode: "cors"
    });
  }
  else {
    return fetch(baseUrl + endpoint, {
      method: method,
      mode: "cors",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(data)
    });
  }
}

export default apiRequest;
