(function () {
    $(function () {
        $('.related-widget-wrapper select').addClass('form-control select2');
        $('.related-widget-wrapper select').select2({});
        $('.select2').select2({});

        $('.datepicker').datepicker({
            autoclose: true,
            format: 'dd/mm/yyyy'
        });

        $('.datepicker').attr('autocomplete', 'off');

        $('.daterange').daterangepicker({
            autoUpdateInput: false,
            locale: {
                format: 'DD/MM/YYYY'
            }
        });

        $('.daterange').on('apply.daterangepicker', function (ev, picker) {
            $(this).val(picker.startDate.format('DD/MM/YYYY') + ' - ' + picker.endDate.format('DD/MM/YYYY'));
        });

        $('.timepicker').timepicker({
            showInputs: false
        });

        $('.js-toggle-advance-search').on('click', function () {
            $(this).closest('.box').find('.advance-search-control-container').toggleClass('hide');
            $(this).find('i').toggleClass('fa-angle-double-down');
            $(this).find('i').toggleClass('fa-angle-double-right');
        });

        $('.nav-tabs').find('li a[data-toggle=tab]').on('click', function (e) {
            debugger
            e.preventDefault();
            $(this).closest('.nav-tabs').find('li').removeClass('active');
            $(this).closest('li').addClass('active');
            $(this).closest('.nav-tabs').siblings('.tab-content').find('.tab-pane').removeClass('active');
            $(this).closest('.nav-tabs').siblings('.tab-content').find('div' + $(this).attr('href')).addClass('active');
        });

        $(document).off('click').on('click', '.js-btn-util-delete', function () {
            let url = $(this).attr('data-url');
            $.confirm({
                title: 'Thông báo',
                animation: 'opacity',
                animationSpeed: 100,
                content: `<form method="post" action="` + url + `"><input type="hidden" name="csrfmiddlewaretoken" value="tVb0pm3nGnbtb87aOOzRz49A3hILlw5KW5KZhDHeui20Ex7EBu0GX6GW5GNHFo72">
                            <div>
                            <p>Bạn có chắc chắn muốn xóa bản ghi này?</p>
                            <input type="hidden" name="post" value="yes">
<!--                            <input type="submit" class="btn btn-primary" value="Xác nhận">-->
                            </div>
                           </form>`,
                buttons: {
                    formSubmit: {
                        text: 'Xác nhận',
                        btnClass: 'btn-primary',
                        action: function () {
                            let form = this.$content.find('form');
                            form.submit();
                        }
                    },
                    cancel: {
                        text: 'Hủy',
                        btnClass: 'btn-default',
                        action: function () {
                            return true;
                        }
                    },
                },
            })
        });

        $(document).on('change', '.js-change-page-size', function () {
            if ($('select[name=action]').length > 0) {
                $('select[name=action]').val('change_page_size');
            } else {
                // if there isn't action dropdown => create one
                $(this).closest('form#changelist-form').append(`<select name="action" class="hide">
                                                                    <option value="change_page_size" selected></option>
                                                                </select>`);
            }
            $(this).closest('form#changelist-form').submit();
        });

        $(document).on('change', '.manual-build-page .js-change-page-size', function () {
            location.href = '?' + $(this).attr('data-query') + '&page_size=' + $(this).val();
        });

        $(document).on('keypress', '.js-input-page', function (e) {
            if (e.keyCode == 13) {
                let max_page = $(this).attr('data-max-page');
                if ($(this).val() > max_page) {
                    $(this).val(max_page);
                } else if ($(this).val() < 1) {
                    $(this).val(1);
                }

                let url = '?' + $(this).attr('data-query');
                if ($(this).attr('data-page-size')) {
                    url += '&page_size=' + $(this).attr('data-page-size') + '&page=' + $(this).val();
                }
                location.href = url;
            }
        });

        $(document).on('submit', 'form.advance-search-form', function (e) {
            let formData = $(this).serializeArray();
            let formValueToSubmit = "";
            for (let i = 0; i < formData.length; i++) {
                formValueToSubmit += ",," + formData[i].name + "=" + formData[i].value
            }
            $(this).find('[name]').removeAttr('name');
            $(this).append('<input type="hidden" name="q" value="' + formValueToSubmit + '" />');
            return true;
        });

        $(document).on('click', '.dropdown-toggle', function () {
            $(this).siblings('.dropdown-menu').toggle();
        });
        
        // $(document).on('click', '#js-ocr', function () {
        //     //ajax api lay cau hinh + cau hinh nhanh (lang, page)
        //     alert(4)
        // });
    });
})();