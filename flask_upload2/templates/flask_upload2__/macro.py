def flask_upload_init():

    return '''
<!-- The Templates plugin is included to render the upload/download listings -->
<script src="{{ url_for('flask_upload__.static', filename='js/tmpl.min.js')"></script>
<!-- The Load Image plugin is included for the preview images and image resizing functionality -->
<script src="{{ url_for('flask_upload__.static', filename='js/load-image.min.js')"></script>
<!-- The Canvas to Blob plugin is included for image resizing functionality -->
<script src="{{ url_for('flask_upload__.static', filename='js/canvas-to-blob.min.js')"></script>
<!-- blueimp Gallery script -->
<script src="{{ url_for('flask_upload__.static', filename='js/jquery.blueimp-gallery.min.js')"></script>
<!-- The Iframe Transport is required for browsers without support for XHR file uploads -->
<script src="{{ url_for('flask_upload__.static', filename='js/jquery.iframe-transport.js')"></script>
<!-- The basic File Upload plugin -->
<script src="{{ url_for('flask_upload__.static', filename='js/jquery.fileupload.js')"></script>
<!-- The File Upload processing plugin -->
<script src="{{ url_for('flask_upload__.static', filename='js/jquery.fileupload-process.js')"></script>
<!-- The File Upload image preview & resize plugin -->
<script src="{{ url_for('flask_upload__.static', filename='js/jquery.fileupload-image.js')"></script>
<!-- The File Upload audio preview plugin -->
<script src="{{ url_for('flask_upload__.static', filename='js/jquery.fileupload-audio.js')"></script>
<!-- The File Upload video preview plugin -->
<script src="{{ url_for('flask_upload__.static', filename='js/jquery.fileupload-video.js')"></script>
<!-- The File Upload validation plugin -->
<script src="{{ url_for('flask_upload__.static', filename='js/jquery.fileupload-validate.js')"></script>
<!-- The File Upload user interface plugin -->
<script src="{{ url_for('flask_upload__.static', filename='js/jquery.fileupload-ui.js')"></script>
<!-- The main application script -->
<script src="{{ url_for('flask_upload__.static', filename='js/csrf.js')"></script>
<!-- The XDomainRequest Transport is included for cross-domain file deletion for IE8+ -->
<!--[if gte IE 8]>
<script src="{{ STATIC_URL }}js/cors/jquery.xdr-transport.js"></script>
<![endif]-->
'''

