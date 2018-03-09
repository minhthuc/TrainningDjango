var User = function () {
    var base = this;
    this.$firstname = $("input[name='firstname']").val();
    this.$lastname = $("input[name='lastname']").val();
    this.$password = $("input[name='password']").val();
    this.$description = $("input[name='description']").val();
    this.$birthday = $("input[name='birthday']").val();
    this.$hobbies = $("input[name='hobbies']").val();
    this.$submit = $("button[name='create']").val();
    this.CreateUser = function () {
        $.ajax({
            url: '/create/',
            type: 'POST',
            datatype:'text',
            data: {
                firstname: this.firstname.val(),
                lastname: this.lastname.val(),
                password: this.password.val(),
                description: this.description.val(),
                birthday: this.birthday.val(),
                hobbies: this.hobbies.val(),
            }
        }).success(function (rs) {
            console.log(rs);
            console.log("hello");
        })
    }
};
$(document).ready(function () {
    var user ;
    $('#loadUser').click(function () {
        // var user = getUser();
        getUser();
        // $("input[name='firstname']").value(user.fields.firstname)
        console.log(user);
    });

    //create user
    $("#submit").click(function () {
        var data = {
        'firstname': $("input[name='firstname']").val(),
        'lastname': $("input[name='lastname']").val(),
        'password': $("input[name='password']").val(),
        'description': $("input[name='description']").val(),
        'birthday': $("input[name='birthday']").val(),
        'hobbies': $("input[name='hobbies']").val(),
        'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val(),
        };
       $.ajax({
            url: 'create/',
            type: 'POST',
            datatype:'json',
            data: data
        }).done(function (rs) {
            if(rs.failure){
                alert(rs.failure);
            }else {
                alert(rs.success);
            }
        });
    });

    function getUser() {
        var url = $(location).attr('href');
        $.ajax({
            url: '../getUser/',
            type: 'POST',
            datatype:'json',
            data: {
                'user_id': url.split("/")[4],
                'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()
            }
        }).done(function (rs) {
            user = JSON.parse(rs)[0].fields;
            // console.log(user);
            $("#firstname")[0].value = user.firstName;
            $("input[name='lastname']")[0].value = user.lastName;
            $("input[name='password']")[0].value = user.PassWord;
            $("input[name='description']")[0].value = user.Description;
            $("input[name='birthday']")[0].value = user.BirthDay;
            $("input[name='hobbies']")[0].value = user.Hobbies;
        });
    }

    $("#update").click(function () {
        var data = {
            'firstname': $("input[name='firstname']").val(),
            'lastname': $("input[name='lastname']").val(),
            'password': $("input[name='password']").val(),
            'description': $("input[name='description']").val(),
            'birthday': $("input[name='birthday']").val(),
            'hobbies': $("input[name='hobbies']").val(),
            'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val(),
        };
       $.ajax({
            url: 'update/',
            type: 'POST',
            datatype:'json',
            data: data
        }).done(function (rs) {
            if(rs.failure){
                alert(rs.failure);
            }else {
                alert(rs.success);
            }
        });
    });

    $("#delete").click(function () {
        $.ajax({
            url: 'delete/',
            type: 'POST',
            datatype:'json',
            data: {
                'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()
            }
        }).done(function (rs) {
            if(rs.failure){
                alert(rs.failure);
            }else {
                alert(rs.success);
            }
            $(location).attr('href','../')
        });
    });
});
