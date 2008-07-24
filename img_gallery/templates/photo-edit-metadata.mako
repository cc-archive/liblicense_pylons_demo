<%inherit file="base.mako"/>

<h1 class="main">Edit Photo Metadata</h1>

${h.form(h.url_for(action='save_edits'))}
<strong>Title:</strong> <input name="title" id="title" value="${c.photo.title}"/><br/>

<strong>License:</strong>
     <div id="cc_widget_container">
<input type="hidden" id="cc_js_seed_uri" value="${c.photo.license}" />
<script type="text/javascript"
	src="http://api.creativecommons.org/jswidget/tags/0.92/complete.js?locale=en_US">
</script>
</div>

${h.submit('Submit')}
${h.end_form()}
