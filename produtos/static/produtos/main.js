const user_input = $("#user-input")
const products_div = $('#replaceable-content')
const endpoint = '/produtos/'
const delay_by_in_ms = 700
let scheduled_function = false

let ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            // fade out the artists_div, then:
            products_div.fadeTo('normal', 0).promise().then(() => {
                // replace the HTML contents
                products_div.html(response['resultado_produtos'])
                // fade-in the div with new contents
                products_div.fadeTo('normal', 1)
            })
        })
}


user_input.on('keyup', function () {

    const request_parameters = {
        p: $(this).val() // value of user_input: the HTML element with ID user-input
    }


    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})
