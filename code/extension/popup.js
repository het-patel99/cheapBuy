document.addEventListener('DOMContentLoaded', () => {
    const dialogBox = document.getElementById('dialog-box');
    const query = { active: true, currentWindow: true };

    chrome.tabs.query(query, async (tabs) => {
              
        var headers = {}
        // console.log("***** Item Search Started on source site! *****")
        const response = await fetch('http://127.0.0.1:8080/scrap?link='+tabs[0].url, {
            method: 'POST',
            headers: headers
          });
        // console.log("***** Item Search ended on source site! *****")
        myJson = await response.json()
        console.log(myJson)
       
        var web_response = ''
       
        for(let i=0;i<myJson['url'].length;i++){
            web_response += '<div class="box"><h3>'+myJson['site'][i]+'</h3><br><h5>Product Name: '+myJson['description'][i]+'</h5><br><a href='+myJson['url'][i]+'><button class="button"><span>View this product</span></button></a><br><h6> Price:'+myJson['price'][i]+'</h6></div><br>'

        }
        dialogBox.innerHTML = web_response;
    });
});

