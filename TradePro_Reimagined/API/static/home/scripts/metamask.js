function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


const showAccount = document.querySelector('.showAccount');


async function integrate_metamask(){

    const csrftoken = getCookie('csrftoken');

    const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
    const account = accounts[0];
    const payload = {account_num : account};
    
    var jsonString = JSON.stringify(payload);

    // return axios.post('receive_web_3_info', payload)
    const xhr = new XMLHttpRequest();

    xhr.open("POST","/receive_web_3_info");
    xhr.setRequestHeader('X-CSRFToken', csrftoken);
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");
    console.log(jsonString);

    xhr.send(jsonString);

    // console.log(xhr);
    // request options
    
}
