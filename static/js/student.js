
function getCSRFToken() { return document.querySelector('[name=csrfmiddlewaretoken]').value; }

function showToast(msg, type="success") {
    let toast = $('#toast');
    toast.removeClass('text-bg-success text-bg-danger');
    toast.addClass(type === 'success' ? 'text-bg-success' : 'text-bg-danger');
    toast.find('.toast-body').text(msg);
    new bootstrap.Toast(toast[0]).show();
}

// Add Student
$('#addForm').submit(function(e){
    e.preventDefault();
    $.ajax({
        url: `/students/add/`,
        method: 'POST',
        data: $(this).serialize(),
        success: function(res){
            showToast(res.message, res.status);
            if(res.status === 'success'){ location.reload(); }
        }
    });
});

// Edit Button
$('#studentTable').on('click', '.editBtn', function(){
    $('#edit_id').val($(this).data('id'));
    $('#edit_name').val($(this).data('name'));
    $('#edit_email').val($(this).data('email'));
    $('#edit_phone').val($(this).data('phone'));
    $('#edit_address').val($(this).data('address'));
    $('#edit_status').val($(this).data('status'));
    var editModal = new bootstrap.Modal(document.getElementById('editModal'));
    editModal.show();
});

// Edit Submit
$('#editForm').submit(function(e){
    e.preventDefault();
    let id = $('#edit_id').val();
    $.ajax({
        url: `/students/update/${id}/`,
        method: 'POST',
        data: $(this).serialize(),
        success: function(res){
            showToast(res.message, res.status);
            if(res.status === 'success'){ location.reload(); }
        }
    });
});

// Delete
$('#studentTable').on('click', '.deleteBtn', function(){
    if(confirm("Are you sure to delete this student?")){
        let id = $(this).data('id');
        $.ajax({
            url: `/students/delete/${id}/`,
            method: 'POST',
            headers: {'X-CSRFToken': getCSRFToken()},
            success: function(res){
                showToast(res.message, res.status);
                if(res.status === 'success'){ $(`#row${id}`).remove(); }
            }
        });
    }
});

