"use strict";

function login_verify() {
    var username = $("#username").val();
    var password = $("#password").val();
    if (username == "") {
        $("#username").attr("placeholder", "用户名不能为空");
        return false;
    }
    else if (username.length < 5 || username.length > 16) {
        $("#username").val("");
        $("#username").attr("placeholder", "用户名长度为5~16");
        return false;
    }
    else if (password == "") {
        $("#password").attr("placeholder", "密码不能为空");
        return false;
    }
    else if (password.length < 5 || password.length > 16) {
        $("#password").val("");
        $("#password").attr("placeholder", "密码长度为5~16");
        return false;
    }

    return true;
}



