document.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('.om-nav').forEach(function(nav){
    var toggle=nav.querySelector('.om-nav-toggle'),links=nav.querySelector('.om-nav-links');
    if(!toggle||!links)return;
    function set(open){
      nav.classList.toggle('om-nav-open',open);
      toggle.setAttribute('aria-expanded',open?'true':'false');
      toggle.setAttribute('aria-label',open?'Zavřít menu':'Otevřít menu');
    }
    toggle.addEventListener('click',function(){set(!nav.classList.contains('om-nav-open'));});
    links.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click',function(){set(false);});
    });
    document.addEventListener('keydown',function(e){
      if(e.key==='Escape'&&nav.classList.contains('om-nav-open')){set(false);toggle.focus();}
    });
  });
});
