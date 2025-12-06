---
title: "Attribution eats Marketing Strategy for Breakfast"
date: "2022-09-27T08:39:08+05:30"
---

![](/images/Breakfast.png)![](/images/Breakfast.png)

It is rare to find a growth marketing team today that is not Data Driven. All the Marketing Strategies (specially in acquisitions) boil down to 2 decisions

  1. Scale-Up what’s working
  2. Scale-Down or STOP what’s not working

But How do you measure what is working? This is where you need Attribution

## 3 Most widely used Attribution Methodologies

Rather than me explaining the basics, [here is a detailed document for someone who loves details. ](https://www.iab.com/wp-content/uploads/2016/10/Digital-Attribution-Primer-2-0-FINAL.pdf)(This article is a product of the working group led by – The Interactive Advertising Bureau (IAB) consisting of Advertising majors like Google, Inmobi, Criteo, Rakuten, Twitter, and more than 30 others)

In summary, Attribution is the methodology that a company follows in order to determine which marketing channel, salesperson, or entity was responsible for getting a customer/user on your platform. There are majorly 3 attribution Models

  1. 1st Click Attribution
  2. Last Click Attribution
  3. Multi-Touch Attribution

![3 types of attribution models - 1st click, last click and multi touch attribution](/images/3-attribution-models-1.png)![3 types of attribution models - 1st click, last click and multi touch attribution](/images/3-attribution-models-1.png)

## But you probably know this already. Real Attribution Challenges emerge in the real world – where things go wrong

There are 3 critical decision points where most attribution mistakes are made.

  1. Not accounting for the Number of Stages in the Funnel
  2. The time it takes to go from one stage to another
  3. User Type – New or Repeat

Let’s look at them with the help of an example to understand them more clearly.

### 1\. Stage in the Funnel

Assume you are designing an attribution methodology for an App based business. There are 2 major states of the user.

  1. Register on the app
  2. Make a Purchase

![](/images/Stages.png)![](/images/Stages.png)

> Decision Point: Apply attribution methodology on the right event. If you care about transactions then put it on transactions.

### 2\. The time it takes to go from one stage to another

Now for our sake, the journey of the user started when he/she registered on the App. Next, we need to identify what is the behavior of the user between these 2 stages. Practically either the user makes a purchase or they don’t. Additionally, if they make a purchase, then there will be a delay between stages A and B, let’s call it t (for time).

However t won’t be a constant number for all the users, it will vary from user to user.

![](/images/time to convert.png)![](/images/time to convert.png)

Now your practical sense comes to test, to determine, what is the time t# by which you have a considerable number of users that were to convert, would have converted. In order to arrive at the number scientifically, you can deploy a few acceptable techniques

  1. Look at the inflection point and determine the time t#
  2. Take the time t# at which 80% or 90% of the people would have converted

> Decision Point – Use t# as a factor to determine what attribution time window fits your company

### User Type – New or Repeat

This is a slightly convoluted one. As there are multiple options at every stage. So let me park this one and come back again to this point in some other post.

* * *

### Now let’s apply our standard – First, Last, and Custom attribution models on a Sample DataSet I created for this exercise

Here we take a random data set and start debunking the last click model, the first click model, and the mixed models one by one.

[Workbook for Attribution / Dataset for Practice](https://docs.google.com/spreadsheets/d/1dn-QHDukA2CP0pfYcoWDSGf_vM41sra2jhlTQDYXOOo/edit#gid=2108564644) – To use this workbook (google sheet format), simply make a copy of the same in your Google drive.

**About The Dataset**

  * It consists of 1000 unique users
  * We have maximum 5 touchpoints for any user
  * A User either registers or doesn’t. And once registered the user either transact or doesn’t.
  * There are 5 primary channels involved in the marketing and conversion mix – Organic, Sales, Google, FB, and CRM
  * Total Cost = 151,700, break up as follows

Let’s look at how the funnel is doing across the 2 stages

  1. Total Users – 1000
  2. Registered – 518
  3. Transactions – 276 (27.6% Conversion from Traffic to Transaction)

More Insights

![](/images/Screenshot-2022-09-23-at-1.09.33-AM.png)![](/images/Screenshot-2022-09-23-at-1.09.33-AM.png)

### 1st Click Attribution in Action

We apply 1st Click attribution on the transactions and here’s what we get.

![](/images/CAC-By-Channel-1st-Click-Attribution-2.png)![](/images/CAC-By-Channel-1st-Click-Attribution-2.png) ![](/images/Screenshot-2022-09-23-at-1.12.53-AM.png)![](/images/Screenshot-2022-09-23-at-1.12.53-AM.png)

**Insights**

  * Google seems to have the lowest CAC amongst paid channels
  * CRM contribution is zero

**Pros**| **Cons**  
---|---  
Prioritizes the channels that bring new users to the platform, and not just win by driving transactions| Transaction happens 120 days later, and hence no other channel would have an incentive to touch this particular user. Even if they do help in transactions, they will not get any credit for it.  
Pros and Cons of 1st Click attribution models

### Last Click Attribution in Action

![](/images/CAC-By-Channel-Last-Click-Attribution-2.png)![](/images/CAC-By-Channel-Last-Click-Attribution-2.png) ![](/images/Screenshot-2022-09-23-at-1.18.47-AM.png)![](/images/Screenshot-2022-09-23-at-1.18.47-AM.png)

**Insights**

  * Google goes from being the cheapest (in 1st click regime) to the costliest channel
  * CRM emerges as a super low CAC channel

**Pros**| **Cons**  
---|---  
Prioritizes the channels that bring transactions to the platform, and not just driving registrations| The later stage marketing actions such as CRM start taking precedence, which in reality didn’t get the users on the platform.  
  
The channels that bring in new users to the platform don’t get enough time for the conversion, for example in the current data set, it takes 122 days for a user to transact post 1st touchpoint, but the last click attribution will mean the attribution keeps changing hands every day. Operationally the last click attribution creates a lot of friction between teams.  
Pros and Cons of Last Click attribution models

### How can we use the Insights in the Data Set to arrive at the optimum balance between the 2 extremes? Time-bound 1st Click Attribution

**Insight – It takes 90 days to register and 30 days thereafter to transact.**

What if we carry the 1st click attribution for 60 days only and post that every channel gets a 60-day window from touchpoint to transaction

![](/images/CAC-By-Channel-60-Day-Moving-Window-for-Attribution.png)![](/images/CAC-By-Channel-60-Day-Moving-Window-for-Attribution.png) ![](/images/Screenshot-2022-09-23-at-1.27.56-AM.png)![](/images/Screenshot-2022-09-23-at-1.27.56-AM.png)

**Insights**

  * CAC of Google and FB rationalizes and starts getting the required credit for bringing in new users
  * CRM continues to extract from the lower funnel and has the lowest CAC amongst paid campaigns

**Pros**| **Cons**  
---|---  
Gives every channel an opportunity to acquire and convert the user  
  
The attribution window is pre-defined and hence if a channel gives a conversion during the lockin period, it will get credit for it| Analysis overload increases 2X or more.  
  
Operationally difficult to transition a user from one bucket to another in larger teams, without causing some disruption.  
Pros and Cons of Time bound 1st Click attribution models

### **Other Possible Models** :

  * Multi-touch weightage-based model

* * *

## Conclusion

We started with the same data, but we saw a major variation in the CAC across channels. This is exactly where being mindful of the attribution models being used, helps the growth marketing teams in achieving the desired CAC and scale from every channel.

![](/images/1st-Click-Attribution-60-days-moving-window-for-attribution-and-Last-Click-Attribution.png)![](/images/1st-Click-Attribution-60-days-moving-window-for-attribution-and-Last-Click-Attribution.png) ![](/images/Contribution of Transacting Users by Channel vs Attribution Methodology.png)![](/images/Contribution of Transacting Users by Channel vs Attribution Methodology.png)

* * *

References

  1. [Workbook for the Exercise](https://docs.google.com/spreadsheets/d/1dn-QHDukA2CP0pfYcoWDSGf_vM41sra2jhlTQDYXOOo/edit#gid=1960145924)
  2. https://www.iab.com/wp-content/uploads/2016/10/Digital-Attribution-Primer-2-0-FINAL.pdf
  3. https://en.wikipedia.org/wiki/Attribution_(marketing)
  4. https://blog.hubspot.com/marketing/attribution-reports-definition
  5. https://advertising.amazon.com/library/guides/marketing-attribution