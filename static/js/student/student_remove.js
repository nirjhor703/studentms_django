$(document).on('click', '.addToEventBtnRight', function(e) {
    e.preventDefault(); // stop default action
    const tr = $(this).closest('tr');
    const student_id = tr.data('id'); // student row must have data-id
    const event_id = $('#event').val();

    if (!student_id) return alert("❌ No student selected");
    if (!event_id) return alert("❌ No event selected");

    if (confirm("Confirm to ADD this student to the event?")) {
        $.ajax({
            url: '/students/add-to-event/',  // endpoint for adding student
            type: 'POST',
            headers: { 'X-CSRFToken': csrftoken },  // CSRF protection
            data: {
                'student_id': student_id,
                'event_id': event_id,
            },
            dataType: 'json',
            success: function(response) {
                console.log("Server returned:", response); // for debugging
                if (response.status === 'success') {
                    reloadRightTable();
                    reloadLeftTable();
                    alert(response.message || "✅ Student added successfully!");
                } else {
                    alert(response.message || "❌ Error occurred");
                }
            },
            error: function(xhr, status, error) {
                console.log(xhr.responseText); // debug server error
                alert("❌ Server error: " + error);
            }
        });
    }
});