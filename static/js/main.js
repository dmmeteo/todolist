jQuery(document).ready(function ($) {

    $('.done').click(changeTask);

    function changeTask() {
        $.ajax({
            type: "GET",
            url: "task/change_status/",
            data:{
                'task_id':$(this).attr('data-task-id'),
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