// Code taken from Code Institute's Project Boutique Ado https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/933797d5e14d6c3f072df31adf0ca6f938d02218
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});