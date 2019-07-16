$("#search-button").click(function() {
    let search_string = $("[name='search-string']").val();
    if (search_string == "") {
        search_string = "empty";
    } else {
        search_string = search_string.replace(' ', '_');
    }
    window.location.href = "/members/" + search_string + "/" + $("[name='gender']").val() + "/" + $("[name='role']").val() + "/" + $("[name='class']").val() + "/" + $("[name='fee-status']").val() + "/";
    return true;

});