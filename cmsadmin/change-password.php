<?php
    include '../includes/php/connect.php';
    session_start();
    $username = $_SESSION['usser'];
    if(!isset($_COOKIE[$username])){
        header("Location: admin-login.php");
    }


?>

<html>
    <head>
        <!------ bootstrap css links ---------->
        <link rel="stylesheet" type="text/css" href='/includes/css/main.css'>
            <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
            <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <title>Change Password</title>
    </head>
    <body>

        <div class="wrapper fadeInDown">
        <h2>Change Password</h2>
            <div id="formContent">
            <!-- Tabs Titles -->
            <form action='change-password.php' method='POST'>
            <!-- Icon -->
                <div class="fadeIn first">
                    <img src="https://www.securemessagingapps.com/wp-content/uploads/2016/09/cropped-security-shield-lock-512-300x300.png" id="icon" alt="Change Password" />
                </div>

                <label>Current Password</label>
                    <div class="form-group pass_show"> 
                        <input type="password" id="password" class="fadeIn first" name="old-pass"> 
                    </div> 
                <label>New Password</label>
                    <div class="form-group pass_show"> 
                        <input type="password" id="password" class="fadeIn second" name="new-pass"> 
                    </div> 
                <label>Confirm Password</label>
                    <div class="form-group pass_show"> 
                        <input type="password" id="password" class="fadeIn third" name="confirm-new-pass"> 
                    </div>
                    <input type="submit" class="fadeIn fourth" value="Change Password" name="sumbit-btn">
                </div>
            </form>
        
        </div>
        </body>
</html>

<?php 

$old_pass = hash("sha256", $_POST['old-pass']);
$new_pass = hash("sha256", $_POST['new-pass']);
$c_new_pass = hash("sha256", $_POST['confirm-new-pass']);

$statement = $db->prepare('SELECT password FROM admins WHERE password=?;');
$statement->bindValue(1, $old_pass);
$result = $statement->execute();

$row = $result->fetchArray(SQLITE3_ASSOC);
if($old_pass == $row['password']){
    if($new_pass == $c_new_pass){

        $statement = $db->prepare('UPDATE admins set password=? WHERE password=?;');
        $statement->bindValue(1, $new_pass);
        $statement->bindValue(2, $old_pass);
        $result = $statement->execute();

        echo "<script>alert('Password Updated!')</script>";
        header("Location: dashboard.php");
    }
    else{
        echo "<script>alert('New password and Confirmation dont match!')</script>";
    }

}
    else{
        echo "<script>alert('Wrong Current Password!')</script>";
    }

?>