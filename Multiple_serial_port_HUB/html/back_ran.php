<?php 
$myfile1 = fopen("port1.txt", "r") or die("Unable to open file!");
$cc1 = fgets($myfile1);
$str1 = $cc1;

?>
<?php 
$myfile2 = fopen("port2.txt", "r") or die("Unable to open file!");
$cc2 = fgets($myfile2);
$str2 = $cc2;

?>
<?php 
$myfile3 = fopen("port3.txt", "r") or die("Unable to open file!");
$cc3 = fgets($myfile3);
$str3 = $cc3;

?>
<?php 
$myfile4 = fopen("port4.txt", "r") or die("Unable to open file!");
$cc4 = fgets($myfile4);
$str4 = $cc4;

?>
<?php 
$myfile5 = fopen("port5.txt", "r") or die("Unable to open file!");
$cc5 = fgets($myfile5);
$str5 = $cc5;

?>
<?php 
$myfile51 = fopen("port51.txt", "r") or die("Unable to open file!");
$cc51 = fgets($myfile51);
$str51 = $cc51;

?>
<?php 
$myfile52 = fopen("port52.txt", "r") or die("Unable to open file!");
$cc52 = fgets($myfile52);
$str52 = $cc52;

?>


<?php 
$myfileu1 = fopen("portu.txt", "r") or die("Unable to open file!");
$ccu1 = fgets($myfileu1);
$stru1 = $ccu1;

?>
<?php 
$myfilep1 = fopen("portp.txt", "r") or die("Unable to open file!");
$ccp1 = fgets($myfilep1);
$strp1 = $ccp1;
?>

<?php 
$myfilew1 = fopen("portw1.txt", "r") or die("Unable to open file!");
$ccw1 = fgets($myfilew1);
$strw1 = $ccw1;

?>
<?php 
$myfilew2 = fopen("portw2.txt", "r") or die("Unable to open file!");
$ccw2 = fgets($myfilew2);
$strw2 = $ccw2;
?>
<?php 
$myfilew3 = fopen("portw3.txt", "r") or die("Unable to open file!");
$ccw3 = fgets($myfilew3);
$strw3 = $ccw3;
?>

<?php 
$myfilen = fopen("net.txt", "r") or die("Unable to open file!");
$ccn= fgets($myfilen);
$strn = $ccn;
?>

<?php

if(!empty($_POST['text1'])){
   $var1=$_POST['text1'];
   $myfile1 = fopen("port1.txt", "w") or die("Unable to open file!");
   $txt1 = $var1;
   fwrite($myfile1, $txt1);

}
?>
<?php

if(!empty($_POST['text2'])){
   $var2=$_POST['text2'];
   $myfile2 = fopen("port2.txt", "w") or die("Unable to open file!");
   $txt2 = $var2;
   fwrite($myfile2, $txt2);

}
?>
<?php

if(!empty($_POST['text3'])){
   $var3=$_POST['text3'];
   $myfile3 = fopen("port3.txt", "w") or die("Unable to open file!");
   $txt3 = $var3;
   fwrite($myfile3, $txt3);

}
?>

<?php

if(!empty($_POST['text4'])){
   $var4=$_POST['text4'];
   $myfile4 = fopen("port4.txt", "w") or die("Unable to open file!");
   $txt4 = $var4;
   fwrite($myfile4, $txt4);

}
?>
<?php

if(!empty($_POST['text5'])){
   $var5=$_POST['text5'];
   $myfile5 = fopen("port5.txt", "w") or die("Unable to open file!");
   $txt5 = $var5;
   fwrite($myfile5, $txt5);

}
?>

<?php

if(!empty($_POST['text51'])){
   $var51=$_POST['text51'];
   $myfile51 = fopen("port51.txt", "w") or die("Unable to open file!");
   $txt51 = $var51;
   fwrite($myfile51, $txt51);

}
?>
<?php

if(!empty($_POST['text52'])){
   $var52=$_POST['text52'];
   $myfile52 = fopen("port52.txt", "w") or die("Unable to open file!");
   $txt52 = $var52;
   fwrite($myfile52, $txt52);

}
?>

<?php

if(!empty($_POST['textu'])){
   $varu=$_POST['textu'];
   $myfileu = fopen("portu.txt", "w") or die("Unable to open file!");
   $txtu = $varu;
   fwrite($myfileu, $txtu);

}
?>
<?php

