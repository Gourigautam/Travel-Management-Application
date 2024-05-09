<?php
session_start();

// initializing variables
$username = "";
$email    = "";
$errors = array(); 

// connect to the database
$db = mysqli_connect('localhost', 'root', 'root', 'chatbot',8889);

// REGISTER USER
if (isset($_POST['submit'])) {
  // receive all input values from the form
  $name = mysqli_real_escape_string($db, $_POST['name']);
  $email = mysqli_real_escape_string($db, $_POST['email']);
  $password = mysqli_real_escape_string($db, $_POST['password']);


  if (empty($name)) { array_push($errors, "Name is required"); header("Location:signup.php?error=Input is required !");}
  if (empty($email)) { array_push($errors, "Email is required"); header("Location:signup.php?error=Input is required !"); }
  if (empty($password)) { array_push($errors, "Password is required");header("Location:signup.php?error= Input is required!"); }

  $user_check_query = "SELECT * FROM users WHERE email='$email' ";
  $result = mysqli_query($db, $user_check_query);
  $user = mysqli_fetch_assoc($result);
  
  if ($user) { // if user exists
    if ($user['email'] === $email) {
      array_push($errors, "email already exists");
      header("Location:signup.php?error=Email already exists !");
    }
  }
  if (count($errors) == 0) {
  $sql = "INSERT INTO users (name, email, pass) VALUES('$name','$email', '$password')";
  mysqli_query($db, $sql);;
  $_SESSION['email'] = $email;
  $_SESSION['name'] = $name;
  header('Location:chatbot.php');
  }
}

//   $sql = "INSERT INTO users (name, email, pass) VALUES('$name','$email', '$password')";
//         $result = mysqli_query($conn, $sql);
//             $row = mysqli_fetch_assoc($result);
            

                    
//                     header('Location:chatbot.php');
//                     exit();


// }

// else {
//     header('Location:signin.php');
// }

?>