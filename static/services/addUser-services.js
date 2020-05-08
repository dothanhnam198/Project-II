var addUser = function () {
    var api_url = '/api/users/';
    return {
        register: function (config) {
            return request('POST', api_url + 'register', config);
        },
         password_reset: function (config) {
            return request('POST', api_url + '?cmd=password_reset', config);
        },
        password_reset_confirm: function (config) {
            return request('POST', api_url + '?cmd=password_reset_confirm', config);
        },
    }
}