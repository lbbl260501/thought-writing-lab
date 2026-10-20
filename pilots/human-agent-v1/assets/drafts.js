
(()=>{const fields=[...document.querySelectorAll('textarea.draft')];let persistent=true;
fields.forEach(x=>{try{x.value=localStorage.getItem('twl-relations-01:'+x.id)||'';}catch(e){persistent=false;}
x.addEventListener('input',()=>{try{localStorage.setItem('twl-relations-01:'+x.id,x.value);}catch(e){document.getElementById('save-note').textContent='当前浏览器不能保存草稿，请使用导出按钮。';}});});
if(!persistent&&document.getElementById('save-note'))document.getElementById('save-note').textContent='当前浏览器不能保存草稿，请使用导出按钮。';
const b=document.getElementById('export');if(b)b.addEventListener('click',()=>{const text=fields.map(x=>{const l=document.querySelector('label[for="'+x.id+'"]');return (l?l.textContent:x.id)+'\n'+x.value;}).join('\n\n');const u=URL.createObjectURL(new Blob([text],{type:'text/plain;charset=utf-8'}));const a=document.createElement('a');a.href=u;a.download='我的科研表达练习.txt';a.click();setTimeout(()=>URL.revokeObjectURL(u),1000);});})();
