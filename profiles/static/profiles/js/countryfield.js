// Set the correct color for the country field
let countrySelected = $('#id_country').val();
if(!countrySelected) {
    $('#id_country').css('color', '#aab7c4');
};
$('#id_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000501');
    }
});