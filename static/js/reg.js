// 注册校验

function check_name(username) {
    var flag = 0
    if (username == "") {
        flag = '用户名不能为空';
    }
    if (username.length < 5 || username.length > 16) {
        flag = '用户名长度为5~16';
    }
    $.ajax({
        type: "GET",
        contentType: "appliction/json; charset=UTF-8",
        dataType: "json",
        url: "/check_username",
        async:false,
        data: "username=" + username,
        timeout: 1000,
        success: function(data) {
            console.log(data);
            if (data["err"] === 0) {
                flag = 0;
            }
            else {
                flag = '用户名已注册';
            }
        },
        error: function () {
            flag = '服务器错误';
        }
    });
    return flag;
};

function check_password(password) {
    if (password == "") {
        return '密码不能为空'
    }
    if (password.length < 5 || password.length > 16) {
        return '密码长度为5~16'
    }
    return 0
};

function check_password1(password1, password) {
    if (password1 !== password) {
        return '密码不一致'
    };
    return 0;
}

function check_phone(phone){
    if (phone == "") {
        return '手机号不能为空'
    }
    if (!(/^1[3456789]\d{9}$/.test(phone))){
        return '手机号格式有误'
    }
    return 0
}

$(function() {
    $("#username").blur(function() {
        var username = $("#username").val();
        if ( !username ) {
            return;
        };
        var flag = check_name(username);
        if (flag === 0) {
            $(".feedback").css("color", "green");
            $(".feedback").text("用户名可注册！");
        } else {
            $("#username").val("");
            $("#username").attr("placeholder", flag);
        };
    });


    $("#password").blur(function(){
        var password = $("#password").val();
        var flag = check_password(password);
        if (flag !== 0) {
            $("#password").val("");
            $("#password").attr("placeholder", flag);
        };
    });

    $("#password1").blur(function(){
        var password = $("#password").val();
        var password1 = $("#password1").val();
        var flag = check_password1(password1, password)
        if (flag !== 0) {
            $("#password1").val("");
            $("#password1").attr("placeholder", flag);
        };
    });

    $("#phone").blur(function(){
        var phone = $("#phone").val();
        var flag = check_phone(phone);
        if (flag !== 0) {
            $("#phone").val("");
            $("#phone").attr("placeholder", flag)
        };
    });

    // $("#email").blur(function(){
    //     var email = $("#email").val();
    //     if (email == "") {
    //         $("#email").attr("placeholder", "邮箱不能为空");
    //         return;
    //     }
    //     vemail = true;
    // });

    $("#btn_reg").click(function() {
        var username = $("#username").val();
        var password = $("#password").val();
        var password1 = $("#password1").val();
        var phone = $("#phone").val();
        var flag1 = check_name(username);
        var flag2 = check_password(password);
        var flag3 = check_password1(password1, password);
        var flag4 = check_phone(phone);
        console.log(flag1, flag2, flag3, flag4);
        if (flag1 && flag2 && flag3 && flag4) {
            $(".feedback").css("color", "red");
            $(".feedback").text("信息不完整");
            alert("请输入完整信息！")
            return false;
        };
        return true;
    });
});


// function reg_verify() {
//     var username = $("#username").val();
//     username = username.replace(/^\s+|\s+$/gm, '');
//     var password = $("#password").val();
//     var password1 = $("#password1").val();
//     var phone = $("#phone").val();
//     var email = $("#email").val();
//     if (username == "") {
//         $("#username").attr("placeholder", "用户名不能为空");
//         return false;
//     }
//     else if (username.length < 5 || username.length > 16) {
//         $("#username").val("");
//         $("#username").attr("placeholder", "用户名长度为5~16");
//         return false;
//     }
//     else if (password == "") {
//         $("#password").attr("placeholder", "密码不能为空");
//         return false;
//     }
//     else if (password.length < 5 || password.length > 16) {
//         $("#password").val("");
//         $("#password").attr("placeholder", "密码长度为5~16");
//         return false;
//     }
//     else if (password1 !== password) {
//         $("#password1").val("");
//         $("#password1").attr("placeholder", "密码不一致");
//         return false;
//     }
//     else if (phone == "") {
//         $("#phone").attr("placeholder", "手机号不能为空")
//         return false;
//     }
//     else if (phone.length !== 11) {
//         $("#phone").val("");
//         $("#phone").attr("placeholder", "手机号不合法")
//         return false;
//     }
//     else if (email == "") {
//         $("#email").attr("placeholder", "邮箱不能为空")
//         return false;
//     }
//     return true;
// }
