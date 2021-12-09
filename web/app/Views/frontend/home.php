<?= $this->extend('frontend/layouts/app'); ?>

<?= $this->section('content'); ?>
<!-- Masthead-->
<header class="masthead bg-primary text-white text-center">
    <div class="container d-flex align-items-center flex-column">
        <!-- Masthead Avatar Image-->
        <img class="masthead-avatar mb-5" src="<?= base_url("assets/front/img/icon.png") ?>" alt="..." />
        <!-- Masthead Heading-->
        <h1 class="masthead-heading text-uppercase mb-0">Mulai Belajar</h1>
        <!-- Icon Divider-->
        <div class="divider-custom divider-light">
            <div class="divider-custom-line"></div>
            <div class="divider-custom-icon"><i class="fas fa-star"></i></div>
            <div class="divider-custom-line"></div>
        </div>
        <!-- Masthead Subheading-->
        <p class="masthead-subheading font-weight-light mb-0">Rambu Peringatan - Rambu Larangan - Rambu Perintah - Rambu Petunjuk</p>
    </div>
</header>
<!-- Portfolio Section-->
<section class="page-section portfolio" id="tentang">
    <div class="container">
        <!-- Portfolio Section Heading-->
        <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Tentang</h2>
        <!-- Icon Divider-->
        <div class="divider-custom">
            <div class="divider-custom-line"></div>
            <div class="divider-custom-icon"><i class="fas fa-star"></i></div>
            <div class="divider-custom-line"></div>
        </div>
        <!-- Portfolio Grid Items-->
        <div class="row text-center">
            <!-- Portfolio Item 1-->
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis, perferendis amet dicta, laudantium nobis dolores provident omnis labore molestiae laborum quia quam expedita magnam consectetur totam sit vel. Recusandae, quo! Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi possimus blanditiis nihil id in, velit adipisci doloribus, molestiae saepe nobis exercitationem distinctio porro expedita dolore, quasi veniam non nemo vitae? Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit, eligendi aperiam vel fuga nesciunt quidem nihil in modi nostrum porro optio dolorum iure corrupti maiores aspernatur hic ut necessitatibus? Quasi.
        </div>
    </div>
</section>
<!-- About Section-->
<section class="page-section bg-primary text-white mb-0" id="tim">
    <div class="container">
        <!-- About Section Heading-->
        <h2 class="page-section-heading text-center text-uppercase text-white">Tim</h2>
        <!-- Icon Divider-->
        <div class="divider-custom divider-light">
            <div class="divider-custom-line"></div>
            <div class="divider-custom-icon"><i class="fas fa-star"></i></div>
            <div class="divider-custom-line"></div>
        </div>
        <!-- About Section Content-->
        <div class="row">
            <div class="col-lg-4 ms-auto">
                <img src="<?= base_url("assets/front/img/tim/ibnu.jpg") ?>" alt="" class="img-fluid rounded border">
                <p class="h4 mt-3">Ibnu Rizqia Ramadan</p>
                <p class="lead">Seorang mahasiswa dari kampus STMIK Bandung dan juga seorang Backend developer yang ...</p>
            </div>
            <div class="col-lg-4 me-auto">
                <img src="<?= base_url("assets/front/img/tim/ibnu.jpg") ?>" alt="" class="img-fluid rounded border">
                <p class="h4 mt-3">Nanda Vian N.</p>
                <p class="lead">You can create your own custom avatar for the masthead, change the icon in the
                    dividers, and add your email address to the contact form to make it fully functional!</p>
            </div>
        </div>
        <!-- About Section Button-->
        <!-- <div class="text-center mt-4">
            <a class="btn btn-xl btn-outline-light" href="https://startbootstrap.com/theme/freelancer/">
                <i class="fas fa-download me-2"></i>
                Free Download!
            </a>
        </div> -->
    </div>
</section>

<!-- Footer-->
<footer class="footer text-center">
    <div class="container">
        <div class="row">
            <!-- Footer Location-->
            <div class="col-lg-6 mb-6 mb-lg-0">
                <h4 class="text-uppercase mb-4">Location</h4>
                <p class="lead mb-0">
                    2215 John Daniel Drive
                    <br />
                    Clark, MO 65243
                </p>
            </div>
            <!-- Footer Social Icons-->
            <div class="col-lg-6 mb-6 mb-lg-0">
                <h4 class="text-uppercase mb-4">Around the Web</h4>
                <a class="btn btn-outline-light btn-social mx-1" href="#!"><i class="fab fa-fw fa-facebook-f"></i></a>
                <a class="btn btn-outline-light btn-social mx-1" href="#!"><i class="fab fa-fw fa-twitter"></i></a>
                <a class="btn btn-outline-light btn-social mx-1" href="#!"><i class="fab fa-fw fa-linkedin-in"></i></a>
                <a class="btn btn-outline-light btn-social mx-1" href="#!"><i class="fab fa-fw fa-dribbble"></i></a>
            </div>
        </div>
    </div>
</footer>
<!-- Copyright Section-->
<div class="copyright py-4 text-center text-white">
    <div class="container"><small>Copyright &copy; Traffic Pixel 2021</small></div>
</div>
<!-- Bootstrap core JS-->
</body>

</html>
<?= $this->endSection() ?>