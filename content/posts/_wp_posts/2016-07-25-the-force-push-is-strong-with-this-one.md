---
author: adam
date: 2016-07-25 15:21:43+00:00
draft: false
title: The force (push) is strong with this one...
type: post
url: /2016/07/25/the-force-push-is-strong-with-this-one/
categories:
- Code
- Cool Stuff
- git
---

[Git](https://en.wikipedia.org/wiki/Git_(software)) is awesome. It's not just open source, but in the last few years, with the help of sites like [GitHub](http://github.com), it has cemented itself as _the_ source control software _for_ open source. At Maniacal Labs we use it for everything and the same goes at my day job with [Red Hat](http://redhat.com). At the latter, I've found myself having to use the "push --force" option a lot recently due to some oddities with the way our code review process works (that's a _much longer_ post for another time) and of course the joke about it being a "force push", as in Star Wars, came up a lot.

So, when I already happened to be looking into how to automate a few things with [Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) recently I came up with a silly little hook that runs whenever you "force push" code up to the repo server. So, now, whenever I force push, I get a little message from Darth Vader himself:
{{< figure src="/wp-content/uploads/2016/07/forcepush.png" caption="forcepush" >}}


Checkout the full git hook code with install instructions over on [GitHub](https://github.com/ManiacalLabs/MiscUtil/blob/master/git/vader-pre-push.sh)
