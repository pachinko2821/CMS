<?php
    $db = new SQLite3('/includes/cms.db');

    if(!$db){
        echo $db->lastErrorCode();
    }