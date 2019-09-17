"use strict"

var username;
var password;

function login_verify() {
    username = $("#username").val();
    password = $("#password").val();
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


function reg_verify() {
    username = $("#username").val();
    password = $("#password").val();
    var password1 = $("#password1").val();
    var phone = $("#phone").val();
    var email = $("#email").val();
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
    else if (password1 !== password) {
        $("#password1").val("");
        $("#password1").attr("placeholder", "密码不一致");
        return false;
    }
    else if (phone == "") {
        $("#phone").attr("placeholder", "手机号不能为空")
        return false;
    }
    else if (phone.length !== 11) {
        $("#phone").val("");
        $("#phone").attr("placeholder", "手机号不合法")
        return false;
    }
    else if (email == "") {
        $("#email").attr("placeholder", "邮箱不能为空")
        return false;
    }
    return true;
}