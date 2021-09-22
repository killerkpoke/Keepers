$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown({
        hover: true,
        inDuration: 500,
        outDuration: 425,
        coverTrigger: false,
        alignment: 'right'
    })
    const spinner = document.querySelector('#spinner-box');
    const databox = document.querySelector('#data-box');

    $.ajax({
        type:'GET',
        url:'/post-json/',
        success: function(response){
            setTimeout(()=>{
                spinner.classList.add('not-visible');
                databox.classList.remove('not-visible');
                databox.classList.add('show-visible');
            }, 600)
        },
        error: function(response){
            setTimeout(()=>{
                spinner.classList.add('not-visible');
                databox.innerHTML = '<b>Failed to load, try again later.</b>';
            }, 600)
        }
    })
});
document.addEventListener( 'DOMContentLoaded', function () {
	var splide = new Splide( '.splide', {
        type: 'fade',
        perPage: 1,
        autoplay: true,
        rewind: true,
        cover: true,
		heightRatio: 1,
        pagination : true,
        pauseOnHover: false,
    } );
        splide.mount();
} );

