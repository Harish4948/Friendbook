$(document).ready(function(){
console.log("success");
var p=$(".posts");
// console.log(array);
// var json=JSON.stringify(p);

var js=JSON.parse(p.text())
var i=0;
$(p).hide();
for(i;i<js.length;i++)
{
    var element=js[i];
    $('.post').append('<br> <li>'+JSON.stringify(element['text'])+'</li><br>');
    console.log(element['text']);
}
});