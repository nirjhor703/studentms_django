$(document).ready(function(){
    $('#saveSubjectBtn').click(function(e) {
            e.preventDefault();   // stop the page from reloading

        const sub_name = $('#name').val();
        const sub_description = $('#description').val();
        const teacher_id = $('#teachers').val();
       
        console.log(sub_name);
        console.log(sub_description);
        console.log(teacher_id);

        if (!sub_name) return alert("⚠️ Please enter subject name.");
        if (!sub_description) return alert("⚠️ Please enter subject description.");
        if (!teacher_id) return alert("⚠️ Please select teacher.");

        $.ajax({
            url: '/subjects/save-subjects/',
            method: 'POST',
            headers: { "X-CSRFToken": csrftoken },  // ✅ this is critical
            data: {
                'name': sub_name,
                'description': sub_description,
                'teachers': teacher_id,
            },
            success: function(response) {
                if (response.status === 'success') {
                    alert(response.message,"✅ Save successful!");
                    loadSubjects();   // 🔥 Reload table
                    $('#addForm')[0].reset(); // clear form
                } 
                else if (response.status === 'exists') {
                    alert(response.message,"⚠️ Schedule already EXISTS");
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
