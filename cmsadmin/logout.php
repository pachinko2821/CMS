<?php
    unset($_SESSION['user']);
    session_abort();
    header("Location: cmsadmin/admin-login.php");
?>