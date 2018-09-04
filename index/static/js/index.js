// 文章页面样式优化
$(document).ready(function () {
    $(".post img").addClass("fancybox-img");
    $(".post img").wrap(function () {
        var thisSrc = $(this).attr("src");
        return "<a class='fancybox-a' href='" + thisSrc + "'></a>"
    });
    $(".fancybox-a").fancybox();
});

// 返回顶部
$(document).ready(function () {
    $(".back-to-top").hide();
    var height = $(window).height();
    $(window).scroll(function () {
        if ($(window).scrollTop() > height) {
            $(".back-to-top").fadeIn(500);
        } else {
            $(".back-to-top").fadeOut(500);
        }
    });
    $('.back-to-top').click(function () {
        $('body,html').animate({
            scrollTop: '0px'
        }, 900);
    });
});

// 文章评论

// 表单验证
function checkVal(e) {
    var flag = 0;
    if ($(e).val() == "") {
        $(e).removeClass("is-valid");
        $(e).addClass("is-invalid");
        $(e).next('.invalid-feedback').html('请填写此字段！');
        flag ++;
    } else {
        $(e).removeClass("is-invalid");
        $(e).addClass("is-valid");
        $(e).next('.invalid-feedback').html('');
    }
    return flag;
}

function checkEmail(e) {
    var flag = 0;
    var re = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (!re.test($(e).val())) {
        $(e).removeClass("is-valid");
        $(e).addClass("is-invalid");
        $(e).next('.invalid-feedback').html('字段格式错误！');
        flag++;
    } else {
        $(e).removeClass("is-invalid");
        $(e).addClass("is-valid");
        $(e).next('.invalid-feedback').html('');
    }
    return flag;
}

function checkFrom() {
    return checkVal($('#nicname')) + checkVal($('#content')) + checkEmail($('#email'));
}

// 提交评论
$(document).ready(function () {
    $('#commentBtn').on('click', function () {
        if (checkFrom() == 0) {
            $.ajax({
                cache: false,
                type: "POST",
                url: "/add_comment/",
                data: $('#commentForm').serialize(),
                dateType: "json",
                async: true,
                beforeSend: function (xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
                },
                success: function (data) {
                    if (data.status == 1) {
                        layer.msg(data.msg);
                        setTimeout(function () {
                            window.location.reload();
                        }, 800);
                    } else if (data.status == -1) {
                        layer.msg(data.msg);
                    }
                },
            });
        }
    });
});