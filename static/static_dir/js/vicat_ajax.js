$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-revid");
    $.get('/vicat/{{ series.id }}/like_review/', {review_id: revid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});