// I want to automatically get all player information when I pull up the page


const playerTable = document.getElementById("playerTable");
const playerTableBody = document.getElementById("playerBody");
const teamTable = document.getElementById("teamTable");
const teamTableBody = document.getElementById("teamBody");


async function getAllPlayerData(){
    let url = "http://127.0.0.1:5000/player";

    let response = await fetch(url);
    
    if (response.status === 200){
        let body = await response.json();
        populateData(body);
    } else {
        alert("There was a problem trying to get the player information: sorry!");
    }
}

async function getAllTeamData(){
    let url = "http://127.0.0.1:5000/team";

    let response = await fetch(url);

    if (response.status === 200){
        let body = await response.json();
        // need to implement this!
        populateTeamData(body);
    } else {
        alert("There was a problem trying to get the team information: sorry!");
    }
}

function populateData(responseBody){
    
    

    for (let player of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${player.teamId}</td><td>${player.playerId}</td><td>${player.firstName}</td><td>${player.lastName}</td><td>${player.jerseyNumber}</td>`;
        playerTableBody.appendChild(tableRow);
    }
}

getAllPlayerData()