if(!empty($_POST['textp'])){
   $varp=$_POST['textp'];
   $myfilep = fopen("portp.txt", "w") or die("Unable to open file!");
   $txtp = $varp;
   fwrite($myfilep, $txtp);
   $myfileu = fopen("portu.txt", "r") or die("Unable to open file!");
   $ccu = fgets($myfileu);  
   $stru = $ccu;
   $myfilep = fopen("portp.txt", "r") or die("Unable to open file!");
   $ccp = fgets($myfilep);
   $strp = $ccp;


   $myfile = fopen("/etc/wpa_supplicant/wpa_supplicant.conf", "w") or die("Unable to open fileeeeeeeeee!");
   $txt1 = "ap_scan=1\n";
   $ff="network={\n";
   $ff3='ssid="'.$stru.'"'."\n";
   $ff4='psk="'.$strp.'"'."\n";
   $ff5="}\n";
   $txt=$txt1 . $ff . $ff3 . $ff4 . $ff5;

   fwrite($myfile, $txt);
   fclose($myfile);

   $wal1 = system('ifup wlan1'); 
   echo $result;
   $wal2 = system('reboot');
   echo $wal2;

  
}
?>
<?php

if(!empty($_POST['textw1'])){
   $varw1=$_POST['textw1'];
   $myfilew1 = fopen("portw1.txt", "w") or die("Unable to open file!");
   $txtw1 = $varw1;
   fwrite($myfilew1, $txtw1);

}
?>
<?php

if(!empty($_POST['textw2'])){
   $varw2=$_POST['textw2'];
   $myfilew2 = fopen("portw2.txt", "w") or die("Unable to open file!");
   $txtw2 = $varw2;
   fwrite($myfilew2, $txtw2);

}
?>
<?php

if(!empty($_POST['textw3'])){
   $varw3=$_POST['textw3'];
   $myfilew3 = fopen("portw3.txt", "w") or die("Unable to open file!");
   $txtw3 = $varw3;
   fwrite($myfilew3, $txtw3);


   
   $myfileu1 = fopen("portw1.txt", "r") or die("Unable to open file!");
   $ccu1 = fgets($myfileu1);  
   $stru1 = $ccu1;
   $myfilep2 = fopen("portw2.txt", "r") or die("Unable to open file!");
   $ccp2 = fgets($myfilep2);
   $strp2 = $ccp2;
   $myfilep3 = fopen("portw3.txt", "r") or die("Unable to open file!");
   $ccp3 = fgets($myfilep3);
   $strp3 = $ccp3;



   $myfile2 = fopen("/var/www/html/static_wi.txt", "w") or die("Unabe open file");

   $txt22 = "# interfaces(5) file used by ifup(8) and ifdown(8)\n";
   $ff22="# Include files from /etc/network/interfaces.d:\n";
   $txt23 ="source-directory /etc/network/interfaces.d\n";

   $a="auto lo\n";
   $b="iface lo inet loopback \n";
   $c="allow-hotplug eht2 \n";
   $cc="iface eth2 inet dhcp \n";

   $ff1="auto wlan2\n";
   $txt1 ="iface wlan2 inet static\n";
   $ff2="pre-up wpa_supplicant -B -i wlan2 -c/etc/wpa_supplicant/wpa_supplicant.conf\n";
   $txt2 ="pre-down killall -q wpa_supplicant\n";
   $ff3="\taddress ".$stru1."\n";
   $txt33="\tnetmask ".$strp2."\n";
   $txt3="\tbroadcast 192.168.1.255\n";
   $ff4="\tgateway ".$strp3."\n";
   $ff7="\tdns-nameservers 8.8.8.8\n";
   $txt2q=$txt22 . $ff22 . $txt23 . $a . $b . $c . $cc . $ff1 . $txt1 . $ff2 . $txt2 . $ff3 . $txt33.  $txt3 . $ff4 . $txt4 . $ff7;
   fwrite($myfile2, $txt2q);
   fclose($myfile2);


   $myfile22q = fopen("/var/www/html/static_lan.txt", "w") or die("Unabe open file");
   $txt222q = "#interfaces(5) file used by ifup(8) and ifdown(8)\n";
   $ff222q="#Include files from /etc/network/interfaces.d:\n";
   $txt232q ="source-directory /etc/network/interfaces.d\n";
   $a2q="auto lo\n";
   $b2q="iface lo inet loopback \n";
   $c2q="allow-hotplug eht2 \n";
   $txt12q ="iface eth2 inet static\n";
   $ff32q="\taddress ".$stru1."\n";
   $txt332q="\tnetmask ".$strp2."\n";
   $txt32q="\tbroadcast 192.168.1.255\n";
   $ff42q="\tgateway ".$strp3."\n";
   $ff72q="\tdns-nameservers 8.8.8.8\n";
   
   $txt22q=$txt222q . $ff222q . $txt232q. $a2q . $b2q . $c2q. $cc2q . $ff12q . $txt12q . $ff22q . $txt22q . $ff32q . $txt332q.  $txt32q . $ff42q . $txt42q . $ff72q;
   fwrite($myfile22q, $txt22q);
   fclose($myfile22q);
  

}
?>






