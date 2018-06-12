---
author: maniacal labs
date: 2015-08-10 13:00:13+00:00
draft: false
title: AllPixel Kickstarter Retrospective
type: post
url: /2015/08/10/allpixel-kickstarter-retrospective/
---

{{< figure src="/wp-content/uploads/2014/11/MainKSThumb.png" caption="MainKSThumb" >}}

The following is an account of our experience with bringing the [AllPixel](/AllPixel) LED Controller to market through Kickstarter. We don't pretend to be experts. This just a record of what we tried, what seemed to work for us, and why we _think_ it worked. While some of this applies to crowd-funding in general, much of it is specific to the realm of electronics.

<!-- more -->



### History



Maniacal Labs got its start way back in 2013 with the release of our, admittedly not successful, [Binary Epoch Clock](/products/becv1). In hind-sight, it was too much of a niche, personal, project to be successful. We thought it was a cool novelty, but that was really all it ever was.

We toyed around with various ideas for some time, most of them time related as we have a bit of an obsession with unique time-pieces. But, again, these were all just too niche to do well in mass market. We even tried, unsuccessfully, launching another [clock design](/2013/11/11/announcing-the-prismachron/) on [Tindie](https://www.tindie.com/products/ManiacalLabs/prismachron-clock/).

But then came the [2014 NC Maker Faire](/nc-maker-faire-2014/). Since the Epoch clock hadn't really been selling anyways, we decided it would be a good opportunity to just show of some of our personal projects. None of them were commercially viable, but they made for much better demonstrations. We arrived with a variety of [projects](/nc-maker-faire-2014/) but it was quickly apparent that the LED displays were the biggest draw.

By the end of the day we had spoken with so many people and answered so many questions that our voices were all but gone. So many of those questions were about how to use the LEDs in our displays. How to program them. How to interface with them. How to power them. These questions mulled in our brains for a couple of weeks until we realized that it didn't have to be so complicated. There had to be a way to make it generic and easy. A way to control _all_ the pixels :) Many prototypes later...

{{< figure src="/wp-content/uploads/2014/11/IMG_0528-16x9.jpg" caption="IMG_0528-16x9" >}}

We've already gone into the details of the AllPixel's creation in [another article](/2014/11/13/allpixel-update-staff-pick/), so we won't do that again. But if you want to learn more details of the development process, it's a good read.



### Preparing for Launch



We've seen far too many Kickstarter campaigns that promise a multitude of things, should the goal be met. Things that haven't even been fully developed at the time of launch. Almost invariably, all of these were either considerably late in delivering or fell through completely. So, to us, the key was to keep things simple and not launch until we knew it could be done. So, unlike those other campaigns, we were not looking for funding to _develop_ the product... we just needed the final funding to put it into production.

Many think that doing this is just not possible without significant up-front investment, that it's just too expensive. But that just doesn't have to be true. It may be hard to believe, but the total development costs of the AllPixel were just $395.18:

{{< figure src="/wp-content/uploads/2015/07/ProtoCosts.png" caption="ProtoCosts" >}}

This did not include our time, of course, but right now we both have day jobs and would be doing this anyway. But certainly don't quit your day job or do this the first time for the sole purpose of making your fortune. It's best to just be content with getting your name and your design out there.

Beyond having a fully functional, ready to go design, we also wanted to keep the rewards as simple as possible. This meant very few tiers and nothing that didn't directly relate to the product, such as shirts or stickers. All that will do is make more work for you later and cut into your profit and time.



### Budgeting



Make spreadsheets. _A lot_ of spreadsheets! You cannot set a price until you know how much the product will cost to produce and ship but don't forget that this include more than just PCBs and components. There's PCB fabrication, assembly, setup, shipping components to the assembler, testing, IC programming, kitting, packaging, and final shipping to the backer (more on shipping below). For every reward component, add a column to your spreadsheet accounting for all of the above listed costs. But you're not done yet! You also need to account for Kickstarter payment fees of 10% of the actual reward price, not the component cost. Then it's best to _include a 10% fudge factor_ applied to all cost calculations. This ensures that if anything unexpected comes up, you are less likely to wind up taking a loss. Our total costs rose to about 7% over the original estimate (without the 10% factor) so we were certainly glad to have that buffer.

{{< figure src="/wp-content/uploads/2015/07/SMDPartCosts.png" caption="SMDPartCosts" >}}

Note that the cost of the Kickstarter fees is a little recursive in that they factor into your total cost, but are dependent on your sale price. In the spreadsheet above that this is factored into the calculations.

Adding things like stickers and shirts would have just complicated this even further. Such things are typically _very_ dependent on volume meaning that our costs could have varied wildly depending on how many backers chose rewards that included those items. Save yourself the trouble and just stick to the basics.



### Taxes



**_DISCLAIMER: We are NOT tax professionals. We highly recommend consulting with a tax professional before launching a crowd-funding campaign._**

We can't talk about budgeting without talking about taxes. First point of note is that you cannot look at your profit calculations from above and just take that number as is. Remember that, at some point after your campaign, the government will want their cut. How much that is will depend on a wide number of things, particularly if the profits are going to an individual, partnership, corporation, non-profit, etc. In the case of Maniacal Labs, we are a registered LLC but we still have to file all income on our _personal_ tax returns, regardless of if the company has paid out profits to us as individuals.

Basically, be prepared to fork over anywhere from 30-50% of your profits in taxes. But note that this is _profit_, not gross earnings. So, in general, you are only paying taxes on whatever is left from the campaign _after_ spending funds on components, promotion, shipping, packing, etc. Also, if you then take what is actual profit and invest it into new product development or a new manufacturing run of products, then that is, in many cases, tax exempt.

Last is timing of your campaign. We'll come right out and say that, from a tax perspective, we launched our campaign at the _worst_ possible time... November. The problem being that a one month campaign will end before the end of the year and you will get the funds but not have time to _spend_ any of those funds before the end of the fiscal year. As far as the government is typically concerned, this makes _everything_ profit and therefore you would owe taxes on the whole amount. Fortunately for us, we have a great tax guy and we found out there is a way to defer paying taxes on that money by declaring it "undelivered goods". This acknowledges that we got the money but that we still need to actually produce the product and that we will claim it on our taxes next year. So, just know that it is not impossible to launch in November, but be _absolutely_ sure that you consult a trusted tax professional before moving forward!



### Pricing and Reward Tiers



Pricing is hard. No question about it. You don't want to undervalue your product and you certainly don't want to _overvalue_ it either. Most products start high and then adjust down as demand dictates but this is _not_ an option for Kickstarter. Once you set your reward prices, they are fixed! But all is not lost...

One great suggestion we got was to have a regular reward tier and an early-bird tier that was slightly cheaper. While you cannot change pricing after launch, you _can_ change tier limits. If you find that not enough people are going for the regular reward tier but _are_ going for the early-bird tier, you can always just open up the limits on that tier. Obviously, be sure that the pricing on that tier is not detrimental, but would you rather get get 100 extra pledges at a 20% discount or only 10 more at the regular price?

Early bird reward tiers also help to give the campaign some extra momentum at the very beginning. If, in the early days, a campaign has already gained many supporters, it will be far more likely to continue to gain support even after those cheaper tiers are gone. For example, take a look at the char below:

**REWARD CHOICE CHART**

The $20 and $30 levels were early-bird specials of the respective $25 and $35 levels. Once the early-bird limit was reached, the pledges did not drop off. But it probably would have been much harder to land the higher priced pledges if we had not already shown support from hundreds of other backers at the early-bird levels.

Those four levels were certainly the core of our campaign, earning $13,680 or 63% of the total pledges. While, as we stated above, we were hesitant to add too many extra items, those that we did have certainly made a difference.

This first major extra was the 5 meter rolls of LEDs. Provided as a $120 tier option (which included the $30/$35 tier plus a roll of LEDs) this added 67 rolls of LEDs and added another $4,965 / 22.8% to our bottom line. This was easy for us to add because they were a pre-made and pre-packaged product that all we had to do was obtain and ship. By acquiring them directly from the manufacturer in China (which happened to be down the street from Seeed) we were able to offer them at a steeply discounted price while still turning some profit on each.

Second, at the suggestion of a friend, we added the $456 Christmas Kit. This was just a silly thing of which there was a very low limit, took little effort, and had decent profit margins. But it still made us $2980 / 13.7% of our total funds. Not bad :)

