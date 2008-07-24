<%inherit file="base.mako"/>

<h1 class="main">View Photo</h1>

<p>
<img src="${h.url_for(controller='photo', action='static', id=c.photo.id)}"
/>
</p>
<p>${c.photo.title}<br/>
${c.photo.license}<br/>
</p>
