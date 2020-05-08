var ocrConfigService = function () {
    var api_url = '/api/ocr/';
    return {
        getOption: function () {
            return request('POST', api_url + '?cmd=get_option');
        },
        save: function (config, id = 0) {
            return request('POST', api_url + '?cmd=save_option&id=' + id, config)
        }
    }
}

