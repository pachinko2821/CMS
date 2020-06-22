<?php
include '../includes/php/connect.php';
?>

<!doctype html>
<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="/includes/css/blog-main.css">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <script src="/includes/js/includer.js"></script>
  <title>The MGM Rant</title>
</head>
<body class="bg-dark">

<!-- include header -->
<div w3-include-html="/includes/php/header.html"></div>

  <img class="center" src="/includes/img/logo.png" alt="The MGM Rant">
  <br><br>

<!--carousel start-->
  <div class="col-lg-9 bg-dark carousel">

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

        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>

        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>

    </div>
</div>
<!--carousel end-->

<!--main cards start-->

<h3 class="display-3 text-center text-reset" >Featured Posts</h3><br>
<div class="container">
  <div class="row text-center">

  <?php 

  $statement = $db->prepare("SELECT * FROM approvedPosts;");
  $result = $statement->execute();
    while($row = $result->fetchArray()){ ?>
      <div class="center card bg-dark shadow rounded" style="width: 18rem;">
        <a href="/blog/posts/<?php echo $row['Title']; ?>.html"><img src="/includes/posts/images/<?php echo $row['Title']; ?>/image1.jpeg" class="card-img-top" alt="Your net slow lol"></a>
        <div class="card-body">
          <h5 class="card-title"><?php echo $row['Title']; ?></h5>
          <p class="card-text"><?php echo $row['small_content']; ?></p>
          <a href="/blog/posts/<?php echo $row['Title']; ?>.html" class="btn btn-primary">View Article</a>
        </div>
      </div>
    <?php } ?>
  </div>
</div>
<!--main cards end-->
</div>
<br><br>

<!-- include footer -->
<div w3-include-html="/includes/php/footer.html"></div>

<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
<script>includeHTML();</script>
</body>
</html>
