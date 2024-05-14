function getBlogDetail(blogIndex, part) {
    fetch(`/getBlogDetail?blog=${blogIndex}&part=${part}`)
    .then(response => response.text())
    .then(data => {
        if (part === 'title') {
            document.getElementById(`blogTitle${blogIndex}`).innerText = data;
        } else if (part === 'content') {
            document.getElementById(`blogContent${blogIndex}`).innerText = data;
        } else if (part === 'link') {
            document.getElementById(`blogLink${blogIndex}`).setAttribute("href", data);
        }
    })
    .catch(error => console.error('Error:', error));
}
for (let blogIndex = 0; blogIndex <= 5; blogIndex++) {
    document.getElementById('blogs').innerHTML += `
        <div class="blog">
            <a id="blogLink${blogIndex}" class="blogLink">
                <h2 id="blogTitle${blogIndex}" class="blogTitle"></h2>
                <p id="blogContent${blogIndex}" class="blogContent"></p>
            </a>
        </div>
    `;
    getBlogDetail(blogIndex, 'title');
    getBlogDetail(blogIndex, 'content');
    getBlogDetail(blogIndex, 'link');
}