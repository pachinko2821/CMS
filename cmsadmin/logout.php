<?php
    session_start();
    unset($_SESSION['user']);
    unset($_COOKIE[$_SESSION['user']]);
    header("Location: admin-login.php");
?>