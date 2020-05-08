function request(method, url, body = null, options = null) {
    $('#loadingIcon').removeClass('hide');
    if (!options)
        options = {
            contentType: 'application/json',
            dataType: 'json'
        }
    if (method == 'GET' || method == 'DELETE')
        return $.ajax({
            method: method,
            url: url,
            ...options
        }).always(() => {
            $('#loadingIcon').addClass('hide');
        });
    else
        return $.ajax({
            beforeSend: function (xhrObj) {
                xhrObj.setRequestHeader("Authorization", "Token " + localStorage.getItem('token'));
            },
            method: method,
            url: url,
            ...options,
            data: body
        }).always(() => {
            $('#loadingIcon').addClass('hide');
        });
}

function alert(message, title = 'Thông báo') {
    $.alert({
        title: title,
        content: message,
    });
}