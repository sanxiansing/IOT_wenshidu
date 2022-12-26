<?php
$servername = "localhost";
$username = "数据库用户名";
$password = "数据库密码";
$dbname = "数据库名";
 
// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
} 
 
$sql = "SELECT temperature, humidity, time FROM data WHERE 1";
$result = $conn->query($sql);
 
if ($result->num_rows > 0) {
    // 输出数据
    while($row = $result->fetch_assoc()) {
        
$temperature=$row["temperature"];
$humidity=$row["humidity"];
$time=$row["time"];

    }
} else {
    echo "0 结果";
}

$conn->close();
?>

<!DOCTYPE html>
<html lang="en" >
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="30">

<title>三弦家的室内温湿度情况</title>

<link rel="stylesheet" href="css/style.css">

</head>
<body>

<div id="wrapper">
    	
<div style="float:left;width:200px;">
		<div id="termometer">
		<div id="temperature" style="height:0" data-value="0°C"></div>
		<div id="graduations"></div>
		</div>
		<div id="temVal" data-value='<?php echo $temperature ;?>'></div>
		<p id="unit">室内温度 <?php echo $temperature ;?>C°</p>
</div>

<div >
		<div id="termometer">
		<div id="humidity" style="height:0" data-value="0°C"></div>
		<div id="graduations"></div>
		</div>
		<div id="humVal" data-value='<?php echo $humidity ;?>'></div>
		<p id="unit">室内湿度 <?php echo $humidity ;?>%</p>
</div>
</div>
</div>
<div style="
width:400px;
height:500px;
position:absolute;
left:55%;
bottom:25%;
margin-left: -280px;
margin-bottom: -450px;
">

<h2 >数据更新时间：   <?php echo $time ;?></h2>
</div>
<div style="
width:400px;
height:500px;
position:absolute;
left:50%;
top:50%;
margin-left: -160px;
margin-top: -300px;
">
    <h1 >三弦家的室内温湿度情况</h1>
</div>


<script >
const units = {
  Celcius: "°C",
  Fahrenheit: "°F" ,
  humidity: "%"};


const config_T = {
  minTemp: -20,
  maxTemp: 50,
  unit: "Celcius"
};
const config_H = {
  minHum: 0,
  maxHum: 100,
  unit: "humidity"
};
const tem = document.getElementById("temVal");
const hum = document.getElementById("humVal");
Tval=tem.dataset.value;
Hval=hum.dataset.value;


const temperature = document.getElementById("temperature");

function setTemperature() {
  temperature.style.height = (Tval - config_T.minTemp) / (config_T.maxTemp - config_T.minTemp) * 100 + "%";
  temperature.dataset.value = Tval + units[config_T.unit];
}
const humidity = document.getElementById("humidity");

function setHumidity() {
  humidity.style.height = (Hval - config_H.minHum) / (config_H.maxHum - config_H.minHum) * 100 + "%";
  humidity.dataset.value = Hval + units[config_H.unit];
}

setTimeout(setTemperature, 1000);
setTimeout(setHumidity, 1000);
    
</script>


</body>
</html>