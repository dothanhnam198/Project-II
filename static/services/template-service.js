var templateService = function () {
    var api_url = '/api/ocr/';
    return {
        getTemplate: function (id) {
            return request('POST', api_url + '?cmd=get_template&id=' + id)
        },
        saveTemplate: function (id, model) {
            return request('POST', api_url + '?cmd=save_template&id=' + id, model)
        },

        //template area
        getTemplateAreasByTemplate: function (template_id) {
            return request('POST', api_url + '?cmd=get_list_template_area&template_id=' + template_id)
        },
        saveTemplateArea: function (id, model) {
            return request('POST', api_url + '?cmd=save_template_area&id=' + id, model)
        },
        deleteTemplateArea: function (id) {
            return request('POST', api_url + '?cmd=delete_template_area&id=' + id)
        },
        uploadImage: function (file) {
            return new Promise((resolve, reject) => {
                let reader = new FileReader();
                reader.onload = function (event) {
                    let uploadImage = {
                        data: btoa(event.target.result),
                        size: file.size,
                        name: file.name,
                        type: file.type
                    }
                    return request('POST', api_url + '?cmd=upload_template_file', JSON.stringify(uploadImage))
                        .then(res => resolve(res))
                        .catch(err => reject(err))
                }
                reader.readAsBinaryString(file);
            })
        }
    }
}