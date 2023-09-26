#Loop from 2 to 19 and create the HTML files
import os

base_path = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
output_directory = os.path.join(base_path, 'boards', 'cbse', 'Rdsharma', 'class_11_solution')  # Specify the output directory


for chapter_no in range(1, 34):
    file_name = f"chapter_{chapter_no}_solution.html"
    file_path = os.path.join(output_directory, file_name)

    # Create the HTML file with your embedded HTML code
    with open(file_path, 'w') as html_file:
        html_code = '''
        <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>chapter-33 solution</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta content="Free HTML Templates" name="keywords">
    <meta content="Free HTML Templates" name="description">

    <!-- Favicon -->
    <link href="/img/cropped-favicon-270x270.png" rel="icon">

    <!-- Google Web Fonts -->
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">

    <!-- Font Awesome -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">

    <!-- Libraries Stylesheet -->
    <link href="/lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">

    <!-- Customized Bootstrap Stylesheet -->
    <link href="/css/style.css" rel="stylesheet">
    <style>
        .bg-blue-arrow {
            width: 23px;
            height: 23px;
            border-radius: 50%;
            background: transparent linear-gradient(180deg, #ebc034 0, #eb7134 100%) 0 0 no-repeat padding-box;
            box-shadow: 0 2px 3px #00000029;
            border: 1px solid #fff;
            display: flex;
            align-items: center;
        }

        div,
        span,
        h1 {
            padding: 0;
            border: 0;
            font-size: 100%;
        }

        .bg-gray {
            background: #e6e5e5;
        }

        section {
            display: block;
        }

        .max-container {
            max-width: 1150px;
            margin: 0 auto;
        }

        #image-container {
            position: relative;
            width: 100%;
            height: auto;
            overflow: hidden;
            margin: 0 auto;
            transition: width 0.3s ease-in-out, height 0.3s ease-in-out;
        }

        span,
        img {
            margin: 0;
            padding: 0;
            border: 0;
            font-size: 100%;
        }

        .soln-cont div {
            font: normal normal normal 16px/24px 'Open Sans', sans-serif;
            color: #3e3e3e;
        }

        .soln-cont {
            border-bottom: 2px solid #e7e7e7;
        }

        .soln-cont p {
            font: normal normal xx-large 16px/24px 'Open Sans', sans-serif;
            color: #3e3e3e;
        }
    </style>
</head>

<body>


    <!-- Header Start -->
    <div class="container-fluid page-header " style="margin-bottom: 90px;">
        <div class="container">
            <div class="d-flex flex-column justify-content-center" style="min-height: 300px">
                <h3 class="display-4 text-white text-uppercase">Binomial Distribution</h3>
                <div class="d-inline-flex text-white" style="font-size: 25px; font-weight: bold;">
                    <p class="m-0 text-uppercase"><a style="color: #F4C430" href="">Home</a></p>
                    <i class="fa fa-angle-double-right pt-1 px-3"></i>
                    <p class="m-0">Class 12th</p>
                </div>
            </div>
        </div>
    </div>
    <!-- Header End -->

    <!-- Main content-->
    <section class="bg-gray pad30">
        <div class="max-container">
            <h1 class="section-title" style="font-weight:  bold; font-size:x-large ;padding-top:40px;">Class 12-science
                RD Sharma
                Maths
                Chapter 33 - Binomial Distribution</h1>
            <hr style="
            height: 10px; /* Set the desired height for the line */
            background-color: #eb7134; /* Set the line color */
            border: none; margin-bottom: 2%;">
            <div class="container justify-content-center" style="align-items: center; width: 100%;">
                <div id="image-container">


                </div>
            </div>

        </div>
    </section>
    <!-- main content end -->

    <!-- Footer Start -->
    <div class="container-fluid bg-dark text-white py-5 px-sm-3 px-lg-5" style="margin-top: 90px;">
        <div class="row pt-5">
            <div class="col-lg-7 col-md-12">
                <div class="row">
                    <div class="col-md-6 mb-5">
                        <h5 class="text-primary text-uppercase mb-4" style="letter-spacing: 5px;">Get In Touch</h5>
                        <p><i class="fa fa-map-marker-alt mr-2"></i>123 Street, New York, USA</p>
                        <p><i class="fa fa-phone-alt mr-2"></i>+012 345 67890</p>
                        <p><i class="fa fa-envelope mr-2"></i>info@example.com</p>
                        <div class="d-flex justify-content-start mt-4">
                            <a class="btn btn-outline-light btn-square mr-2" href="#"><i class="fab fa-twitter"></i></a>
                            <a class="btn btn-outline-light btn-square mr-2" href="#"><i
                                    class="fab fa-facebook-f"></i></a>
                            <a class="btn btn-outline-light btn-square mr-2" href="#"><i
                                    class="fab fa-linkedin-in"></i></a>
                            <a class="btn btn-outline-light btn-square" href="#"><i class="fab fa-instagram"></i></a>
                        </div>
                    </div>
                    <div class="col-md-6 mb-5">
                        <h5 class="text-primary text-uppercase mb-4" style="letter-spacing: 5px;">Our Courses</h5>
                        <div class="d-flex flex-column justify-content-start">
                            <a class="text-white mb-2" href="#"><i class="fa fa-angle-right mr-2"></i>Web Design</a>
                            <a class="text-white mb-2" href="#"><i class="fa fa-angle-right mr-2"></i>Apps
                                Design</a>
                            <a class="text-white mb-2" href="#"><i class="fa fa-angle-right mr-2"></i>Marketing</a>
                            <a class="text-white mb-2" href="#"><i class="fa fa-angle-right mr-2"></i>Research</a>
                            <a class="text-white" href="#"><i class="fa fa-angle-right mr-2"></i>SEO</a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-5 col-md-12 mb-5">
                <h5 class="text-primary text-uppercase mb-4" style="letter-spacing: 5px;">Newsletter</h5>
                <p>Rebum labore lorem dolores kasd est, et ipsum amet et at kasd, ipsum sea tempor magna tempor.
                    Accu
                    kasd sed ea duo ipsum. Dolor duo eirmod sea justo no lorem est diam</p>
                <div class="w-100">
                    <div class="input-group">
                        <input type="text" class="form-control border-light" style="padding: 30px;"
                            placeholder="Your Email Address">
                        <div class="input-group-append">
                            <button class="btn btn-primary px-4">Sign Up</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="container-fluid bg-dark text-white border-top py-4 px-sm-3 px-md-5"
        style="border-color: rgba(256, 256, 256, .1) !important;">
        <div class="row">
            <div class="col-lg-6 text-center text-md-left mb-3 mb-md-0">
                <p class="m-0 text-white">&copy; <a href="#">Domain Name</a>. All Rights Reserved. Designed by <a
                        href="https://htmlcodex.com">HTML Codex</a>
                </p>
            </div>
            <div class="col-lg-6 text-center text-md-right">
                <ul class="nav d-inline-flex">
                    <li class="nav-item">
                        <a class="nav-link text-white py-0" href="#">Privacy</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white py-0" href="#">Terms</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white py-0" href="#">FAQs</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white py-0" href="#">Help</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <!-- Footer End -->


    <!-- Back to Top -->
    <a href="#" class="btn btn-lg btn-primary btn-lg-square back-to-top"><i class="fa fa-angle-double-up"></i></a>


    <!-- JavaScript Libraries -->
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.bundle.min.js"></script>
    <script src="/lib/easing/easing.min.js"></script>
    <script src="/lib/owlcarousel/owl.carousel.min.js"></script>

    <!-- Contact Javascript File -->
    <script src="/mail/jqBootstrapValidation.min.js"></script>
    <script src="/mail/contact.js"></script>

    <!-- Template Javascript -->
    <script src="/js/main.js"></script>
    <script>
        // Disable right-click on the image container
        var imageContainer = document.getElementById('image-container');
        imageContainer.addEventListener('contextmenu', function (e) {
            e.preventDefault();
        });

        // Function to generate image elements based on folder path and number of images
        function generateImages(folderPath, numImages) {
            const imageContainer = document.getElementById('image-container');
            for (let i = 1; i <= numImages; i++) {
                const img = document.createElement('img');
                img.src = `${folderPath}/${i.toString().padStart(4, '0')}.jpg`;
                img.alt = `Embedded Image`;
                img.style.display = 'block';
                img.style.objectFit = 'cover';
                img.style.transition = 'transform 0.3s ease-in-out';
                img.style.width = '100%';
                img.style.height = 'auto';

                // Create a parent paragraph element
                const p = document.createElement('p');
                p.appendChild(img);

                // Append the paragraph to the image container
                imageContainer.appendChild(p);
            }
        }

        // Call the generateImages function with your folder path and the number of images in the folder
        generateImages('/img/RD_sharma_solution/RD_SHARMA_12_MATH_2019/RD SHARMA 12 MATH 2019/PART-1/Rd Sharma 12 Vol 1 2019 Solutions for Class 12 Science MATH Chapter 1 - Relation-images', 49);
    </script>

</body>

</html>
        '''
        html_file.write(html_code)

    print(f"Created {file_name} in {output_directory}")
