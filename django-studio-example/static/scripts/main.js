console.log('js loaded')
// show that the js is connected

let form = document.querySelector('form')
// check if js found the form
// console.log(form)

// when submit button is clicked, perform a function
// event refers to the click of the button
form.addEventListener('submit', function (event){
    event.preventDefault()
    console.log(event.target)
})