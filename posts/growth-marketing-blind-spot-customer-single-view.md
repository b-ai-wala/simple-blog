---
title: "Growth Marketing “Blind Spot” — Why do we need a Customer Single View"
date: "2022-08-10T01:52:52+05:30"
---

* * *

![](/images/Growth Blindspot Logo.png)![](/images/Growth Blindspot Logo.png)Growth BlindSpot — What it is and How to Avoid

### Justice is Blind, Growth Marketing should not be

Just as a startup starts finding its feet, the search for Growth begins. More often, teams make similar mistakes over and over again. This post is about these common mistakes that I committed or learned vicariously.

Let’s run through a few day-to-day situations :

  1. **Participated in meetings where 2 different teams come with Data Points on a Project, that point in diametrically opposite directions**.
  2. **Ran Acquisition or Marketing basis Shallow Conversion Events** such as Installs, Signups that typically landed up with minimal revenue a quarter later.
  3. **Favored Channels which gave a Higher Short term ROI** (because that data was available) vs actually giving the rightful share to the channels with a higher Customer Lifetime Value.
  4. **Kept working with a very narrow set of metrics**(because that data was available). Missed out on Key Product Interactions that could have been utilized as early indicators for successful user acquisition.
  5. **Missed out on utilizing Customer Experience touch points/channels** early on for a more proactive retention nudge, and later wasted time doing “post-churn-post-mortem” endlessly.
  6. **“New product release impact assessment” errors and delays** , which typically happened due to a lack of clarity on success metrics or their measurement

If all this sounds very familiar, you are not alone! As the teams mature in their understanding of what works, there is one concept that slowly starts to dawn in the common discussions — **Customer Single View**. But before we discuss Customer Single View beyond the textbook definition, let’s understand the typical Information silos that brew up over time in most companies.

When you are growing a company — there is little time to share what you know with the other teams and this leads to 4 Key Data silos (**PACT**) that are born out of the effort of the typical functions you see in Startups.

PACT — the 4 Data Silos

![](/images/Team wise Data Silo.png)![](/images/Team wise Data Silo.png)PACT — Typical Data Silos that exist in every Startup

  * Product
  * Acquisition
  * Customer Engagement plus Experience
  * Transactions

_Note: Have skipped Financial Data from above to keep the discussions focused on Growth Marketing. Otherwise, that would be the 5th._

Let’s look at each of the Data Silo in little more detail

#### A. Transactions Data (or should we call it Business Data)

![](/images/Transaction Data.png)![](/images/Transaction Data.png)Transactions Data also called Business Data

This is usually considered the most important information you have at a company level. Business teams rely on the above for setting the direction, business planning, budgetary planning, etc. Primarily Transactions Data is based on one key identifier — **User Identity.** _(User Identity also calls for defining a user, depending on the business it could be a consumer, an account, or another company with multiple sub-users)_. This usually sits within your Company’s Database in the basic form of tables either in RDBMS (relational database management system) or distributed file systems like Hive.

#### B. Customer Engagement Data (or CRM-related info)

![](/images/CRM Engagement.png)![](/images/CRM Engagement.png)CRM or Customer Engagement Data

Customer Engagement Data usually evolves as the very second piece of information beyond business which you need to keep a business running. All your support requests, customer interactions, post sales queries, customer feedback, and tickets sit here. For a business to deliver a smooth customer experience, this becomes vital. While this is pretty important from Day 1, typically it evolves parallel to business data, because of very different use cases involved. The primary identifier is still based on the User ID.

This data is either on one of the platforms

  1. CRM Tools — such as MoEngage
  2. Customer Support CRMs — such as Zoho, Freshdesk
  3. OR sometimes In house tools

#### C. Acquisition Data (or Marketing related info)

![](/images/Acquisition Data.png)![](/images/Acquisition Data.png)Acquisition or Marketing Data

Acquisition Data starts to evolve as soon as basic marketing or growth activities start to take their feet. While both Transaction data and Customer Experience data typically evolve internally, Acquisition Data typically relies on some major Advertising Channels (i.e. Google, FB, etc.) for one reason. These platforms offer pretty holistic reporting frameworks to begin with, which serves most of the use cases. The only exception to this is Referral or Organic Marketing. (Typically referral marketing requires an internal analytics approach as its a product built in-house, however with the advent of referral marketing SAAS platforms, this may change in the future)

The biggest challenge in Acquisition Data is that it’s generated and distributed across sources and relies on the Ad Platform. Hence teams typically juggle as many sources of data as there are channels.

#### D. Product Usage Data

![](/images/Product Usage Data.png)![](/images/Product Usage Data.png)Product Usage Data

As the name explains, this refers to how users are using and interacting with your product. This is a fairly evolved space and various analytics tools support the basic use cases encountered by most teams and products. To name a few —

  * Google Analytics — Free and Pro Versions for Website
  * Firebase (Another offshoot of Google Analytics) — For Apps
  * MixPanel and Amplitude — For both website and app
  * In-house Web/Product Analytics Solutions