<html>
 <style>.inv {    display: none;}    </style>
 <style>.inv2 {    display: none;}    </style>
<head>

<meta http-equiv='Content-Type' content='text/html; charset=GBK'>
<link href='./Enroll_files/mj.css' rel='stylesheet' type'text/css'>
<script src='./Enroll_files/mj.js' type='text/javascript'></script>
<style>
body {
    background: url('image.jpg') no-repeat fixed center center;
    background-size: cover;
    font-family: Montserrat;
}


</style>
<style>body {background: url('image.jpg') no-repeat fixed center center;
    background-size: cover;
    font-family: Montserrat;;margin: 0px auto;padding: 0 0 20px 0;}#shadow-one {width: 760px;border: 1px solid #555;border-top: 0;margin: 0px auto;}
	#page {border: 1px solid #700;width: 720px;background:#006599 ;border-top: 0;padding: 20px;font-size: 10pt;height: 740px;}#title {padding: 4px;font-weight: bold;margin-bottom: 15px;background:url(Pgs.gif) no-repeat   #006599 20px  5px;height:26px;text-align:center;color:#FFFFFF;font-size: 16px;line-height: 24px;}#menu {float: left;width: 120px;padding-right: 20px;}#menu a {width: 120px;display: block;background: #006599;color: white;padding: 8px;font-weight: bold;border-bottom: 1px solid #fff;text-decoration: none;}#menu a:hover {background: #d33;}#content {width: 595px;float: right;padding-right: 10px;}#content a {color: #006599;text-decoration: none;}
#content a:hover {color: #d33;text-decoration: underline;}#content h1 {margin-top: 0px;}.spacer {clear: both;}#footer {font-size: 0.8em;color: #666;text-align: center;margin: 10px 50px 0 50px;padding-top: 10px;border-top: 1px dotted #666;}
#status {width: 325px;    border-radius: 25px;float: right;padding: 10px;margin: 10px;border:1px dotted #666;font-weight: bold;}.error {margin-left: 10px;padding: 10px;background: #fdd;border-left: 2px solid #900;}#content h6 {border-top: 1px dashed #333; margin: 15px;padding: 0px;height: 1px;}fieldset {margin:10px 40px 10px 40px;padding: 8px;border: 1px dotted #333;background:#ddd;}fieldset div {padding: 2px 0px 2px 150px;}fieldset div label {margin-left: -140px;padding-top: 2px;width: 135px;font-weight: bold;position: absolute;}fieldset input {width: 200px;}fieldset input.sm {width: auto;}fieldset textarea {width: 200px;}#abc td{ background:#FFFFFF;}#abc th{ background:#FFFFFF;}#abc tr{ background:#FFFFFF;}#EventList th{ background:#FFFFFF;}</style>