{{< figure src="/wp-content/uploads/2015/07/Rewards.png" caption="Rewards" >}}

Last, and referenced before, was the PowerTap. Sometimes the small things surprise you.

The PowerTap was literally the result of 15 minutes playing around in KiCAD on a side idea that was not meant to be part of the campaign. The final shipped version of that board is basically unchanged from the original design which took so little time. But the rewards _with_ PowerTaps were _far_ more popular than those without, with nearly three times the pledges! We may never know how well the campaign would have done without the PowerTap but that was certainly 15 minutes well spent. It's worth nothing that, unlike the AllPixel, the PowerTap had a very low profit margin, barely a $1, but since all those pledges _also_ included an AllPixel it was certainly well worth it.

We determined all of the reward tier pricing based on the cost breakdown spreadsheet from above. We had to find a good balance between sale price, profit margin, and minimum quantity to make everything viable. Blah blah... not sure what else to say.............



### Liftoff



For the record, we wish we had a giant red button to press, initiating go-live of the campaign.
{{< figure src="/wp-content/uploads/2015/08/BigRedButton-1024x951.jpg" caption="BigRedButton" >}}


This will happen next time :)

Finally launching the campaign was by far the scariest part. You are going to feel like you forgot something. You probably _did_ forget something. We forgot to include a few things in the budgeting... so, hooray for that fudge factor! Kickstarter now lets you send a private draft view of your campaign to anyone you choose. Find a trusted friend that has a serious Kickstarter habit and, even better, one who has launched their own and see what they think. This really helped us fine tune the pricing, wording, spelling, etc. before launch.

