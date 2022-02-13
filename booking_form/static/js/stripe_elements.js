

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
console.log(clientSecret)
console.log (stripePublicKey)
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});


var form = document.getElementById('payment-form');
var bookingName = document.getElementById('full-name')
var bookingEmail = document.getElementById('email')
var bookingPhoneNumber = document.getElementById('phone-number')




 
form.addEventListener('submit', function(ev) {
ev.preventDefault();
card.update({ 'disabled': true});
$('#submit-button').attr('disabled', true);
stripe.confirmCardPayment(clientSecret, {
    payment_method: {
        card: card,
        billing_details:{
            name:form.inputName.value,
            email:bookingEmail.innerText,
            phone:bookingPhoneNumber.innertext,
            address:{
                line1:form.inputAddress.value,
                line2:inputAddress2.value,
                city:inputCity.value,
                country:inputCountry.value,
            }
            
        }
    }
}).then(function(result) {
    if (result.error) {
        var errorDiv = document.getElementById('card-errors');
        var html = `
            <span class="icon" role="alert">
            <i class="fas fa-times"></i>
            </span>
            <span>${result.error.message}</span>`;
        $(errorDiv).html(html);
        card.update({ 'disabled': false});
        $('#submit-button').attr('disabled', false);
    } else {
        if (result.paymentIntent.status === 'succeeded') {
            form.submit();
        }
    }
});


});

