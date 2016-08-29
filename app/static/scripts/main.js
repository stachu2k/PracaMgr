/**
 * Created by Paweł on 12.08.2016.
 */

function getCookie(name){
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).on("pageshow", "#students", function(){
    $.ajax({
        url : "/students/",
        type : "GET",
        beforeSend : function(){
            $('#students-main').html('<div class="loading"><img src="/static/images/ajax-loader.gif" alt="Loading..." ></div>');
        },
        success : function(students) {
            var btn = '<a href="#new-student" class="ui-btn ui-icon-plus ui-btn-icon-right">Dodaj studenta</a>';
            $('#students-main').append(btn).trigger("create");

            var ul = $('<ul></ul>').attr({"data-role":"listview", "data-inset":"true", "data-autodividers":"true"});
            for(i in students)
            {
                var li = '<li><a data-id="' + students[i].id + '" href="#student-details">' + students[i].surname + " " + students[i].name + '</a></li>';
                ul.append(li);
            }
            $('#students-main').append(ul).trigger("create");
        },
        complete : function(){
            $('#students-main .loading').remove();
        }
    });
});

$(document).on("pagehide", "#students", function(){
    $('#students-main *').remove();
});

$(document).on("pagehide", "#new-student", function(){
    $('#result-box').html("");
});

function newStudentFormPost(){
    console.log("newStudentFormPost is working!") // sanity check
    $.ajax({
        url : "/students/create/",
        type : "POST",
        data : {name : $('#id_name').val(), surname : $('#id_surname').val()},
        success : function(json) {
            $('#id_name').val(''); // remove the value from the input
            $('#id_surname').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            if(json.error == true) $('#result-box').css("color", "red");
            else $('#result-box').css("color", "#47a447");
            $('#result-box').html(json.result);
        },
        error : function(xhr,errmsg,err) {
            $('#results-box').html("Error: " + errmsg); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}