<?php

include '../includes/php/connect.php';
session_start();
$username = $_SESSION['user'];
if(!isset($_COOKIE[$username])){
    header("Location: admin-login.php");
}

$file = $_GET['file'];
echo file_get_contents($file);

?>
<head>
    <link rel="stylesheet" type="text/css" href='/includes/css/main.css'>
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</head>

<form action="approval.php?file=<?php echo $file; ?>" method="POST">
    <input type="submit" value="approve" name="decision">
    <input type="submit" value="disapprove" name="decision">
</form>