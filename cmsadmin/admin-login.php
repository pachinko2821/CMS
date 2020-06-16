<?php
    include 'includes/connect.php';
?>

<html>
        <head>
            <link rel="stylesheet" type="text/css" href='includes/main.css'>
            <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
            <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
            <!------ Include the above in your HEAD tag ---------->
            <title>Admin Login</title>
        </head>

        <body>

            <div class="wrapper fadeInDown">
            <h2>CMS-ADMIN</h2>
            <div id="formContent">
            <!-- Tabs Titles -->

            <!-- Icon -->
            <div class="fadeIn first">
            <img src="https://logodix.com/logo/1707088.png" id="icon" alt="Admin Login" />
            </div>

            <!-- Login Form -->
            <form action='admin-login.php' method="POST">
            <input type="text" id="login" class="fadeIn second" name="user" placeholder="login">
            <input type="password" id="password" class="fadeIn third" name="pass" placeholder="password">
            <input type="submit" class="fadeIn fourth" value="Log In" name="sumbit-btn">
            </form>

            <!-- Remind Passowrd -->
            <div id="formFooter">
            <a class="underlineHover" href="#">Forgot Password?</a>
            </div>

            </div>
            </div>
        </body>

</html>

<?php


$username= $_POST['user'];
$password= hash("sha256", $_POST['pass']);

$statement = $db->prepare('SELECT * FROM users WHERE username=? AND password=?');
$statement->bindValue(1, $username);
$statement->bindValue(2, $password);
$result = $statement->execute();

if(!empty($username)){
if(empty($result->fetchArray(SQLITE3_ASSOC))){
    echo "<script>alert('Invalid Credentials')</script>";
    }

else{
    session_start();
    $_SESSION['user'] = $username;
    header("Location: dashboard.php");
    }
}

?>