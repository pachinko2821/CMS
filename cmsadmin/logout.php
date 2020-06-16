<?php
    unset($_SESSION['user']);
    session_abort();
    header("Location: admin-login.php");
?>