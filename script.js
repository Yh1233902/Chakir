
function checkPassword() {
    let pw = document.getElementById("password").value;
    if (pw === "221133") {
        document.getElementById("login-screen").style.display = "none";
        document.getElementById("main-screen").style.display = "block";
    } else {
        alert("كلمة السر خاطئة");
    }
}
function submitLink() {
    let link = document.getElementById("linkInput").value;
    fetch("/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({link: link})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("responseArea").innerHTML = data.message;
        if (data.message.includes("انتظار")) {
            pollForResponse(link);
        }
    });
}
function pollForResponse(link) {
    setInterval(() => {
        fetch("/check", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({link: link})
        })
        .then(res => res.json())
        .then(data => {
            document.getElementById("responseArea").innerHTML = data.message;
        });
    }, 3000);
}
