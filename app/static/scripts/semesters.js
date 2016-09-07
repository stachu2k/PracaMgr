/**
 * Created by Paweł on 05.09.2016.
 * This file contains script for handling semesters in application.
 */

$(document).on("pageshow", "#semesters", function(){
    $.ajax({
        url : "/semesters/",
        type : "GET",
        beforeSend : function(){
            $('#semesters-main').html('<div class="loading">' +
                '<img src="/static/images/ajax-loader.gif" alt="Loading..." ></div>');
        },
        success : function(semesters) {
            var btn = '<a href="#new-semester"' +
                'class="ui-btn ui-icon-plus ui-btn-icon-right ui-corner-all ui-shadow ui-mini">' +
                'Nowy semestr</a>';

            $('#semesters-main').append(btn).trigger("create");

            if(semesters.length) {
                var ul = $('<ul></ul>').attr({
                    "data-role": "listview",
                    "data-inset": "true"
                });

                var li = $('<li data-role="list-divider">Aktywny</li>');
                ul.append(li);

                for (i in semesters) {
                    if (semesters[i].active) {
                        var li = $('<li></li>');
                        var a = $('<a data-id="' + semesters[i].id + '" href="">' +
                            '<h2>' + semesters[i].name + '</h2>' +
                            '<p>Od: ' + semesters[i].start_date + ' | ' +
                            'Do: ' + semesters[i].end_date + '</p>' +
                            '</a>');
                        a.on("click", getStudent);
                        ul.append(li.append(a));
                    }
                }

                $('#semesters-main').append(ul).trigger("create");

                ul = $('<ul></ul>').attr({
                    "data-role": "listview",
                    "data-inset": "true"
                });

                li = $('<li data-role="list-divider">Pozostałe</li>');
                ul.append(li);

                for (i in semesters) {
                    if (!semesters[i].active) {
                        li = $('<li></li>');
                        a = $('<a data-id="' + semesters[i].id + '" href="">' +
                            '<h2>' + semesters[i].name + '</h2>' +
                            '<p>Od: ' + semesters[i].start_date + ' | ' +
                            'Do: ' + semesters[i].end_date + '</p>' +
                            '</a>');
                        a.on("click", getStudent);
                        ul.append(li.append(a));
                    }
                }

                $('#semesters-main').append(ul).trigger("create");
            }
            else {
                var div = $('<div class="no-data-infobox">Brak semestrów w bazie danych</div>');
                $('#semesters-main').append(div).trigger("create");
            }
        },
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        },
        complete : function(){
            $('#semesters-main .loading').remove();
        }
    });
});

$(document).on("pagehide", "#semesters", function(){
    $('#semesters-main *').remove();
});

$(document).on("pageshow", "#new-semester", function(){
    $('#new-semester-form').on("submit", function(event){
        $('#sem-result-box').html("");
        event.preventDefault();
        console.log("form submitted!");
        newSemesterFormPost();
    });
});

$(document).on("pagehide", "#new-semester", function(){
    $('#sem-result-box').html("");
});

function newSemesterFormPost(){
    console.log("newSemesterFormPost is working!") // sanity check

    var sem_type;

    if($('#id_sem_type_0').is( ":checked")) sem_type = 'z';
    else if($('#id_sem_type_1').is( ":checked")) sem_type = 'l';
    else sem_type = 'z';

    $.ajax({
        url : "/semesters/create/",
        type : "POST",
        data : {
            academic_year : $('#id_academic_year').val(),
            sem_type : sem_type,
            start_date : $('#id_start_date').val(),
            end_date : $('#id_end_date').val()
        },
        success : function(json) {
            $('#id_academic_year').val('');
            $('#id_start_date').val('');
            $('#id_end_date').val('');
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            if(json.error == true) $('#sem-result-box').css("color", "red");
            else $('#sem-result-box').css("color", "#47a447");
            $('#sem-result-box').html(json.result);
        },
        error : function(xhr,errmsg,err) {
            $('#sem-result-box').html("Error: " + errmsg); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}