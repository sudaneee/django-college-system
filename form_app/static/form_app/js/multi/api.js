function testy() {
    var ref = document.getElementsByName('ref')[0].value
    var email = document.getElementsByName('email')[0].value
    var tel = document.getElementsByName('tel')[0].value
    var name = document.getElementsByName('name')[0].value
    var lga = document.getElementsByName('lga')[0].value
    var city = document.getElementsByName('city')[0].value
    var address = document.getElementsByName('address')[0].value
    var dob = document.getElementsByName('dob')[0].value
    var nok = document.getElementsByName('nok')[0].value
    var nokTel = document.getElementsByName('nokTel')[0].value




    if (document.getElementsByName('schoolName')[1] == null) {
        var attendedSchool1 = "null"
    } else {
        var attendedSchool1 = document.getElementsByName('schoolName')[1].value
    }
    if (document.getElementsByName('schoolName')[2] == null) {
        var attendedSchool2 = "null"
    } else {
        var attendedSchool2 = document.getElementsByName('schoolName')[2].value
    }
    if (document.getElementsByName('schoolName')[3] == null) {
        var attendedSchool3 = "null"
    } else {
        var attendedSchool3 = document.getElementsByName('schoolName')[3].value
    }




    var courseApplied = document.getElementById('exampleFormControlSelect1')
    var optionSelected = courseApplied.options[courseApplied.selectedIndex].text
    console.log(optionSelected)


    if (attendedSchool1 === "") {
        attendedSchool1 = "null"
    }
    if (attendedSchool2 === "") {
        attendedSchool2 = "null"
    }
    if (attendedSchool3 === "") {
        attendedSchool3 = "null"
    }


    var dataObject = {
        paymentReference: ref,
        email: email,
        phoneNo: tel,
        name: name,
        lga: lga,
        city: city,
        address: address,
        dob: dob,
        nokName: nok,
        nokPhone: nokTel,
        attendedSchool1: attendedSchool1,
        attendedSchool2: attendedSchool2,
        attendedSchool3: attendedSchool3,
        courseApplied: optionSelected,
    }


    var jsonData = JSON.stringify(dataObject)

    var csrfToken = document.getElementById('csrf_token').innerHTML

    let xhr = new XMLHttpRequest();

    var authorizationBasic = window.btoa('sudanee' + ':' + 'ismailk2@');
    xhr.open("POST", "http://nihaz.org.ng/api/api-createApplication");
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader('Authorization', 'Basic ' + authorizationBasic);
    xhr.setRequestHeader('X-CSRFToken', csrfToken);

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            console.log(xhr.status);
            console.log(xhr.responseText);
        }
    };

    let data = jsonData;

    xhr.send(data);

}

function nexter() {

    var ref = document.getElementsByName('ref')[0].value
    var email = document.getElementsByName('email')[0].value
    var tel = document.getElementsByName('tel')[0].value
    var name = document.getElementsByName('name')[0].value
    var lga = document.getElementsByName('lga')[0].value
    var city = document.getElementsByName('city')[0].value
    var address = document.getElementsByName('address')[0].value
    var dob = document.getElementsByName('dob')[0].value
    var nok = document.getElementsByName('nok')[0].value
    var nokTel = document.getElementsByName('nokTel')[0].value



    if ((email !== "") || (tel !== "") || (name !== "") ||
        (lga !== "") || (city !== "") || (address !== "") || (dob !== "") ||
        (nok !== "") || (nokTel !== "")) {

        var nextBTN = document.getElementsByClassName('next')[0]
        nextBTN.style.visibility = 'visible'
    }

}

function nexter2() {

    var ref = document.getElementsByName('ref')[0].value
    var email = document.getElementsByName('email')[0].value
    var tel = document.getElementsByName('tel')[0].value
    var name = document.getElementsByName('name')[0].value
    var lga = document.getElementsByName('lga')[0].value
    var city = document.getElementsByName('city')[0].value
    var address = document.getElementsByName('address')[0].value
    var dob = document.getElementsByName('dob')[0].value
    var nok = document.getElementsByName('nok')[0].value
    var nokTel = document.getElementsByName('nokTel')[0].value



    if ((email === "") || (tel === "") || (name === "") ||
        (lga === "") || (city === "") || (address === "") || (dob === "") ||
        (nok === "") || (nokTel === "")) {

        var nextBTN = document.getElementsByClassName('next')[0]
        nextBTN.style.visibility = 'hidden'
    }

}