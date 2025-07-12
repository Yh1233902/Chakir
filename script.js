function selectReason(reason) {
    localStorage.setItem('reason', reason);
    window.location = "report.html";
}
function reportByLink() {
    alert('يرجى إدخال رابط لمعالجته في النسخة الفعلية (سيتم برمجة التواصل مع البوت).');
}
function reportByMessage() {
    alert('سيتم تحويلك لإرسال رسالة يدوية.');
}
window.onload = function(){
    if (document.getElementById('selected-reason')) {
        document.getElementById('selected-reason').innerText = "لقد اخترت: " + localStorage.getItem('reason');
    }
}