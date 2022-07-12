A python script to display events from Markdown files.

The default path for the markdown files to be searched is `~/vimwiki/*.md`, but this can be changed on line 102.

Events in markdown are any checkbox item that ends with the format `KEYWORD: ISO-DATE`, where the ISO-DATE is in the format `%Y-%m-%d %H-%M`, and KEYWORD is set in the code.
For example:
```
- [ ] Make a good README DEADLINE:2000-01-01 12:00
```

By default the script contains DEADLINE and SCHEDULED as options for KEYWORD, but this is easily extended as on lines 105 through 108.

For editing the Markdown files, the vim keybinding:

``` vim.keymap.set('n', '<Leader>id', 'A KEYWORD:<ESC>:put =strftime(\'%Y-%m-%d %H:%M\')<CR>kJx$') ```

or

``` nnoremap <Leader>id A KEYWORD:<ESC>:put =strftime(\'%Y-%m-%d %H:%M\')<CR>kJx$ ```

is very useful.

To stop the script at a certain line in a file, place `##SKIP` where it should stop. 
Place this at the top of a file to skip the file (recommended for any long Markdown files that do not contain events).

The script also includes the ability to keep an inbox file, the path to which is specified on line 103.
`markdown-events.py c` returns the number of entries in the inbox, and `markdown-events i -in text to input to inbox` adds add text after -in as an event in the inbox file.
