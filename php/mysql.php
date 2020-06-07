<?php
$servername = "";
$username = "";
$password = "";
$dbname = "";

 
// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname,3306);
// Check connection
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
} 
 
$sql = "SELECT * FROM test";
$result = $conn->query($sql);
print_r($result);

while($rows = mysqli_fetch_assoc($result)){
    print_r($rows);
}

 
$conn->close();
?>