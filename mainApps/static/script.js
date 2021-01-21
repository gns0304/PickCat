//로딩

$( document ).ready( function() {
    click();
    $( window ).scroll( scrollMove );
})
  
  //스크롤 이동시(모든 페이지)
  function scrollMove() {
    temp_scroll=$(this).scrollTop();
    // if ( $( this ).scrollLeft() > 0 ) {
    //     window.scrollTo({left:0});
    // }
    if ( temp_scroll > 400 ) {
        $( '.top' ).fadeIn();
    } else {
        $( '.top' ).fadeOut();
    }
  }
  
  function click(){
    $( '.top' ).click( function() {
        $( 'html, body' ).filter(":not(:animated)").animate( { scrollTop : 0 }, 300 );
        return false;
    } );
  }



  
  /*main페이지 드래그*/

//   document.querySelector(".imgbox-container").addEventListener("pointerdown", getMouseDown, false);
//     window.addEventListener("pointermove", getMouseMove, false);
//     window.addEventListener("pointerup", getMouseUp, false);
//     let x_down=0;
//     let x_move;
//     let now_x=0;
//     let temp=0;
//     function getMouseMove(event){
//         x_move = event.clientX;
//         if(x_down == 0)
//             null;
//         else{
//             if(now_x + x_move - x_down <= 0){
//               temp = now_x + x_move - x_down;
//               document.querySelector(".imgbox-container").style.left = temp+'px';
//             }
              
//         }
//     }
//     function getMouseUp(event){
//         now_x = temp;
//         x_down=0;
//     }
//     function getMouseDown(event){
//         x_down = event.clientX;
//         document.querySelector(".imgbox-container").style.left += 20+'px';
//     }


    /*펼치기 접기*/
    $( '.unfold1' ).click( function() {
        let temp = $('.infobox').css('display');
        if(temp=="none"){
            document.querySelector('.unfold1').innerHTML=`<img src="../static/img/direction-up.png">&nbsp;접기`;
            $( '.infobox' ).css('display','flex');
        }
        else{
            document.querySelector('.unfold1').innerHTML=`<img src="../static/img/direction-down.png">&nbsp;펼치기`;
            $( '.infobox' ).css('display','none');
        }
        return false;
    } );
    $( '.unfold2' ).click( function() {
        let temp = $('.albumbox').css('display');
        if(temp=="none"){
            document.querySelector('.unfold2').innerHTML=`<img src="../static/img/direction-up.png">&nbsp;접기`;
            $( '.albumbox' ).css('display','flex');
        }
        else{
            document.querySelector('.unfold2').innerHTML=`<img src="../static/img/direction-down.png">&nbsp;펼치기`;
            $( '.albumbox' ).css('display','none');
        }
        return false;
    } );