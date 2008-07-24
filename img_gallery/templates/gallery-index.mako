<%inherit file="base.mako"/>

<h1 class="main">Photos</h1>

% if not c.photos:
<p>No photos here; why don't you 
${h.rails.link_to('add one', 
  h.rails.url_for(controller='photo', action='add'))}?</p>
% else:
% for p in c.photos:
<p>
<a href="${h.url_for(controller='photo', action='static', id=p.id)}">
<img src="${h.url_for(controller='photo', action='thumbnail', id=p.id)}"
/>
</a>
</p>
<p>${p.title}<br/>
${h.link_to(p.license_name, p.license)}
</p>
% endfor
% endif
