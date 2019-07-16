$("#add-member").click(function() {
    data = new FormData();
    data.append("image", $("input[name='image']")[0].files[0]);
    data.append("first_name", $("input[name='fname']").val());
    data.append("last_name", $("input[name='lname']").val());
    data.append("username", $("input[name='username']").val());
    data.append('email', $("input[name='email']").val());
    data.append('gender', $("select[name='gender']").val());
    data.append('role', $("select[name='role']").val());
    data.append('date_joined', $("input[name='joiningdate']").val());
    data.append('date_of_birth', $("input[name='dob']").val());
    data.append('mobile_number', $("input[name='number']").val());
    data.append('payment_date', $("input[name='paymentdate']").val());
    data.append('password', $("input[name='password']").val());
    data.append('address', $("textarea[name='address']").val());
    data.append('security', $("input[name='security']").val());
    data.append('profession', $("input[name='profession']").val());
    data.append('classes', $("select[name='classes']").val());
    data.append('csrfmiddlewaretoken', $("[name='csrfmiddlewaretoken']").val());

    var username = $("input[name='username']").val();
    if (username.length > 3 && username.length < 21) {
        $.ajax({
            type: "GET",
            url: ("/username-validator/" + username),
            error: function() {
                alert("Username is already in Use");
            }
        })
        if (
            $("input[name='fname']").val() !== '' &&
            $("input[name='fname']").val() !== '' &&
            $("input[name='username']").val() !== '' &&
            $("input[name='email']").val() !== '' &&
            $("input[name='number']").val() !== '' &&
            $("textarea[name='address']").val() !== '' &&
            $("textarea[name='address']").val() !== '' &&
            $("input[name='security']").val() !== '' &&
            $("input[name='profession']").val() !== '') {
            $.ajax({
                type: "post",
                url: "/add-member",
                data: data,
                processData: false,
                contentType: false,
                success: function(result) {
                    window.location.href = "/add-member/" + "True/";
                    return true;
                },
                error: function(error) {
                    window.location.href = "/add-member/" + "False/";
                    return true;
                }
            });
        };
    };
});

$("input[name='username']").change(function() {
    var username = $("input[name='username']").val();
    if (username.length > 3 && username.length < 21) {
        $.ajax({
            type: "GET",
            url: ("/username-validator/" + username),
            error: function() {
                alert("Username is already in Use");
            }
        })
    };
})