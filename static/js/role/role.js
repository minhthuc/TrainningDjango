$(document).ready(function () {
    $("#create").click(function () {
       getRoleChoice()
    });
    function getRoleChoice() {
        // var url = $(location).attr('href');
        $.ajax({
            url: '../getrole/',
            type: 'POST',
            datatype:'json',
            data: {
                'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()
            }
        }).done(function (rs) {
            var option = "<option value='-' selected='selected'>Permission</option>";
            for(i =0; i<rs.length;i++){
                option = option + '<option value="'+ rs[i][0] +'">'+ rs[i][1] + '</option>';
            }
            $('#Permission').html(option);
        });
    }

//Create a new role
    $("#submit").click(function () {
        $.ajax({
            url: 'create/',
            type: 'POST',
            datatype:'json',
            data: {
                'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val(),
                'firstname':$("input[name='firstname']").val(),
                'permission':$("#Permission").val(),
                'description':$("input[name='description']").val(),
            }
        }).done(function (rs) {
            // console.log(rs.failure);
            if(rs.failure) {
                alert(rs.failure);
            }
            else{
                alert(rs.success);
                }
            });
        });

    $("#search").click(function () {
        searchUser();
    })
//edit role

});
function searchUser() {
    // console.log($("#firstname").val());
    $.ajax({
        url: '../search/',
        type: 'POST',
        datatype:'json',
        data: {
            'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val(),
            'firstname':$("#firstname").val(),
        }
    }).done(function (rs) {
        // console.log(rs.result);
        var list ="";
        rs.result.forEach(function (value) {
            // console.log(value.FullName);
            list += '<button onclick="selected_user(this)" class="list-group-item" type="button"  value ="'+ value.pk +','+value.FullName+'">'
                        + value.FullName +'</button>'
        });
        $("#list_name").html(list);
    });
}

function selected_user(element) {
    var m = confirm("Are you sure to apply this role to "+ element.value.split(',')[1]+"?");
    console.log(m);
    $.ajax({
        url:'../add_user_to_role/',
        type: 'POST',
        datatype: 'json',
        data: {
            'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val(),
            'user_id' : element.value.split(',')[0],
            'role_id': $("#role_id").val()

        }
    }).done(function (rs) {
        console.log(rs);
        if(rs.success){
            $("#list_user").append('<li>'+element.value.split(',')[1]+'</li>');
            $(".btn-secondary").click();
        }else {
            $(".btn-secondary").click();
            alert(rs.failure);
        }
    })
}