Kickstarter used to have an approval process by which your campaign could not go live until one of their staff approved it. Be it a good thing or not, this process no longer exists. When you push the go-live button, it's live. It's important to note that if you set the campaign as, for example, 30 days in length, it will end in 30 days, exactly, from the moment you click that button. So consider the time of day and day of the week you want it to end beforehand.

But now, people need to know about it...



### Backer Acquisition



Some Kickstarters have huge marketing campaigns behind them. We spent $300 on R&D, so there wasn't exactly the funds to advertise. There's certainly more we could have done or things we could have done better, but here was our basic strategy for getting the word out.




  * **Tell Everyone**: We typically are the quiet types and not ones to spam everyone we know about whatever we are doing. But this was a time to forget all of that. Sure, we certainly tried to target that spamming since our grandparents are probably not the target demographic, but we told everyone who might even know someone else who would be interested. This involved a lot of posting to Facebook, Twitter, Google+, Forums, mailing lists, and emailing directly just about anyone we knew with the slightly interest in electronics, software, or LEDs.


It was extremely helpful to keep a series of, for lack of a better term, form letters to send out. Writing a well thought out message to someone without sounding greedy or desperate is _hard_. So it was a lot easier to do it once, and then tweak things a bit for each recipient. Even though we had a couple masters, we even kept a document containing the contents of every message we sent out and to who. This served both to remind us of who was already contacted as well as gave us that many more previously written messages to start from.




  * **Show Off**: An awesome intro video is great, but they are intentionally short and to the point. Or at least they should be. But sometimes what is going to get someone really interested is a more in depth demonstration of what can be done with your product. During the campaign, we posted a ton of fun examples of all the things that could be done such as: [POVStick](/2014/11/19/weekend-project-povstick/), [FFT Audio](/2014/11/25/fft-audio-animation-with-bibliopixel-and-the-allpixel/), and [Community Collaboration](/2014/11/24/sharing-among-the-community/).
  * **Get People Talking**: This is by far the hardest... getting others to talk about your cool new thing. Even we fell into the trap of thinking there was one or two key sites that, if they posted about our campaign, would rocket us to the top. Not so much...




Sites like Hack A Day are extremely popular in this community and we thought that, if they posted, about the AllPixel, we'd be set. And [they did](http://hackaday.com/2014/11/20/a-usb-controlled-pov-light-stick/). But of our 384 backers, we got... 5 that clicked through from Hack A Day and pledged. Now, don't get us wrong, we aren't trying to knock Hack A Day, we love them. But we fell into that trap of thinking that there was one magic bullet that would fix it all.

