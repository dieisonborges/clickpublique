/* Masks */
$(document).ready(function () {
    $("#id_cell_phone").mask('(00) 00000-0000');   
})

/* Modal Scripts */
$(document).on('click', '.confirm-delete', function () {
    $('#modal-danger').attr('caller-id', $(this).attr('id'));
});

$(document).on('click', '#modal-danger-confirm', function () {
    var caller = $('#modal-danger-confirm').closest('.modal').attr('caller-id');
    window.location = $('#'.concat(caller)).attr('href');
});

/* Calendar */
$(function () {
    $("#id_end_date").datepicker(
        {
            dateFormat: "dd/mm/yy",
            dayNamesMin: ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"],
            monthNames: ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        }
    );
});

/* Select2 */
$("#id_category").select2();  