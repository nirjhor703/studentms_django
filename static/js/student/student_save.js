$(document).ready(function(){
    $('#saveStudentBtn').click(function(e) {
        e.preventDefault();   // stop the page from reloading

        const student_name = $('#name').val();
        const student_email = $('#email').val();
        const student_phone = $('#phone').val();
        const student_address = $('#address').val();
        const student_status = $('#status').val();
       
        console.log(student_name);
        console.log(student_email);
        console.log(student_phone);
        console.log(student_address);
        console.log(student_status);

        if (!student_name) return alert("⚠️ Please enter student name.");
        if (!student_email) return alert("⚠️ Please enter student email.");
        if (!student_phone) return alert("⚠️ Please enter student phone.");
        if (!student_address) return alert("⚠️ Please enter student address.");
        if (!student_status) return alert("⚠️ Please select student status.");

        $.ajax({
            url: '/students/save-students/',
            method: 'POST',
            headers: { "X-CSRFToken": csrftoken },  // ✅ CSRF protection
            data: {
                'name': student_name,
                'email': student_email,
                'phone': student_phone,
                'address': student_address,
                'status': student_status,
            },
            success: function(response) {
                if (response.status === 'success') {
                    alert(response.message || "✅ Save successful!");
                    loadStudents();   // 🔥 Reload student table
                    $('#addStudentForm')[0].reset(); // clear form
                } 
                else if (response.status === 'exists') {
                    alert(response.message || "⚠️ Student already exists");
                } 
                else {
                    alert("❌ Error: " + response.message);
                }
            },
            error: function(xhr, status, error) {
                alert("❌ Server error: " + error);
            }
        });
    });
});