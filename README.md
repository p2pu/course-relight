Fix locale_url:

```
sed -i -E "s#locale_url ([a-zA-Z_]+)#url \1#g" templates/courses/edit_content.html
```
