// teacher.js

// Create + Update Teacher (Same Form)
$("#teacherForm").submit(function (e) {
    e.preventDefault()

    let id = $("#teacherId").val()
    let url = id ? `/teachers/update/${id}/` : `/teachers/create/`

    $.ajax({
        url: url,
        method: "POST",
        data: {
            name: $("#name").val(),
            email: $("#email").val(),
            subject_speciality: $("#subject_speciality").val(),
            phone: $("#phone").val(),
            csrfmiddlewaretoken: csrf_token,   // <-- important
        },
        success: function (response) {
            alert(response.message)
            location.reload()
        }
    })
})

function editTeacher(id, name, email, subject, phone) {
    $("#teacherId").val(id)
    $("#name").val(name)
    $("#email").val(email)
    $("#subject_speciality").val(subject)
    $("#phone").val(phone)
}

function deleteTeacher(id) {
    $.ajax({
        url: `/teachers/delete/${id}/`,
        method: "POST",
        data: {
            csrfmiddlewaretoken: csrf_token,
        },
        success: function (response) {
            alert(response.message)
            location.reload()
        }
    })
}
