$(document).ready(function () {
    function getRoleChoice() {
        // var url = $(location).attr('href');
        $.ajax({
            url: '../getrole/',
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
});