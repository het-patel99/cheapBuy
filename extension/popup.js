document.addEventListener('DOMContentLoaded', () => {
    const dialogBox = document.getElementById('dialog-box');
    const query = { active: true, currentWindow: true };

    function fetch_data(tabs){
        var headers = {}
        const response = fetch('http://127.0.0.1:5000/scrap?link='+tabs[0].url, {
            method: 'POST',
            headers: headers
          }).then(response => response.json()).then(data => data)
    }    

    chrome.tabs.query(query, async (tabs) => {
              
        var headers = {}
        const response = await fetch('http://127.0.0.1:5000/scrap?link='+tabs[0].url, {
            method: 'POST',
            headers: headers
          });

        myJson = await response.json()
        console.log(myJson)
        // })
        
        const barkTitle = 'hehe, get started with se project.'+myJson['url']
        dialogBox.innerHTML = barkTitle;
    });
});

