$(document).ready(function(){
  setTimeout(function(){
    location.reload();
  }, 3600000);

  
});

function deleteToDoRec(num){
  $('#delToDoModal').modal({
    backdrop: true,
    keyboard: true,
    focus: true,
    show:true
  });
  $('#delToDoLink').attr('href', '/del_event/'+num+'/');
}
