window.latest = 0;
let chatbox = document.getElementById('chatbox')
const ENDPOINT = 'getKitchenMentions'
function update() {
    let url = `/${ENDPOINT}?id=1&latest=${window.latest}`
    xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.responseType = 'json';
    xhr.send();
    xhr.onreadystatechange = (e) => {
        if (xhr.readyState == 4 && xhr.status == 200) {
            data = xhr.response
            if (data.count != 0) {
                window.latest = data.data[0].id
                writeData(data.data)
            }
        }
    }
}
function writeData(data) {
    for (k in data) {
        chatbox.innerHTML += `<span>${data[k].text}</span><br>\n`;
    }
}
update()
window.setInterval(update, 3000);