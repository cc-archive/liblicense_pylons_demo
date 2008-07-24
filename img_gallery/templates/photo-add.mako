<%inherit file="base.mako"/>

<h1 class="main">Add Photo</h1>

${h.form(h.url_for(action='upload'), multipart=True)}
Title: <input name="title" id="title" /><br/>
Upload file:      ${h.file_field('new_image')} <br />
                  ${h.submit('Submit')}
${h.end_form()}