### Putting it all together — Map of Customer Data

![](/images/Customer Single View.png)![](/images/Customer Single View.png)PACT — 4 Data Silos and the typical metrics which sometimes help in crossing from one to another

### The Case for “Customer Single View”

> The case for CSV (Customer Single View) is based on the hypothesis that Customer is one and hence if the journey across the company is available to every stakeholder it would lead to Global Optima vs a Local Optima

#### The guide to building a Customer Single View — How we did it

  1. **Basics** — Start with a common understanding of the User ID. A User ID should be a robust, static, unique identifier that you recognize a user by in your own systems. User IDs are consistent across a customer’s lifetime. User IDs are typically based on a combination of a unique Phone Number and Email ID. (Phone Numbers in India are more prevalent, hence it’s not uncommon to see Phone Numbers as the main basis for UID generation.
  2. **Next start with building a common Analytical Database** which will ingest data from all the key sources listed previously i.e. Transactions, Customer Engagement Touchpoints, Acquisition, and Product Usage Data. The UserID is typically used in stitching these data sources. Since UserID may not be present in all the sources, for ex: Acquisition Data, here you will have to build logic for attribution to make the connection.
  3. **Next comes the Main Materialised View** that will house your Customer Single View. We will be referring to it as the CSV. The CSV would require defining the Key Attributes and corresponding Values that you would need against them. **_It is not uncommon to have a CSV with more than 500+ attributes._**_The number_ of attributes should be decided basis common minimum standards across most functional teams rather than making it unnecessarily complex.
  4. Once you have the CSV Table Structure in Place, you will have two kinds of attributes — **Static and Dynamic.** As the name signifies, Static attributes house static values, which don’t change over a user’s lifetime, ex: Date of Birth of Customer, Primary Source of Acquisition on 1st Signup, etc. Dynamic attributes house stuff that can change, ex: Last Activity Date, Last Order Value, etc. Your Analytics team will have to have a plan in place for keeping the CSV Table updated for the Dynamic and Static parts with a proper regimen.
  5. **Finally, the success of CSV depends on its Company-wide adoption.**

![Growth Blind Spot - Customer Single View](/images/Group 22.png)![Growth Blind Spot - Customer Single View](/images/Group 22.png)CSV in its completed form — A guide map

#### How will you make a large number of teams (if not every team) use it? Some approaches.

  1. **CSV as the single source of Truth — Start evangelizing the CSV Table as a gold standard for inter-team reporting** , which will mean moving team-level reports to start using CSV Table as a source of Truth for major items Ex: Attribution of Acquisition sources, LTV of the Customer.
  2. **CSV L0 Reports — Build a visualization layer for the most common items** —  _The life cycle of the Customer from Acquisition to Retention or Churn_.
  3. **Centralized Ownership of CSV** — The ownership of maintaining data pipelines & reporting needs to rest with one team. This is usually split across Data Engineering & Data Analytics teams. Having a common leader across these functions ensures that all teams access the same data sources for their respective views.

* * *

In Summary, once you have reached the Customer Single View Stage you can build the following applications effortlessly

  1. Build a clear understanding of Users — New versus Returning. And optimize the acquisition channels to focus on New more effectively, by avoiding the $ going to returning users in vain.
  2. Track Revenue, Conversion, Complaints, Refunds, Retention, and Churn across a specific cohort of users — say those who have been acquired from Google vs Organic Channels.
  3. Build a pricing or discount strategy in line with the Channels of Acquisition and subsequent funnel performances.
  4. Develop channel-wise CAC that suits the ROI of that particular channel. For ex: Facebook may be giving you a higher ROI vs Google and hence can have a higher CAC. (P.S. — This is an actual example)

**Basically, this approach enables the whole organization to focus their energy on taking action rather than validating whose is accurate!**

Feel free to share with me in the comments if you have experienced some of the things mentioned in the blog. Or some further applications, you may have built already.

* * *

**Credits:**

[Arun Kumar](https://www.linkedin.com/in/arun-kumar-07b1886/), [Arpit Srivastav](https://www.linkedin.com/in/srivaarpit/) — For showing it 1st Hand how it is done, and for reviewing this story so it is easy to understand, yet explains the key concepts

[Madan Rawtani](https://medium.com/u/efc4075f6d9a) for always patiently reviewing and nudging to bring out the best stories that will be useful for the growth marketers out there.

References:

  1. [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)
  2. [Best practices for UID](https://segment.com/docs/connections/spec/best-practices-identify)

* * *

![](/images/Burhan Photo Main-compressed.jpg)![](/images/Burhan Photo Main-compressed.jpg)

burhanuddin.pithawala

Growth Marketing Leader, Startup Growth Practitioner, Advisor to Startups on Growth, Marketing, and Product Marketing. Currently, I Head Growth Marketing @HealthPlix. Earlier I was the Global Head of Marketing @OYO.

Email(required)

Subscribe here for an occasional email from me whenever I publish a new note on growth, marketing, and analytics.

Subscribe to Growth Notes by Burhan