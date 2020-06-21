<?php
  include '../includes/php/connect.php';
?>


<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="shortcut icon" href="/includes/img/small_icon.png" />
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <link rel="stylesheet" href="/includes/stylesheets/index.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link id="pagestyle" rel="stylesheet" type="text/css" href="/includes/stylesheets/hdft.css">
    <link rel="stylesheet" href="/includes/stylesheets/dark-mode.css">
    <title>The MGM Rant</title>
  </head>
  <body>
       <!---navigation bar------------>
  <section id="nav-bar">
    <nav class="navbar navbar-expand-lg navbar-dark">
        <a class="navbar-brand logold" href="/blog/index.php"><img src="/includes/img/logo.png"></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item ml-auto">
              <div class="nav-link custom-control custom-switch">
                <input type="checkbox" class="custom-control-input" id="darkSwitch">
                <label class="custom-control-label" for="darkSwitch"><i class="fa fa-moon-o"></i></label>
              </div>
              </li>
            <li class="nav-item ml-auto">
              <a class="nav-link" href="aboutus.html">ABOUT US</a>
            </li>
            <li class="nav-item ml-auto">
                <a class="nav-link" href="https://fcrit.ac.in/redirectportal" target="_blank"> <button type="button" class="btn1">Sign in</button></a>
              </li>
          </ul>
        </div>
      </nav>
</section>
<!--navigation bar end-->

<!--carousel start-->
<div class="col-lg-9" style="width:55%; margin:0 auto;">

  <div id="carouselExampleIndicators" class="carousel slide my-4" data-ride="carousel" >
    <ol class="carousel-indicators">
      <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
      <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
      <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
    </ol>
    <div class="carousel-inner" role="listbox">
      <div class="carousel-item active">
        <img class="d-block img-fluid" src="https://www.mgmmumbai.ac.in/mgmcet/sites/default/files/inline-images/accellors.jpg" alt="First slide">
      </div>
      <div class="carousel-item">
        <img class="d-block img-fluid" src="https://www.mgmmumbai.ac.in/mgmcet/sites/default/files/inline-images/marathi-day-3.JPG" alt="Second slide">
      </div>
      <div class="carousel-item">
        <img class="d-block img-fluid" src="https://www.mgmmumbai.ac.in/mgmcet/sites/default/files/inline-images/marathi-day-1.JPG" alt="Third slide">
      </div>
    </div>
    <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
<!--carousel end-->
<!--main cards start-->

    <h3 class="display-3 text-center" >Featured Posts</h3>
    <div class="container">
      <div class="row text-center">
        
    <?php 
    
    $statemet = $db->prepare("SELECT * FROM approvedPosts;");
    $result = $statemet->execute();
    while($row = $result->fetchArray()){ ?>
        <div class="col-md-4 pb-1 pb-md-0">
            <div class="card shadow bg-primary">
                <a href="/blog/posts/<?php echo $row['Title']?>.html"><img class="card-img-top" src="/includes/posts/images/<?php echo $row['Title']; ?>/image1.jpeg" alt="Card image cap"></a>
                <div class="card-body">
                <h5 class="card-title"> <?php echo $row['Title']; ?> </h5>
                <p class="card-text"> <?php echo $row['small_content']; ?> </p>
                <a href="/blog/posts/<?php echo $row['Title']?>.html" class="btn">View Article</a>
                </div>
            </div>
        </div>
      
    <?php } ?>
    
    </div>
    </div>
<!--main cards end-->

  <br><br>
  <!-- Site footer start -->
  <footer class="site-footer">
    <div class="container">
      <div class="row">
        <div class="col-sm-1 col-md-3 col-xl-3">
          <a  href="#"><img class="mx-auto d-block" src="/includes/img/mr carter.png" width="250" height="250px" ></a>
        </div>
        <div class="col-sm-12 col-md-6">
          <h6 class="text-center"><b>About</b></h6>
          <p class="text-center">The official blog of Fr. C. Rodrigues Institute of Technology showcasing the up and coming creative talent in the institution. The Website is a showcase to the immense potential of engineering students around the world.</p>
        </div>
      </div>
      <hr>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md-8 col-sm-6 col-xs-12">
          <p class="copyright-text">Copyright &copy; 2020 All Rights Reserved by
       <a href="https://www.fcrit.ac.in/">FCRIT-Vashi</a>.
          </p>
        </div>
        <div class="col-md-4 col-sm-6 col-xs-12">
          <ul class="social-icons">
            <li><a class="instagram" href="https://www.instagram.com/oeuvre.fcrit/" target="_blank"><i class="fa fa-instagram"></i></a></li>
            <li><a class="facebook" href="https://www.facebook.com/Oeuvre-114987203566335/" target="_blank"><i class="fa fa-facebook"></i></a></li>
            <li><a class="twitter" href="https://twitter.com/oeuvrefcrit" target="_blank"><i class="fa fa-twitter"></i></a></li>
          </ul>
        </div>
      </div>
    </div>
</footer>
<!--footer end-->
  <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="/includes/scripts/dark-mode-switch.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</body>
</html>
