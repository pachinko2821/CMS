<?php
    unset($_COOKIE);
    session_abort();
    header("Location: admin-login.php");
?>