document.addEventListener('DOMContentLoaded',function(){
  var grid=document.getElementById('om-grid'),pager=document.getElementById('om-pager');
  if(!grid||!pager)return;
  var cards=[].slice.call(grid.querySelectorAll('.om-card')),per=6,
      pages=Math.max(1,Math.ceil(cards.length/per)),page=1,
      nums=[].slice.call(pager.querySelectorAll('.om-page')),
      next=pager.querySelector('.om-next');
  function show(p){
    page=Math.min(pages,Math.max(1,p));
    cards.forEach(function(c,i){c.hidden=(Math.floor(i/per)+1!==page);});
    nums.forEach(function(b){
      var on=Number(b.textContent.trim())===page;
      b.style.background=on?'#0F3D2E':'transparent';
      b.style.color=on?'#fff':'#0B1F17';
      b.style.borderColor=on?'#0F3D2E':'#DDE9E3';
      b.setAttribute('aria-current',on?'page':'false');
    });
    if(next)next.textContent=page>=pages?'← Zpět':'Další →';
    window.scrollTo({top:grid.getBoundingClientRect().top+window.scrollY-100,behavior:'smooth'});
  }
  nums.forEach(function(b){b.addEventListener('click',function(){show(Number(b.textContent.trim()));});});
  if(next)next.addEventListener('click',function(){show(page>=pages?1:page+1);});
  show(1);
});

document.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('.om-nav').forEach(function(nav){
    var toggle=nav.querySelector('.om-nav-toggle'),links=nav.querySelector('.om-nav-links');
    if(!toggle||!links)return;
    toggle.addEventListener('click',function(){
      var open=nav.classList.toggle('om-nav-open');
      toggle.setAttribute('aria-expanded',open?'true':'false');
    });
    links.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click',function(){
        nav.classList.remove('om-nav-open');
        toggle.setAttribute('aria-expanded','false');
      });
    });
  });
});
