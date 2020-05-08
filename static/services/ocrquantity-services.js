var ocrQuantity = function () {
    var api_url = '/api/ocr/api/ocrquantity/';
    return {
                create: function ( config) {
            return request('POST', api_url + 'create' ,  config);
        },
        edit: function (id, config) {
            return request('POST', api_url  + 'update/' +  id, config);
        },
        }
    }