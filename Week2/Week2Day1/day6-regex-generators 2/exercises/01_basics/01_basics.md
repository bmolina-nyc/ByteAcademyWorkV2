## Foundation Week 2 Day 3 - Regular Expressions

#### Basics

* Name a yellow food that this regular expression will match ```"[abn]+"```

* Write a sentence that this regular expression will match ```"^Once.*end\.$"```

* Write a similar sentence that the expression won't match.

* If a name record has to have a first name and a last name, separated by
and each beginning with a capital letter, write an expression that matches
this and excludes non-matching records.

```
"Carter Adams"
"Jackie O"
"Joe McGuy"

but not

"Sam"
"Alan  Hodgson"
"sarah smith"
" Larry Sanders"
```

* Write an expression that matches "[timestamp: 123456]" where 123456 can be any integer. Include the [ and ] in the string to be matched.

* Write an expression that matches a string that is exactly the equals sign twenty times.
```
====================
```

* Write an expression that matches an email address. NAME@SERVER.TLD where NAME can be any combination of letters, numbers, dashes, and dots, SERVER follows the same rules as NAME and TLD is three lowercase letters (like com or edu)

* Now write a function that takes a string and returns None if it is not an email address in it and returns just the address if there is an email address in it.

So ```find_email("My name is Carter and my email address is carteradams@gmail.com")```

should return "carteradams@gmail.com"

* Write an expression that can find time expressed like 12:00
