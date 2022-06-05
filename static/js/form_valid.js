function verifyPassword() {
        var name = document.getElementById('name1');
        var mail = document.getElementById('email1');
        var phone = document.getElementById('phone');

        var mailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        console.log(name.value)
        if (name.value == ""){
        document.getElementById("msg1").innerHTML = "enter a name please!";
        }
        else{
        document.getElementById("msg1").innerHTML = "";
        }
        if (mail.value.match(mailFormat) ) {
       document.getElementById("msg2").innerHTML = "";
document.regForm.email.focus();
return true;}
        else  {
        document.getElementById("msg2").innerHTML = "enter a valid email!";
        document.regForm.email.focus();
        return false;
        }

        }


        function pass() {

        var pw = document.getElementById('pw').value;
        var pw1 = document.getElementById('pw1').value;
        if (pw == "" || pw !== pw1) {
           document.getElementById("msg3").innerHTML = "enter a password!";
           document.getElementById("msg4").innerHTML = "password do not match !!";
           document.regForm.password.focus();
        return false;

          }
          else{
          document.getElementById("msg4").innerHTML = "";
           document.getElementById("msg3").innerHTML = "";
           document.regForm.password2.focus();
        return false;
         console.log("done")
          }
          if (phone.value.length  !== 10 ) {
        document.getElementById("phnmsg").innerHTML = "enter a phone number!";

        }
        else  {
        document.getElementById("phnmsg").innerHTML = "";

        }

        }



