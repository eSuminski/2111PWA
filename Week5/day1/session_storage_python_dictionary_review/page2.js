const header = document.createElement("h1");
header.textContent = `you logged in successfully`;
document.body.appendChild(header);

function logout(){
    sessionStorage.clear();
    window.location.href = "page1.html";
}