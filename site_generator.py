'''
# Nav = art_nav,
# Title = "Art",
# Html_Contents = html_content
'''

from string import Template

 
index_nav='''
              <li><a href="index.html" class="active">About</a></li>
              <li><a href="blog.html">Blog</a></li>
              <li><a href="art.html">Artwork</a></li>
'''
blog_nav='''
              <li><a href="index.html">About</a></li>
              <li><a href="blog.html" class="active">Blog</a></li>
              <li><a href="art.html">Artwork</a></li>
'''
art_nav='''
              <li><a href="index.html">About</a></li>
              <li><a href="blog.html">Blog</a></li>
              <li><a href="art.html" class="active">Artwork</a></li>
'''

# 1. Read template.html and create a template object
html_template = open('template.html', 'r+').read()
template = Template(html_template)

# 2. Create a set of lists to replace variables in templates
content_files = [ 'c_index.html', 'c_art.html', 'c_blog.html']
title_values = [ 'About Hello', 'Art', 'Blog']
nav_values = [ index_nav, art_nav, blog_nav ]

# 3. Generate full contents and write to a html file
for i in range(0, 3):
    html_content = open(content_files[i], 'r+').read()
    # Create a output file name by removing "c_" suffix from the content html file
    output_file = 'docs/' + content_files[i][2:]

    # Substitute Nav, Title, Html_Contents
    full_content = template.safe_substitute(
        Nav = nav_values[i],
        Title = title_values[i],
        Html_Contents = html_content
    )
    # Write the final html contents to a html file
    open(output_file, 'w+').write(full_content)
    


