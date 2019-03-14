import './styles/app.css';

function changeGreeting() {
    let greeting = "Goodbye"

    let elementsByTagName = document.getElementsByTagName("H1");

    elementsByTagName[0].textContent = greeting;
}

setTimeout(changeGreeting, 5000);