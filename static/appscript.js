var data;

function handleAPILoaded() {
    $("#search-button").attr("disabled", false);
}

function youtubeRequest() {
    var queryString = $("#query").val();
    var searchString = $("#search-string").val();

    //var req = new XMLHttpRequest();
    //req.open("GET", searchString, true);
    
    /*$.getJSON(searchString, function(data) {
        console.log(data);
    });*/

    $.ajax({
        url: searchString,
        dataType: "jsonp",
        success: function (response) {
        callFunction(response);
    }});

    /*var request = gapi.client.youtube.search.list({
        q : searchString,
        part : 'snippet'
    });

    request.execute(function(response) {
        var str = JSON.stringify(response.result);
        data = response.result;
    });*/
}
function callFunction(data) {
    console.log(data);
}