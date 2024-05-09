<?php
include "include/db_conn.php";
session_start();

if (isset($_POST['email']) && isset($_POST['password'])) {
    function validate($data){
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
    $uname = validate($_POST['email']);
    $pass = validate($_POST['password']);
    if (empty($uname)){
        header("Location: index.php?error=Email is Required!");
        exit();
    }else if(empty($pass)){
        header("Location: index.php?error=Password is Required!");
        exit();
    }else{
        $sql = "SELECT * FROM users WHERE email='$uname' AND pass='$pass' ";
        $result = mysqli_query($conn, $sql);
            $row = mysqli_fetch_assoc($result);
            if ($row['email'] === $uname) {
                    $_SESSION['name'] = $row['name'];
                    $_SESSION['email'] = $row['email'];
                    
                    header('Location:chatbot.php');
                    exit();
            }else{
                header("Location:index.php?error=Incorrect Username or Password or Not Registered!");
                exit();
          }
        }}

?>