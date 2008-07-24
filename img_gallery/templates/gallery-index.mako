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
${h.link_to(p.license_name, p.license)}<br/>
${h.link_to('download stamped version',
h.url_for(controller='photo', action='stamped'))}<br/>
${h.link_to('edit metadata',
h.url_for(controller='photo', action='edit', id=p.id))}<br/>

</p>
% endfor

<br/>
${h.rails.link_to('add a photo', 
  h.rails.url_for(controller='photo', action='add'))}</p>

% endif
