$(document).ready(function(){
  $('#like-button').click(function(){
      var blog_id;
      blog_id = $(this).attr("data-catid");
      $.ajax({
          type:"GET",
          url: "/blogapp/likepost",
          data:{
                   'blog_id': blog_id
          },
          success: function( response ){
            document.getElementById('like-count-span').innerHTML = response['like_count'];
          }
       })
   });

   $('#dislike-button').click(function(){
     var blog_id;
     blog_id = $(this).attr('data-catid');
     $.ajax({
       type:'GET',
       url:"/blogapp/dislikepost",
       data:{
                'blog_id': blog_id
       },
       success: function( response ){
         document.getElementById('dislike-count-span').innerHTML = response['dislike_count'];
       }
     })
   });
});
