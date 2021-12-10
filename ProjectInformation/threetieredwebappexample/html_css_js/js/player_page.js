// I want to automatically get all player information when I pull up the page


const table = document.getElementById("playerTable");
const tableBody = document.getElementById("playerBody");

async function getAllPlayerData(){
    let url = " http://127.0.0.1:5000/player";

    let response = await fetch(url);
    
    if (response.status === 200){
        let body = await response.json();
        populateData(body);
    } else {
        alert("There was a problem trying to get the player information: sorry!");
    }
}

function populateData(responseBody){
    
    

    for (let player of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${player.teamId}</td><td>${player.playerId}</td><td>${player.firstName}</td><td>${player.lastName}</td><td>${player.jerseyNumber}</td>`;
        tableBody.appendChild(tableRow);
    }
}

getAllPlayerData()