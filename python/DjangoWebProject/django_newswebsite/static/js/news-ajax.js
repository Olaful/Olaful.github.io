$('#likes').click(
    function()
    {
        var nCateid;
        nCateid = $(this).attr("data-catid");
        // ajax请求
        $.get(
            '/news/like/', 
            {"category_id": nCateid},
            // data 请求后返回的数据
            function(data)
            {
                $('#like_count').html(data);
                $('#likes').hide();
            }
        );
    }
)

$('#suggestion').keyup(
    function()
    {
        var strQuery;
        strQuery = $(this).val();
        $.get(
            '/news/suggest/', 
            {"query": strQuery},
            function(data)
            {
                // 解析成json
                // var jsonObj = eval('(' + data + ')');
                // var aryObj = jsonObj.name;
                // var html = "";
                // if (aryObj != undefined)
                // {
                //     for (var i = 0; i < aryObj.length; i++)
                //     {
                //         html += '<li class="list-inline">'+aryObj[i]+'</li>'
                //     }
                // }
                $('#cates').html(data);
            }
        );
    }
)

$(".news-page-add").click(
    function()
    {
        var cate_id = $(this).attr('data-catid');
        var title = $(this).attr('data-title');
        var url = $(this).attr('data-url');
        var my = $(this);

        $.get(
            '/news/add_page/',
            {"cate_id": cate_id, "title": title, "url": url},
            function(data)
            {
                $("#pages").html(data);
                my.hide()
            }
        );
    }
)