The biggest shock to us was that, in the end, a whopping 60.5% of our backers came from users browsing Kickstarter! If anything, this confirms right away that one of the best advantages of Kickstarter is the exposure it gives. We spent countless hours trying to get the word out yet the vast majority of our backers came either directly through Kickstarter or direct to it from our own site. See the graph below for more:

{{< figure src="/wp-content/uploads/2015/07/Backers.png" caption="Backers" >}}

{{< figure src="/wp-content/uploads/2015/07/Funding.png" caption="Funding" >}}



### Reward Fulfillment



Once you've got the funds, now you have to actually _do_ something with all that money! One thing to note first is that it can take some time to get everything. From the end of the campaign, it took about 2 weeks to process all of the payments and then another 2 weeks to actually have the money available for withdrawal. Since our campaign ended, Kickstarter switched from Amazon Payments to Stripe, so this may have changed.

When you do have the money in hand, contact your manufacturer _immediately_! The quicker you can get all the details nailed down, the quicker they can start making everything. Also note that, if your manufacturer is overseas, it may take some time to wire the funds to them. Wiring $12,000 to China is certainly a strange experience!

Now is the time where your initial fulfillment time estimates will be put to the test. We initially calculated, based on estimates from Seeed, that we could likely ship by late February. But this accounted for no error. So, just to be safe, we gave ourselves a two month buffer and promised an April shipment date. Remember, shipping late always looks bad. People will complain if you said April and ship May 1st. So, when we shipped March 30th, we looked great. It turned out we did need that extra time, because we forgot that most of China shuts down for a few weeks in February for Chinese New Year.

Now is also when your original cost estimates will be tested. If you did not plan well, you may either be left with a lot of debt or no way to fulfill the rewards. Fortunately, our estimates were quite sufficient, just check out the chart below:

{{< figure src="/wp-content/uploads/2015/07/Funds.png" caption="Funds" >}}



### Shipping



Our original plan was to kit, pack, and ship everything ourselves. That was also when we thought we would be lucky to get 100 backers. But, instead, we shipped 428 AllPixels, 636 PowerTaps, and 67 rolls of LEDs. Certainly _not_ something that the two of use would want to handle all ourselves. We would have required 141 customs forms just for all the non USA shipping!
{{< figure src="/wp-content/uploads/2015/07/Backers-1024x576.png" caption="Backers" >}}

{{< figure src="/wp-content/uploads/2015/07/BackerMap-1024x575.png" caption="BackerMap" >}}


Fortunately, Seeed came to our rescue again by offering to kit, pack, and ship _everything_. Originally we thought this would be cost prohibitive, but between their better buying power for packing materials and shipping and saving our own time, the $2,643.55 spent on packing and shipping was _well_ worth every penny. As you may note, from the estimates chart above, we _had_ already accounted for packing and shipping costs. Seeed's prices were a little higher than we originally budgeted for, but that's why you keep that 10% fudge factor! Also note, that we later calculated that it would have cost nearly $700 just to ship all the final boards to the USA for us to pack and ship ourselves!

The downside to all of this was that now _everything_ was being shipped overseas, regardless of where the backer was located. Overseas shipping is not without its occasional failures, which we certainly experienced. As of the writing of this, we had five shipments that showed up _very_ late, as much as 3 months, after being stuck in customs, and only one that simply never made it and had to be replaced. But a 1.6% error rate in shipping doesn't really seem all that bad to us. Fortunately, none of them were higher price rewards.



### After the Dust Settles



This is where we are at now. The backers have their rewards and are hopefully making awesome stuff. But that's where it has probably been the most frustrating. While some people are certainly very willing to share and show off what they are working on, that has by far been the minority. Now is the time to build a community around the product and that has probably taken even more marketing effort than the Kickstarter did. We no longer have our product showing up on the front pages of Kickstarter anymore.

We've created a [forum](http://forum.maniacallabs.com/) and post to [Facebook](https://www.facebook.com/ManiacalLabs) and [Twitter](https://www.twitter.com/ManiacalLabs) as much as possible. But when you have a user-base of only about 400 people and only a handful of those will ever interact with you publicly, it's still hard.

Having day jobs doesn't help. We cannot work on new projects to show off the AllPixel and BiblioPixel nearly as much as we would like. But we are not about to stop or slow down.

Hopefully this has shed a little light on the inner workings of a Kickstarter campaign for those curious. Feel free to leave any questions in the comments below.
