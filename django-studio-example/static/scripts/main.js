console.log('js loaded')
// show that the js is connected

// from Django Docs 
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// get the elements 
let danceClassForm = document.querySelector('#class-form')
let temp = document.querySelector('#weather-data')

let danceClasses = document.querySelectorAll('.dance-classes')

for (let danceClass of danceClasses){
    //do something
}
// check if js found the div
const teacherURL = 'api/teachers/new'
const danceClassURL = 'api/classes/new'
let teacherForm = document.querySelector('#teacher-form')

// when submit button is clicked, perform a function
// event refers to the click of the button
danceClassForm.addEventListener('submit', function (event){
    event.preventDefault()
    console.log(event.target)
    formData = new FormData(danceClassForm)
    fetch(danceClassURL, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Request-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: formData
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
    })
})

teacherForm.addEventListener('submit', function (event){
    event.preventDefault()
    console.log(event.target)
    formData = new FormData(teacherForm)
    fetch(teacherURL, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Request-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: formData
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
    })
})



let forecast
// Get data from an external api and put it on your page
fetch("https://weatherapi-com.p.rapidapi.com/forecast.json?q=Durham&days=1", {
	"method": "GET",
	"headers": {
		"x-rapidapi-host": "weatherapi-com.p.rapidapi.com",
		"x-rapidapi-key": "96fc9d36cfmshd44f68355a6b5edp1ce557jsn85bcc6eb665a"
	}
})
.then(response => {
	return response.json();
})
.then(data => {
    console.log(data)
    forecast = data
    console.log(forecast.current.temp_f)
    let temp_text = document.createTextNode(`The current temp is ${forecast.current.temp_f}`)
    temp.appendChild(temp_text)
})
.catch(err => {
	console.error(err);
});