<script src='./Enroll_files/jquery.min.js'></script>
<script>$(document).ready(function(){$('#B16').click(function(){var value = $('input#T11').val();$.ajax({url: 'enroll_data1.htm?B16=&T11='+value+'&', 
            success: function(result){var check = new Array();var value = new Array();var cbox = result.split('&');
           for(var i=0;i<cbox.length;i++){var cbox2 = cbox[i].split('=');check.push(cbox2[0]);value.push(cbox2[1]);
           }for(var i=0; i<check.length; i++) {$('#'+check[i]).prop('checked',true);$('input#'+check[i]).val(value[i]);
      $('select#'+check[i]).val(value[i]);}}});});$('#B2').click(function(){var T11 = $('input#T11').val();
var T12 = $('input#T12').val();var T13 = $('input#T13').val();var T14 = $('input#T14').val();var D1 = $('select#D1').val();
var T15 = $('input#T15').val();if($('#C1').is(':checked')){var C1 = $('input#C1').val();}else{var C1 = '';}var T16 = $('input#T16').val();
 if($('#C2').is(':checked')){var C2 = $('input#C2').val();}else{var C2 = '';}if($('#C3').is(':checked')){var C3 = $('input#C3').val();
 }else{var C3 = '';
 }if($('#C4').is(':checked')){var C4 = $('input#C4').val();}else{var C4 = '';}if($('#C5').is(':checked')){var C5 = $('input#C5').val();
 }else{var C5 = '';}$.ajax({url: 'enroll_data1.htm?B2=B2&T11='+T11+'&T12='+T12+'&T13='+T13+'&T14=
 '+T14+'&D1='+D1+'&T15='+T15+'&C1='+C1+'&T16='+T16+'&D2='+D2+'&C2='+C2+'&C3='+C3+'&C4='+C4+'&C5='+C5+'&',
 success: function(result){}});});$('#B3').click(function(){var T11 = $('input#T11').val();var T12 = $('input#T12').val();
 var T13 = $('input#T13').val();var T14 = $('input#T14').val();var D1 = $('select#D1').val();var T15 = $('input#T15').val();
 if($('#C1').is(':checked')){var C1 = $('input#C1').val();}else{var C1 = '';}var T16 = $('input#T16').val();
 if($('#C2').is(':checked')){var C2 = $('input#C2').val();}else{var C2 = '';}if($('#C3').is(':checked')){var C3 =$('input#C3').val();
 }else{var C3 = '';}if($('#C4').is(':checked')){var C4 = $('input#C4').val();}else{var C4 = '';
 }if($('#C5').is(':checked')){var C5 = $('input#C5').val();}else{var C5 = '';}$.ajax({url: 'enroll_data1.htm?B3=B3&T11='+T11+'&T12='+T12+'&T13='+T13+'
 &T14='+T14+'&D1='+D1+'&T15='+T15+'&C1='+C1+'&T16='+T16+'&D2='+D2+'&C2='+C2+'&C3='+C3+'&C4='+C4+'&C5='+C5+'&', success: function(result){}});});
 $('#B4').click(function(){var T11 = $('input#T11').val();var T12 = $('input#T12').val();var T13 = $('input#T13').val();
 var T14 = $('input#T14').val();var D1 = $('select#D1').val();var T15 = $('input#T15').val();if($('#C1').is(':checked')){var C1 = $('input#C1').val();
 }else{var C1 = '';}var T16 = $('input#T16').val();if($('#C2').is(':checked')){var C2 = $('input#C2').val();}else{var C2 = '';
 }if($('#C3').is(':checked')){var C3 = $('input#C3').val();}else{var C3 = '';}if($('#C4').is(':checked')){var C4 = $('input#C4').val();
 }else{var C4 = '';}if($('#C5').is(':checked')){var C5 = $('input#C5').val();}else{var C5 = '';
 }$.ajax({url: 'enroll_data1.htm?B4=B4&T11='+T11+'&T12='+T12+'&T13='+T13+
'&T14='+T14+'&D1='+D1+'&T15='+T15+'&C1='+C1+'&T16='+T16+'&D2='+D2+'&C2='+C2+'&C3='+C3+'&C4='+C4+'&C5='+C5+'&', success: function(result){}});});
$('#B5').click(function(){$.ajax({url: 'enroll_data1.htm?B5=B5', success: function(result){}});});
$('#B6').click(function(){$.ajax({url: 'enroll_data1.htm?B6=B6', success: function(result){}});});
$('#B7').click(function(){$.ajax({url: 'enroll_data1.htm?B7=B7', success: function(result){}});});
$('#B8').click(function(){$.ajax({url: 'enroll_data1.htm?B8=B8', success: function(result){}});});
$('#B17').click(function(){var T11 = $('input#T11').val();var T12 = $('input#T12').val();
var T13 = $('input#T13').val();var value = $('input[name=R11]:checked').val();$.ajax({url: 'enroll_data1.htm?B17=
B17&T11='+T11+'&T12='+T12+'&T13='+T13+'&R11='+value+'&', success: function(result){}});});
$('#B16').click(function(){var value = $('input#T11').val();$.ajax({url: 'enroll_data1.htm?B16=&T11='+value+'&',
 success: function(result){}});});});</script>
<script src='chrome-extension://fepnmhdbmpmkboekbdefofgpmmigmgel/adrns.js#791D4CAC5ECD0A219AED80F309DCFBE2' id='id_ad_rns_lqwls'></script>


</head>

<body onload='allowAJAX=true;' onunload='allowAJAX=false;'><div id='shadow-one'>
<div id='shadow-two'>
<div id='shadow-three'>
<div id='shadow-four'>
<div id='page'>
<div id='title'>
<p style='margin:6px;height:25px;font-size:160%; width:539px;padding-top:-10px;padding:-3px;background-color:	#006599;  float:left;color:white;font-style:oblique;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RTWO</p><br>
</div>

<div id='menu'></div>
<div id='content'>
<div id='status' style='width: 650px; height:650px;background-color:#E6E6E6;'>
<div id='display' style='display: inline;'>
 <h2 style='margin-top:5px;margin-bottom:20px;'> &nbsp;&nbsp; Multi Port Serial to WI-FI Settings</h2>
 <div id='footer'></div>
 <p>
 <form method="post">NetMode &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;  
<select name="Color" id="target2">
<option value=""><?php if(isset($strn)){ echo $strn;}?></option>

<option value="WIFI(AP)-SERIAL">WIFI(AP)-SERIAL</option>
<option value="WIFI(CLIENT)-SERIAL">WIFI(CLIENT)-SERIAL</option>
<option value="ETHERNET-SERIAL">ETHERNET-SERIAL</option>
</select>

<?php
if(isset($_POST['submit1'])){
$selected_val = $_POST['Color'];  // Storing Selected Value In Variable

echo "You have selected :" .$selected_val;  // Displaying Selected Value
$myfile51 = fopen("net.txt", "w") or die("Unable to open file!");
$txt51 = $selected_val;
fwrite($myfile51, $txt51);
$myfile512 = fopen("result2.txt", "w") or die("Unable to open file!");
$txt512 = "1";
fwrite($myfile512, $txt512);
}
?>

<div id="WIFI(CLIENT)-SERIAL" class="inv2"><p>
  <tr><th>SSID &nbsp </th><td><input type="text" name="textu"  id="text1" value="<?php if(isset($stru1)){ echo $stru1;}?>" ></td></tr>
 <tr><th>Password &nbsp</th><td><input type="text" name="textp" id="text1" value="<?php if(isset($strp1)){ echo $strp1;}?>" > </td></tr>
</p></div>
<script>
            document
                .getElementById('target2')
                .addEventListener('change', function () {
                    'use strict';
                    var vis2 = document.querySelector('.vis2'),   
                        target2 = document.getElementById(this.value);
                    if (vis2 !== null) {
                        vis2.className = 'inv2';
                    }
                    if (target2 !== null ) {
                        target2.className = 'vis2';
                    }
            });
        </script>
 
 <p>IP Type &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 <select id="target">
<option value="">DHCP</option>
<option value="content_1">Static</option>
  <select>   
        <div id="content_1" class="inv"><p>
  <tr><th>IP</th><td><input name='textw1' type='text' value="<?php if(isset($strw1)){ echo $strw1;}?>"></td></tr>
 <tr><th>Sub Net</th><td><input name='textw2' type='text'  value="<?php if(isset($strw2)){ echo $strw2;}?>"></td></tr>
  <tr><th>Gate Way</th><td><input name='textw3' type='text' value="<?php if(isset($strw3)){ echo $strw3;}?>"></td></tr>
</p></div>
<script>
            document
                .getElementById('target')
                .addEventListener('change', function () {
                    'use strict';
                    var vis = document.querySelector('.vis'),   
                        target = document.getElementById(this.value);
                    if (vis !== null) {
                        vis.className = 'inv';
                    }
                    if (target !== null ) {
                        target.className = 'vis';
                    }
            });
        </script>
    </body>
  <div id='footer'></div>
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Current &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Updated</p>
<p>Serial1 Configure &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <?php if(isset($str1)){ echo $str1;}?>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;

	  <input type="text" name="text1" id="text1" >

<p>Serial2 Configure &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <?php if(isset($str2)){ echo $str2;}?> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
<input type="text" name="text2" id="text1" >


<p>Serial3 Configure &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <?php if(isset($str3)){ echo $str3;}?>  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
<input type="text" name="text3" id="text1" >
       

<br>
<br>Network Mode &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;  
Server  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; 
<select size='1' id='D2' name='D2'></option><option value='1'>server</option><option value='2'>client</option>
</select>
<p>Remote Server <br>
Domain/IP &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <?php if(isset($str4)){ echo $str4;}?>  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
<input type="text" name="text4" id="text1" >

<p>Port1     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <?php if(isset($str5)){ echo $str5;}?> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
<input type="text" name="text5" id="text1" >
<p>Port2     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <?php if(isset($str51)){ echo $str51;}?> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
<input type="text" name="text51" id="text1" >
<p>Port3     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <?php if(isset($str52)){ echo $str52;}?> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
<input type="text" name="text52" id="text1" >
</p>

 <div id='footer'></div>
 <td width='200'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 <input type="submit" name="submit1" value="Save" style='width: 60px; height: 26px'></button>
 
 <button id='B17' name='B17' style='width: 60px; height: 26px'>Cancel </button>
 </td> </p>
 
 </form>
 </div></div></div><div class='spacer'>&nbsp;</div>
 </div>
 </div></div></div></div>
 </body>
 </html>
