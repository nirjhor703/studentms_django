function loadStudents() {
    $.ajax({
        url: '/students/get-students/',
        method: 'GET',
        success: function(response) {
            let students = response.students;
            let tbody = '';
            $.each(students, function(index, s) {
                tbody += `
                    <tr
                        class="student-row"
                        data-id="${s.id}"
                        data-name="${s.name}"
                        data-email="${s.email}"
                        data-phone="${s.phone}"
                        data-address="${s.address}"
                        data-status="${s.status}"
                        >

                        <td>${index + 1}</td>
                        <td>${s.id}</td>
                        <td>${s.name}</td>
                        <td>${s.email}</td>
                        <td>${s.phone}</td>
                        <td>${s.address}</td>
                        <td>${s.status}</td>
                        <td>
                            <button class="btn btn-sm btn-warning editBtn"
                                data-id="${s.id}"
                                data-name="${s.name}"
                                data-email="${s.email}"
                                data-phone="${s.phone}"
                                data-address="${s.address}"
                                data-status="${s.status}">
                                Edit
                            </button>
                            <button class="btn btn-sm btn-danger deleteBtn" data-id="${s.id}">Delete</button>
                        </td>
                    </tr>`;
            });
            $('#studentTableBody').html(tbody);
        },
        error: function() {
            alert('❌ Failed to load student list...');
        }
    });
}

$(document).ready(function () {
    loadStudents();
});

// Row click event
$(document).on("click", ".student-row", function() {
    $("#student_id").val($(this).data("id"));
    $("#name").val($(this).data("name"));
    $("#email").val($(this).data("email"));
    $("#phone").val($(this).data("phone"));
    $("#address").val($(this).data("address"));
    $("#status").val($(this).data("status"));
});