const form = document.querySelector('form');
const submit = document.getElementsByClassName('next-button');

const sex_male= document.getElementById('male');
const sex_female= document.getElementById('female');
const smoking_yes= document.getElementById('smoking_yes');
const smoking_no= document.getElementById('smoking_no');
const alchole_yes= document.getElementById('alchole_yes');
const alchole_no= document.getElementById('alchole_no');
const physicalactivity_yes= document.getElementById('physicalactivity_yes');
const physicalactivity_no= document.getElementById('physicalactivity_no');
const diffwalking_yes= document.getElementById('diffwalking_yes');
const diffwalking_no= document.getElementById('diffwalking_no');
const heartdisease_yes= document.getElementById('heartdisease_yes');
const heartdisease_no= document.getElementById('heartdisease_no');
const Asthma_yes= document.getElementById('Asthma_yes');
const Asthma_no= document.getElementById('Asthma_no');
const kidneydisease_yes= document.getElementById('kidneydisease_yes');
const kidneydisease_no= document.getElementById('kidneydisease_no');
const stroke_yes= document.getElementById('stroke_yes');
const stroke_no= document.getElementById('stroke_no');
const diebtic_yes= document.getElementById('diebtic_yes');
const diebtic_no= document.getElementById('diebtic_no');

form.addEventListener('submit', (e) => {
    if (sex_male.checked == false && sex_female.checked == false) {
        e.preventDefault();
        alert('성별 중 하나를 선택하세요!');
    }

    if (smoking_yes.checked == false && smoking_no.checked == false) {
        e.preventDefault();
        alert('흡연 여부 중 하나를 선택하세요!');
    }

    if (alchole_yes.checked == false && alchole_no.checked == false) {
        e.preventDefault();
        alert('음주 여부 중 하나를 선택하세요!');
    }

    if (physicalactivity_yes.checked == false && physicalactivity_no.checked == false) {
        e.preventDefault();
        alert('신체활동 여부 중 하나를 선택하세요!');
    }

    if (diffwalking_yes.checked == false && diffwalking_no.checked == false) {
        e.preventDefault();
        alert('걷기힘듦의 여부 중 하나를 선택하세요!');
    }

    if (Asthma_yes.checked == false && Asthma_no.checked == false) {
        e.preventDefault();
        alert('천식의 여부 중 하나를 선택하세요!');
    }

    if (kidneydisease_yes.checked == false && kidneydisease_no.checked == false) {
        e.preventDefault();
        alert('신장질환의 여부 중 하나를 선택하세요!');
    }

    if (stroke_yes.checked == false && stroke_no.checked == false) {
        e.preventDefault();
        alert('뇌졸중의 여부 중 하나를 선택하세요!');
    }

    if (diebtic_yes.checked == false && diebtic_no.checked == false) {
        e.preventDefault();
        alert('당뇨병의 여부 중 하나를 선택하세요!');
    }
})