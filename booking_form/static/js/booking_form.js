// Update Total Course Cost 
const courseLength = document.getElementById('id_course_length')
const totalCourseCost = document.getElementById('total_course_cost')
const courseCostPerWeek =totalCourseCost.textContent

let currentTotal  

courseLength.addEventListener("change", calculateTotal);

function calculateTotal(){

    currentTotal = parseFloat(courseLength.value) * parseFloat(courseCostPerWeek)
    totalCourseCost.innerText = currentTotal.toFixed(2)
}





