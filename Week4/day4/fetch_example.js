// we are going to write some code to send a request to the PokeAPI and then we are going to dynamically
// display some of the information we recieve on our web page.

const url = "https://pokeapi.co/api/v2/pokemon/";

let button = document.getElementById("getData");
button.onclick = getData;
let data = document.getElementById("data");
let x = 10
do{
    console.log(x);
} while (x < 10)

async function getData(){
    let userInput = document.getElementById("numberInput");

    
    data.innerHTML = "";

    console.log(url + userInput.value);
    let response = await fetch(url + userInput.value);

    if (response.status === 200){
        let information = await response.json()
        populateData(information);
        console.log(information);
    } else {
        data.textContent = "It got away!";
    }
}

function populateData(json){
    let pokeName = document.createElement("h3")
    pokeName.textContent = json.name;
    data.appendChild(pokeName);
    let abilityList = document.createElement("ul");
    let abilities = json.abilities;
    for (let ability of abilities){
        let abilityHolder = document.createElement("li");
        abilityHolder.innerHTML = ability.ability.name;
        abilityList.appendChild(abilityHolder);
    }
    data.appendChild(abilityList);

    let sprites = json.sprites;
    let linksArray = []
    let index = 0;
    for (let img in sprites){
        linksArray[index] = sprites[img];
        index++;
    }
    for (let i = 0; i < linksArray.length - 2; i++){
        if(linksArray[i]){
            let spriteImage = document.createElement("img");
            spriteImage.src = linksArray[i];
            data.appendChild(spriteImage)
        }
    }

    console.log(linksArray)
    

}