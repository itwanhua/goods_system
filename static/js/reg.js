// 注册校验
$(function() {
    var vname = false;
    var vpassword = false;
    var vpassword1 = false;
    var vphone = false;
    var vemail = false;
    $("#username").blur(function() {
        var username = $("#username").val();
        if (username == "") {
            $("#username").attr("placeholder", "用户名不能为空");
            return;
        }
        if (username.length < 5 || username.length > 16) {
            $("#username").val("");
            $("#username").attr("placeholder", "用户名长度为5~16");
            return;
        }
        
        $.ajax({
            type: "GET",
            contentType: "appliction/json; charset=UTF-8",
            dataType: "json",
            url: "/check_username",
            data: "username=" + username,
            timeout: 1000,
            success: function(data) {
                if (data["err"] === 0) {
                    $(".feedback").css("color", "green");
                    $(".feedback").text("用户名可注册！");
                    vname = true;
                }
                else {
                    $(".feedback").css("color", "red");
                    $(".feedback").text("用户名已注册！");
                }
            }
        });
    });


    $("#password").blur(function(){
        var password = $("#password").val();
        if (password == "") {
            $("#password").attr("placeholder", "密码不能为空");
            return;
        }
        if (password.length < 5 || password.length > 16) {
            $("#password").val("");
            $("#password").attr("placeholder", "密码长度为5~16");
            return;
        }
        vpassword = true;
    });

    $("#password1").blur(function(){
        password = $("#password").val();
        var password1 = $("#password1").val();
        if (password1 !== password) {
            $("#password1").val("");
            $("#password1").attr("placeholder", "密码不一致");
            return;
        }
        vpassword1 = true;
    });

    $("#phone").blur(function(){
        var phone = $("#phone").val();
        if (phone == "") {
            $("#phone").val("");
            $("#phone").attr("placeholder", "手机号不能为空")
            return;
        }
        if (!(/^1[3456789]\d{9}$/.test(phone))){
            $("#phone").val("");
            $("#phone").attr("placeholder", "手机号格式有误");
            return;
        }
        vphone = true;
    });

    $("#email").blur(function(){
        var email = $("#email").val();
        if (email == "") {
            $("#email").attr("placeholder", "邮箱不能为空");
            return;
        }
        vemail = true;
    });

    $("#btn_reg").click(function() {
        console.log(vname, vpassword, vpassword1, vphone, vemail)
        if (!(vname && vpassword && vpassword1 && vphone && vemail)) {
            $(".feedback").css("color", "red");
            $(".feedback").text("信息不完整");
            alert("请输入完整信息！")
            return false;
        }
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
