const username = document.getElementById("usernameInput")
const password = document.getElementById("passwordInput")

async function login(){
    let response = await fetch(
        // first add the url, then for the second input create an object literal
        " http://127.0.0.1:5000/login", {
            // first key value pair is the method verb
            method:"POST",
            // for header I include Content-Type so that my application knows what it is dealing with
            headers: {"Content-Type": "application/json"},
            // for my body I use the JSON.stringify() method and pass in an object literal of the body I wish to send
            // in order for that object to be converted into a json in the request
            body: JSON.stringify({"username":username.value, "password":password.value})
        }
    )
    // assuming I get a 200 status code in the response...
    if (response.status === 200){
        // I convert the response body from a json into an object literal
        let body = await response.json()
        if (body["validated"]){
            sessionStorage.setItem("validated", true)
            window.location.href = "player_page.html"
        } else {
            alert("login failed: please try again")
        }
    } else {
        alert("the request failed")
    }
}