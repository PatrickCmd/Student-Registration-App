$(document).ready(function(){
    
    // dataTables
    $('#students').dataTable();
    
    //create student modal
    $('#add_student').DjangoModalRunner();
});