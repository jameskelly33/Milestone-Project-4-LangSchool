// Code taken from Code Institute's Project Boutique Ado https://github.com/Code-Institute-Solutions/boutique_ado_v1/
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

let levelSelected = $('#id_default_current_english_level').val();
if(!levelSelected) {
    $('#id_default_current_english_level').css('color', '#aab7c4');
};
$('#id_default_current_english_level').change(function() {
    levelSelected = $(this).val();
    if(!levelSelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});
