---
author: adam
date: 2016-04-15 13:00:00+00:00
draft: false
title: All Hail the Robotic Event Scheduling Overlord
type: post
url: /2016/04/15/all-hail-the-robotic-event-scheduling-overlord/
---

And now for something completely different! Not _everything_ that Dan and I work on is LED related...

For years, our local group of friends have a had a weekly dinner, referred to as Hang Out Time or HOT for short. It was at a different restaurant each week, chosen from a rotating list of options... or at least it was supposed to be. Our friend Miles managed the weekly event creation but then passed off the duties to me a couple years ago. And over time the events (which were scheduled on Facebook) would get created closer and closer to the day, and the rotating restaurants became much less random and from a much smaller list.

At one HOT event a couple months ago, the topic of the poor quality of my planning duties came up and Miles jokingly said I needed to have a computer AI that would create the events for us. But it sounded like a perfect excuse for a fun project!

After a handful of evenings pounding away at some Python code, our HOT scheduling AI overlord came to life... I call it [HOTBot](https://github.com/adammhaile/HOTBot) :)

HOTBot is a small console program (Linux only at the moment) that communicates with Google Calendar, searches for placeholder events with a specific naming scheme, chooses a random event location, and then updates that event with all the pertinent details and invites the event guests.

We've been using it for the last month to great success. HOT is every Thursday night and about 30 minutes into dinner an automated email goes out with the Google Calendar invite and event details. Now, as I said, HOTBot is pretty bare-bones... so there's no internal scheduling of when to run and send out the invites. This is all controlled via [Cron](https://en.wikipedia.org/wiki/Cron) which in my case is set up to run HOTBot nightly at 7:30pm. It only searches through the scheduling calendar 7 days into the future and since the events are at 7:00pm, by 7:30pm the next event is within that 7 day range. HOTBot picks a random restaurant (without repeating) and sends out the details.

There's a lot you can do with entering guests, locations, event messages, etc... but I'll leave that for the HOTBot [Readme](https://github.com/adammhaile/HOTBot). There you'll also find details on how to install HOTBot on your system.

As with everything we do, HOTBot is open source and free to use :)
