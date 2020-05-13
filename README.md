# scrapz
Human readable metadata scraping from the LBRY blockchain.

### Install

```Shell
  $ pip install -r requirements.txt
```


### Limitations

Public chainquery API:


>"Queries must take less than 10 seconds or they are cancelled..."

## Guidelines

Follow this guidelines if you want your content data to be discover and analysed by `scrapz`:

### Anonymous

`Scrapz` will ignore anonymously published content by default.

### Licensed content

Unlicensed Content will be ignored by default.

- Always provide a valid license for your content.

- Freeing your content globally without restrictions? use a public-domain-equivalent license.

### Tags

- Use only lowercase characters if possible.

- Use a single word for each tag.

- Don't Start With or Use Only Numbers.

- We recommend using no more than 3 tags per claim.

- Don't use or add spaces or punctuation in the tag.

Recommended tag model:

```
[type] [category] ['subcategory'] [...]
```

- Type: the first tag represent what kind of content are you publishing.

- category: the second tag rpresent a category of the content type.

- subcategory: the third tag represents a subcategory of the previous tag asigned. You can use more than one tag for this.

Examples

```
[music] [classical] [piano] [...]
```

```
[book] [anthology] [mystery] [...]
```  

### Block scrapz

Here are some things you can do to prevent `scrapz` from analyzing and collecting any of your claims data on the database:

- Don't follow the guidelines.

- Add the `scrapz-ignore` tag to any of your channels or a specific claim.

- Create a playlist with the name  `scrapz-ignore` and add all your claim urls that you want to ignore.
