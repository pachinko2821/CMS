<?php
    $db = new SQLite3('cms.db');

    if(!$db){
        echo $db->lastErrorCode();
    }
?>