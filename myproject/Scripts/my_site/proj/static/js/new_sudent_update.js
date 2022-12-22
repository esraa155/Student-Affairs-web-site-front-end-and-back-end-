

function invalide_no(){
let num1=document.getElementById("form1").value +"";

if(num1.length!=8){
   window.alert("number is not correct  need to 8 number only");
}

}

function invalide_no2(){
let num2=document.getElementById("form2").value +"";

if(num2.length!=8){
   window.alert("number is not correct  need to 8 number only");
}

}

function invalide_no3(){
let num3=document.getElementById("form3").value ;

for(let i=0;i<num3.length;i++){
if(num3[i]<=9 || num3[i]=='[' ||num3[i]==']' ||num3[i]==';'|| num3[i]=='/'|| num3[i]==','|| num3[i]=='#'|| num3[i]=='@'|| num3[i]=='!'|| 
 num3[i]=='*' || num3[i]=='-'|| num3[i]=='+'|| num3[i]=='{' ||num3[i]=='}'|| num3[i]==')' ||num3[i]=='(' || num3[i]=='%'|| num3[i]=='?')
{ window.alert("name not correct");}
}

}


function invalide_no4(){
let num4=document.getElementById("form4").value ;


if(num4>4)
{ window.alert("GPA must lees than or equal 4");}


}

function invalide_no5(){
let num5=document.getElementById("form5").value +"";

if(num5.length!=12){
   window.alert("number is not correct  need to 12 number only");
}
}

