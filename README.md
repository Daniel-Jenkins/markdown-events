A python script to display events from Markdown files.

The default path for the markdown files to be searched is ~/vimwiki/*.md, but this can be changed on line 12.

Events in markdown are any checkbox item that ends with the format "KEYWORD: ISO-DATE", where the ISO-DATE is in the format "%Y-%m-%d %H-%M", and KEYWORD is set in the code.
For example:
```
- [ ] Make a good README DEADLINE:2000-01-01 12:00
```

By default the script contains DEADLINE and SCHEDULED as options for KEYWORD, but this is easily extended as on lines 81 through 84.

For editing the Markdown files, the vim keybinding:

``` vim.keymap.set('n', '<Leader>id', 'A KEYWORD:<ESC>:put =strftime(\'%Y-%m-%d %H:%M\')<CR>kJx$') ```

or

``` nnoremap <Leader>id A KEYWORD:<ESC>:put =strftime(\'%Y-%m-%d %H:%M\')<CR>kJx$ ```

is very useful.
