<?php
defined('BASEPATH') OR exit('No direct script access allowed');
?><!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>To Do List</title>
        <link rel="stylesheet" href="<?php echo base_url(); ?>/asset/css/bootstrap.css" type="text/css" />
        <link rel="stylesheet" href="<?php echo base_url(); ?>/asset/css/bootstrap.js" type="text/js" />
        <link rel="stylesheet" href="<?php echo base_url(); ?>/asset/js/jquery.js" type="text/js" />

    </head>
    <body>

        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <a class="navbar-brand" href="#">To Do List</a>
            <button class="navbar-toggler" type="button" >
                <span class="navbar-toggler-icon"></span>
            </button>

            <form class="form-inline my-6 my-lg-0"  role="form" action="<?php echo base_url(); ?>'Welcome/search' " method="post">
                <input class="form-control mr-sm-2" type="text" name="search" placeholder="Search">
                <button class="btn btn-secondary my-2 my-sm-0" type="submit" name="submit">Search</button>
            </form><br>
        
        </div>
        
    </nav>