var ocrService = function () {
    var api_url = '/api/config/';
    return {
        createConfig: function (config) {
            debugger
            return request('POST', api_url + '?cmd=insert_config', config);
        },
        saveSpider: function (id, config) {
            debugger
            return request('POST', api_url + '?cmd=save_spider', config);
        },
    }
}