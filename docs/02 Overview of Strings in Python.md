Let us get an overview of strings in Python.
* Enclose Characters
* Dealing with single quotes in strings
* Multi-line strings
* Concatenating strings
* String Formatting - Old Style
* String Formatting - New Style

## Enclose Characters
Here are the common enclose characters - single quote and double quotes.

## Dealing with single quotes in strings
* Enclose string with single quotes in double quote - eg: "ITVersity's Courses"
* Escape single quotes - 'ITVersity\'s Courses'
* Using double quotes is better for readability purposes

## Multi-line strings
We can use triple single quotes or triple double quotes for multi-line strings.
```
'''We can use triple single quotes or triple double quotes for multi-line strings.

You can have single quotes or double quotes as part of the strings enclosed in triple single quotes (') or triple double quotes (")'''
```

## Concatenating strings
We can concatenate strings using +. But starting from Python 3.x, it is not very popular.

```
msg = 'Hello'
audience = 'World'
print(msg + ' ' + audience)
```

## String Formatting - Old Style
String Formatting is used widely instead of concatenation. However, this is old style.

```
msg = 'Hello'
audience = 'World'

print('%s %s' % (msg, audience))
```

## String Formatting - New Style
Here are the examples of modern way of String Formatting. We can format strings by position or by name.

```
# By position
msg = 'Hello'
audience = 'World'

print('{} {}'.format(msg, audience))

print('{msg} {audience}'.format(audience=audience, msg=msg))

# The variables should be defined by now with the names used in the string enclosed in `f''`.
print(f'{msg} {audience}')
```
