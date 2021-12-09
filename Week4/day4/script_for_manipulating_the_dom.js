let elementOpen = "<p>"
let elementClose = "</p>"

// this is a simple way to add an element to the dom
let myDiv = document.createElement("div");
// I can use back tics here to allow for string interpolation
myDiv.innerHTML = `${elementOpen}this was created, alongside the div container, using JavaScript${elementClose}`;
// this appends the myDiv element as the last child of the body element
document.body.appendChild(myDiv);

// it is even easier to remove elements from the dom
document.body.removeChild(myDiv);

document.body.appendChild(myDiv);

// you can also replace elements instead of just deleting them

// create the new element
let newDiv = document.createElement("div")
// create any internal html and/or text
newDiv.innerHTML = `${elementOpen}this is a new div container that is replacing the old one${elementClose}`;
// call the replaceChild method from the parent node, which is referenced by the element you are replacing
myDiv.parentNode.replaceChild(newDiv, myDiv);

// you can use JavaScript to populate lists and tables dynamically

// first create your list element and append it to your dom
let animalList = document.createElement("ul");
document.body.appendChild(animalList);

// then create the content to add to the list
let bear = "Bear";
let cat = "Cat";
let wolf = "wolf";

// create a function to add the content into a list element
function addAnimal(animal){
    let li = document.createElement("li");
    li.textContent = animal;
    return li;
}

// and now you can append the data to your list
animalList.appendChild(addAnimal(bear));
animalList.appendChild(addAnimal(cat));
animalList.appendChild(addAnimal(wolf));

let names = ["Eric", "Sam", "Luke"];

let nameList = document.createElement("ol");
nameList.id = "names";
document.body.appendChild(nameList);

function addName(name){
    let li = document.createElement("li");
    li.textContent = name;
    return li;
}

// this is the long-hand way of iterating through an array
// for (let i = 0; i < names.length; i++){
//     nameList.appendChild(addName(names[i]));
// }

// this is the short-hand way of iterating through the content of an array
for (let name of names){
    nameList.appendChild(addName(name));
}


// you can do the same with objects, but use the in key word instead.
let myObject = {
    name:"Eric",
    job:"Instructor"
}

for (let key in myObject){
    console.log(myObject[key]);
}

// this is how you can add an element before the first child element that already exists
nameList.insertBefore(addName("Kyla"),nameList.firstChild);

// but what if I wanted to do the second or third element that already exists?
let newLi = document.createElement("li");
newLi.textContent = "Alejandro";
// you need to make use of the nextSibling property to go beyond the first element child
nameList.insertBefore(newLi,nameList.firstElementChild.nextElementSibling);

// there are a few different ways you can access elements on the dom (this list is not exhaustive)

/*
    firstElementChild returns the first child element of the node
    lastElementChild returns the last child element of the node
    nextElementSibling returns the next sibling of the selected element, or returns null
*/

// text content should be used when you just want the text of an element, whereas innerHTML should be used when you need
// to access the tags as well

let example = document.createElement("div")
example.innerHTML = `${elementOpen}the text will appear with both innerHTML and textContent${elementClose}`
document.body.appendChild(example);

alert("using textContent: " + example.textContent); // only will show text
alert("using innerHTML: " + example.innerHTML); // shows the tags as well



