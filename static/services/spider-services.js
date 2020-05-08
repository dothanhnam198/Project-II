var spiderService = function () {
    var api_url = '/api/spider/';
    return {
        saveSpider: function (config) {
            debugger
            return request('POST', api_url + '?cmd=save_spider' , config);
        },
        editSpider: function (id, config) {
            debugger
            return request('POST', api_url + '?cmd=save_spider&id=' + id , config);
        },
        deleteSpider: function (id) {
            debugger
            return request('POST', api_url + '?cmd=delete_spider&id=' + id);
        },
         getAllSpiders: function () {
            return request('POST', api_url + '?cmd=get_all_spiders');
        },
        createXpath: function (config) {
            debugger
            return request('POST', api_url + '?cmd=save_spider_xpath&id=' , config);
        },
        saveXpath: function (spider_id, config) {
            debugger
            return request('POST', api_url + '?cmd=save_spider_xpath&id=' + spider_id , config);
        },
        startCrawl: function (id, config) {
            debugger
            return request('POST', api_url + '?cmd=start_crawl&spider_id=' + id , config);
        },
        stopCrawl: function (pid, timestamp) {
            debugger
            return request('POST', api_url + '?cmd=stop_crawl&pid=' + pid + '&timestamp=' + timestamp);
        },
        getCrawlerConfig: function () {
            return request('POST', api_url + '?cmd=get_crawler_config');
        },
        saveCrawlerConfig: function (id, config) {
            return request('POST', api_url + '?cmd=save_crawler_config&id='+ id , config);
        },
        getAIConfig: function () {
            return request('POST', api_url + '?cmd=get_ai_config');
        },
        saveAIConfig: function (id, config) {
            return request('POST', api_url + '?cmd=save_ai_config&id='+ id , config);
        },
        getAllaimodel: function () {
            return request('POST', api_url + '?cmd=get_all_aimodel');
        },
        createAitraining: function ( config) {
            return request('POST', api_url + '?cmd=save_ai_train' , config);
        },
        saveAItraining: function (id, config) {
            return request('POST', api_url + '?cmd=save_ai_train&id='+ id , config);
        },
        getAllaitraining: function () {
            return request('POST', api_url + '?cmd=get_all_ai_train');
        },
    }
}