window.onload = function() {
    fetch(`/getFileList?user=${user}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        displayFileList(data);
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
};
function displayFileList(files) {
    const fileListElement = document.getElementById('files');
    fileListElement.innerHTML = '';
    files.forEach(file => {
        const listItem = document.createElement('li');
        const a = document.createElement('a');
        a.href = '/download?file=' + user + '/' + file;
        a.class = "fileLink";
        a.textContent = file;
        listItem.appendChild(a);
        fileListElement.appendChild(listItem);
    });
}