<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
        <meta name="generator" content="Hugo 0.80.0">
        <title>Image form</title>

        <link rel="canonical" href="https://getbootstrap.com/docs/5.0/examples/dashboard/">



        <!-- Bootstrap core CSS -->
        <link href="/dict/bootstrap.min.css" rel="stylesheet">

        <style>
            .bd-placeholder-img {
                font-size: 1.125rem;
                text-anchor: middle;
                -webkit-user-select: none;
                -moz-user-select: none;
                user-select: none;
            }

            @media (min-width: 768px) {
                .bd-placeholder-img-lg {
                    font-size: 3.5rem;
                }
            }
        </style>


        <!-- Custom styles for this template -->
        <link href="../dict/self/questboard.css" rel="stylesheet">
        <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    </head>
    <body>

        % include('headerSec.tpl', link="/logout",linkStr = "Logout")

        <div class="container-fluid">
            <div class="row">
                
                % include('html/navigation.html')

                <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 ">

                    <div class="mx-auto y-4 mt-5">
                        <form class="form-horizontal" role="form" method="POST" onSubmit="return confirm('Do you confirm to modify the image?') " enctype="multipart/form-data">
                            
                            <div class="form-group">
                                <label class="col-sm control-label">Image in server:</label>
                                <div class="col-sm-10">
                                    <img src="/file/{{filename}}" class="img-fluid" alt="{{filename}}">
                                </div>
                            </div>
                            <div class="form-group mt-2">
                                <label for="upload" class="col-sm control-label">Select a file: </label>
                                <div class="col-sm-10">
                                    <input type="file" class="form-control" name="upload" />
                                </div>
                            </div>
                            <div class="form-group mt-2">
                                <label for="inputPassword" class="col-sm control-label">Password</label>
                                <div class="col-sm-10">
                                    <input type="password" class="form-control" id="inputPassword" name="confirmPwd" placeholder="Please input the password">
                                </div>
                            </div>
                            <div class="form-group mt-4">
                                <button type="submit" class="btn btn-primary">Submit</button>
                            </div>
                        </form>
                    </div>
                </main>
            </div>
        </div>


        <script src="/dict/bootstrap.bundle.min.js"></script>
        

        <script src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/feather.min.js" integrity="sha384-uO3SXW5IuS1ZpFPKugNNWqTZRRglnUJK6UAZ/gxOX80nxEkN9NcGZTftn6RzhGWE" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.4/dist/Chart.min.js" integrity="sha384-zNy6FEbO50N+Cg5wap8IKA4M/ZnLJgzc6w2NqACZaK0u0FXfOWRRJOnQtpZun8ha" crossorigin="anonymous"></script>
    </body>
</html>
