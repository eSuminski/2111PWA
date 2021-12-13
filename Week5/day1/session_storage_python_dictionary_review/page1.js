// This is bad practice: don't send someones username and password around web pages. That being said, this is an example
// of how you COULD send data from one web page to another using session storage

const username = document.getElementById("username");
const password = document.getElementById("password");

function transfer(){
    // this is how you create a session object: it is a key value pair that is deleted when the browser or tab is closed
    sessionStorage.setItem("username", username.value);
    sessionStorage.setItem("password", password.value);

    if (sessionStorage.getItem("username") === "ericRev"){
        if (sessionStorage.getItem("password") === "supersecretpassword"){
            // you can use this to change to a new page
            window.location.href = "page2.html";
        }
    } else {
        alert("bad username and or password");
    }
    
}
