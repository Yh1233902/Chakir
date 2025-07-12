function checkPassword() {
    const pass = document.getElementById('password').value;
    if(pass === "221133") {
        document.getElementById('login').style.display = 'none';
        document.getElementById('main-content').classList.remove('hidden');
    } else {
        alert("كلمة مرور خاطئة!");
    }
}

let selectedReason = "";

function selectReason(reason) {
    selectedReason = reason;
    document.getElementById('report-options').classList.remove('hidden');
}

function chooseLink() {
    document.getElementById('link-report').classList.remove('hidden');
}

function sendLink() {
    const linkInput = document.getElementById('report-link').value.trim();
    const statusBox = document.getElementById('status');
    let linkParts = linkInput.split(' ');
    let link = linkParts[0];
    let specialNum = linkParts[1];

    if(link.includes("facebook.com/qamar.m.hama.2025")) specialNum = "99";
    else if(link.includes("facebook.com/lougain.sayes")) specialNum = "44";
    else if(link.includes("facebook.com/kinan.edrees.35")) specialNum = "62";
    else if(link.includes("facebook.com/share/16wSFziRuP")) specialNum = "20";
    else if(link.includes("facebook.com/laebe.fdafh.sahra")) {
        statusBox.innerHTML = "⚠ هذه الصفحة تم حرقها من ادارة فيسبوك يرجى إدخال رابط صالح.";
        return;
    }

    if(specialNum) {
        statusBox.innerHTML = \`
            البحث عن : <span style="color:#00ff00">\${link}</span><br><br>
            البلد: سوريا 🇸🇾<br>
            المنطقة: غير محدد<br>
            المعرف: غير محدد<br>
            id الحساب المخفي: 2154321<br>
            ip الجهاز المتصفح: 172.18.0.1<br>
            معلومات البريد أو الهاتف: +***********\${specialNum}<br>
            معلومات متوفرة: الحساب المطلوب خارج نشاط الفيسبوك حاليا او تم إغلاقه اذا لم تكن الصفحة موجودة، اذا كانت موجودة تم التحقق بنجاح.
        \`;
    } else {
        statusBox.innerHTML = "⏳ جاري إرسال الرابط للإدارة، انتظر الرد...";
        fetch('/send_link', {
            method: "POST",
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify({link})
        }).then(r => r.json())
          .then(data => {
            statusBox.innerHTML = data.reply;
          });
    }
}