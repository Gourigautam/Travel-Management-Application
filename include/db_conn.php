<?php
$sname= "localhost";
$unmae= "root";
$password="root";
$db_name= "chatbot";
$conn = mysqli_connect($sname, $unmae, $password, $db_name,8889);
if (!$conn) {
    echo "Connection Failed...!";
}

