# sample_static_site_generation
A practice of creating a static site generation based on Template module

## Example with Template module
```python
# Template
from string import Template

some_string = 'Hi ${name}, how are you?'
template = Template(some_string)
print(template.safe_substitute(name='Ash Ketchum'))
```
