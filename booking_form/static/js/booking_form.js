// Update Total Course Cost in realttime as course length select input changes
const courseLength = document.getElementById('id_course_length');
const totalCourseCost = document.getElementById('total_course_cost');
const courseCostPerWeek =totalCourseCost.textContent;

let currentTotal;

courseLength.addEventListener("change", calculateTotal);

function calculateTotal(){

    currentTotal = parseFloat(courseLength.value) * parseFloat(courseCostPerWeek);
    totalCourseCost.innerText = currentTotal.toFixed(2);
}




