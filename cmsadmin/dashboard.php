<?php
    include '../includes/php/connect.php';
    session_start();
    $username = $_SESSION['user'];

    if(!isset($_COOKIE[$username])){
        header("Location: admin-login.php");
    }


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Bootstrap core CSS -->
    <link href="/includes/css/dashboard.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/includes/css/dashboard-homepage.css" rel="stylesheet">
</head>

<body>
  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
    <div class="container">
      <a class="navbar-brand" href="#"><?php echo "Welcome ".$username;?></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
          <a class="nav-link" href="logout.php"><button class="btn btn-primary">Logout</button></a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->
  <div class="container">

    <div class="row">

      <div class="col-lg-3">

        <h1 class="my-4">CMS ADMIN</h1>
        <div class="list-group">
          <a href="dashboard.php" class="list-group-item">Submits</a>
          <a href="change-password.php" class="list-group-item">Change admin password</a>
          <a href="dashboard.php" class="list-group-item">Graphs</a>
        </div>

      </div>
      <!-- /.col-lg-3 -->

      <div class="col-lg-9">

        <div id="carouselExampleIndicators" class="carousel slide my-4" data-ride="carousel">
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

        <h5>Recently Submitted Posts(Red if we found profane words):</h5>
        <div class="row">

        
        <!-- shows all recently submitted posts, for review by admin, footers is red if said post contains profane words, else green -->
        
          <?php
            
            $statement = $db->prepare('SELECT * FROM postDetails');
            $result = $statement->execute();
            while($row = $result->fetchArray(SQLITE3_ASSOC)){ ?>  
                    <div class="col-lg-4 col-md-6 mb-4">
                        <div class="card h-100">
                        <a href="#"><img class="card-img-top" src="/includes/posts/images/<?php echo $row['Title']; ?>/image1.jpeg"></a>
                        <div class="card-body">
                            <h4 class="card-title">
                            <a href="viewer.php?file=<?php echo $row['Profanity'].'-posts/'.str_replace('_', ' ', $row['Title']); ?>.html"><?php echo $row['Title']; ?></a>
                            </h4>
                            <h5><?php echo $row['Author']; ?></h5>
                            <h6><?php echo $row['Date']; ?></h6>
                            <p class="card-text"><?php echo $row['small_content'];?></p>
                        </div>
                        <div class="card-footer" style="background-color:<?php echo $row['Profanity']; ?>;">
                            
                        </div>
                        </div>
                    </div>
            <?php } ?>

        </div>
        <!-- /.row -->

      </div>
      <!-- /.col-lg-9 -->

    </div>
    <!-- /.row -->

  </div>
  <!-- /.container -->

  <!-- Footer -->
  <footer class="py-5 bg-dark">
    <div class="container">
      <p class="m-0 text-center text-white">cmsadmin 2020</p>
    </div>
    <!-- /.container -->
  </footer>

  <!-- Bootstrap core JavaScript -->
  <script src="/includes/js/jquery.min.js"></script>
  <script src="/includes/js/dashboard.min.js"></script>

    </body>
</html>

<!-- 
       ,~~.
      (  6 )-_, quack?
 (\___ )=='-'
  \ .   ) )
   \ `-' /    
~'`~'`~'`~'`~ 

-->