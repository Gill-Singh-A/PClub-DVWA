document.getElementById('searchIPForm').addEventListener('submit', function (event) {
    document.getElementById("result").style.display = "block";
    event.preventDefault();
    var ip_addr = document.getElementById('ip').value;
    fetch('/ipDetails', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ip: ip_addr })
    })
        .then(response => response.json())
        .then(data => {
            let outputHTML = "<h2>IP Details</h2><p>";
            data.commandOutput.forEach(str => {
                outputHTML += `${str}<br />`;
            });
            outputHTML += "</p>";
            document.getElementById('result').innerHTML = outputHTML;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById("result").style.display = "none";
        });
});