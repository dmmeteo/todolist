jQuery(document).ready(function ($) {

    $('.done').click(changeTask);
    $('.close').click(changeTask);

    function changeTask() {
        var url = window.location.protocol+'//'+window.location.host+'/';
        var status = $(this).attr('data-status');

        if ($(this).attr('class') === 'done') {
            switch (status) {
                case 'active':
                    status = 'completed';
                    break;
                case 'completed':
                    status = 'active';
                    break;
                default:
                    status = 'active';
            }
        };

        $.ajax({
            type: "GET",
            url: url+"task/change_status/",
            data:{
                'task_id':$(this).attr('data-task-id'),
                'task_status': status,
            },
            dataType: "html",
            cache: false,
            success: function(data){
                if (data == 'ok'){
                    location.reload();
                }
            }
        });
    }
});